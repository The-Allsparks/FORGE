---
id: S028
title: Adversity drill — obstructed camera and stale sensors
date: 2026-12-21
meeting_type: A
season_phase: adversity-simulations
event_checkpoint: league-5s-6s
status: complete
difficulty: Developing
projects:
- TRACE
active_features: []
---

# S028 — Meeting A — adversity drill

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S028 |
| Title | Adversity drill — obstructed camera and stale sensors |
| Calendar date | 2026-12-21 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Meeting type | A |
| Season phase | adversity-simulations |
| Event checkpoint | league-5s-6s |
| Difficulty | Developing |

## Driving question

Can we drive safely when vision or sensors lie?

## Student-facing objective

Students run manual-override drills; ViDAR observe-only or unplugged per dashboard.

## Robot outcome

- Override procedure verified
- Dashboard status unchanged unless evidenced


## Prerequisites

- [calendar.yaml](../calendar.yaml) row for S028
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
| 10 | Opening | Goals; safety; read **title** in calendar for this week's mechanism |
| 75 | Construction | [cadence-meeting-a.md](../../../templates/cadence-meeting-a.md) |
| 25 | Integration | TRACE / passive library touchpoint on today's mechanism |
| 10 | Closeout | Explain-back; dashboard; cleanup |

## Mentor demonstration

Follow [cadence-meeting-a.md](../../../templates/cadence-meeting-a.md).

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

- [templates/cadence-meeting-a.md](../../../templates/cadence-meeting-a.md)
- [season-plan.md](../season-plan.md)

## Mentor notes

**Filename is fixed:** `S028-meeting-a.md`. Edit `title` in this file and `calendar.yaml` when the week's topic changes.
