---
id: S037
title: "Cadence Meeting B — driver and auto reps"
date: 2027-01-29
meeting_type: B
season_phase: state-prep
event_checkpoint: state-championship
status: complete
difficulty: Developing
projects: [TRACE]
active_features: []
---

# S037 — Cadence Meeting B — driver and auto reps

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S037 |
| Title | Cadence Meeting B — driver and auto reps |
| Calendar date | 2027-01-29 (planning input; Monday/Friday 4:00–6:00 PM unless noted) |
| Meeting type | B |
| Season phase | state-prep |
| Event checkpoint | state-championship |
| Difficulty | Developing |

## Driving question

What is the highest-value robot improvement we can finish today without breaking rollback?

## Student-facing objective

Students will run the numbered cadence for Meeting B from the season templates, log evidence in TRACE or the notebook, and update the readiness dashboard.

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
| 10 | Opening | Review logs; repair priorities |
| 35 | Repair / tune / program | Highest-priority fix from last drive or event |
| 55 | Driving reps | Driver and conventional auto repetitions |
| 20 | Closeout | Inspection checklist; dashboard; cleanup |

## Mentor demonstration

Follow [cadence-meeting-b.md](../../../templates/cadence-meeting-b.md).

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

- [templates/cadence-meeting-b.md](../../../templates/cadence-meeting-b.md)
- [season-plan.md](../season-plan.md)
- [readiness-dashboard.md](../readiness-dashboard.md)

## Mentor notes

Numbered cadence slot — customize mechanism name in the opening block. Do not treat as permission to enable advanced libraries.
