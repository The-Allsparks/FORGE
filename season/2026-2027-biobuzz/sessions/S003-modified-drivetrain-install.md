---
id: S003
title: "Modified Strafer drivetrain installation"
date: 2026-08-25
meeting_type: A
season_phase: preseason
event_checkpoint: none
status: complete
difficulty: Foundation
projects: []
active_features: []
---

# S003 — Modified Strafer drivetrain installation

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S003 |
| Title | Modified Strafer drivetrain installation |
| Calendar date | 2026-08-25 (planning input; Tuesday Meeting A) |
| Relative week | Preseason week 0 |
| Meeting type | A |
| Season phase | preseason |
| Event checkpoint | none |
| Difficulty | Foundation |

## Driving question

Why did we move wheels and motors from the standard StarterBot layout, and does the drivetrain roll smoothly with correct mecanum roller orientation?

## Student-facing objective

Students will confirm revised front and rear wheel locations, install drivetrain motors inside chassis rails, mount bearings, shafts, mecanum wheels and outside wheel supports, verify roller orientation, push-test for binding, measure front-wheel clearance for the planned intake wheel and angled servo mount, and document why this layout differs from the standard StarterBot.

## Robot outcome

- Mechanically complete rolling drivetrain (unpowered push-test acceptable)
- Measurements recorded for custom front servo/intake mount clearance
- Written design rationale comparing modified layout to standard StarterBot

## Prerequisites

- S002 chassis frame assembled and squared
- Strafer StarterBot drivetrain parts pulled and verified
- Mentors reviewed planned wheel/motor layout before students arrive

## Vocabulary

mecanum · roller orientation · binding · clearance · design rationale · inside-rail mount

## Safety concerns

- Pinch points at chains, belts, or shaft couplers if present
- Fingers clear during wheel spin push-test
- No battery connected unless mentor explicitly approves a later exception (default: **unpowered** today)
- Hair, hoodies, and lanyards away from rotating test areas

## Required hardware

- Completed chassis frame from S002
- Drivetrain motors, bearings, shafts, mecanum wheels, outside wheel supports
- Measuring tape or calipers; straightedge
- Hand tools per kit instructions

## Required software

- Team notebook
- Onshape (`36117-preseason` — update layout from S002)
- [templates/decision-record.md](../../../templates/decision-record.md) (paper) for layout rationale

## Preparation required before the meeting

- Print or open standard Strafer StarterBot drivetrain diagram for comparison
- Stage motors, bearings, and wheels at the frame
- Assign: left/right rail pairs, measurement lead, documentation writer

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Review S002 frame; confirm today's layout sketch; safety; roles |
| 75 | Construction | Confirm wheel locations; install motors inside rails; bearings, shafts, mecanum wheels, outside supports; verify roller orientation |
| 25 | Integration | Push-test for binding; measure front-wheel clearance; **update Onshape layout** with as-built wheel/motor positions; write design rationale vs standard StarterBot |
| 10 | Closeout | Evidence photos; explain-back; cleanup; S004 prep list |

## Mentor demonstration

Two minutes: show correct mecanum roller direction on one wheel. Students verify all four before push-test.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Motor mount, bearings, shafts, wheels, supports |
| Electrical | Route motor leads loosely — no final dress (S004) |
| Programming | No code — record motor names and ports planned on paper |
| Drive team | Push-test each corner; note binding feel |
| Documentation | Clearance measurements; decision record; photos; Onshape layout revision |

## Integrated build or test activity

Push-test across the shop floor (unpowered) after mechanical complete. Measure clearance at the front wheel/intake zone before leaving.

## Failure-injection scenario

Mentor rotates one mecanum wheel to wrong roller direction. Push-test pair must detect crab-walk bias and correct before closeout.

## Evidence to collect

- Photos of installed drivetrain (motor inside rails visible)
- Mecanum roller orientation checklist (four wheels)
- Front-wheel clearance measurements for intake/servo mount
- Onshape layout revision (wheel/motor/clearance zones)
- Push-test notes (binding yes/no, which corner)

## Student explain-back questions

1. Why are motors inside the rails instead of the standard StarterBot placement?
2. How do you verify mecanum roller orientation without powering motors?
3. What clearance did you measure for the intake wheel zone?
4. What would happen if one wheel's rollers were reversed?

## Assessment or exit check

Drivetrain rolls with push-test; all four roller orientations verified; rationale written; measurements logged.

## Portfolio or engineering-notebook artifact

Decision record (topic C — comparing choices) for modified layout. Clearance sketch with dimensions (topic D — math choices). Construction photos (Design/Innovate candidates).

## Competition enablement impact

Mechanical only. No TeleOp, no Control Hub acceptance claimed.

## Rollback procedure

Remove the offending wheel or motor mount and revert to standard layout **only** if the modified layout fails safety or cannot be made to roll — document the revert in the notebook.

## Cleanup requirements

Robot on blocks or side; motor leads bundled loosely; tools stored; floor swept.

## Next-session preparation

- S004 (2026-08-27): mount Control Hub, battery, switch; wire drivetrain; individual motor tests if code ready
- Charge batteries
- Mentors: confirm whether minimal drive OpMode exists (blocked on [#2](https://github.com/The-Allsparks/FORGE/issues/2) for repo — shop laptop sample OK)

## Hardware-unavailable fallback

Install wheels and shafts on a partial frame or practice board. Write rationale and measurements against a paper diagram.

## Robot-unavailable simulation option

Scale drawing of chassis — students mark motor and wheel positions and defend layout in explain-back without metal.

## Links to authoritative project documentation

- [learning-paths/onshape-cad.md](../../../learning-paths/onshape-cad.md)
- [docs/safety-and-enablement.md](../../../docs/safety-and-enablement.md)
- [docs/award-and-portfolio-traceability.md](../../../docs/award-and-portfolio-traceability.md)
- [templates/decision-record.md](../../../templates/decision-record.md)
- [projects/pedro-pathing.md](../../../projects/pedro-pathing.md) — read for later; Pedro owns chassis motion
- [docs/team-robot-project.md](../../../docs/team-robot-project.md) — **BLOCKED** on [#2](https://github.com/The-Allsparks/FORGE/issues/2)

## Mentor notes

This is a **student mechanical design decision** — mentors coach, students choose and document. Do not install Pedro or claim autonomous readiness. Standard StarterBot comparison must be honest — link kit docs in the notebook, do not invent part numbers.
