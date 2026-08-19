---
id: P006
title: "Driver baseline and chassis reliability"
date: 2026-09-04
meeting_type: B
season_phase: preseason
event_checkpoint: none
status: complete
difficulty: Foundation
projects: [TRACE]
active_features: []
---

# P006 — Driver baseline and chassis reliability

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | P006 |
| Title | Driver baseline and chassis reliability |
| Calendar date | 2026-09-04 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | Preseason week 1 |
| Meeting type | B |
| Season phase | preseason |
| Event checkpoint | none |
| Difficulty | Foundation |

## Driving question

Can every student enable, drive all mecanum directions, stop on command, and produce a measurable baseline?

## Student-facing objective

Students will establish reliable driver control: forward/reverse, strafe both ways, rotation, fixed-distance straight-line tests, enable/start/stop/emergency disable, rotation through all drivers, and post-run inspection of fasteners, wiring, and motor temperatures.

## Robot outcome

- Safely driving chassis on restraint or short carpet (mentor OK)
- Baseline measurements recorded
- Mecanum orientation errors corrected or documented
- Repair list for P007/K001 prep

## Prerequisites

- P005 motor bring-up complete **or** honest blocker with partial progress
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

- Strafer drivetrain from P002–P004; battery; Hub
- Measuring tape for fixed-distance tests
- IR thermometer optional (mentor)

## Required software

- Team TeleOp (minimal arcade/mecanum)
- TRACE or paper timeline optional (≤10 min)

## Preparation required before the meeting

- Charge batteries; open P005 motor table
- Mark a fixed distance on the floor (e.g. 2 m) for straight-line tests

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | P005 status; test goals; safety; every driver will drive |
| 35 | Repair / tune / program | Fix P005 items; correct mecanum orientation; tune stick signs only — no feature creep |
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
3. What is on the repair list before P007?
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

- P007: capstan/tower/transport experiments — chassis must stay serviceable
- P008: consolidate evidence before Kickoff

## Hardware-unavailable fallback

Gamepad drills on blocks with paper event log. Inspection on static chassis.

## Robot-unavailable simulation option

Walk the baseline path; verbal stick calls; still rotate all students through enable/disable roles.

## Links to authoritative project documentation

- [preseason-software-allocation.md](../docs/preseason-software-allocation.md)
- [P005 bring-up](P005-meeting-a.md)
- [projects/pedro-pathing.md](../../../projects/pedro-pathing.md) — defer tuning

## Mentor notes

Preseason success = **reliable Strafer**, not BIOBUZZ scoring. If teleop missing, use 35-minute block — not 55-minute lecture. Pedro follower tuning waits until post-Kickoff when justified.
