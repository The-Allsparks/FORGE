---
id: S009
title: "MIMIC interlocks"
date: 2026-09-29
meeting_type: A
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: complete
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
| Calendar date | 2026-09-29 (planning input; Tuesday Meeting A) |
| Relative week | Kickoff-to-clinic week 3 |
| Meeting type | A |
| Season phase | kickoff-to-clinic |
| Event checkpoint | clinic |
| Difficulty | Developing |

## Driving question

How can two individually "fine" mechanisms become unsafe together?

## Student-facing objective

Students keep building MVP mechanisms and produce a named interlock table (legal / reject / defer). Software protections stay **off**. Paper and optional desktop tests only.

## Robot outcome

- Interlock table for the real or mock geometry on the robot this week
- Hard-stop discussion recorded
- No MIMIC Phase 7 (or any actuation phase) enabled

## Prerequisites

- S004 state names
- [interlocks.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/interlocks.md)
- [safety-model.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/safety-model.md)
- Second mechanism **or** cardboard stand-in. Elevator-specific racking work stays out until hardware exists ([MIMIC assessment](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/assessment.md))

## Vocabulary

interlock · reject · defer · clamp · deadlock · hard stop vs software

## Safety concerns

- Adult supervision. Do **not** test interlocks by crashing hardware
- Gravity loads secured; no "see if it hits"
- Software limits do not replace mechanical stops
- Unpowered for geometry checks unless a mentor is jogging a mechanism slowly with a clear exclusion zone

## Required hardware

- Two mechanisms or one real + cardboard volume
- Hard stops where the design needs them
- Camera/intake as a typical pair if that is the MVP

## Required software

- Notebook table (required)
- Optional: MIMIC desktop tests / fake hardware — no robot actuation flags
- TRACE event `Interlock/would-reject` when students identify an illegal pair (paper is enough)

## Preparation required before the meeting

- Photograph current travel
- Print a blank state×state grid from S004 names (update names if Kickoff changed them)
- Read interlocks.md outcomes: reject, defer, clamp, confirmation — do not invent a scheduler

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Two safe motions can still collide; no surprise powered motion; assignments |
| 75 | Construction | MVP mechanisms: geometry, hard stops, cable routing that will not be sheared by travel |
| 25 | Integration | Fill the interlock table; pick one illegal pair and write reject vs defer; optional unit test on laptops |
| 10 | Closeout | Photo of table; dashboard MIMIC still observation; explain-back; cleanup |

## Mentor demonstration

Two unpowered poses that would collide. Write `REJECT` on the board. Thirty seconds of "this is not a global command scheduler" pointing at MIMIC README.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Travel, hard stops, pinch points |
| Electrical | Limit-switch routing if switches exist; otherwise label future ports |
| Programming | Named constraints on paper; not a competing scheduler |
| Drive team | Practice the callout "clear" / "not clear" they will use in teleop later |
| Documentation | Interlock table |

## Integrated build or test activity

For each pair of states, mark legal / illegal. Choose one illegal: would you **reject** the command, **defer** until the other mechanism moves, or **clamp** travel? Cite the interlocks doc, do not invent deadlock loops.

## Failure-injection scenario

Mentor: "Just raise while extended." Students refuse unless the table already names an exception with a mechanical reason. If they comply on hardware, stop the session's powered work.

## Evidence to collect

- Interlock table
- Geometry photo
- Confirmation: MIMIC actuation still off (no write counts if using fake actuators)

## Student explain-back questions

1. Why is this not a global scheduler?
2. What is deadlock, in one sentence?
3. Difference between a software interlock and a hard stop?
4. How do we roll back? (Do not enable Phase 7.)

## Assessment or exit check

Table complete. Construction visibly progressed. No new motor flags.

## Portfolio or engineering-notebook artifact

State×state grid. Link MIMIC interlocks.md as authority.

## Competition enablement impact

MIMIC protections **disabled**. Observation/snapshots only until a later controlled failure test.

## Rollback procedure

Do not enable Phase 7 or homing. Teleop remains manual. Power off mechanisms.

## Cleanup requirements

Mechanisms unpowered and down; no loaded arms left standing.

## Next-session preparation

S010 ECHO is off-robot. Bring hearing-safety willingness. Keep building Thursday if Meeting B has repair time.

## Hardware-unavailable fallback

Cardboard overlapping volumes on the table. Same table exercise.

## Robot-unavailable simulation option

MIMIC `gradlew test` / fake hardware plus the paper grid.

## Links to authoritative project documentation

- [interlocks.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/interlocks.md)
- [lifecycle.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/lifecycle.md)
- [safety-model.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/safety-model.md)
- [phases.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/phases.md)
- [assessment.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/assessment.md)
- [testing.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/testing.md)
- [projects/mimic.md](../../../projects/mimic.md)

## Mentor notes

If only one mechanism exists, teach the idea and **build the second** in the 75 minutes. Do not fabricate a second elevator. Phase 0 remains the implemented scaffold at audit.
