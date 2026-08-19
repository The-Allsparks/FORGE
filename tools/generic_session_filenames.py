#!/usr/bin/env python3
"""Rename session files to {ID}-meeting-{a|b|s|k|e}.md and shuffle post-Kickoff topics."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SESSIONS = ROOT / "season/2026-2027-biobuzz/sessions"
CALENDAR = ROOT / "season/2026-2027-biobuzz/calendar.yaml"

SUFFIX = {"A": "a", "B": "b", "S": "s", "K": "k", "E": "e"}

# calendar row: id, date, mt, phase, checkpoint, title
ROWS = [
    ("P001", "2026-08-17", "A", "preseason", "none", "Onboarding, parts organization, safety, and sponsor stewardship"),
    ("P002", "2026-08-19", "S", "preseason", "none", "Sponsor stewardship and chassis foundation"),
    ("P003", "2026-08-24", "A", "preseason", "none", "Modified Strafer drivetrain installation"),
    ("P004", "2026-08-26", "S", "preseason", "none", "Electrical foundation and power path"),
    ("P005", "2026-08-31", "A", "preseason", "none", "Bring-up, system map, and evidence"),
    ("P006", "2026-09-04", "B", "preseason", "none", "Driver baseline and chassis reliability"),
    ("P007", "2026-09-07", "A", "preseason", "none", "Reusable mechanism laboratory"),
    ("P008", "2026-09-11", "B", "preseason", "none", "Kickoff readiness review"),
    ("K001", "2026-09-12", "K", "kickoff", "kickoff", "BIOBUZZ Kickoff analysis and minimum viable robot"),
    ("S001", "2026-09-14", "A", "kickoff-to-clinic", "clinic", "Post-Kickoff MVP build and season execution"),
    ("S002", "2026-09-18", "B", "kickoff-to-clinic", "clinic", "MVP teleop tuning and driver reps"),
    ("S003", "2026-09-21", "A", "kickoff-to-clinic", "clinic", "Pedro Pathing conventional autonomous"),
    ("S004", "2026-09-25", "B", "kickoff-to-clinic", "clinic", "ViDAR camera geometry and one-camera observation"),
    ("S005", "2026-09-28", "A", "kickoff-to-clinic", "clinic", "BEACON communications freshness and recovery"),
    ("S006", "2026-10-02", "B", "kickoff-to-clinic", "clinic", "ViDAR game-relevant detection"),
    ("S007", "2026-10-05", "A", "kickoff-to-clinic", "clinic", "MIMIC interlocks"),
    ("S008", "2026-10-09", "B", "kickoff-to-clinic", "clinic", "Clinic and scrimmage preparation"),
    ("S009", "2026-10-12", "A", "reliability-sprint", "clinic", "Clinic retrospective and reliability sprint"),
    ("S010", "2026-10-16", "B", "reliability-sprint", "league-1s-2s", "ECHO cue vocabulary and off-robot driver lab"),
    ("S011", "2026-10-19", "A", "reliability-sprint", "league-1s-2s", "Integrated failure injection"),
    ("S012", "2026-10-23", "B", "reliability-sprint", "league-1s-2s", "League meet 1S/2S preparation"),
    ("S013", "2026-10-26", "A", "reliability-sprint", "league-1s-2s", "Full match simulation"),
    ("S014", "2026-10-30", "B", "reliability-sprint", "league-1s-2s", "HELM intent-tree vocabulary"),
    ("S015", "2026-11-02", "A", "league-development", "league-1s-2s", "HELM shadow recommendations"),
    ("S016", "2026-11-06", "B", "league-development", "league-1s-2s", "Meeting B — driver and auto reps"),
    ("S017", "2026-11-09", "A", "league-development", "league-3s-4s", "Meeting A — mechanism of the week"),
    ("S018", "2026-11-13", "B", "league-development", "league-3s-4s", "Meeting B — driver and auto reps"),
    ("S019", "2026-11-16", "A", "league-development", "league-3s-4s", "Meeting A — mechanism of the week"),
    ("S020", "2026-11-20", "B", "league-development", "league-3s-4s", "Meeting B — driver and auto reps"),
    ("S021", "2026-11-23", "A", "league-development", "league-3s-4s", "Meeting A — mechanism of the week"),
    ("S022", "2026-11-30", "A", "league-development", "league-3s-4s", "Meeting A — mechanism of the week"),
    ("S023", "2026-12-04", "B", "league-development", "league-3s-4s", "Meeting B — driver and auto reps"),
    ("S024", "2026-12-07", "A", "adversity-simulations", "league-3s-4s", "Meeting A — adversity drill"),
    ("S025", "2026-12-11", "B", "adversity-simulations", "league-3s-4s", "Meeting B — driver and auto reps"),
    ("S026", "2026-12-14", "A", "adversity-simulations", "league-5s-6s", "Meeting A — adversity drill"),
    ("S027", "2026-12-18", "B", "adversity-simulations", "league-5s-6s", "Meeting B — driver and auto reps"),
    ("S028", "2026-12-21", "A", "adversity-simulations", "league-5s-6s", "Meeting A — adversity drill"),
    ("S029", "2026-12-28", "A", "adversity-simulations", "league-5s-6s", "Meeting A — adversity drill"),
    ("S030", "2027-01-04", "A", "adversity-simulations", "league-5s-6s", "Meeting A — adversity drill"),
    ("S031", "2027-01-08", "B", "adversity-simulations", "league-5s-6s", "Meeting B — driver and auto reps"),
    ("S032", "2027-01-11", "A", "feature-freeze", "league-tournament", "Meeting A — pre-tournament build"),
    ("S033", "2027-01-15", "B", "feature-freeze", "league-tournament", "Meeting B — mock match reps"),
    ("S034", "2027-01-18", "A", "feature-freeze", "league-tournament", "Tournament feature freeze"),
    ("E004", "2027-01-22", "E", "feature-freeze", "league-tournament", "League Tournament — day 1 (no regular meeting)"),
    ("S036", "2027-01-25", "A", "feature-freeze", "league-tournament", "Meeting A — post-tournament repair"),
    ("S037", "2027-01-29", "B", "state-prep", "state-championship", "Meeting B — driver and auto reps"),
    ("S038", "2027-02-01", "A", "state-prep", "state-championship", "Meeting A — state prep build"),
    ("S039", "2027-02-05", "B", "state-prep", "state-championship", "Meeting B — mock match reps"),
    ("S040", "2027-02-08", "A", "state-prep", "state-championship", "State preparation"),
    ("S041", "2027-02-12", "B", "state-prep", "state-championship", "Meeting B — final reps"),
    ("S042", "2027-02-15", "A", "state-prep", "state-championship", "Meeting A — final build window"),
    ("E005", "2027-02-19", "E", "state-prep", "state-championship", "Nevada State Championship — day 1 (contingent)"),
]

# target_id -> source basename (without path); None = generate new; "cadence" = generic stub
CONTENT_SRC: dict[str, str | None] = {
    "S001": None,
    "S002": "P006-driver-baseline.md",
    "S003": "S003-pedro-conventional-auto.md",
    "S004": "S001-vidar-one-camera.md",
    "S005": "S002-beacon-freshness-recovery.md",
    "S006": "S004-vidar-game-detection.md",
    "S007": "S005-mimic-interlocks.md",
    "S008": "S008-clinic-scrimmage-prep.md",
    "S009": "S009-event-retrospective.md",
    "S010": "S006-echo-cue-vocabulary.md",
    "S011": "S007-integrated-failure-injection.md",
    "S012": "S012-league-meet-prep.md",
    "S013": "S013-full-match-simulation.md",
    "S014": "S010-helm-intent-vocabulary.md",
    "S015": "S011-helm-shadow.md",
    "S034": "S034-tournament-feature-freeze.md",
    "S040": "S040-state-preparation.md",
    "E004": "E004-league-tournament-day1.md",
    "E005": "E005-state-championship-day1.md",
    "K001": "K001-kickoff-biobuzz.md",
}

for i in range(1, 9):
    CONTENT_SRC[f"P{i:03d}"] = {
        1: "P001-onboarding-parts-safety-sponsors.md",
        2: "P002-chassis-sponsor-cards.md",
        3: "P003-modified-drivetrain-install.md",
        4: "P004-electrical-foundation.md",
        5: "P005-bring-up-system-map-evidence.md",
        6: "P006-driver-baseline.md",
        7: "P007-mechanism-laboratory.md",
        8: "P008-kickoff-readiness-review.md",
    }[i]

CADENCE_IDS = {
    "S016", "S017", "S018", "S019", "S020", "S021", "S022", "S023",
    "S024", "S025", "S026", "S027", "S028", "S029", "S030", "S031",
    "S032", "S033", "S036", "S037", "S038", "S039", "S041", "S042",
}


def target_name(sid: str, mt: str) -> str:
    return f"{sid}-meeting-{SUFFIX[mt]}.md"


def patch_front_matter(text: str, sid: str, title: str, date: str, mt: str, phase: str, checkpoint: str) -> str:
    text = re.sub(r"^id: .+$", f"id: {sid}", text, count=1, flags=re.MULTILINE)
    text = re.sub(r'^title: ".+"', f'title: "{title}"', text, count=1, flags=re.MULTILINE)
    text = re.sub(r"^date: .+$", f"date: {date}", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"^meeting_type: .+$", f"meeting_type: {mt}", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"^season_phase: .+$", f"season_phase: {phase}", text, count=1, flags=re.MULTILINE)
    if re.search(r"^event_checkpoint:", text, flags=re.MULTILINE):
        text = re.sub(r"^event_checkpoint: .+$", f"event_checkpoint: {checkpoint}", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"^# [A-Z0-9]+ —", f"# {sid} —", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"^\| Session ID \| .+ \|", f"| Session ID | {sid} |", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"^\| Title \| .+ \|", f"| Title | {title} |", text, count=1, flags=re.MULTILINE)
    text = re.sub(
        r"^\| Calendar date \| .+ \|",
        f"| Calendar date | {date} (planning input; 4:00–6:00 PM unless Kickoff/event) |",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    text = re.sub(r"^\| Meeting type \| .+ \|", f"| Meeting type | {mt} |", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"^\| Season phase \| .+ \|", f"| Season phase | {phase} |", text, count=1, flags=re.MULTILINE)
    if "| Event checkpoint |" in text:
        text = re.sub(r"^\| Event checkpoint \| .+ \|", f"| Event checkpoint | {checkpoint} |", text, count=1, flags=re.MULTILINE)
    return text


def s001_mvp_build() -> str:
    return patch_front_matter(
        """---
id: S001
title: "Post-Kickoff MVP build and season execution"
date: 2026-09-14
meeting_type: A
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: complete
difficulty: Integration
projects: [TRACE]
active_features: []
---

# S001 — Post-Kickoff MVP build and season execution

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S001 |
| Title | Post-Kickoff MVP build and season execution |
| Calendar date | 2026-09-14 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | First shop meeting after K001 |
| Meeting type | A |
| Season phase | kickoff-to-clinic |
| Event checkpoint | clinic |
| Difficulty | Integration |

## Driving question

Did we leave Kickoff with a buildable MVP — and does today's work move **that** robot forward, not a side quest?

## Student-facing objective

Students will translate K001 outputs into shop action: confirm mechanism owners, update `calendar.yaml` **titles** (not session IDs or filenames), start or continue MVP construction, and record what is proven vs assumed from preseason experiments.

## Robot outcome

- Visible MVP mechanism progress (substantial, not cosmetic)
- Owner list posted with next-test column in [readiness-dashboard.md](../readiness-dashboard.md)
- Optional: edit session **titles** in `calendar.yaml` for upcoming weeks — **never rename** `P001-meeting-a.md`-style files

## Prerequisites

- [K001-meeting-k.md](K001-meeting-k.md) outputs: MVP, brainstorm, decision record if used
- [kickoff-replan-guide.md](../kickoff-replan-guide.md)
- [preseason-kickoff-gate.md](../docs/preseason-kickoff-gate.md) if tower/capstan/transport is in debate
- Strafer drivetrain from preseason (P002–P006)

## Vocabulary

MVP · owner · planning-input title · evidence vs assumption · rollback

## Safety concerns

- Mentor present for powered tests
- No library enablement because Kickoff was exciting
- DS disable path before any enable

## Required hardware

- MVP mechanism materials from Kickoff list
- Strafer chassis; hand tools; notebook

## Required software

- Minimal TeleOp only if needed for mechanism clearance checks
- TRACE optional for build milestones (≤10 min)

## Preparation required before the meeting

- Print mechanism owner list from K001
- Mentors: identify **one** scoring subsystem for today's 75-minute block
- Read [preseason-software-allocation.md](../docs/preseason-software-allocation.md) — software cap lifts after Kickoff but still serves the robot

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Review K001 MVP, owners, and preseason evidence; safety; **this meeting is about the season robot** |
| 75 | Construction | Build the highest-priority MVP subsystem; integrate with Strafer only as the MVP requires |
| 25 | Integration | TRACE or notebook: record build milestone; update dashboard; **optional:** edit upcoming `calendar.yaml` titles to name this week's mechanism |
| 10 | Closeout | Explain-back: what shipped vs what is still assumption; assign S002 teleop checks |

## Mentor demonstration

Two minutes: show K001 MVP written goal vs one physical part that proves progress today.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Lead the 75-minute construction block |
| Electrical | Power path for new mechanism; labeled wires |
| Programming | TeleOp trim only if blocking mechanical progress |
| Drive team | Clearance checks; call out driver visibility |
| Documentation | Dashboard update; photo of today's subsystem |

## Integrated build or test activity

Construction **is** the session. No ViDAR/HELM/ECHO lecture block today.

## Failure-injection scenario

Mentor asks: "Does this part serve the K001 MVP or a leftover preseason experiment?" Students defend with K001 decision record or park the work.

## Evidence to collect

- Photo of MVP progress
- Dashboard row updates with owners
- Note linking preseason P007 data to today's design choice (if applicable)

## Student explain-back questions

1. What is the MVP scoring action from K001?
2. Who owns each subsystem?
3. What preseason evidence informed today's build?
4. What library stays **off** until the MVP drives?

## Assessment or exit check

Mechanism progress is visible; owners named; no competitor treated a library session as today's priority.

## Portfolio or engineering-notebook artifact

Before/after photo of MVP subsystem with owner initials and K001 task reference.

## Competition enablement impact

None. Build and document only.

## Rollback procedure

Remove untested mechanism additions; return to Strafer-only teleop if integration fails.

## Cleanup requirements

Robot safe; floor clear; tools stored.

## Next-session preparation

- S002: teleop and driver reps on the MVP configuration
- Charge batteries; list teleop blockers

## Hardware-unavailable fallback

Cardboard MVP prototype and full K001 mapping table on paper.

## Robot-unavailable simulation option

Walk through teleop commands and mechanism states without Hub power.

## Links to authoritative project documentation

- [kickoff-replan-guide.md](../kickoff-replan-guide.md)
- [preseason-kickoff-gate.md](../docs/preseason-kickoff-gate.md)
- [readiness-dashboard.md](../readiness-dashboard.md)
- [docs/safety-and-enablement.md](../../../docs/safety-and-enablement.md)

## Mentor notes

**Filename stays `S001-meeting-a.md`.** Change the `title` in front matter and calendar when this week's focus shifts. First shop meeting after Kickoff is for **building the season robot**, not a standalone library lab.
""",
        "S001",
        "Post-Kickoff MVP build and season execution",
        "2026-09-14",
        "A",
        "kickoff-to-clinic",
        "clinic",
    )


def adapt_s002_from_p006(text: str) -> str:
    text = text.replace("P006", "@@OWN@@")
    text = text.replace("P005", "S001")
    text = text.replace("P007/K001", "S003")
    text = text.replace("P007", "S003")
    text = text.replace("P008", "K001")
    text = text.replace("Preseason week 1", "First Meeting B after Kickoff")
    text = text.replace("Preseason success = **reliable Strafer**, not BIOBUZZ scoring.", "Success = **MVP teleop** on the Kickoff robot configuration, not library features.")
    text = text.replace(
        "Can every student enable, drive all mecanum directions, stop on command, and produce a measurable baseline?",
        "Can every driver operate the **MVP teleop** configuration safely and produce a measurable baseline?",
    )
    text = text.replace(
        'title: "Driver baseline and chassis reliability"',
        'title: "MVP teleop tuning and driver reps"',
    )
    text = text.replace(
        "# P006 — Driver baseline and chassis reliability",
        "# S002 — MVP teleop tuning and driver reps",
    )
    text = text.replace("Strafer drivetrain from P002–P004", "Robot as built through S001 (Strafer + MVP progress)")
    text = text.replace("@@OWN@@", "S002")
    return text


def cadence_body(sid: str, title: str, date: str, mt: str, phase: str, checkpoint: str) -> str:
    agenda_a = "| 10 | Opening | Goals; safety; read **title** in calendar for this week's mechanism |\n| 75 | Construction | [cadence-meeting-a.md](../../../templates/cadence-meeting-a.md) |\n| 25 | Integration | TRACE / passive library touchpoint on today's mechanism |\n| 10 | Closeout | Explain-back; dashboard; cleanup |"
    agenda_b = "| 10 | Opening | Review logs; repair priorities |\n| 35 | Repair / tune / program | Highest-priority fix from last drive or event |\n| 55 | Driving reps | Driver and conventional auto repetitions |\n| 20 | Closeout | Inspection checklist; dashboard; cleanup |"
    agenda = agenda_a if mt == "A" else agenda_b
    letter = mt
    return f"""---
id: {sid}
title: "{title}"
date: {date}
meeting_type: {mt}
season_phase: {phase}
event_checkpoint: {checkpoint}
status: complete
difficulty: Developing
projects: [TRACE]
active_features: []
---

# {sid} — {title}

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | {sid} |
| Title | {title} |
| Calendar date | {date} (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Meeting type | {letter} |
| Season phase | {phase} |
| Event checkpoint | {checkpoint} |
| Difficulty | Developing |

## Driving question

What is the highest-value robot improvement we can finish today without breaking rollback?

## Student-facing objective

Students will run Meeting {letter} from the season template. Update the **calendar title** when the week's mechanism changes — do not rename this file.

## Robot outcome

- Documented progress on the focus named in `calendar.yaml` `title` for {sid}
- No new active features without evidence

## Prerequisites

- [calendar.yaml](../calendar.yaml) row for {sid}
- [readiness-dashboard.md](../readiness-dashboard.md)

## Vocabulary

meeting-a · meeting-b · planning-input title · rollback

## Safety concerns

- Mentor present for powered tests
- DS disable before enable

## Required hardware

- Robot as it exists; pit checklist

## Required software

- Only what serves today's mechanism ([student-install.md](../../../docs/student-install.md))

## Preparation required before the meeting

- Review prior meeting repair list

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
{agenda}

## Mentor demonstration

Follow [cadence-meeting-{'a' if mt == 'A' else 'b'}.md](../../../templates/cadence-meeting-{'a' if mt == 'A' else 'b'}.md).

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Construction or repair block |
| Electrical | Wiring fixes |
| Programming | Integration minutes only |
| Drive team | Driving reps block |
| Documentation | Dashboard + notebook |

## Integrated build or test activity

Cadence block — customize via calendar **title**, not filename.

## Failure-injection scenario

Mentor names one subsystem to disable; students state rollback before continuing.

## Evidence to collect

- Notebook or TRACE entry tied to today's physical work

## Student explain-back questions

1. What shipped today?
2. What stays disabled and why?
3. What is the next test?

## Assessment or exit check

Dashboard updated; cleanup complete.

## Portfolio or engineering-notebook artifact

Photo or log line tied to mechanism work.

## Competition enablement impact

None unless a separate decision record exists.

## Rollback procedure

Disable optional systems independently per [student-install.md](../../../docs/student-install.md).

## Cleanup requirements

Robot safe; battery stored.

## Next-session preparation

- Read next numbered session in [sessions/](.)

## Hardware-unavailable fallback

Paper diagram + verbal walkthrough.

## Robot-unavailable simulation option

Desktop or paper-only per project manuals.

## Links to authoritative project documentation

- [templates/cadence-meeting-{'a' if mt == 'A' else 'b'}.md](../../../templates/cadence-meeting-{'a' if mt == 'A' else 'b'}.md)
- [season-plan.md](../season-plan.md)

## Mentor notes

**Filename is fixed:** `{sid}-meeting-{SUFFIX[mt]}.md`. Edit `title` in this file and `calendar.yaml` when the week's topic changes.
"""


def find_source(src_name: str) -> Path | None:
    p = SESSIONS / src_name
    if p.exists():
        return p
    # try glob by prefix
    stem = src_name.replace(".md", "")
    for f in SESSIONS.glob("*.md"):
        if f.name == src_name or f.name.endswith(src_name.split("-", 1)[-1]):
            return f
    return None


def main() -> None:
    row_by_id = {r[0]: r for r in ROWS}
    allowed = {target_name(sid, mt) for sid, _, mt, *_ in ROWS}

    # load all existing content by path
    existing = {p.name: p.read_text(encoding="utf-8") for p in SESSIONS.glob("*.md")}

    # delete everything in sessions (clean slate for targets)
    for p in SESSIONS.glob("*.md"):
        p.unlink()

    for sid, date, mt, phase, checkpoint, title in ROWS:
        fname = target_name(sid, mt)
        if sid == "S001":
            body = s001_mvp_build()
        elif sid in CADENCE_IDS:
            body = cadence_body(sid, title, date, mt, phase, checkpoint)
        else:
            src_key = CONTENT_SRC.get(sid)
            if src_key and src_key in existing:
                raw = existing[src_key]
            elif src_key:
                raw = existing.get(src_key, "")
                if not raw:
                    raise SystemExit(f"missing source {src_key} for {sid}")
            else:
                raise SystemExit(f"no source for {sid}")
            if sid == "S002":
                raw = adapt_s002_from_p006(raw)
            body = patch_front_matter(raw, sid, title, date, mt, phase, checkpoint)
        (SESSIONS / fname).write_text(body, encoding="utf-8")
        print("wrote", fname)

    # rewrite calendar file paths
    cal_lines = CALENDAR.read_text(encoding="utf-8").splitlines()
    out = []
    i = 0
    while i < len(cal_lines):
        line = cal_lines[i]
        if line.strip().startswith("- id:"):
            sid = line.split(":", 1)[1].strip()
            if sid in row_by_id:
                _, date, mt, phase, checkpoint, title = row_by_id[sid]
                out.append(line)
                i += 1
                while i < len(cal_lines) and not cal_lines[i].strip().startswith("- id:"):
                    l = cal_lines[i]
                    if l.strip().startswith("date:"):
                        out.append(f'    date: "{date}"')
                    elif l.strip().startswith("meeting_type:"):
                        out.append(f"    meeting_type: {mt}")
                    elif l.strip().startswith("season_phase:"):
                        out.append(f"    season_phase: {phase}")
                    elif l.strip().startswith("event_checkpoint:"):
                        out.append(f"    event_checkpoint: {checkpoint}")
                    elif l.strip().startswith("file:"):
                        out.append(f"    file: sessions/{target_name(sid, mt)}")
                    elif l.strip().startswith("title:"):
                        out.append(f"    title: {title}")
                    else:
                        out.append(l)
                    i += 1
                continue
        out.append(line)
        i += 1
    CALENDAR.write_text("\n".join(out) + "\n", encoding="utf-8")
    print("updated calendar.yaml")


if __name__ == "__main__":
    main()
