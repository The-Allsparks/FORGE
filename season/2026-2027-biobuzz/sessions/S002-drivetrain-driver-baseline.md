---
id: S002
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

# S002 — Drivetrain inspection, driver baseline, and log review

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S002 |
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

Students will inspect the drivetrain, collect a driver baseline (blocks first), and review TRACE (or paper) logs from S001 plus today's runs.

## Robot outcome

- Drivetrain inspection checklist complete
- Wheels-off or restrained teleop baseline **or** documented blocker
- At least one TRACE event around `Drive/Baseline start` and `Drive/Baseline stop` if software is ready; otherwise paper log

## Prerequisites

- S001 chassis progress
- Mentor present for any powered motors
- Gamepads; Driver Station
- Blocks, crate, or known restraint

## Vocabulary

baseline · loop · disable · inspection · input (driver stick) vs event

## Safety concerns

- First motion: blocks/restraint, adult supervision, exclusion zone
- Hair, hoodies, ties away from chain/belt/pulleys
- Battery connector fully seated; no drive if wiring is unknown
- Stop test if a wheel retention fails

## Required hardware

- Drivetrain as assembled; battery; Control Hub if available
- Blocks/restraint; safety glasses

## Required software

- Team teleop OpMode (even a sample arcade drive)
- TRACE if already wired; otherwise DS timer + paper events
- Driver Station

## Preparation required before the meeting

- Charge batteries
- Confirm a teleop OpMode deploys (mentor laptop + Hub)
- Print inspection checklist (fasteners, wires, wheel screws)
- Open S001 event export

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Review S001 event order; today's test goal: **straight, stop, log**; safety: blocks first |
| 35 | Repair / tune / program | Inspection repair (tightening, wire dress); if teleop missing, programmers finish a minimal drive OpMode while others continue inspection |
| 55 | Driving / auto reps | Wheels-off stick mapping 10 min; then restrained or short carpet runs if mentor OK. Repeat: start event → 15 s drive → stop event. No Pedro tuning marathon. Drivers rotate |
| 20 | Closeout | Inspection sign-off; log review (did events match what drivers felt?); explain-back; dashboard: Driver-control + mechanical; cleanup |

## Mentor demonstration

Two minutes: show a bad log (`Drive start` after the robot already moved). Ask why the story is wrong. Then students instrument their own runs.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Inspection and repair |
| Electrical | Battery/Hub power path check with mentor |
| Programming | TRACE events around the baseline; loop does not block on disk |
| Drive team | Baseline repetitions; call "stop" and mean it |
| Documentation | Times, surprises, photo of restraint setup |

## Integrated build or test activity

The 55-minute block is the product. Software exists to timestamp it, not to replace it.

## Failure-injection scenario

Mentor calls "disable" at a random time. Robot must stop via DS. Students mark whether TRACE captured a stop event. If TRACE was not on the robot, they write the gap — do not fake Hub success.

## Evidence to collect

- Inspection checklist
- Count of baseline reps
- TRACE or paper timeline
- Note: Control Hub TRACE file sink is **not** claimed unless they actually exported from the Hub ([TRACE README current limitations](https://github.com/The-Allsparks/TRACE/blob/main/README.md))

## Student explain-back questions

1. What was the test goal in one sentence?
2. Is a stick value an input or an event?
3. What happens if TRACE is off — can you still drive?
4. Name one mechanical defect inspection found (or "none, and here is how we looked").

## Assessment or exit check

Driver can enable, drive the baseline, and disable without mentor hands on the sticks. Programmer or documenter can retell the run from the log.

## Portfolio or engineering-notebook artifact

Baseline table: driver, surface (blocks/carpet), duration, result, log pointer.

## Competition enablement impact

Driver-control ladder toward 4–5 later. **Not** competition approved. Pedro not enabled as a follower yet — only chassis motion via teleop.

## Rollback procedure

DS stop. Unplug battery if DS fails (mentor). Remove TRACE configure if it interferes — driving without TRACE is required to still work.

## Cleanup requirements

Battery off and stored; robot on blocks; gamepads away; cables un-trip-hazarded.

## Next-session preparation

- Label two batteries "A" and "B" if possible for S003
- Install AMPER into the FTC project **passively** if mentors completed [AMPER install](https://github.com/The-Allsparks/AMPER/blob/main/docs/install.md); otherwise S003 uses graphs of DS voltage or a desktop walkthrough
- Continue drivetrain remaining fasteners

## Hardware-unavailable fallback

Push-bot or unpowered roll on carpet while a partner logs paper events. Inspection performed on whatever structure exists.

## Robot-unavailable simulation option

Driver practice on a gamepad-to-telemetry dummy OpMode if a Hub exists without a drivebase. If no Hub: watch a recorded FTC teleop (team choice) and write an event log as homework-in-meeting; construction-capable students work on any available mechanical kit.

## Links to authoritative project documentation

- [TRACE mentor guide](https://github.com/The-Allsparks/TRACE/blob/main/docs/mentor-guide.md)
- [TRACE student path](https://github.com/The-Allsparks/TRACE/blob/main/docs/student-learning-path.md)
- [TRACE examples](https://github.com/The-Allsparks/TRACE/blob/main/examples/README.md)
- [Pedro Pathing introduction](https://pedropathing.com/docs/pathing) (read for later; do not install during driving block)
- [projects/trace.md](../../../projects/trace.md)
- [projects/pedro-pathing.md](../../../projects/pedro-pathing.md)

## Mentor notes

If teleop is not ready, the 35-minute repair/program block is the place to finish it — not the 55-minute drive block. Do not skip restraint. Hardware validation of TRACE on a Control Hub is still **unclaimed** by the TRACE project; do not tell students it is match-proven.
