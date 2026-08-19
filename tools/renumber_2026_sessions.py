#!/usr/bin/env python3
"""One-shot renumber: P001-P008, K001, S001-S043 (+ E004/E005). Run from repo root."""
from __future__ import annotations

import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SESSIONS = ROOT / "season/2026-2027-biobuzz/sessions"

# old basename -> new basename (content-bearing files only)
RENAME_MAP = {
    "P000-onboarding-parts-safety-sponsors.md": "P001-onboarding-parts-safety-sponsors.md",
    "P001-chassis-sponsor-cards.md": "P002-chassis-sponsor-cards.md",
    "P002-modified-drivetrain-install.md": "P003-modified-drivetrain-install.md",
    "P003-electrical-foundation.md": "P004-electrical-foundation.md",
    "S001-bring-up-system-map-evidence.md": "P005-bring-up-system-map-evidence.md",
    "S002-driver-baseline.md": "P006-driver-baseline.md",
    "P004-mechanism-laboratory.md": "P007-mechanism-laboratory.md",
    "P005-kickoff-readiness-review.md": "P008-kickoff-readiness-review.md",
    "SK01-kickoff-biobuzz.md": "K001-kickoff-biobuzz.md",
    "S009-vidar-one-camera.md": "S001-vidar-one-camera.md",
    "S010-beacon-freshness-recovery.md": "S002-beacon-freshness-recovery.md",
    "S011-pedro-conventional-auto.md": "S003-pedro-conventional-auto.md",
    "S012-vidar-game-detection.md": "S004-vidar-game-detection.md",
    "S013-mimic-interlocks.md": "S005-mimic-interlocks.md",
    "S014-echo-cue-vocabulary.md": "S006-echo-cue-vocabulary.md",
    "S015-integrated-failure-injection.md": "S007-integrated-failure-injection.md",
    "S016-clinic-scrimmage-prep.md": "S008-clinic-scrimmage-prep.md",
    "S017-event-retrospective.md": "S009-event-retrospective.md",
    "S018-helm-intent-vocabulary.md": "S010-helm-intent-vocabulary.md",
    "S019-helm-shadow.md": "S011-helm-shadow.md",
    "S020-league-meet-prep.md": "S012-league-meet-prep.md",
    "S021-full-match-simulation.md": "S013-full-match-simulation.md",
    "S022-tournament-feature-freeze.md": "S034-tournament-feature-freeze.md",
    "S023-state-preparation.md": "S040-state-preparation.md",
}

VESTIGIAL = [
    "S001-system-map-safety-trace.md",
    "S002-drivetrain-driver-baseline.md",
    "S003-amper-passive-power.md",
    "S004-mimic-mechanism-states.md",
    "S005-vidar-one-camera.md",
    "S006-beacon-freshness-recovery.md",
    "S007-pedro-conventional-auto.md",
    "S008-vidar-game-detection.md",
    "S009-mimic-interlocks.md",
    "S010-echo-cue-vocabulary.md",
    "S011-integrated-failure-injection.md",
    "S012-clinic-scrimmage-prep.md",
    "S013-event-retrospective.md",
    "S014-helm-intent-vocabulary.md",
    "S015-helm-shadow.md",
    "S016-league-meet-prep.md",
    "S017-full-match-simulation.md",
    "S018-tournament-feature-freeze.md",
    "S019-state-preparation.md",
]

CALENDAR_ROWS = [
    ("P001", "2026-08-17", "A", "preseason", "none", "P001-onboarding-parts-safety-sponsors.md", "Onboarding, parts organization, safety, and sponsor stewardship"),
    ("P002", "2026-08-19", "S", "preseason", "none", "P002-chassis-sponsor-cards.md", "Sponsor stewardship and chassis foundation"),
    ("P003", "2026-08-24", "A", "preseason", "none", "P003-modified-drivetrain-install.md", "Modified Strafer drivetrain installation"),
    ("P004", "2026-08-26", "S", "preseason", "none", "P004-electrical-foundation.md", "Electrical foundation and power path"),
    ("P005", "2026-08-31", "A", "preseason", "none", "P005-bring-up-system-map-evidence.md", "Bring-up, system map, and evidence"),
    ("P006", "2026-09-04", "B", "preseason", "none", "P006-driver-baseline.md", "Driver baseline and chassis reliability"),
    ("P007", "2026-09-07", "A", "preseason", "none", "P007-mechanism-laboratory.md", "Reusable mechanism laboratory"),
    ("P008", "2026-09-11", "B", "preseason", "none", "P008-kickoff-readiness-review.md", "Kickoff readiness review"),
    ("K001", "2026-09-12", "K", "kickoff", "kickoff", "K001-kickoff-biobuzz.md", "BIOBUZZ Kickoff analysis and minimum viable robot"),
    ("S001", "2026-09-14", "A", "kickoff-to-clinic", "clinic", "S001-vidar-one-camera.md", "ViDAR camera geometry and one-camera observation"),
    ("S002", "2026-09-18", "B", "kickoff-to-clinic", "clinic", "S002-beacon-freshness-recovery.md", "BEACON communications freshness and recovery"),
    ("S003", "2026-09-21", "A", "kickoff-to-clinic", "clinic", "S003-pedro-conventional-auto.md", "Pedro Pathing conventional autonomous"),
    ("S004", "2026-09-25", "B", "kickoff-to-clinic", "clinic", "S004-vidar-game-detection.md", "ViDAR game-relevant detection"),
    ("S005", "2026-09-28", "A", "kickoff-to-clinic", "clinic", "S005-mimic-interlocks.md", "MIMIC interlocks"),
    ("S006", "2026-10-02", "B", "kickoff-to-clinic", "clinic", "S006-echo-cue-vocabulary.md", "ECHO cue vocabulary and off-robot driver lab"),
    ("S007", "2026-10-05", "A", "kickoff-to-clinic", "clinic", "S007-integrated-failure-injection.md", "Integrated failure injection"),
    ("S008", "2026-10-09", "B", "kickoff-to-clinic", "clinic", "S008-clinic-scrimmage-prep.md", "Clinic and scrimmage preparation"),
    ("S009", "2026-10-12", "A", "reliability-sprint", "clinic", "S009-event-retrospective.md", "Clinic retrospective and reliability sprint"),
    ("S010", "2026-10-16", "B", "reliability-sprint", "league-1s-2s", "S010-helm-intent-vocabulary.md", "HELM intent-tree vocabulary"),
    ("S011", "2026-10-19", "A", "reliability-sprint", "league-1s-2s", "S011-helm-shadow.md", "HELM shadow recommendations"),
    ("S012", "2026-10-23", "B", "reliability-sprint", "league-1s-2s", "S012-league-meet-prep.md", "League meet 1S/2S preparation"),
    ("S013", "2026-10-26", "A", "reliability-sprint", "league-1s-2s", "S013-full-match-simulation.md", "Full match simulation"),
    ("S014", "2026-10-30", "B", "reliability-sprint", "league-1s-2s", "S014-cadence-meeting-b.md", "Cadence Meeting B — reliability reps"),
    ("S015", "2026-11-02", "A", "league-development", "league-1s-2s", "S015-cadence-meeting-a.md", "Cadence Meeting A — mechanism of the week"),
    ("S016", "2026-11-06", "B", "league-development", "league-1s-2s", "S016-cadence-meeting-b.md", "Cadence Meeting B — driver and auto reps"),
    ("S017", "2026-11-09", "A", "league-development", "league-3s-4s", "S017-cadence-meeting-a.md", "Cadence Meeting A — mechanism of the week"),
    ("S018", "2026-11-13", "B", "league-development", "league-3s-4s", "S018-cadence-meeting-b.md", "Cadence Meeting B — driver and auto reps"),
    ("S019", "2026-11-16", "A", "league-development", "league-3s-4s", "S019-cadence-meeting-a.md", "Cadence Meeting A — mechanism of the week"),
    ("S020", "2026-11-20", "B", "league-development", "league-3s-4s", "S020-cadence-meeting-b.md", "Cadence Meeting B — driver and auto reps"),
    ("S021", "2026-11-23", "A", "league-development", "league-3s-4s", "S021-cadence-meeting-a.md", "Cadence Meeting A — mechanism of the week"),
    ("S022", "2026-11-30", "A", "league-development", "league-3s-4s", "S022-cadence-meeting-a.md", "Cadence Meeting A — mechanism of the week"),
    ("S023", "2026-12-04", "B", "league-development", "league-3s-4s", "S023-cadence-meeting-b.md", "Cadence Meeting B — driver and auto reps"),
    ("S024", "2026-12-07", "A", "adversity-simulations", "league-3s-4s", "S024-cadence-meeting-a.md", "Cadence Meeting A — adversity drill"),
    ("S025", "2026-12-11", "B", "adversity-simulations", "league-3s-4s", "S025-cadence-meeting-b.md", "Cadence Meeting B — driver and auto reps"),
    ("S026", "2026-12-14", "A", "adversity-simulations", "league-5s-6s", "S026-cadence-meeting-a.md", "Cadence Meeting A — adversity drill"),
    ("S027", "2026-12-18", "B", "adversity-simulations", "league-5s-6s", "S027-cadence-meeting-b.md", "Cadence Meeting B — driver and auto reps"),
    ("S028", "2026-12-21", "A", "adversity-simulations", "league-5s-6s", "S028-cadence-meeting-a.md", "Cadence Meeting A — adversity drill"),
    ("S029", "2026-12-28", "A", "adversity-simulations", "league-5s-6s", "S029-cadence-meeting-a.md", "Cadence Meeting A — adversity drill"),
    ("S030", "2027-01-04", "A", "adversity-simulations", "league-5s-6s", "S030-cadence-meeting-a.md", "Cadence Meeting A — adversity drill"),
    ("S031", "2027-01-08", "B", "adversity-simulations", "league-5s-6s", "S031-cadence-meeting-b.md", "Cadence Meeting B — driver and auto reps"),
    ("S032", "2027-01-11", "A", "feature-freeze", "league-tournament", "S032-cadence-meeting-a.md", "Cadence Meeting A — pre-tournament build"),
    ("S033", "2027-01-15", "B", "feature-freeze", "league-tournament", "S033-cadence-meeting-b.md", "Cadence Meeting B — mock match reps"),
    ("S034", "2027-01-18", "A", "feature-freeze", "league-tournament", "S034-tournament-feature-freeze.md", "Tournament feature freeze"),
    ("E004", "2027-01-22", "E", "feature-freeze", "league-tournament", "E004-league-tournament-day1.md", "League Tournament — day 1 (no regular meeting)"),
    ("S036", "2027-01-25", "A", "feature-freeze", "league-tournament", "S036-cadence-meeting-a.md", "Cadence Meeting A — post-tournament repair"),
    ("S037", "2027-01-29", "B", "state-prep", "state-championship", "S037-cadence-meeting-b.md", "Cadence Meeting B — driver and auto reps"),
    ("S038", "2027-02-01", "A", "state-prep", "state-championship", "S038-cadence-meeting-a.md", "Cadence Meeting A — state prep build"),
    ("S039", "2027-02-05", "B", "state-prep", "state-championship", "S039-cadence-meeting-b.md", "Cadence Meeting B — mock match reps"),
    ("S040", "2027-02-08", "A", "state-prep", "state-championship", "S040-state-preparation.md", "State preparation"),
    ("S041", "2027-02-12", "B", "state-prep", "state-championship", "S041-cadence-meeting-b.md", "Cadence Meeting B — final reps"),
    ("S042", "2027-02-15", "A", "state-prep", "state-championship", "S042-cadence-meeting-a.md", "Cadence Meeting A — final build window"),
    ("E005", "2027-02-19", "E", "state-prep", "state-championship", "E005-state-championship-day1.md", "Nevada State Championship — day 1 (contingent)"),
]

# Session ID replacements in body text (order matters — longest first)
ID_REPLACEMENTS = [
    ("SK01", "K001"),
    ("P000", "P001"),
    ("P008", "@@P008@@"),
    ("P007", "@@P007@@"),
    ("P006", "@@P006@@"),
    ("P005", "@@P005@@"),
    ("P004", "@@P004@@"),
    ("P003", "@@P003@@"),
    ("P002", "@@P002@@"),
    ("P001", "@@P001@@"),
    ("S023", "@@S023@@"),
    ("S022", "@@S022@@"),
    ("S021", "@@S021@@"),
    ("S020", "@@S020@@"),
    ("S019", "@@S019@@"),
    ("S018", "@@S018@@"),
    ("S017", "@@S017@@"),
    ("S016", "@@S016@@"),
    ("S015", "@@S015@@"),
    ("S014", "@@S014@@"),
    ("S013", "@@S013@@"),
    ("S012", "@@S012@@"),
    ("S011", "@@S011@@"),
    ("S010", "@@S010@@"),
    ("S009", "@@S009@@"),
    ("S008", "@@S008@@"),
    ("S007", "@@S007@@"),
    ("S006", "@@S006@@"),
    ("S005", "@@S005@@"),
    ("S004", "@@S004@@"),
    ("S003", "@@S003@@"),
    ("S002", "@@S002@@"),
    ("S001", "@@S001@@"),
]
UNPLACEHOLDER_TO_NEW = {
    "@@P001@@": "P001", "@@P002@@": "P002", "@@P003@@": "P003", "@@P004@@": "P004",
    "@@P005@@": "P005", "@@P006@@": "P006", "@@P007@@": "P007", "@@P008@@": "P008",
    "@@S001@@": "S001", "@@S002@@": "S002", "@@S003@@": "S003", "@@S004@@": "S004",
    "@@S005@@": "S005", "@@S006@@": "S006", "@@S007@@": "S007", "@@S008@@": "S008",
    "@@S009@@": "S009", "@@S010@@": "S010", "@@S011@@": "S011", "@@S012@@": "S012",
    "@@S013@@": "S013", "@@S014@@": "S014", "@@S015@@": "S015", "@@S016@@": "S016",
    "@@S017@@": "S017", "@@S018@@": "S018", "@@S019@@": "S019", "@@S020@@": "S020",
    "@@S021@@": "S021", "@@S022@@": "S022", "@@S023@@": "S023",
}
# Map old season id -> new (for content files after rename)
OLD_TO_NEW = {
    "P000": "P001", "P001": "P002", "P002": "P003", "P003": "P004",
    "P004": "P007", "P005": "P008",
    "S001": "P005", "S002": "P006",
    "SK01": "K001",
    "S009": "S001", "S010": "S002", "S011": "S003", "S012": "S004",
    "S013": "S005", "S014": "S006", "S015": "S007", "S016": "S008",
    "S017": "S009", "S018": "S010", "S019": "S011", "S020": "S012",
    "S021": "S013", "S022": "S034", "S023": "S040",
}

LINK_RENAMES = {
    "P000-onboarding-parts-safety-sponsors.md": "P001-onboarding-parts-safety-sponsors.md",
    "P001-chassis-sponsor-cards.md": "P002-chassis-sponsor-cards.md",
    "P002-modified-drivetrain-install.md": "P003-modified-drivetrain-install.md",
    "P003-electrical-foundation.md": "P004-electrical-foundation.md",
    "S001-bring-up-system-map-evidence.md": "P005-bring-up-system-map-evidence.md",
    "S002-driver-baseline.md": "P006-driver-baseline.md",
    "P004-mechanism-laboratory.md": "P007-mechanism-laboratory.md",
    "P005-kickoff-readiness-review.md": "P008-kickoff-readiness-review.md",
    "SK01-kickoff-biobuzz.md": "K001-kickoff-biobuzz.md",
    "S009-vidar-one-camera.md": "S001-vidar-one-camera.md",
    "S010-beacon-freshness-recovery.md": "S002-beacon-freshness-recovery.md",
    "S011-pedro-conventional-auto.md": "S003-pedro-conventional-auto.md",
    "S012-vidar-game-detection.md": "S004-vidar-game-detection.md",
    "S013-mimic-interlocks.md": "S005-mimic-interlocks.md",
    "S014-echo-cue-vocabulary.md": "S006-echo-cue-vocabulary.md",
    "S015-integrated-failure-injection.md": "S007-integrated-failure-injection.md",
    "S016-clinic-scrimmage-prep.md": "S008-clinic-scrimmage-prep.md",
    "S017-event-retrospective.md": "S009-event-retrospective.md",
    "S018-helm-intent-vocabulary.md": "S010-helm-intent-vocabulary.md",
    "S019-helm-shadow.md": "S011-helm-shadow.md",
    "S020-league-meet-prep.md": "S012-league-meet-prep.md",
    "S021-full-match-simulation.md": "S013-full-match-simulation.md",
    "S022-tournament-feature-freeze.md": "S034-tournament-feature-freeze.md",
    "S023-state-preparation.md": "S040-state-preparation.md",
}


def remap_text(text: str, own_id: str) -> str:
    own_ph = "@@OWN_ID@@"
    text = text.replace(own_id, own_ph)
    for old in sorted(OLD_TO_NEW.keys(), key=len, reverse=True):
        if old != own_id:
            text = text.replace(old, OLD_TO_NEW[old])
    for old, new in LINK_RENAMES.items():
        text = text.replace(old, new)
    return text.replace(own_ph, own_id)


def write_calendar() -> None:
    cal = ROOT / "season/2026-2027-biobuzz/calendar.yaml"
    lines = [
        "# 2026–2027 BIOBUZZ season calendar",
        "#",
        "# PLANNING INPUTS — verify if the FIRST Nevada calendar changes.",
        "# All regular shop meetings: 4:00–6:00 PM local (America/Los_Angeles).",
        "# Numbering: P001–P008 preseason · K001 Kickoff · S001+ official season · E### event days.",
        "",
        'season: "2026-2027"',
        "season_name: BIOBUZZ",
        "team: The Allsparks",
        "team_number: 36117",
        "timezone: America/Los_Angeles",
        'last_reviewed: "2026-08-19"',
        "dates_are_planning_inputs: true",
        "",
        "meeting_pattern:",
        "  meeting_a_weekday: Monday",
        "  meeting_b_weekday: Friday",
        "  duration_minutes: 120",
        "  start_time: \"16:00\"",
        "  end_time: \"18:00\"",
        "  notes: \"Wednesday preseason meetings (P002, P004) use meeting_type S. Event rows E004/E005 replace regular meetings on competition days.\"",
        "",
        "assumptions:",
        '  - "Treat ViDAR, AMPER, MIMIC, BEACON, TRACE, HELM, and ECHO as functionally complete for scheduling after the week of 2026-08-24."',
        '  - "Functional completeness for scheduling is not combined Control Hub acceptance. FORGE#4 remains the integration gate."',
        '  - "Preseason builds a capable team and reusable mechanism evidence — not a speculative BIOBUZZ tower or hopper."',
        '  - "BIOBUZZ game details are unknown until Kickoff 2026-09-12."',
        "",
        "events:",
        "  - id: kickoff",
        "    name: FTC Kickoff, Southern Nevada",
        '    date: "2026-09-12"',
        '    end_date: "2026-09-12"',
        "    verify: true",
        "  - id: clinic",
        "    name: Clinic / scrimmage",
        '    date: "2026-10-10"',
        '    end_date: "2026-10-10"',
        "    verify: true",
        "  - id: league-1s-2s",
        "    name: League Meets 1S and 2S",
        '    date: "2026-10-31"',
        '    end_date: "2026-10-31"',
        "    verify: true",
        "  - id: league-3s-4s",
        "    name: League Meets 3S and 4S",
        '    date: "2026-12-05"',
        '    end_date: "2026-12-05"',
        "    verify: true",
        "  - id: league-5s-6s",
        "    name: League Meets 5S and 6S",
        '    date: "2027-01-09"',
        '    end_date: "2027-01-09"',
        "    verify: true",
        "  - id: league-tournament",
        "    name: League Tournament",
        '    date: "2027-01-22"',
        '    end_date: "2027-01-23"',
        "    verify: true",
        "  - id: state-championship",
        "    name: Nevada State Championship",
        '    date: "2027-02-19"',
        '    end_date: "2027-02-20"',
        "    verify: true",
        '    contingent: "Only if the team advances."',
        "",
        "sessions:",
    ]
    for sid, dt, mt, phase, checkpoint, fname, title in CALENDAR_ROWS:
        lines.append(f"  - id: {sid}")
        lines.append(f'    date: "{dt}"')
        lines.append(f"    meeting_type: {mt}")
        lines.append(f"    season_phase: {phase}")
        lines.append(f"    event_checkpoint: {checkpoint}")
        lines.append(f"    file: sessions/{fname}")
        lines.append(f"    title: {title}")
    lines.extend([
        "",
        "cadence_windows:",
        "  - id: preseason",
        '    start: "2026-08-17"',
        '    end: "2026-09-11"',
        '    intent: P001–P008 — capable team, Strafer drivetrain, reusable mechanism experiments, ~30 min/week software cap.',
        "  - id: kickoff-to-clinic",
        '    start: "2026-09-12"',
        '    end: "2026-10-10"',
        "    intent: K001 MVP lock; S001–S008 minimum viable BIOBUZZ robot and clinic prep.",
        "  - id: reliability-sprint",
        '    start: "2026-10-12"',
        '    end: "2026-10-31"',
        "    intent: S009–S013 repairs, auto reps, driver practice; passive optional libraries.",
        "  - id: league-development",
        '    start: "2026-11-02"',
        '    end: "2026-12-05"',
        "    intent: S014–S023 match evidence and calibration; numbered cadence slots.",
        "  - id: adversity-simulations",
        '    start: "2026-12-07"',
        '    end: "2027-01-09"',
        "    intent: S024–S031 failure drills and full-match reps.",
        "  - id: feature-freeze",
        '    start: "2027-01-11"',
        '    end: "2027-01-23"',
        "    intent: S032–S034 mock competition; E004 League Tournament; no new active features.",
        "  - id: state-prep",
        '    start: "2027-01-25"',
        '    end: "2027-02-20"',
        "    intent: S036–S042 if advancing; E005 State Championship; evidenced improvements only.",
        "",
    ])
    cal.write_text("\n".join(lines), encoding="utf-8")
    print("wrote calendar.yaml")


def stub_session(sid: str, dt: str, mt: str, phase: str, checkpoint: str, title: str) -> str:
    agenda_a = "| 10 | Opening | Goals; safety; cadence intent for this week |\n| 75 | Construction | Mechanism of the week per [cadence-meeting-a.md](../../../templates/cadence-meeting-a.md) |\n| 25 | Integration | TRACE / passive library touchpoint on today's mechanism |\n| 10 | Closeout | Explain-back; dashboard; cleanup |"
    agenda_b = "| 10 | Opening | Review logs; repair priorities |\n| 35 | Repair / tune / program | Highest-priority fix from last drive or event |\n| 55 | Driving reps | Driver and conventional auto repetitions |\n| 20 | Closeout | Inspection checklist; dashboard; cleanup |"
    agenda = agenda_a if mt == "A" else agenda_b
    slug = sid.lower()
    return f"""---
id: {sid}
title: "{title}"
date: {dt}
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
| Calendar date | {dt} (planning input; Monday/Friday 4:00–6:00 PM unless noted) |
| Meeting type | {mt} |
| Season phase | {phase} |
| Event checkpoint | {checkpoint} |
| Difficulty | Developing |

## Driving question

What is the highest-value robot improvement we can finish today without breaking rollback?

## Student-facing objective

Students will run the numbered cadence for Meeting {mt} from the season templates, log evidence in TRACE or the notebook, and update the readiness dashboard.

## Robot outcome

- Documented progress on the mechanism or reliability focus for this week
- No new active features without evidence

## Prerequisites

- [calendar.yaml](../calendar.yaml) cadence window for this date
- [readiness-dashboard.md](../readiness-dashboard.md)

## Vocabulary

cadence · rollback · evidence · mechanism of the week

## Safety concerns

- Mentor present for powered tests
- DS disable path before enable
- No competition enablement from this cadence session alone

## Required hardware

- Robot as it exists; pit checklist

## Required software

- Per [preseason-software-allocation.md](../docs/preseason-software-allocation.md) after Kickoff: only what serves today's mechanism

## Preparation required before the meeting

- Review prior meeting repair list and dashboard rows

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
{agenda}

## Mentor demonstration

Follow [cadence-meeting-{'a' if mt == 'A' else 'b'}.md](../../../templates/cadence-meeting-{'a' if mt == 'A' else 'b'}.md).

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Construction block |
| Electrical | Wiring fixes surfaced in repair block |
| Programming | Integration minutes only |
| Drive team | Driving reps block |
| Documentation | Dashboard + notebook |

## Integrated build or test activity

Cadence construction or drive block — not a deep library lecture.

## Failure-injection scenario

Mentor names one subsystem to disable; students state rollback before continuing.

## Evidence to collect

- Notebook or TRACE entry tied to today's physical work

## Student explain-back questions

1. What shipped today?
2. What is still disabled and why?
3. What is the next test before enabling anything new?

## Assessment or exit check

Dashboard updated; cleanup complete; rollback named for any optional system touched.

## Portfolio or engineering-notebook artifact

Photo or log line tied to mechanism work.

## Competition enablement impact

None unless a separate decision record exists.

## Rollback procedure

Disable optional systems independently per [student-install.md](../../../docs/student-install.md).

## Cleanup requirements

Robot safe; battery stored; floor clear.

## Next-session preparation

- Read next numbered session in [sessions/](.)
- Update repair list

## Hardware-unavailable fallback

Paper diagram + verbal walkthrough of intended change.

## Robot-unavailable simulation option

Desktop or paper-only integration per project manuals.

## Links to authoritative project documentation

- [templates/cadence-meeting-{'a' if mt == 'A' else 'b'}.md](../../../templates/cadence-meeting-{'a' if mt == 'A' else 'b'}.md)
- [season-plan.md](../season-plan.md)
- [readiness-dashboard.md](../readiness-dashboard.md)

## Mentor notes

Numbered cadence slot — customize mechanism name in the opening block. Do not treat as permission to enable advanced libraries.
"""


def event_session(sid: str, dt: str, title: str, phase: str, checkpoint: str, body: str) -> str:
    return f"""---
id: {sid}
title: "{title}"
date: {dt}
meeting_type: E
season_phase: {phase}
event_checkpoint: {checkpoint}
status: complete
difficulty: Competition readiness
projects: [TRACE]
active_features: []
---

# {sid} — {title}

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | {sid} |
| Title | {title} |
| Calendar date | {dt} (competition day — replaces a regular Mon/Fri meeting) |
| Meeting type | E (event) |
| Season phase | {phase} |
| Event checkpoint | {checkpoint} |
| Difficulty | Competition readiness |

## Driving question

{body}

## Student-facing objective

Students compete or support pit/inspection/scouting per FIRST event rules — not a shop curriculum session.

## Robot outcome

- Event participation evidence in the notebook
- Post-event repair list for the next shop meeting

## Prerequisites

- Official FIRST event materials and mentor travel plan
- [pit-and-inspection.md](../pit-and-inspection.md)

## Vocabulary

event session · pit · inspection · scouting

## Safety concerns

- Follow venue and FIRST safety rules
- Battery transport policies
- No shop-style powered tests at the venue unless rules allow

## Required hardware

- Inspection-ready robot; pit cart; spare parts per pit checklist

## Required software

- Competition-configured TeleOp/auto only — no experiments at the field

## Preparation required before the meeting

- Complete [pit-and-inspection.md](../pit-and-inspection.md) checklist
- Assign drive, pit, and scouting roles

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 120 | Event | Full competition day — see mentor schedule; no FORGE shop blocks |

## Mentor demonstration

Not applicable — event day.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Pit repairs between matches |
| Electrical | Battery rotation; connector checks |
| Programming | Only hotfixes with mentor approval and rollback |
| Drive team | Matches and debrief |
| Documentation | Match log; failure notes for next shop session |

## Integrated build or test activity

Competition — data collection for next numbered shop session.

## Failure-injection scenario

Use real match failures as evidence — capture in notebook for retrospective.

## Evidence to collect

- Match scores, reliability notes, inspection result (notebook — not git if sensitive)

## Student explain-back questions

1. What broke or degraded today?
2. What rollback is still valid?
3. What is the top repair before the next shop meeting?

## Assessment or exit check

Team debrief complete; robot secured for transport.

## Portfolio or engineering-notebook artifact

Event summary page for engineering notebook.

## Competition enablement impact

Competition configuration only — no new features at the event.

## Rollback procedure

Revert any pit hotfix that fails next shop test.

## Cleanup requirements

Pit packed; robot secured; travel home checklist.

## Next-session preparation

- First shop meeting back: run [event-retrospective.md](../../../templates/event-retrospective.md)

## Hardware-unavailable fallback

Not applicable — event cancelled; run retrospective on next shop date.

## Robot-unavailable simulation option

Not applicable.

## Links to authoritative project documentation

- [pit-and-inspection.md](../pit-and-inspection.md)
- [templates/event-retrospective.md](../../../templates/event-retrospective.md)
- FIRST official event materials (authoritative — not FORGE)

## Mentor notes

This calendar row replaces regular meeting **{'S035' if sid == 'E004' else 'S043'}** on {dt}. Do not schedule a duplicate shop session the same day.
"""


def update_front_matter(text: str, sid: str, dt: str, mt: str) -> str:
    text = re.sub(r"^id: .+$", f"id: {sid}", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"^date: .+$", f"date: {dt}", text, count=1, flags=re.MULTILINE)
    if "date_requires_confirmation" in text:
        text = re.sub(r"^date_requires_confirmation: .+\n", "", text, flags=re.MULTILINE)
        text = text.replace("date: requires_confirmation\n", f"date: {dt}\n")
    text = re.sub(r"^meeting_type: .+$", f"meeting_type: {mt}", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"^\| Session ID \| .+ \|", f"| Session ID | {sid} |", text, count=1, flags=re.MULTILINE)
    return text


def main() -> None:
    for name in VESTIGIAL:
        p = SESSIONS / name
        if p.exists():
            p.unlink()
            print("deleted vestigial", name)

    # two-phase rename via temp
    temps: dict[str, Path] = {}
    for old, new in RENAME_MAP.items():
        src = SESSIONS / old
        if not src.exists():
            print("skip missing", old)
            continue
        tmp = SESSIONS / f"__tmp__{new}"
        src.rename(tmp)
        temps[new] = tmp

    for new, tmp in temps.items():
        tmp.rename(SESSIONS / new)
        print("renamed ->", new)

    # build lookup from calendar
    cal_by_file = {row[5]: row for row in CALENDAR_ROWS}

    for fname, row in cal_by_file.items():
        path = SESSIONS / fname
        sid, dt, mt, phase, checkpoint, _, title = row
        if not path.exists():
            if sid.startswith("E"):
                body = (
                    "Are we ready to compete today with rollback intact?"
                    if sid == "E004"
                    else "If we advanced, are we prepared for state-level inspection and match load?"
                )
                path.write_text(event_session(sid, dt, title, phase, checkpoint, body), encoding="utf-8")
            else:
                path.write_text(stub_session(sid, dt, mt, phase, checkpoint, title), encoding="utf-8")
            print("created", fname)
        else:
            text = path.read_text(encoding="utf-8")
            # heading id
            old_heading = re.search(r"^# [A-Z0-9]+ —", text, re.MULTILINE)
            if old_heading:
                text = re.sub(r"^# [A-Z0-9]+ —", f"# {sid} —", text, count=1, flags=re.MULTILINE)
            text = update_front_matter(text, sid, dt, mt)
            text = remap_text(text, sid)
            path.write_text(text, encoding="utf-8")
            print("updated fm", fname)

    # delete any session file not in calendar
    allowed = {row[5] for row in CALENDAR_ROWS}
    for p in SESSIONS.glob("*.md"):
        if p.name not in allowed:
            p.unlink()
            print("removed orphan", p.name)

    write_calendar()

    print("done — run validate and fix repo cross-refs")


if __name__ == "__main__":
    main()
