---
id: P007
title: "Finish bring-up, first movement, and Kickoff preparation"
date: 2026-09-07
meeting_type: A
season_phase: preseason
event_checkpoint: none
status: scheduled
difficulty: Foundation
projects: []
active_features: []
---

# P007 — Finish bring-up, first movement, and Kickoff preparation

## Planned versus actual (this session has not run)

Original P007 plan was the **reusable mechanism laboratory** (capstan, slide, transport). That lab is deferred after Kickoff to [S001](S001-meeting-a.md) / [S003](S003-meeting-a.md) **only if** official BIOBUZZ materials justify those principles.

The 2 September rescope used ~75 minutes to **dial in** the drivetrain from P006 first movement, then Kickoff preparation. **That dial-in plan is not tonight’s opening.** [P006](P006-meeting-b.md) was a code walkthrough: no electrical diagram, no useful programming, no enable, no movement.

Tonight is the **last shop meeting before Kickoff.** [P008](P008-meeting-b.md) is an FRC team tour. [K001](K001-meeting-k.md) is the next day. Construction time **finishes P006:** as-built electrical/power path as needed for safe enable, hardware configuration, minimal robot-centric TeleOp, restrained one-motor tests, disable/stop, then first movement if no blocking fault. Dial-in (mix, speed limit, deadband, practice laps) is **leftover only** after the robot already moves. Kickoff worksheets still use integration + closeout — P008 cannot recover them.

Do **not** claim a full performance baseline. Do **not** open as if P006 already produced first movement.

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | P007 |
| Title | Finish bring-up, first movement, and Kickoff preparation |
| Calendar date | 2026-09-07 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | Preseason week 2 (rescoped after P006 variance) |
| Meeting type | A |
| Season phase | preseason |
| Event checkpoint | none |
| Difficulty | Foundation |

## Driving question

Can we put a legal power path on paper and on the robot, command drivetrain motors safely, leave with **first driver-controlled movement** if nothing blocks it — **and** still pack for Kickoff — knowing Friday is a tour, not more shop time?

## Student-facing objective

**Primary objective:** Complete the P006 work that did not happen: electrical diagram and wiring as needed for safe enable, a deployable hardware configuration and minimal TeleOp, restrained motor tests, disable/stop, and first controlled movement **if** no blocking hardware fault is found. Then finish Kickoff worksheets, analysis roles, and materials for [K001](K001-meeting-k.md).

**Dial-in is not the primary objective.** Correct reversed motors and mixing only if first movement already happened with time remaining. Otherwise write the leftover list for [S002](S002-meeting-b.md).

**Student learning outcomes:**

- Draw and explain the as-built electrical / power diagram
- Record Control Hub and Expansion Hub port assignments
- Help install or verify wiring, labels, strain relief, polarity, and a legal power path
- Open the FTC robot project, confirm it builds and deploys, and create a Robot Controller hardware configuration plus a code hardware map
- Test one motor at a time with wheels off the floor or restrained
- Disable and stop the robot from the Driver Station
- Attempt slow floor movement only after restrained tests pass
- Take a Kickoff analysis role and pack rule-question, scoring, field-element, strategy, robot-requirement, and inspection worksheets
- Separate facts, assumptions, and ideas
- Name minimum viable robot thinking for after the reveal

## Robot outcome

- As-built electrical / power diagram that matches the robot **or** a named blocker
- Hub port assignment table **or** enable explicitly forbidden
- Wiring installed or verified **or** a named blocker
- Minimal robot-centric mecanum TeleOp deployed **or** a named software blocker
- Each drivetrain motor commanded individually on blocks or restrained **or** blocked in writing
- First controlled movement on the floor **if** no blocking hardware fault is found
- Written list of reversed motors, wrong wheel behavior, wiring faults, configuration mismatches, and work deferred to S002
- Kickoff role sheet, worksheets, and packed notebook for K001
- Student learning-goal baselines ([FORGE#26](https://github.com/The-Allsparks/FORGE/issues/26) lives here because P008 is the tour)

**Not tonight unless first movement already succeeded with spare time:** field-centric control, odometry, autonomous, detailed tuning, polished driver controls, trigger-boost, or a claim that the drivetrain is a performance baseline.

## Prerequisites

- P002–P004 construction (as-built configuration is **not** fully documented — inspect what is actually on the robot)
- [P006](P006-meeting-b.md) was a **code walkthrough only** — do not wait for a P006 diagram, port table, or TeleOp that does not exist
- Mentor present for any battery connection or motor enable
- Coach-prepared FTC SDK project on a laptop that **already builds and deploys** ([The-Allsparks/FtcRobotController](https://github.com/The-Allsparks/FtcRobotController), `bumblebee` branch)
- Blocks, crate, or stand for wheels-off-floor tests
- P005 v0 open-question list (study notes only)
- Printed Kickoff worksheets (mentor)
- [p006-power-path-example.html](../docs/p006-power-path-example.html)
- [kickoff-replan-guide.md](../kickoff-replan-guide.md)
- [preseason-kickoff-gate.md](../docs/preseason-kickoff-gate.md)
- [student-learning-goal.md](../../../templates/student-learning-goal.md) × 4

## Vocabulary

as-built · power path · port map · hardware configuration · hardware map · TeleOp · robot-centric · enable · disable · strain relief · fact · assumption · idea · minimum viable robot · official materials · v0

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
- No powered prototype game mechanisms on the Strafer
- Do not treat P005 v0 notes as inspection-legal rules

## Required hardware

- Robot as left after P002–P004 (P006 did not change the as-built electrical state in FORGE)
- Control Hub; Expansion Hub **if present**; battery; main switch
- Drivetrain motors and leads that are actually installed
- Any servos, sensors, USB devices, or power-distribution hardware that is actually present — do not invent extras
- Zip ties, labels, edge protection
- Blocks or stand; safety glasses
- Gamepad and Driver Station device

## Required software

- FTC SDK project pinned to the team’s chosen version (coach-prepared, building **before** students arrive)
- Robot Controller hardware configuration
- Minimal robot-centric mecanum TeleOp
- Driver Station app
- Team notebook and camera
- No new library installs
- Onshape **not required**
- TRACE library **not required** — paper notes are enough

## Preparation required before the meeting

- Mentors: FTC project must **build and deploy** on a laptop before students arrive — do not spend the last shop night installing Android Studio
- Print or project [p006-power-path-example.html](../docs/p006-power-path-example.html) — students copy **this robot**, not a generic internet drawing
- Print blank tables: power-path components; hub ports; motor-test results
- Charge robot batteries and the Driver Station device
- Stage electrical parts on a clear table
- Mark an exclusion zone and a blocks/restraint station
- Print K001 role sheet (game manual, scoring, field elements, strategy, robot requirements, inspection)
- Print fact / assumption / idea headers
- Print [student-learning-goal.md](../../../templates/student-learning-goal.md) × 4
- Pack a Kickoff bag list (notebook, worksheets, charged laptop if used Saturday)
- Confirm P008 tour logistics separately — **do not steal tonight for tour planning beyond a one-line reminder**

## Exact 120-minute agenda

Meeting A durations. Construction **is P006 catch-up** (~75 min). Kickoff preparation uses the 25-minute integration block plus closeout (~35 min total). Do not skip worksheets for extra laps. Do not skip enable work to decorate worksheets if the robot can be made safe to test.

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Last shop night. Friday is the FRC tour; Kickoff process must finish tonight. P006 was code reading only — tonight starts with wiring and restrained tests, not dial-in. Battery and disable rules. Roles. |
| 75 | Construction | (1) Create and review the as-built electrical/power diagram. (2) Assign Control Hub and Expansion Hub ports. (3) Install or verify wiring, retention, strain relief, polarity, and legal power paths. (4) Create or open the FTC project; verify it builds and deploys. (5) Hardware configuration and code hardware map. (6) Minimal robot-centric mecanum TeleOp. (7) One motor at a time, wheels restrained. (8) Test disable/stop. (9) If restrained tests pass, attempt slow forward, backward, strafe, and rotation on the floor. (10) **Only if** the robot already moves with time remaining: correct reversed motors/mix, conservative speed limit, deadbands. Record leftover faults for S002. |
| 25 | Integration | Kickoff preparation: assign game-manual and field-analysis roles. Prepare rule-question, scoring, field-element, strategy, robot-requirement, and inspection worksheets. Review how the team will separate facts, assumptions, and ideas. Identify how students will name **minimum viable robot** functions after the reveal. Confirm materials, links, and K001 responsibilities. |
| 10 | Closeout | Learning-goal baselines; pack notebook and worksheets; dashboard; explain-back; battery off; cleanup. |

## Mentor demonstration

Three minutes: trace battery → switch → Hub on the real robot, then show one unacceptable wire near a wheel. Two minutes: one restrained motor enable and an immediate Driver Station disable **before** anyone else enables. One minute: a worksheet row marked **fact** vs **assumption** vs **idea**. Students then do the work.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Inspect wheel retention; keep the robot on blocks until tests pass |
| Electrical | Diagram, port table, wiring, polarity, strain relief |
| Programming | Hardware configuration, hardware map, minimal TeleOp, deploy — time-boxed; mix/deadband only if movement already works |
| Drive team | Call disable; later, slow floor commands if the mentor releases the robot |
| Documentation | Diagram, port table, motor-test notes, leftover list for S002; Kickoff worksheets; learning goals |

Rotate paths. Do not silo one student on code for the whole meeting.

## Integrated build or test activity

The integrated test is **one motor at a time on blocks**, then disable/stop, then slow floor movement only if those tests pass. Drawing a diagram with no robot test is not done. Driving without a matching diagram and port table is not done. Kickoff worksheets **are** the integration block.

## Failure-injection scenario

Mentor asks where the emergency disconnect is, then asks which DS control stops the robot. If a student cannot point to both, do not go to the floor. If a wheel turns the wrong way on blocks, record it — do not “fix it later” by driving faster. Second: mentor claims “we already know the game from v0, so skip Kickoff reading.” Students must refuse: v0 is study notes; official Kickoff materials win. Third: mentor asks to enable full-speed trigger before the robot has even moved. Students must refuse.

## Evidence to collect

- As-built electrical / power diagram (notebook page plus photo) **or** blocker with owner
- Hub port assignment table
- Wiring photos showing labels and strain relief **or** blocker with owner
- Hardware configuration / hardware-map notes
- Motor-by-motor test table (corner, port, direction, bind Y/N)
- Disable/stop demonstration note
- First-movement note: succeeded, partial, or blocked — **honest**
- Deferred list for S002 (dial-in leftover)
- Kickoff role assignment sheet
- Completed or started worksheets listed above
- Four learning-goal baselines
- Packed-for-K001 checklist

## Student explain-back questions

1. Trace the power path from battery to one motor on **this** robot.
2. How do you disable or stop from the Driver Station?
3. Why did we test on blocks before the floor?
4. Did BumbleBee move under driver control tonight, and what is still wrong?
5. What is your K001 role, and which v0 note must be **reverified** from official Kickoff materials?

## Assessment or exit check

**Definition of done (realistic):**

- The electrical diagram matches the robot’s actual configuration **or** a named blocker
- Hub port assignments are recorded **or** enable is forbidden in writing
- The Driver Station can connect, enable, disable, and safely stop **or** that gap is written
- Each drivetrain motor can be commanded individually **or** blocked in writing
- BumbleBee achieves first controlled movement **if** no blocking hardware fault is found
- Every student has a K001 role and can say it
- Worksheets and notebook are packed for Saturday
- Four learning-goal baselines exist
- Field-centric control, odometry, autonomous, detailed tuning, and a full measured baseline are explicitly deferred
- Battery is disconnected at cleanup

A full measured driver baseline is **not** required. Capstan/slide/transport experiments are **not** tonight. Pretending P006 already moved the robot is failure.

## Portfolio or engineering-notebook artifact

Power-path sketch + port table + first-movement note **and** Kickoff role sheet (Control / Design / Think process). Learning-goal baselines. Inspection photos.

## Competition enablement impact

First enable and first movement only, if achieved. Ladder may reach restrained hardware or slow floor practice. Combined-stack acceptance **not** claimed ([FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4)). No optional library enabled. Kickoff process ready; game strategy **not** locked.

## Rollback procedure

Driver Station stop. Disconnect battery. Do not keep driving to “see if it gets better.” Revert TeleOp changes that break disable. Do not improvise illegal power adapters. If worksheets over-commit mechanisms from v0, mark them **Kickoff pending**.

## Cleanup requirements

Battery disconnected and stored; robot stable; Hub off; gamepads stored; worksheets in the Kickoff bag; aisles clear; tools returned.

## Next-session preparation

- [P008](P008-meeting-b.md) (2026-09-11): **FRC team tour** — not shop bring-up
- [K001](K001-meeting-k.md) (2026-09-12): official Kickoff materials; bring tonight’s packed bag
- If first movement was blocked, [S001](S001-meeting-a.md) may finish R0 chassis; [S002](S002-meeting-b.md) driving block is dial-in catch-up — do not pretend tonight produced a baseline
- Confirm tour permission slips / transport with mentors (details live outside git)
- Travel battery off for Saturday

## Hardware-unavailable fallback

If Hub or battery is missing: finish the paper diagram and port plan; walk through DS screens on a phone with no robot; write the blocker; **still complete the full Kickoff-prep block**. Do not claim movement. Do not cancel K001 prep.

If the SDK project will not deploy: keep wiring and restrained diagnosis; document the software blocker; do not skip disable teaching on a simulator or paper DS; **still pack Kickoff worksheets**.

## Robot-unavailable simulation option

Paper chassis: students mark battery, switch, Hub, and motor ports and defend the layout. Practice pointing to disable on a DS screenshot. Fill the as-built table as “not inspected on metal.” Role sheet and worksheets still required.

## Links to authoritative project documentation

- [preseason-deferred-work.md](../docs/preseason-deferred-work.md)
- [P006 code walkthrough](P006-meeting-b.md)
- [p006-power-path-example.html](../docs/p006-power-path-example.html)
- [P008 FRC team tour](P008-meeting-b.md)
- [K001 kickoff session](K001-meeting-k.md)
- [P005 v0 rules record](P005-meeting-a.md)
- [kickoff-replan-guide.md](../kickoff-replan-guide.md)
- [kickoff-decision-package.md](../../../templates/kickoff-decision-package.md)
- [student-learning-goal.md](../../../templates/student-learning-goal.md)
- [preseason-kickoff-gate.md](../docs/preseason-kickoff-gate.md)
- [learning-paths/electrical.md](../../../learning-paths/electrical.md)
- [learning-paths/programming.md](../../../learning-paths/programming.md)
- [learning-paths/drive-team.md](../../../learning-paths/drive-team.md)
- [docs/safety-and-enablement.md](../../../docs/safety-and-enablement.md)
- [docs/stack-acceptance.md](../../../docs/stack-acceptance.md)
- [docs/team-robot-project.md](../../../docs/team-robot-project.md) — [The-Allsparks/FtcRobotController](https://github.com/The-Allsparks/FtcRobotController)
- [preseason-software-allocation.md](../docs/preseason-software-allocation.md)
- [season-plan.md](../season-plan.md)

## Mentor notes

Protect the 25-minute Kickoff block. P008 cannot recover it. P006 produced a code walkthrough — construction tonight is wiring, deploy, restrained tests, and first movement, **not** mix tuning. If wiring eats most of the 75 minutes, still attempt one restrained motor before leaving — that is more honest than a pretty diagram with no enable. If a blocking hardware fault appears, stop and write it; do not claim a performance baseline. Original mechanism-lab stations do **not** fill leftover time. Keep CAD and GitHub workflow off this meeting. Learning-goal baselines live here, not at the tour.
