---
id: P006
title: "Code walkthrough — no bring-up or first movement"
date: 2026-09-04
meeting_type: B
season_phase: preseason
event_checkpoint: none
status: complete
difficulty: Foundation
projects: []
active_features: []
---

# P006 — Completed — Code walkthrough (no bring-up or first movement)

## Planned versus actual

| | |
| --- | --- |
| **Original plan** | Driver baseline and chassis reliability (full performance baseline) |
| **Rescoped plan (2 Sep)** | Electrical diagram, programming bring-up, and **first controlled movement** if no blocking hardware fault was found |
| **Confirmed actual** | The team **read through some existing code** and did **not** complete useful programming |
| **Classification** | **Completed code-walkthrough record.** Electrical diagram, wiring, hardware configuration, hardware map, TeleOp, motor tests, Driver Station enable/disable, and first movement did **not** occur |
| **Preserved original material** | Electrical + programming bring-up + first movement → [P007](P007-meeting-a.md) (last shop night before Kickoff). Drivetrain dial-in → P007 leftover **only if** first movement succeeds; otherwise [S002](S002-meeting-b.md). Kickoff worksheets still occupy P007’s integration/closeout — [P008](P008-meeting-b.md) is the FRC tour |

Do not claim an as-built power-path diagram, hub port table, deployed TeleOp, restrained motor test, or floor movement from this date.

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | P006 |
| Title | Code walkthrough — no bring-up or first movement |
| Calendar date | 2026-09-04 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | Preseason week 1 (completed — variance) |
| Meeting type | B |
| Season phase | preseason |
| Event checkpoint | none |
| Difficulty | Foundation |

## Driving question

Did we look at robot code together, and can we be honest that BumbleBee was not wired, configured, deployed, or moved tonight?

## Student-facing objective

Students read through some existing FTC / robot code. They did **not** create a Robot Controller hardware configuration, write a hardware map, implement or deploy a TeleOp, command motors, or produce first driver-controlled movement.

**Student learning outcomes (what actually happened):**

- Saw existing code as a group
- Did **not** finish a programming product that the robot can run

**Not achieved (rescoped plan):**

- Draw and explain the as-built electrical / power diagram
- Record Control Hub and Expansion Hub port assignments
- Install or verify wiring, labels, strain relief, polarity, and a legal power path
- Confirm a pinned FTC SDK project builds and deploys
- Test one motor at a time with wheels off the floor
- Disable and stop from the Driver Station
- Slow floor movement

## Robot outcome

- **None on hardware.** No electrical diagram, port table, wiring verification, hardware configuration, TeleOp, motor-test table, disable demonstration, or first movement
- Code was read; no useful programming product was left on the robot or in a deployable project as a recorded outcome
- Electrical foundation (originally P004, then this meeting) remains **incomplete**
- First movement and restrained bring-up remain **incomplete**

## Prerequisites

- P002–P004 Strafer / first-robot construction (as-built configuration is **not** fully documented in FORGE)
- P005 v0 rules review does **not** gate hardware
- Coach-prepared FTC SDK project on a laptop (published TeamCode URL remains **BLOCKED** on [#2](https://github.com/The-Allsparks/FORGE/issues/2))
- [preseason-deferred-work.md](../docs/preseason-deferred-work.md)

These prerequisites were for the rescoped bring-up plan. The actual session did not consume them as enablement evidence.

## Vocabulary

code walkthrough · TeleOp (planned, not executed) · hardware map (planned, not executed) · power path (planned, not executed)

## Safety concerns

- **No documented battery connection or motor enable this session**
- Do not retroactively treat this meeting as first enable
- If a robot was in the room, battery remains disconnected at cleanup
- Hair, hoodies, lanyards, and fingers stay away from wheels whenever the robot is later energized — that rule still starts at P007, not tonight

## Required hardware

- Not required for the actual code-reading session
- Robot, hubs, battery, and gamepads remain **P007 prep**, not this meeting’s product

## Required software

- Existing code that the team read through (source not recorded in FORGE)
- FTC SDK project, hardware configuration, and TeleOp remain **P007 work**
- Onshape **not required**
- TRACE library **not required**

## Preparation required before the meeting

- Historical (rescoped plan): print [p006-power-path-example.html](../docs/p006-power-path-example.html), blank port tables, charged batteries, a building FTC project
- Actual: those products were **not** produced tonight. Mentors still need a building FTC project **before P007**

## Exact 120-minute agenda

Reconstructed **actual** Meeting B pattern. The electrical-diagram and first-movement agenda **did not run.**

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Goal as planned was first movement; the meeting did not reach that work |
| 35 | Work block 1 | Read through existing robot / FTC code. No hardware configuration, TeleOp, or deploy |
| 55 | Work block 2 | Continued code reading in the slot that would have been driving; nobody enabled the robot |
| 20 | Closeout | Cleanup. Remaining electrical, programming, and first-movement work is still ahead at P007 |

Times are approximate. FORGE does not have a minute-by-minute attendance log.

## Mentor demonstration

The planned three-minute power-path trace and restrained disable demo **did not run.** Do not invent them.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | None documented |
| Electrical | None documented — diagram and wiring did not run |
| Programming | Read existing code; no deployable TeleOp or hardware map recorded |
| Drive team | No enable, disable, or floor commands recorded |
| Documentation | This session record; no port table or motor-test sheet |

## Integrated build or test activity

**Did not occur.** One motor at a time on blocks, disable/stop, and slow floor movement remain the integrated test for [P007](P007-meeting-a.md). Reading code with no robot test is not first movement.

## Failure-injection scenario

Not run. Keep for P007: if a student cannot point to the emergency disconnect **and** the Driver Station stop, do not go to the floor.

## Evidence to collect

- Honest session record: code was read; programming product was not
- Explicit **non-evidence:** as-built electrical diagram, hub port table, wiring photos, hardware configuration, hardware map, motor-by-motor test table, disable/stop demonstration, first-movement note

## Student explain-back questions

1. Did we deploy code to the robot tonight? (Honest answer: **no**.)
2. Did BumbleBee move under driver control tonight? (Honest answer: **no**.)
3. What still has to happen before anyone enables a motor? (Wiring/power path, configuration, restrained test, disable path.)
4. Why is reading code not the same as a hardware map or TeleOp?
5. What is **not** finished (electrical diagram, first movement, field-centric, odometry, auto, tuning)?

## Assessment or exit check

**Met:** team read through some code; the record does not pretend bring-up happened.  
**Not met (rescoped plan):** electrical diagram matches the robot; hub ports recorded; DS connect/enable/disable; each drivetrain motor commanded; first controlled movement or a named hardware blocker.

Path B (partial) would have been success with written blockers. A code walkthrough without those blockers is **not** first movement.

## Portfolio or engineering-notebook artifact

Process note: we looked at code and did not yet command the robot (Control / Design process). Not a power-path sketch.

## Competition enablement impact

None. No hardware enablement. Combined-stack acceptance **not** claimed ([FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4)). No optional library enabled.

## Rollback procedure

Not applicable to hardware. Do not keep a half-edited TeleOp that was never deployed as if it were the robot’s drive code.

## Cleanup requirements

Battery disconnected and stored if a battery was present; robot stable; Hub off; gamepads stored; aisles clear; tools returned.

## Next-session preparation

- **Current next shop meeting:** [P007](P007-meeting-a.md) (2026-09-07) — **finish P006:** electrical diagram and wiring as needed for safe enable, hardware configuration, minimal TeleOp, restrained motor tests, first movement if no blocking fault. Then Kickoff worksheets. Dial-in only if movement already works.
- [P008](P008-meeting-b.md) (2026-09-11) is an **FRC tour**, not more shop time
- Mentors: FTC project must **build and deploy** on a laptop before students arrive Monday — do not spend P007 installing Android Studio
- Charge batteries; stage Hub/battery/switch, labels, blocks, and [p006-power-path-example.html](../docs/p006-power-path-example.html)
- Print blank tables: power-path components; hub ports; motor-test results; Kickoff worksheets
- Do **not** assign Onshape or GitHub homework as a gate

## Hardware-unavailable fallback

If Hub or battery is missing at P007: finish the paper diagram and port plan; walk through DS screens with no robot; write the blocker. Do not claim movement.

## Robot-unavailable simulation option

Paper chassis: students mark battery, switch, Hub, and motor ports and defend the layout. Practice pointing to disable on a DS screenshot. Fill the as-built table as “not inspected on metal.”

## Links to authoritative project documentation

- [preseason-deferred-work.md](../docs/preseason-deferred-work.md)
- [P002](P002-meeting-s.md)–[P004](P004-meeting-s.md) construction records
- [P007 finish bring-up and Kickoff preparation](P007-meeting-a.md)
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

Meeting B **filename stays** `P006-meeting-b.md`. Honest record: code was read; useful programming was not done; the robot did not move. [P007](P007-meeting-a.md) is the last shop meeting before Kickoff. Do not open Monday with drivetrain “dial-in” as if tonight produced first movement. Protect P007’s Kickoff-prep block — the Friday tour cannot recover it. Keep CAD, GitHub workflow, and mechanism brainstorming off P007 construction time.
