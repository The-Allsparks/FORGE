---
id: S011
title: "Integrated failure injection"
date: 2026-10-06
meeting_type: A
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: outline
difficulty: Integration
projects: [TRACE, AMPER, MIMIC, ViDAR, BEACON]
active_features: []
---
# S011 — Integrated failure injection

## Session identity
| Field | Value |
| ----- | ----- |
| Session ID | S011 |
| Title | Integrated failure injection |
| Calendar date | 2026-10-06 (planning input) |
| Relative week | Week before clinic |
| Meeting type | A |
| Season phase | kickoff-to-clinic |
| Event checkpoint | clinic |
| Difficulty | Integration |

## Driving question

Can we tell a single story when several incomplete logs disagree?

## Student-facing objective

Students keep building MVP while practicing a coordinated failure (covered camera, weak labeled pack, stale snapshot) and writing INSUFFICIENT_EVIDENCE when appropriate.

## Robot outcome

MVP progress plus a redacted failure timeline.

## Prerequisites

S003–S006 vocab. [BEACON exercise 3](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/exercises.md).

## Vocabulary

correlation · insufficient evidence · domain

## Safety concerns

No uncontrolled brownout. No gravity crashes. Mentor present. Restrain if needed.

## Required hardware

Robot; labeled weaker pack optional; lens cap.

## Required software

TRACE; passive AMPER/BEACON if installed; ViDAR observe only.

## Preparation required before the meeting

Pick ONE injected fault for the integration block. Construction stays MVP.

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | One fault only; safety; clinic is for data not features |
| 75 | Construction | Finish what clinic needs mechanically/electrically. |
| 25 | Integration | Inject the chosen fault; TRACE story; do not enable new active features to 'catch' it. |
| 10 | Closeout | TRACE evidence, explain-back, dashboard, cleanup |

## Mentor demonstration

Show a bad diagnosis ('jammed') from mixed symptoms.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | MVP |
| Electrical | Connector check |
| Programming | Timeline export |
| Drive team | Drive after construction if time — otherwise S012 |
| Documentation | Timeline |

## Integrated build or test activity

Cover camera + note voltage + mechanism snapshot. Write one paragraph that ends with insufficient evidence if needed.

## Failure-injection scenario

The session is the failure injection.

## Evidence to collect

Timeline; dashboard risks column updated.

## Student explain-back questions

1. Name the domain you actually have evidence for.
2. What did you not prove?
3. Rollback of each optional system?
4. Will this feature be on at clinic?

## Assessment or exit check

Paragraph complete. MVP still the priority.

## Portfolio or engineering-notebook artifact

Failure timeline.

## Competition enablement impact

No new approvals. Clinic systems-validation only.

## Rollback procedure

All optional systems off or passive as dashboard.

## Cleanup requirements

Restore healthy battery; uncover camera; robot safe.

## Next-session preparation

S012 clinic prep.

## Hardware-unavailable fallback

Paper multi-log exercise from BEACON/AMPER sample CSV if any; otherwise invented-but-labeled hypothesis logs marked as practice only.

## Robot-unavailable simulation option

Desktop TRACE memory sink + BEACON exercises.

## Links to authoritative project documentation

- [TRACE integrations](https://github.com/The-Allsparks/TRACE/blob/main/docs/integrations.md)
- [BEACON exercises](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/exercises.md)
- [AMPER phases](https://github.com/The-Allsparks/AMPER/blob/main/docs/power-management/phases.md)
- [projects/trace.md](../../../projects/trace.md)

## Mentor notes

TRACE Phase 4 adapters may not exist. Correlate manually. Do not claim unified adapters.
