---
id: P006
title: "Electrical diagram, programming bring-up, and first movement"
date: 2026-09-04
meeting_type: B
season_phase: preseason
event_checkpoint: none
status: scheduled
difficulty: Foundation
projects: []
active_features: []
---

# P006 — Electrical diagram, programming bring-up, and first movement

## Planned versus actual (this session has not run)

Original P006 plan was **driver baseline and chassis reliability**. That full performance baseline is **not** tonight. Tonight is first wiring documentation, first programming bring-up, and **first controlled movement** if no blocking hardware fault is found.

Electrical work originally planned for P004 and motor/SDK bring-up originally planned for P005 move here. Polished driving, field-centric control, odometry, autonomous, and drivetrain dial-in move to [P007](P007-meeting-a.md). The original P007 mechanism laboratory stays deferred after Kickoff.

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | P006 |
| Title | Electrical diagram, programming bring-up, and first movement |
| Calendar date | 2026-09-04 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | Preseason week 1 (rescoped) |
| Meeting type | B |
| Season phase | preseason |
| Event checkpoint | none |
| Difficulty | Foundation |

## Driving question

Can we draw the power path that is actually on Sparkee, command each drivetrain motor safely, and leave with **first driver-controlled movement** — even if the drive is not yet tuned?

## Student-facing objective

**Primary objective:** By the end of the meeting, Sparkee should move under driver control if no blocking hardware fault is found. It does **not** need to be fully tuned.

**Student learning outcomes:**

- Draw and explain the as-built electrical / power diagram
- Record Control Hub and Expansion Hub port assignments
- Name battery, main switch, hubs, drivetrain motors, and any servos, sensors, USB devices, and power-distribution connections that are **actually present**
- Help install or verify wiring, labels, strain relief, polarity, and a legal power path
- Open the FTC robot project, confirm the pinned FTC SDK builds and deploys, and create a Robot Controller hardware configuration plus a code hardware map
- Test one motor at a time with wheels off the floor or restrained
- Disable and stop the robot from the Driver Station
- Attempt slow floor movement only after restrained tests pass

## Robot outcome

- As-built electrical / power diagram that matches the robot
- Hub port assignment table
- Wiring installed or verified **or** a named blocker
- Minimal robot-centric mecanum TeleOp deployed **or** a named software blocker
- Each drivetrain motor commanded individually on blocks or restrained
- First controlled movement on the floor **if** no blocking hardware fault is found
- Written list of reversed motors, wrong wheel behavior, wiring faults, configuration mismatches, and work deferred to P007

**Not tonight:** field-centric control, odometry, autonomous, detailed tuning, polished driver controls, or a claim that the drivetrain is a performance baseline.

## Prerequisites

- P002–P004 Strafer / first-robot construction (as-built configuration is **not** fully documented in FORGE — inspect what is actually on the robot)
- P005 v0 rules review does **not** gate hardware
- Control Hub, battery, main switch, labels, zip ties, USB cable, and gamepad staged
- Mentor present for any battery connection or motor enable
- Coach-prepared FTC SDK project on a laptop (published TeamCode URL remains **BLOCKED** on [#2](https://github.com/The-Allsparks/FORGE/issues/2) — use the local project the team will actually flash)
- Blocks, crate, or stand for wheels-off-floor tests
- [preseason-deferred-work.md](../docs/preseason-deferred-work.md)

## Vocabulary

as-built · power path · port map · hardware configuration · hardware map · TeleOp · robot-centric · enable · disable · strain relief

## Safety concerns

- **Mentor present** for battery connection and every motor enable
- **Wheels off the floor or restrained** before any motor is commanded
- One motor at a time until each drivetrain motor is identified
- Test disable / stop **before** floor movement
- Hair, hoodies, lanyards, and fingers away from wheels
- Confirm polarity before seating power connectors
- Protect wiring from wheels; add strain relief
- No floor driving if retention, binding, unknown wiring, or disable-path failure exists
- Slow speed only if the robot reaches the floor
- Battery disconnected at cleanup

## Required hardware

- Robot as left after P002–P004
- Control Hub; Expansion Hub **if present**; battery; main switch
- Drivetrain motors and leads that are actually installed
- Any servos, sensors, USB devices, or power-distribution hardware that is actually present — do not invent extras
- Zip ties, labels, edge protection
- Blocks or stand; safety glasses
- Gamepad and Driver Station device

## Required software

- FTC SDK project pinned to the team’s chosen version (coach-prepared)
- Robot Controller hardware configuration
- Minimal robot-centric mecanum TeleOp
- Driver Station app
- Team notebook and camera
- Onshape **not required**
- TRACE library **not required** — paper notes are enough

## Preparation required before the meeting

- Print or project [p006-power-path-example.html](../docs/p006-power-path-example.html) — students copy **this robot**, not a generic internet drawing
- Print blank tables: power-path components; hub ports; motor-test results
- Charge robot batteries and the Driver Station device
- Mentors: FTC project must **build and deploy** on a laptop before students arrive — do not spend the meeting installing Android Studio
- Stage electrical parts on a clear table
- Mark an exclusion zone and a blocks/restraint station
- Assign rotating pairs: diagram, wiring, configuration/code, documentation

## Exact 120-minute agenda

Meeting B durations. The 55-minute block starts with code and restrained tests, then floor movement only if those tests pass.

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Goal: first controlled movement, not a tuned robot. Battery and disable rules. Wheels-off-floor first. Roles. |
| 35 | Electrical diagram and wiring | (1) Create and review the as-built electrical/power diagram. (2) Assign Control Hub and Expansion Hub ports. (3) Document battery, main switch, hubs, drivetrain motors, and any servos, sensors, USB devices, and power-distribution connections that are actually present. (4) Install or verify wiring, wire retention, strain relief, polarity, serviceability, and legal power paths. |
| 55 | Programming and first movement | (5) Create or open the FTC robot project; verify the pinned FTC SDK builds and deploys. (6) Create the Robot Controller hardware configuration and code hardware map. (7) Implement a minimal robot-centric mecanum TeleOp. (8) Test one motor at a time with wheels restrained or off the floor. (9) Test disable/stop. (10) If restrained tests pass, attempt slow forward, backward, strafe, and rotation on the floor. |
| 20 | Closeout | (11) Record reversed motors, incorrect wheel behavior, wiring faults, configuration mismatches, and work deferred to P007. Photos; dashboard; explain-back; battery off; cleanup. |

## Mentor demonstration

Three minutes: trace battery → switch → Hub on the real robot, then show one unacceptable wire near a wheel. Two minutes: one restrained motor enable and an immediate Driver Station disable **before** anyone else enables. Students then do the work.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Help inspect wheel retention and keep the robot on blocks until tests pass |
| Electrical | Diagram, port table, wiring, polarity, strain relief |
| Programming | Hardware configuration, hardware map, minimal TeleOp, deploy |
| Drive team | Call disable; later, slow floor commands if the mentor releases the robot |
| Documentation | Diagram, port table, motor-test notes, deferred list for P007 |

Rotate paths. Do not silo one student on code for the whole meeting.

## Integrated build or test activity

The integrated test is **one motor at a time on blocks**, then disable/stop, then slow floor movement only if those tests pass. Drawing a diagram with no robot test is not done. Driving without a matching diagram and port table is not done.

## Failure-injection scenario

Mentor asks where the emergency disconnect is, then asks which DS control stops the robot. If a student cannot point to both, do not go to the floor. If a wheel turns the wrong way on blocks, record it — do not “fix it later” by driving faster.

## Evidence to collect

- As-built electrical / power diagram (notebook page plus photo)
- Hub port assignment table
- Wiring photos showing labels and strain relief **or** blocker with owner
- Hardware configuration / hardware-map notes
- Motor-by-motor test table (corner, port, direction, bind Y/N)
- Disable/stop demonstration note
- First-movement note: succeeded, partial, or blocked — **honest**
- Deferred list for P007

## Student explain-back questions

1. Trace the power path from battery to one motor on **this** robot.
2. How do you disable or stop from the Driver Station?
3. Why did we test on blocks before the floor?
4. Did Sparkee move under driver control tonight, and what is still wrong?
5. What is **not** finished (field-centric, odometry, auto, tuning)?

## Assessment or exit check

**Definition of done (realistic):**

- The electrical diagram matches the robot’s actual configuration
- Hub port assignments are recorded
- The Driver Station can connect, enable, disable, and safely stop the robot
- Each drivetrain motor can be commanded individually
- Sparkee achieves first controlled movement **if** no blocking hardware fault is found
- Field-centric control, odometry, autonomous, detailed tuning, and polished driver controls are explicitly deferred
- Battery is disconnected at cleanup

Path B (partial) is success if blockers are written. Pretending P004 wiring or P005 bring-up already happened is failure.

## Portfolio or engineering-notebook artifact

Power-path sketch + port table + first-movement note (Control / Design process). Inspection photos.

## Competition enablement impact

First enable and first movement only. Ladder may reach restrained hardware or slow floor practice. Combined-stack acceptance **not** claimed ([FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4)). No optional library enabled.

## Rollback procedure

Driver Station stop. Disconnect battery. Do not keep driving to “see if it gets better.” Revert TeleOp changes that break disable. Do not improvise illegal power adapters.

## Cleanup requirements

Battery disconnected and stored; robot stable; Hub off; gamepads stored; aisles clear; tools returned.

## Next-session preparation

- [P007](P007-meeting-a.md) (2026-09-07): drivetrain dial-in **and** Kickoff preparation
- Pack tonight’s diagram, port table, and deferred-fault list
- Charge batteries; confirm gamepads
- Mentors: if first movement was blocked, plan P007 opening to finish the blocker before any tuning claim
- Do **not** assign Onshape or GitHub homework as a gate

## Hardware-unavailable fallback

If Hub or battery is missing: finish the paper diagram and port plan; walk through DS screens on a phone with no robot; write the blocker. Do not claim movement.

If the SDK project will not deploy: keep wiring and restrained diagnosis; document the software blocker; do not skip disable teaching on a simulator or paper DS.

## Robot-unavailable simulation option

Paper chassis: students mark battery, switch, Hub, and motor ports and defend the layout. Practice pointing to disable on a DS screenshot. Fill the as-built table as “not inspected on metal.”

## Links to authoritative project documentation

- [preseason-deferred-work.md](../docs/preseason-deferred-work.md)
- [P002](P002-meeting-s.md)–[P004](P004-meeting-s.md) construction records
- [P007 drivetrain dial-in and Kickoff preparation](P007-meeting-a.md)
- [p006-power-path-example.html](../docs/p006-power-path-example.html)
- [learning-paths/electrical.md](../../../learning-paths/electrical.md)
- [learning-paths/programming.md](../../../learning-paths/programming.md)
- [learning-paths/drive-team.md](../../../learning-paths/drive-team.md)
- [docs/safety-and-enablement.md](../../../docs/safety-and-enablement.md)
- [docs/stack-acceptance.md](../../../docs/stack-acceptance.md)
- [docs/team-robot-project.md](../../../docs/team-robot-project.md) — **BLOCKED** on [#2](https://github.com/The-Allsparks/FORGE/issues/2)
- [preseason-software-allocation.md](../docs/preseason-software-allocation.md)
- [readiness-dashboard.md](../readiness-dashboard.md)

## Mentor notes

Meeting B **filename stays** `P006-meeting-b.md`. First movement is the goal, not a perfect mecanum mix. If wiring eats the 35-minute block, still attempt one restrained motor before leaving — that is more honest than a pretty diagram with no enable. If a blocking hardware fault appears, stop and write it; [P007](P007-meeting-a.md) must not claim a full performance baseline. Keep CAD, GitHub workflow, and mechanism brainstorming off this meeting.
