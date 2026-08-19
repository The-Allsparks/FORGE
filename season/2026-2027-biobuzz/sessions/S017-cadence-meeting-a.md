---
id: S017
title: "Cadence Meeting A — mechanism of the week"
date: 2026-11-09
meeting_type: A
season_phase: league-development
event_checkpoint: league-3s-4s
status: complete
difficulty: Developing
projects: [TRACE]
active_features: []
---

# S017 — Cadence Meeting A — mechanism of the week

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S017 |
| Title | Cadence Meeting A — mechanism of the week |
| Calendar date | 2026-11-09 (planning input; Monday/Friday 4:00–6:00 PM unless noted) |
| Meeting type | A |
| Season phase | league-development |
| Event checkpoint | league-3s-4s |
| Difficulty | Developing |

## Driving question

What is the highest-value robot improvement we can finish today without breaking rollback?

## Student-facing objective

Students will run the numbered cadence for Meeting A from the season templates, log evidence in TRACE or the notebook, and update the readiness dashboard.

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
| 10 | Opening | Goals; safety; cadence intent for this week |
| 75 | Construction | Mechanism of the week per [cadence-meeting-a.md](../../../templates/cadence-meeting-a.md) |
| 25 | Integration | TRACE / passive library touchpoint on today's mechanism |
| 10 | Closeout | Explain-back; dashboard; cleanup |

## Mentor demonstration

Follow [cadence-meeting-a.md](../../../templates/cadence-meeting-a.md).

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

- [templates/cadence-meeting-a.md](../../../templates/cadence-meeting-a.md)
- [season-plan.md](../season-plan.md)
- [readiness-dashboard.md](../readiness-dashboard.md)

## Mentor notes

Numbered cadence slot — customize mechanism name in the opening block. Do not treat as permission to enable advanced libraries.
