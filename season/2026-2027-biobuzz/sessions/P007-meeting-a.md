---
id: P007
title: "Drivetrain dial-in and Kickoff preparation"
date: 2026-09-07
meeting_type: A
season_phase: preseason
event_checkpoint: none
status: scheduled
difficulty: Foundation
projects: []
active_features: []
---

# P007 — Drivetrain dial-in and Kickoff preparation

## Planned versus actual (this session has not run)

Original P007 plan was the **reusable mechanism laboratory** (capstan, slide, transport). That lab is deferred after Kickoff to [S001](S001-meeting-a.md) / [S003](S003-meeting-a.md) **only if** official BIOBUZZ materials justify those principles.

Tonight uses about **75 minutes** to dial in the drivetrain from [P006](P006-meeting-b.md) first movement, then **30–45 minutes** (integration + closeout) to finish Kickoff preparation. [P008](P008-meeting-b.md) is an FRC team tour, not a shop meeting and not the Kickoff-readiness review. [K001](K001-meeting-k.md) is the next day.

Do **not** claim a full performance baseline if P006 found a blocking hardware or software fault.

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | P007 |
| Title | Drivetrain dial-in and Kickoff preparation |
| Calendar date | 2026-09-07 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | Preseason week 2 (rescoped) |
| Meeting type | A |
| Season phase | preseason |
| Event checkpoint | none |
| Difficulty | Foundation |

## Driving question

Can we make robot-centric driving predictable enough to practice, **and** leave packed for Kickoff tomorrow-plus-one — knowing Friday is a tour, not more shop time?

## Student-facing objective

**Primary objective:** Correct motor directions and mixing enough for controlled forward, backward, strafe, and rotation, then finish Kickoff worksheets, analysis roles, and materials for [K001](K001-meeting-k.md).

**Student learning outcomes:**

- Correct reversed motors and hardware-configuration mistakes found at P006
- Check mecanum wheel arrangement against the motion they see
- Explain robot-centric forward, strafe, and rotation mixing in student language
- Use conservative speed limiting; add the planned trigger-based speed increase **only if** basic drive is already reliable
- Set controller deadbands
- Inspect wheel retention, fasteners, wiring, battery behavior, and unusual current or heat
- Practice controlled driving without treating it as a finished baseline if faults remain
- Take a Kickoff analysis role and pack rule-question, scoring, field-element, strategy, robot-requirement, and inspection worksheets
- Separate facts, assumptions, and ideas
- Name minimum viable robot thinking for after the reveal

## Robot outcome

- Motor directions and hardware configuration corrected **or** remaining blockers with owners
- Robot-centric mixing good enough for slow practice **or** honest “not yet”
- Conservative speed limit in TeleOp
- Trigger-based speed increase **only if** basic drive is reliable; otherwise leave it off
- Controller deadbands recorded
- Inspection notes: retention, fasteners, wiring, battery, heat/current if observed
- Repeatable problems and baseline **observations** written — not a fake performance sheet
- Kickoff role sheet, worksheets, and packed notebook for K001
- Student learning-goal baselines ([FORGE#26](https://github.com/The-Allsparks/FORGE/issues/26) moved here because P008 is the tour)

## Prerequisites

- [P006](P006-meeting-b.md) electrical diagram, port table, and first-movement attempt **or** written blocker
- If P006 never enabled motors, tonight’s construction block **starts by finishing P006 safety tests** — then dial-in is partial
- Mentor present for energized tests
- P006 power-path diagram and deferred-fault list
- P005 v0 open-question list (study notes only)
- Printed Kickoff worksheets (mentor)
- [kickoff-replan-guide.md](../kickoff-replan-guide.md)
- [preseason-kickoff-gate.md](../docs/preseason-kickoff-gate.md)
- [student-learning-goal.md](../../../templates/student-learning-goal.md) × 4

## Vocabulary

robot-centric · mecanum mix · deadband · speed limit · fact · assumption · idea · minimum viable robot · official materials · v0

## Safety concerns

- Blocks or restraint first if directions are still unknown
- Exclusion zone for floor practice
- Disable/stop before anyone else picks up a gamepad
- Stop on binding, loose retention, hot motors, or mystery current draw
- No powered prototype game mechanisms on the Strafer
- Do not treat P005 v0 notes as inspection-legal rules

## Required hardware

- Robot after P006
- Blocks/stand; safety glasses
- Charged battery; gamepads
- P006 diagram and motor-test table

## Required software

- Same TeleOp as P006, edited for directions, mix, speed limit, and deadband
- Driver Station
- No new library installs

## Preparation required before the meeting

- Charge batteries and gamepads
- Print P006 deferred-fault list and blank observation sheet
- Print K001 role sheet (game manual, scoring, field elements, strategy, robot requirements, inspection)
- Print fact / assumption / idea headers
- Print [student-learning-goal.md](../../../templates/student-learning-goal.md) × 4
- Pack a Kickoff bag list (notebook, worksheets, charged laptop if used Saturday)
- Confirm P008 tour logistics separately — **do not steal tonight for tour planning beyond a one-line reminder**

## Exact 120-minute agenda

Meeting A durations. Construction is drivetrain work (~75 min). Kickoff preparation uses the 25-minute integration block plus closeout (~35 min total).

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Friday is the FRC tour; Kickoff process must finish tonight. Review P006 faults. Blocks first if directions are still wrong. |
| 75 | Construction | Correct motor directions and hardware configuration. Verify mecanum wheel arrangement and resulting motion. Correct robot-centric forward/strafe/rotation mixing. Add conservative speed limiting. Add trigger-based speed increase **only if** basic drive is reliable. Set deadbands. Inspect wheel retention, fasteners, wiring, battery behavior, and unusual current/heat. Practice controlled forward, backward, strafe, and rotation. Record repeatable problems. If P006 was blocked, finish safe enable before any “dial-in” claim. |
| 25 | Integration | Kickoff preparation: assign game-manual and field-analysis roles. Prepare rule-question, scoring, field-element, strategy, robot-requirement, and inspection worksheets. Review how the team will separate facts, assumptions, and ideas. Identify how students will name **minimum viable robot** functions after the reveal. Confirm materials, links, and K001 responsibilities. |
| 10 | Closeout | Learning-goal baselines; pack notebook and worksheets; dashboard; explain-back; battery off; cleanup. |

## Mentor demonstration

Two minutes: one wrong motor direction and how the mix looks “haunted.” One minute: a worksheet row marked **fact** vs **assumption** vs **idea**. Students then drive and fill their own sheets.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Retention, wheel arrangement, fastener inspection |
| Electrical | Recheck labels and power path if a motor still misbehaves |
| Programming | Directions, mix, speed limit, deadband — time-boxed |
| Drive team | Controlled practice; call stop |
| Documentation | Observation sheet; Kickoff worksheets; learning goals |

## Integrated build or test activity

Dial-in **is** the construction block. Kickoff worksheets **are** the integration block. Do not skip worksheets to take extra laps. Do not skip driving to decorate worksheets if the robot is safe to practice.

## Failure-injection scenario

Mentor claims “we already know the game from v0, so skip Kickoff reading.” Students must refuse: v0 is study notes; official Kickoff materials win. Second: mentor asks to enable full-speed trigger before forward/strafe/rotate are correct. Students must refuse.

## Evidence to collect

- Updated motor-direction / configuration table
- Mixing and speed-limit notes
- Driving observation sheet (repeatable problems, not a fake score)
- Kickoff role assignment sheet
- Completed or started worksheets listed above
- Four learning-goal baselines
- Packed-for-K001 checklist

## Student explain-back questions

1. What still makes the drivetrain confusing, if anything?
2. Why is trigger-boost off until basic drive is reliable?
3. What is your K001 role?
4. Name one v0 note that must be **reverified** from official Kickoff materials.
5. What is the difference between a fact, an assumption, and an idea?

## Assessment or exit check

**Definition of done:**

- Drivetrain is practice-able **or** remaining faults have owners (no fake baseline if P006 was blocked)
- Every student has a K001 role and can say it
- Worksheets and notebook are packed for Saturday
- Four learning-goal baselines exist
- Team can explain that Friday is a tour and Kickoff analysis uses **official** materials

A full measured driver baseline is **not** required. Capstan/slide/transport experiments are **not** tonight.

## Portfolio or engineering-notebook artifact

Driving observations + Kickoff role sheet (Think process). Learning-goal baselines.

## Competition enablement impact

Practice driving only. No competition approval. No optional libraries. Kickoff process ready; game strategy **not** locked.

## Rollback procedure

If TeleOp edits break disable or mixing, revert to the P006 version that could stop. If worksheets over-commit mechanisms from v0, mark them **Kickoff pending**.

## Cleanup requirements

Battery disconnected; robot stable; worksheets in the Kickoff bag; tools away.

## Next-session preparation

- [P008](P008-meeting-b.md) (2026-09-11): **FRC team tour** — not shop bring-up
- [K001](K001-meeting-k.md) (2026-09-12): official Kickoff materials; bring tonight’s packed bag
- Confirm tour permission slips / transport with mentors (details live outside git)
- Travel battery off for Saturday

## Hardware-unavailable fallback

If the robot cannot drive: document the blocker, then **still complete the full Kickoff-prep block**. Paper-drive the mix on a whiteboard. Do not cancel K001 prep.

## Robot-unavailable simulation option

Same as fallback. Role sheet and worksheets still required.

## Links to authoritative project documentation

- [preseason-deferred-work.md](../docs/preseason-deferred-work.md)
- [P006 first movement](P006-meeting-b.md)
- [P008 FRC team tour](P008-meeting-b.md)
- [K001 kickoff session](K001-meeting-k.md)
- [P005 v0 rules record](P005-meeting-a.md)
- [kickoff-replan-guide.md](../kickoff-replan-guide.md)
- [kickoff-decision-package.md](../../../templates/kickoff-decision-package.md)
- [student-learning-goal.md](../../../templates/student-learning-goal.md)
- [preseason-kickoff-gate.md](../docs/preseason-kickoff-gate.md)
- [learning-paths/drive-team.md](../../../learning-paths/drive-team.md)
- [learning-paths/programming.md](../../../learning-paths/programming.md)
- [docs/safety-and-enablement.md](../../../docs/safety-and-enablement.md)
- [season-plan.md](../season-plan.md)

## Mentor notes

Protect the 25-minute Kickoff block. P008 cannot recover it. If P006 never moved, spend construction on safe enable and simple robot-centric drive — then still pack for K001. Original mechanism-lab stations do **not** fill leftover time; extra minutes go to disable drills or worksheet quality. Learning-goal baselines live here, not at the tour.
