---
id: S008
title: "MIMIC mechanism states using simulated or simple hardware"
date: 2026-09-10
meeting_type: B
season_phase: preseason
event_checkpoint: none
status: complete
difficulty: Foundation
projects: [MIMIC, TRACE]
active_features: []
---

# S008 — MIMIC mechanism states using simulated or simple hardware

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S008 |
| Title | MIMIC mechanism states using simulated or simple hardware |
| Calendar date | 2026-09-10 (planning input; last meeting before Kickoff) |
| Relative week | Preseason week 2 |
| Meeting type | B |
| Season phase | preseason |
| Event checkpoint | none |
| Difficulty | Foundation |

## Driving question

If we cannot name the state a mechanism is in, how will we ever make it safe?

## Student-facing objective

Students will inspect or mock a simple mechanism, draw named states, capture a MIMIC (or paper) snapshot, and keep driving practice on the drivetrain.

## Robot outcome

- State diagram for one real or mock mechanism
- Phase 0-style snapshot with **no actuator writes**
- Additional driver baseline reps on the chassis

## Prerequisites

- S007 wiring in a known-safe condition
- MIMIC examples/tests available: [examples](https://github.com/The-Allsparks/MIMIC/blob/main/examples/README.md)
- Elevator hardware is **not** assumed ([MIMIC assessment](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/assessment.md))

## Vocabulary

snapshot · state · ticks ≠ inches · stale · uncalibrated · fake actuator

## Safety concerns

- No homing into hard stops ([MIMIC phases](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/phases.md) — Phase 2 not today)
- Software limits do not replace mechanical stops ([safety model](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/safety-model.md))
- Gravity loads: do not energize an unsecured arm
- MIMIC Phase 0 must not change motor/servo output

## Required hardware

- Simple mechanism **or** cardboard joints + servo horn for naming only
- Drivetrain for the 55-minute drive block
- Laptop for fake hardware tests

## Required software

- MIMIC desktop tests / fake actuator
- TRACE events when mechanism "state" is declared
- Team teleop for driving

## Preparation required before the meeting

- Clone MIMIC; `gradlew test` on one laptop
- Decide the mechanism of the day (intake, servo, or mock)
- Print state-diagram blank

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Review S007 sag sentence; today's test goal: **name states, snapshot, then drive**; safety: no homing |
| 35 | Repair / tune / program | Repair drivetrain issues from logs; programmers run MIMIC Phase 0 tests; others assemble or mock the mechanism and draft states (`STOWED`, `CLEAR`, `INTAKING`, `FAULTED` — names may change after Kickoff) |
| 55 | Driving / auto reps | Driver rotations on chassis. Between runs, mechanism pair updates the snapshot from sensors **or** from fake hardware on a laptop at the field table. Do not steal this block for a MIMIC lecture |
| 20 | Closeout | Inspect mechanism pinch points; log review; explain-back; dashboard MIMIC ladder 1–2; Kickoff reminder for Saturday |

## Mentor demonstration

Show that a fake actuator write count stays 0 in Phase 0. Draw `UNCALIBRATED` vs "we think it's at 500 ticks." Stop before controllers.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Mock or real mechanism structure; hard-stop discussion |
| Electrical | Encoder/limit switch routing if hardware exists; otherwise label future ports |
| Programming | Snapshot capture; TRACE `Mechanism/state` events |
| Drive team | Reps; they must say the mechanism state before requesting "go" |
| Documentation | State diagram in notebook |

## Integrated build or test activity

Capture one snapshot while the mechanism is still, one after a **manual** unpowered move (or fake clock). Students explain what stayed `VALID` vs what would be `STALE` if capture stopped.

## Failure-injection scenario

Unplug a named sensor in a safe config **or** freeze a fake supplier while the loop still runs. Students must not invent a pose. See MIMIC Phase 0 stale notes in [phases.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/phases.md).

## Evidence to collect

- State diagram
- Snapshot print/screenshot or notebook copy
- Drive rep count
- Confirmation: no MIMIC actuation

## Student explain-back questions

1. Why are encoder ticks not inches?
2. What should software do if the sensor is missing?
3. Who owns chassis motion? (Pedro / teleop — not MIMIC)
4. What is the disable path for MIMIC? (do not enable later flags; Phase 0 defaults)

## Assessment or exit check

Pair presents the state diagram and one snapshot. Another student drives a baseline without using the mechanism.

## Portfolio or engineering-notebook artifact

State diagram + "wait until hardware exists" note for elevator-specific work.

## Competition enablement impact

MIMIC **disabled** for actuation. Observation/snapshots only. Not approved.

## Rollback procedure

Do not call any MIMIC enable that actuates. Remove snapshot code if it breaks teleop. Mechanical disable: power off.

## Cleanup requirements

Unpowered mechanisms; no loaded gravity arms left standing; batteries stored.

## Next-session preparation

- Saturday Kickoff: SK01. Bring notebook. Do not pack experimental libraries as if they were game strategy.
- After Kickoff: webcam for S009 if the team has one; otherwise sim laptops

## Hardware-unavailable fallback

Cardboard mechanism + sticky-note states. MIMIC tests on laptop entirely.

## Robot-unavailable simulation option

MIMIC `gradlew test` + [lifecycle.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/lifecycle.md) reading during the 35-minute block. Drive block becomes unpowered push-bot or gamepad dry-run.

## Links to authoritative project documentation

- [MIMIC README](https://github.com/The-Allsparks/MIMIC/blob/main/README.md)
- [Phases](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/phases.md)
- [Lifecycle](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/lifecycle.md)
- [Safety model](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/safety-model.md)
- [Testing](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/testing.md)
- [Examples](https://github.com/The-Allsparks/MIMIC/blob/main/examples/README.md)
- [projects/mimic.md](../../../projects/mimic.md)

## Mentor notes

Do not start Phase 2 homing because Kickoff is in two days. Allsparks elevator was not selected at audit. Keep HELM out of this meeting except "we still have no authority layer."
