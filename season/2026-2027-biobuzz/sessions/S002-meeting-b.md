---
id: S002
title: Post-Kickoff week 1 — ideation scale-up and low-fi prototypes
date: 2026-09-18
meeting_type: B
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: scheduled
difficulty: Foundation
projects:
- TRACE
active_features: []
compressed_week: 1
forge_gate: G1
---

# S002 — Post-Kickoff week 1 — ideation scale-up and low-fi prototypes

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

Did we generate enough ideas, finish G1 with a documented strategy (including the not-yet list), and still give every student **more** driving time?

## Student-facing objective

Students scale visual ideation from S001, finish low-fidelity prototypes if ideas exist, complete G1 Strategy gate review using [kickoff-decision-package.md](../../../templates/kickoff-decision-package.md), and run the **55-minute** driver block. Every student has already driven (15 Sep) and will practice again **16 Sep**. Friday is more reps, not first enable. Electrical stays temporary. Do not steal driving time to fabricate.

## Robot outcome

- Ideation count recorded (target 60–100 across team)
- [Gate review G1](../../../templates/gate-review.md) completed
- Kickoff decision package complete enough to pass G1
- Risk register started
- Starter-bot fallback documented


## Prerequisites

- Driveable chassis: all students drove **15 Sep**; extra practice **16 Sep**. Electrical is still **temporary** until a real design. Do not assume a frozen wiring diagram.
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
| 10 | Opening | S001 game/brainstorm status; G1 checklist; clinic attendance clock (75% in 4 weeks before an event); Appendix F/G consent if still missing; safety; every driver will drive |
| 35 | Repair / tune / program | Finish decision-package rows; ideation count; fix S001 items; correct mecanum orientation — **no custom scoring fab** |
| 55 | Driving reps | Forward/reverse; strafe L/R; rotation; fixed-distance straight lines; **every student** enables, drives, disables; emergency-disable drill |
| 20 | Closeout | [Gate review G1](../../../templates/gate-review.md); inspect fasteners; baseline table; explain-back |

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
3. What is on the repair list before S004 comparative tests?
4. Is the chassis ready for mechanism experiments? (honest answer)
5. Who still needs Onshape parental consent before Monday?

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

- S003 (21 Sep): FRC-hosted Onshape training — chassis stays serviceable at home if the class is offsite
- Appendix F consent before student Onshape accounts
- S004: G2 comparative tests; 55-minute driving stays

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
- [P007 first movement](P007-meeting-a.md)
- [projects/pedro-pathing.md](../../../projects/pedro-pathing.md) — defer tuning

## Mentor notes

Success = **G1 package + every student drove again**. First enable already happened (15 Sep; extra 16 Sep). If G1 slips, do not skip driving to write a novel. Electrical stays temporary. S001 was game review and brainstorm, not fabrication. Pedro follower tuning waits until S010 / later Meeting B repair.
