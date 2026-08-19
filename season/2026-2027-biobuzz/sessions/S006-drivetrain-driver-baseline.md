---
id: S006
title: "Drivetrain inspection, driver baseline, and log review"
date: 2026-09-03
meeting_type: B
season_phase: preseason
event_checkpoint: none
status: complete
difficulty: Foundation
projects: [TRACE, PEDRO]
active_features: []
---

# S006 — Drivetrain inspection, driver baseline, and log review

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S006 |
| Title | Drivetrain inspection, driver baseline, and log review |
| Calendar date | 2026-09-03 (planning input; Thursday Meeting B) |
| Relative week | Preseason week 1 |
| Meeting type | B |
| Season phase | preseason |
| Event checkpoint | none |
| Difficulty | Foundation |

## Driving question

Can we drive in a straight line, stop on command, and then tell the story of that run from a log?

## Student-facing objective

Students will inspect the **S003–S004** drivetrain, collect a driver baseline (blocks first, then restrained carpet if mentor OK), and review TRACE (or paper) logs from S005 plus today's runs. If the robot is not ready to drive, students will document the blocker honestly and use the repair block productively.

## Robot outcome

- Drivetrain inspection checklist complete (post-S004 wiring)
- Wheels-off or restrained teleop baseline **or** documented blocker with repair plan
- At least one TRACE event around `Drive/Baseline start` and `Drive/Baseline stop` if software is ready; otherwise paper log
- Emergency-disable test recorded

## Prerequisites

- S003–S004 drivetrain installed and wired; S005 corrections applied
- Mentor present for any powered motors
- Gamepads; Driver Station
- Blocks, crate, or known restraint

## Vocabulary

baseline · loop · disable · inspection · input (driver stick) vs event · blocker

## Safety concerns

- First motion: blocks/restraint, adult supervision, exclusion zone
- Hair, hoodies, ties away from chain/belt/pulleys
- Battery connector fully seated; no drive if wiring is unknown
- Stop test if a wheel retention fails
- Emergency-disable (DS stop) tested before carpet

## Required hardware

- Drivetrain as assembled in S003–S004; battery; Control Hub
- Blocks/restraint; safety glasses

## Required software

- Team teleop OpMode (even a sample arcade drive) — or documented absence if [#2](https://github.com/The-Allsparks/FORGE/issues/2) blocks deploy
- TRACE if already wired; otherwise DS timer + paper events
- Driver Station

## Preparation required before the meeting

- Charge batteries
- Confirm a teleop OpMode deploys (mentor laptop + Hub) **or** pre-write blocker path
- Print inspection checklist (fasteners, wires, wheel screws, mecanum orientation)
- Open S005 event export

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Review S005 events and S004 motor-test notes; today's test goal: **straight, stop, log**; safety: blocks first |
| 35 | Repair / tune / program | Inspection repair from S005/S004 lists; if teleop missing, programmers finish minimal drive OpMode while others inspect — **if still blocked, document and continue mechanical/electrical repair** |
| 55 | Driving / auto reps | **If ready:** wheels-off stick mapping 10 min; emergency-disable test; individual wheel-direction check; forward/reverse, strafe, rotation; short straight-line baselines on restraint/carpet with mentor OK. **If not ready:** wheels-off inspection drills, gamepad mapping on blocks, paper event log — no fake drive success |
| 20 | Closeout | Inspection sign-off or blocker record; log review; explain-back; dashboard: Driver-control + mechanical; cleanup |

## Mentor demonstration

Two minutes: show a bad log (`Drive start` after the robot already moved). Ask why the story is wrong. Then students instrument their own runs — or write what **would** be logged when the blocker clears.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Inspection and repair; mecanum orientation re-check |
| Electrical | Battery/Hub power path check with mentor |
| Programming | TRACE events around baseline; minimal teleop if missing |
| Drive team | Baseline repetitions **or** gamepad drills on blocks if blocked |
| Documentation | Times, surprises, blocker note if applicable, restraint photo |

## Integrated build or test activity

The 55-minute block is the product. Software exists to timestamp driving, not to replace it. Honest blocker documentation with continued inspection counts as success.

## Failure-injection scenario

Mentor calls "disable" at a random time during a restrained test. Robot must stop via DS. Students mark whether TRACE captured a stop event. If TRACE was not on the robot, they write the gap — do not fake Hub success.

## Evidence to collect

- Inspection checklist
- Count of baseline reps **or** blocker record with next fix owner
- Emergency-disable test result
- Individual wheel-direction verification (if powered)
- Forward/reverse, strafe, rotation notes (if powered)
- TRACE or paper timeline
- Note: Control Hub TRACE file sink is **not** claimed unless they actually exported from the Hub ([TRACE README current limitations](https://github.com/The-Allsparks/TRACE/blob/main/README.md))

## Student explain-back questions

1. What was the test goal in one sentence?
2. Is a stick value an input or an event?
3. What happens if TRACE is off — can you still drive?
4. Name one mechanical defect inspection found (or "none, and here is how we looked").
5. If we could not drive today, what is the blocker and what happens in S007?

## Assessment or exit check

**Path A:** Driver enables, drives baseline, disables without mentor hands on sticks; programmer retells run from log.  
**Path B:** Blocker written with owner and date; inspection complete; repair plan for S007 — no exaggerated claims.

## Portfolio or engineering-notebook artifact

Baseline table: driver, surface (blocks/carpet), duration, result, log pointer — **or** blocker page with inspection evidence.

## Competition enablement impact

Driver-control ladder toward 4–5 later. **Not** competition approved. Pedro not enabled as a follower yet — only chassis motion via teleop.

## Rollback procedure

DS stop. Unplug battery if DS fails (mentor). Remove TRACE configure if it interferes — driving without TRACE is required to still work.

## Cleanup requirements

Battery off and stored; robot on blocks; gamepads away; cables un-trip-hazarded.

## Next-session preparation

- Label two batteries "A" and "B" if possible for S007
- Install AMPER into the FTC project **passively** if mentors completed [AMPER install](https://github.com/The-Allsparks/AMPER/blob/main/docs/install.md); otherwise S007 uses graphs of DS voltage or a desktop walkthrough
- Clear any S006 blockers before AMPER passive work

## Hardware-unavailable fallback

Push-bot or unpowered roll on carpet while a partner logs paper events. Inspection on whatever structure exists.

## Robot-unavailable simulation option

Driver practice on gamepad-to-telemetry dummy OpMode if a Hub exists without drivebase. If no Hub: gamepad drills + paper event log; construction students finish S004 repair list items.

## Links to authoritative project documentation

- [TRACE mentor guide](https://github.com/The-Allsparks/TRACE/blob/main/docs/mentor-guide.md)
- [TRACE student path](https://github.com/The-Allsparks/TRACE/blob/main/docs/student-learning-path.md)
- [TRACE examples](https://github.com/The-Allsparks/TRACE/blob/main/examples/README.md)
- [Pedro Pathing introduction](https://pedropathing.com/docs/pathing) (read for later; do not install during driving block)
- [projects/trace.md](../../../projects/trace.md)
- [projects/pedro-pathing.md](../../../projects/pedro-pathing.md)
- [S003 modified drivetrain](S003-modified-drivetrain-install.md)
- [S004 control wiring](S004-control-system-wiring-prep.md)

## Mentor notes

Drivetrain construction **started in S002–S004**, not today. If teleop is not ready, the 35-minute block finishes it — not the 55-minute drive block. Do not skip restraint. Do not skip the honest blocker path. Hardware validation of TRACE on a Control Hub is still **unclaimed** by the TRACE project.
