#!/usr/bin/env python3
"""Lightweight FORGE curriculum validator."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:
    print("error: PyYAML is required. pip install -r tools/validation/requirements.txt", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = ROOT / "tools" / "curriculum-manifest.json"
MD_LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
HEADING = re.compile(r"^## (.+?)\s*$")
AGENDA_DUR = re.compile(r"^\|\s*(\d+)\s*\|")
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
FRONT_MATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)

GITHUB_BLOB = re.compile(
    r"^https://github\.com/([^/]+)/([^/]+)/(?:blob|tree)/([^/]+)/(.+)$"
)


class Findings:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def err(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def parse_front_matter(text: str, path: Path, findings: Findings) -> tuple[dict, str]:
    match = FRONT_MATTER.match(text)
    if not match:
        findings.err(f"{path}: missing YAML front matter")
        return {}, text
    try:
        data = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        findings.err(f"{path}: invalid front matter: {exc}")
        return {}, text
    if not isinstance(data, dict):
        findings.err(f"{path}: front matter must be a mapping")
        return {}, text
    return data, text[match.end() :]


def headings_and_sections(body: str) -> dict[str, str]:
    lines = body.splitlines()
    found: dict[str, list[str]] = {}
    current = None
    for line in lines:
        hm = HEADING.match(line)
        if hm:
            current = hm.group(1).strip()
            found[current] = []
            continue
        if current is not None:
            found[current].append(line)
    return {k: "\n".join(v).strip() for k, v in found.items()}


def parse_agenda_durations(section: str) -> list[int]:
    durs = []
    for line in section.splitlines():
        m = AGENDA_DUR.match(line.strip())
        if m:
            durs.append(int(m.group(1)))
    return durs


def nonempty(text: str) -> bool:
    stripped = re.sub(r"\s+", "", text)
    return len(stripped) > 0


def parse_date(value: str, where: str, findings: Findings) -> None:
    if not isinstance(value, str) or not ISO_DATE.match(value):
        findings.err(f"{where}: date must be YYYY-MM-DD, got {value!r}")
        return
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        findings.err(f"{where}: invalid calendar date {value!r}")


def validate_calendar(calendar: dict, manifest: dict, findings: Findings) -> None:
    events = calendar.get("events") or []
    event_ids = set()
    for i, event in enumerate(events):
        loc = f"calendar.yaml events[{i}]"
        if not isinstance(event, dict):
            findings.err(f"{loc}: must be a mapping")
            continue
        eid = event.get("id")
        if not eid:
            findings.err(f"{loc}: missing id")
        elif eid in event_ids:
            findings.err(f"{loc}: duplicate event id {eid}")
        else:
            event_ids.add(eid)
        parse_date(str(event.get("date", "")), f"{loc}.date", findings)
        if event.get("end_date"):
            parse_date(str(event["end_date"]), f"{loc}.end_date", findings)
    if calendar.get("dates_are_planning_inputs") is not True:
        findings.err("calendar.yaml: dates_are_planning_inputs must be true")

    sessions = calendar.get("sessions") or []
    session_ids = []
    for i, sess in enumerate(sessions):
        loc = f"calendar.yaml sessions[{i}]"
        if not isinstance(sess, dict):
            findings.err(f"{loc}: must be a mapping")
            continue
        sid = sess.get("id")
        if not sid:
            findings.err(f"{loc}: missing id")
        elif sid in session_ids:
            findings.err(f"{loc}: duplicate session id {sid}")
        else:
            session_ids.append(sid)
        if sess.get("date_requires_confirmation"):
            if sess.get("date"):
                findings.err(
                    f"{loc}: omit date when date_requires_confirmation is true"
                )
        else:
            parse_date(str(sess.get("date", "")), f"{loc}.date", findings)
        mt = sess.get("meeting_type")
        if mt not in manifest["allowed_meeting_types"]:
            findings.err(f"{loc}: invalid meeting_type {mt!r}")
        phase = sess.get("season_phase")
        if phase not in manifest["allowed_season_phases"]:
            findings.err(f"{loc}: unknown season_phase {phase!r}")
        cp = sess.get("event_checkpoint")
        if cp not in (None, "none") and cp not in event_ids:
            findings.err(f"{loc}: unknown event_checkpoint {cp!r}")
        rel = sess.get("file")
        if not rel:
            findings.err(f"{loc}: missing file")
            continue
        path = ROOT / manifest["season_dir"] / rel
        if not path.is_file():
            findings.err(f"{loc}: missing session file {path.relative_to(ROOT)}")


def validate_session(path: Path, calendar_row: dict, manifest: dict, findings: Findings) -> dict:
    text = path.read_text(encoding="utf-8")
    fm, body = parse_front_matter(text, path, findings)
    rel = path.relative_to(ROOT).as_posix()

    sid = fm.get("id")
    if sid != calendar_row.get("id"):
        findings.err(f"{rel}: front matter id {sid!r} != calendar id {calendar_row.get('id')!r}")
    if fm.get("meeting_type") != calendar_row.get("meeting_type"):
        findings.err(f"{rel}: meeting_type mismatch with calendar")
    cal_tbc = calendar_row.get("date_requires_confirmation") is True
    fm_tbc = fm.get("date_requires_confirmation") is True
    if cal_tbc or fm_tbc:
        if not cal_tbc or not fm_tbc:
            findings.err(
                f"{rel}: date_requires_confirmation must match between calendar and front matter"
            )
        if str(fm.get("date")) != "requires_confirmation":
            findings.err(
                f"{rel}: date must be requires_confirmation when date_requires_confirmation is set"
            )
    elif str(fm.get("date")) != str(calendar_row.get("date")):
        findings.err(f"{rel}: date mismatch with calendar")
    if fm.get("season_phase") not in manifest["allowed_season_phases"]:
        findings.err(f"{rel}: unknown season_phase {fm.get('season_phase')!r}")
    if fm.get("meeting_type") not in manifest["allowed_meeting_types"]:
        findings.err(f"{rel}: invalid meeting_type {fm.get('meeting_type')!r}")

    projects = fm.get("projects") or []
    if not isinstance(projects, list):
        findings.err(f"{rel}: projects must be a list")
        projects = []
    for proj in projects:
        if proj not in manifest["allowed_projects"]:
            findings.err(f"{rel}: unknown project identifier {proj!r}")

    sections = headings_and_sections(body)
    for required in manifest["required_headings"]:
        if required not in sections:
            findings.err(f"{rel}: missing required heading ## {required}")
    for required in manifest["headings_must_be_nonempty"]:
        if required in sections and not nonempty(sections[required]):
            findings.err(f"{rel}: heading ## {required} must not be empty")

    agenda = sections.get("Exact 120-minute agenda", "")
    durs = parse_agenda_durations(agenda)
    if not durs:
        findings.err(f"{rel}: no agenda durations parsed")
    elif sum(durs) != 120:
        findings.err(f"{rel}: agenda durations {durs} sum to {sum(durs)}, not 120")
    else:
        mt = fm.get("meeting_type")
        if mt == "A" and durs != manifest["agenda_a"]:
            findings.err(f"{rel}: Meeting A durations must be {manifest['agenda_a']}, got {durs}")
        if mt == "B" and durs != manifest["agenda_b"]:
            findings.err(f"{rel}: Meeting B durations must be {manifest['agenda_b']}, got {durs}")

    active = fm.get("active_features") or []
    if active and "Rollback procedure" in sections and not nonempty(sections["Rollback procedure"]):
        findings.err(f"{rel}: active_features set but rollback guidance is empty")

    return fm


def iter_markdown_files() -> list[Path]:
    skip_parts = {".git"}
    files = []
    for path in ROOT.rglob("*.md"):
        if skip_parts.intersection(path.parts):
            continue
        files.append(path)
    return files


def resolve_internal(link: str, source: Path) -> Path | None:
    if link.startswith(("http://", "https://", "mailto:", "#")):
        return None
    raw = link.split("#", 1)[0]
    if not raw:
        return None
    return (source.parent / raw).resolve()


def check_internal_links(findings: Findings) -> None:
    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        for match in MD_LINK.finditer(text):
            target = match.group(2).strip()
            dest = resolve_internal(target, path)
            if dest is None:
                continue
            try:
                dest.relative_to(ROOT)
            except ValueError:
                findings.err(f"{rel}: link escapes repository: {target}")
                continue
            if not dest.exists():
                findings.err(f"{rel}: broken internal link {target}")


def check_github_path(url: str, token: str | None) -> tuple[bool, str]:
    m = GITHUB_BLOB.match(url.split("#", 1)[0])
    if not m:
        return True, "not a blob/tree path"
    owner, repo, ref, file_path = m.groups()
    api = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}?ref={ref}"
    req = urllib.request.Request(api, method="GET")
    req.add_header("User-Agent", "forge-curriculum-validator")
    req.add_header("Accept", "application/vnd.github+json")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            if 200 <= resp.status < 300:
                return True, "ok"
            return False, f"HTTP {resp.status}"
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return False, "404"
        if exc.code in (403, 429):
            return True, f"rate-limited HTTP {exc.code}"
        return False, f"HTTP {exc.code}"
    except urllib.error.URLError as exc:
        return True, f"network {exc.reason}"


def check_external_url(url: str) -> tuple[bool, str]:
    req = urllib.request.Request(url.split("#", 1)[0], method="HEAD")
    req.add_header("User-Agent", "forge-curriculum-validator")
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            if 200 <= resp.status < 400:
                return True, "ok"
            return False, f"HTTP {resp.status}"
    except urllib.error.HTTPError as exc:
        if exc.code in (403, 405, 429):
            # Some doc hosts reject HEAD; try GET range.
            return check_external_get(url)
        if exc.code == 404:
            return False, "404"
        return False, f"HTTP {exc.code}"
    except urllib.error.URLError as exc:
        return True, f"network {exc.reason}"


def check_external_get(url: str) -> tuple[bool, str]:
    req = urllib.request.Request(url.split("#", 1)[0], method="GET")
    req.add_header("User-Agent", "forge-curriculum-validator")
    req.add_header("Range", "bytes=0-64")
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            if 200 <= resp.status < 400:
                return True, "ok"
            return False, f"HTTP {resp.status}"
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return False, "404"
        if exc.code in (403, 429):
            return True, f"skipped HTTP {exc.code}"
        return False, f"HTTP {exc.code}"
    except urllib.error.URLError as exc:
        return True, f"network {exc.reason}"


def check_external_links(findings: Findings, enabled: bool) -> None:
    if not enabled:
        findings.warn("external link checks skipped (--offline)")
        return
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    seen: dict[str, tuple[bool, str]] = {}
    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        for match in MD_LINK.finditer(text):
            url = match.group(2).strip()
            if not url.startswith("https://"):
                continue
            host_ok = (
                url.startswith("https://github.com/")
                or url.startswith("https://pedropathing.com/")
                or url.startswith("https://raw.githubusercontent.com/")
            )
            if not host_ok:
                continue
            if url not in seen:
                if GITHUB_BLOB.match(url.split("#", 1)[0]):
                    seen[url] = check_github_path(url, token)
                else:
                    seen[url] = check_external_url(url)
            ok, reason = seen[url]
            if not ok:
                findings.err(f"{rel}: invalid external link {url} ({reason})")
            elif reason.startswith("rate-limited") or reason.startswith("network") or reason.startswith("skipped"):
                findings.warn(f"{rel}: external link not fully verified {url} ({reason})")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate FORGE curriculum")
    parser.add_argument("--offline", action="store_true", help="skip external URL checks")
    args = parser.parse_args()

    findings = Findings()
    if not MANIFEST_PATH.is_file():
        print(f"error: missing {MANIFEST_PATH}", file=sys.stderr)
        return 2
    manifest = load_manifest()
    calendar_path = ROOT / manifest["calendar_file"]
    if not calendar_path.is_file():
        findings.err(f"missing {calendar_path.relative_to(ROOT)}")
        print_report(findings)
        return 1
    calendar = yaml.safe_load(calendar_path.read_text(encoding="utf-8"))
    if not isinstance(calendar, dict):
        findings.err("calendar.yaml must be a mapping")
        print_report(findings)
        return 1

    validate_calendar(calendar, manifest, findings)

    seen_ids = []
    for row in calendar.get("sessions") or []:
        if not isinstance(row, dict) or not row.get("file"):
            continue
        path = ROOT / manifest["season_dir"] / row["file"]
        if not path.is_file():
            continue
        fm = validate_session(path, row, manifest, findings)
        sid = fm.get("id") or row.get("id")
        if sid in seen_ids:
            findings.err(f"duplicate session id {sid}")
        else:
            seen_ids.append(sid)

    check_internal_links(findings)
    check_external_links(findings, enabled=not args.offline)

    print_report(findings)
    return 1 if findings.errors else 0


def print_report(findings: Findings) -> None:
    for msg in findings.warnings:
        print(f"warning: {msg}")
    for msg in findings.errors:
        print(f"error: {msg}")
    print(
        f"{len(findings.errors)} error(s), {len(findings.warnings)} warning(s)"
    )


if __name__ == "__main__":
    sys.exit(main())
