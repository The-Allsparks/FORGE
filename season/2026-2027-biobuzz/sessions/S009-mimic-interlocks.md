---
id: S009
title: "MIMIC interlocks"
date: 2026-09-29
meeting_type: A
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: outline
difficulty: Developing
projects: [MIMIC, TRACE]
active_features: []
---
# S009 — MIMIC interlocks

## Session identity
| Field | Value |
| ----- | ----- |
| Session ID | S009 |
| Title | MIMIC interlocks |
| Calendar date | 2026-09-29 (planning input) |
| Relative week | Kickoff-to-clinic |
| Meeting type | A |
| Season phase | kickoff-to-clinic |
| Event checkpoint | clinic |
| Difficulty | Developing |

## Driving question

How can two individually 'fine' mechanisms become unsafe together?

## Student-facing objective

Students build/adjust MVP mechanisms and write named interlocks on paper or in tests. No live interlock actuation unless already tested.

## Robot outcome

Interlock table for real geometry. Protections remain off.

## Prerequisites

S004 states. [interlocks.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/interlocks.md). Real or cardboard second mechanism.

## Vocabulary

interlock · reject · defer · clamp · deadlock

## Safety concerns

Adult supervision. Do not test interlocks by crashing hardware. Gravity loads secured.

## Required hardware

Two mechanisms or mocks. Hard stops.

## Required software

MIMIC tests if available; paper constraints otherwise. No Phase 7 enablement claimed.

## Preparation required before the meeting

Photograph current mechanism travel. Read interlocks.md headings.

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Safety; today's interlock names; no surprise motion |
| 75 | Construction | MVP mechanisms: geometry that makes interlocks real. |
| 25 | Integration | Write constraints; optional unit test; TRACE events when a constraint would reject. |
| 10 | Closeout | TRACE evidence, explain-back, dashboard, cleanup |

## Mentor demonstration

Two safe motions that collide. Paper reject.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Travel, hard stops |
| Electrical | Limit switches if they exist |
| Programming | Named constraints, not a scheduler |
| Drive team | Call 'clear' before motion in later teleop |
| Documentation | Interlock table |

## Integrated build or test activity

For each pair of states, mark legal/illegal. Pick one illegal and explain reject vs defer.

## Failure-injection scenario

Ask students to 'just raise while extended.' They must refuse without a named exception.

## Evidence to collect

Interlock table; photo of geometry; no actuation log from MIMIC.

## Student explain-back questions

1. Why is this not a global scheduler?
2. What is deadlock?
3. Software vs hard stop?
4. Rollback?

## Assessment or exit check

Table complete. Construction progressed.

## Portfolio or engineering-notebook artifact

Interlock table in notebook.

## Competition enablement impact

MIMIC protections still disabled until a controlled failure test exists.

## Rollback procedure

Do not enable Phase 7. Teleop manual with mentor-only motion.

## Cleanup requirements

Mechanisms unpowered and down.

## Next-session preparation

S010 ECHO off-robot.

## Hardware-unavailable fallback

Cardboard overlapping volumes.

## Robot-unavailable simulation option

MIMIC fake hardware tests.

## Links to authoritative project documentation

- [interlocks.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/interlocks.md)
- [lifecycle.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/lifecycle.md)
- [safety-model.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/safety-model.md)
- [phases.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/phases.md)
- [projects/mimic.md](../../../projects/mimic.md)

## Mentor notes

If only one mechanism exists, teach the idea and keep building the second. Do not fake a second elevator.
