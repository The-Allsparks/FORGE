---
id: S002
title: Post-Kickoff week 1 — ideation scale-up and low-fi prototypes
date: 2026-09-18
meeting_type: B
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: complete
difficulty: Foundation
projects:
- TRACE
active_features: []
compressed_week: 1
forge_gate: G1
---

# S002 — Driver baseline and chassis reliability

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S002 |
| Title | Post-Kickoff week 1 — ideation scale-up and low-fi prototypes |
| Calendar date | 2026-09-18 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | Compressed week 1 (G1 Strategy) |
| Meeting type | B |
| Season phase | kickoff-to-clinic |
| Event checkpoint | clinic |
| Forge gate | G1 |
| Difficulty | Foundation |

## Driving question

Did we generate enough ideas (60–100 scaled) and finish G1 with a documented strategy before custom fabrication scales up?

## Student-facing objective

Students scale visual ideation, finish low-fidelity prototypes, complete G1 Strategy gate review, and run short driver reps on drivable chassis.

## Robot outcome

- Ideation count recorded (target 60–100 across team)
- [Gate review G1](../../../templates/gate-review.md) completed
- Risk register started
- Starter-bot fallback documented


## Prerequisites

- S001 motor bring-up complete **or** honest blocker with partial progress
- Gamepads; Driver Station; blocks/restraint
- Minimal TeleOp deployed ([preseason-software-allocation.md](../docs/preseason-software-allocation.md))

## Vocabulary

baseline · strafe · rotation · enable · disable · repair list

## Safety concerns

- Blocks/restraint first; exclusion zone
- Emergency disable before carpet
- Stop if retention, temperature, or binding fails
- No speculative mechanism testing on the chassis

## Required hardware

- Robot as built through S001 (Strafer + MVP progress); battery; Hub
- Measuring tape for fixed-distance tests
- IR thermometer optional (mentor)

## Required software

- Team TeleOp (minimal arcade/mecanum)
- TRACE or paper timeline optional (≤10 min)

## Preparation required before the meeting

- Charge batteries; open S001 motor table
- Mark a fixed distance on the floor (e.g. 2 m) for straight-line tests

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | S001 status; test goals; safety; every driver will drive |
| 35 | Repair / tune / program | Fix S001 items; correct mecanum orientation; tune stick signs only — no feature creep |
| 55 | Driving reps | Forward/reverse; strafe L/R; rotation; fixed-distance straight lines; **every student** enables, drives, disables; emergency-disable drill |
| 20 | Closeout | Inspect fasteners, wiring, motor temps; baseline table; repair list; explain-back |

## Mentor demonstration

Two minutes: show wrong stick mapping vs corrected mapping on blocks.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Post-run inspection and repair list |
| Electrical | Connector and wire dress check |
| Programming | TeleOp trim only if needed |
| Drive team | **All students** drive baseline reps |
| Documentation | Baseline table: driver, test, distance, time, notes |

## Integrated build or test activity

The 55-minute rep block is the product. No library integration today.

## Failure-injection scenario

Random DS disable during a rep. Driver must stop; document whether disable was immediate.

## Evidence to collect

- Baseline table (all drivers)
- Emergency-disable result
- Repair list
- TRACE or paper timeline optional

## Student explain-back questions

1. What changed if a wheel drove backward?
2. How do you emergency-disable?
3. What is on the repair list before S003?
4. Is the chassis ready for mechanism experiments? (honest answer)

## Assessment or exit check

**Path A:** All mecanum directions work for every driver with disable discipline.  
**Path B:** Blocker + partial baseline + repair owners — no fake success.

## Portfolio or engineering-notebook artifact

Baseline table (Control/Driver practice evidence). Repair list (engineering process).

## Competition enablement impact

Driver-control ladder only. Not competition approved.

## Rollback procedure

DS stop. Revert TeleOp changes if they broke disable. Drive without TRACE if needed.

## Cleanup requirements

Battery off; robot on blocks; gamepads stored.

## Next-session preparation

- S003: capstan/tower/transport experiments — chassis must stay serviceable
- K001: consolidate evidence before Kickoff

## Hardware-unavailable fallback

Gamepad drills on blocks with paper event log. Inspection on static chassis.

## Robot-unavailable simulation option

Walk the baseline path; verbal stick calls; still rotate all students through enable/disable roles.

## Links to authoritative project documentation

- [docs/season-process.md](../docs/season-process.md)
- [docs/decision-gates.md](../docs/decision-gates.md)
- [docs/pratt-crosswalk.md](../docs/pratt-crosswalk.md)
- [prototype-test-record.md](../../../templates/prototype-test-record.md)
- [gate-review.md](../../../templates/gate-review.md)
- [preseason-software-allocation.md](../docs/preseason-software-allocation.md)
- [S001 bring-up](P005-meeting-a.md)
- [projects/pedro-pathing.md](../../../projects/pedro-pathing.md) — defer tuning

## Mentor notes

Success = **MVP teleop** on the Kickoff robot configuration, not library features. If teleop missing, use 35-minute block — not 55-minute lecture. Pedro follower tuning waits until post-Kickoff when justified.
