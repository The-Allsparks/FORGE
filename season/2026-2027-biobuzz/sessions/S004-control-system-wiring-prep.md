---
id: S004
title: "Control system installation and powered-test preparation"
date: 2026-08-27
meeting_type: B
season_phase: preseason
event_checkpoint: none
status: complete
difficulty: Foundation
projects: []
active_features: []
---

# S004 — Control system installation and powered-test preparation

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S004 |
| Title | Control system installation and powered-test preparation |
| Calendar date | 2026-08-27 (planning input; Thursday Meeting B) |
| Meeting type | B |
| Season phase | preseason |
| Event checkpoint | none |
| Difficulty | Foundation |

## Driving question

Is the control system mounted safely, wired cleanly, and ready for restrained motor tests before S005 — or do we have an honest blocker list?

## Student-facing objective

Students will choose and document battery, Control Hub, and main-switch locations; mount components securely; route motor and power wiring with strain relief; protect wiring from wheels and moving parts; inspect fasteners, shafts, and wheel retention; run individual motor tests if minimal drive code is ready (elevated/restrained chassis); and record defects before S005.

## Robot outcome

- Wired drivetrain ready for controlled testing in S005/S006
- Individual motor test results **or** documented blocker (no fake Hub success)
- Inspection and repair list for S005

## Prerequisites

- S003 rolling drivetrain installed
- Control Hub, battery, main switch, motor controllers or integrated ESC wiring available
- Mentor present for any energized work
- Minimal per-motor test OpMode **if** available — not required if [#2](https://github.com/The-Allsparks/FORGE/issues/2) still blocks TeamCode

## Vocabulary

strain relief · wire dress · retention · blocker · individual motor test · inspection list

## Safety concerns

- **Mentor present** for any battery connection
- Elevate or restrain chassis before powered motor tests — blocks first
- No drive on floor until S006 baseline with mentor OK
- Check wheel retention before any spin
- DS disable path known before first enable

## Required hardware

- S003 drivetrain assembly
- Control Hub, battery, main switch, USB cables, motor wires
- Zip ties, tape, grommets or edge protection for strain relief
- Blocks, crate, or stand for elevated test

## Required software

- Driver Station (if testing)
- Minimal motor test or teleop OpMode if deployed — otherwise manual DS motor test channel
- Team notebook
- Onshape — Hub/battery/switch mount plate concept

## Preparation required before the meeting

- Charge batteries
- Print inspection checklist (fasteners, shafts, wheel screws, wire routing)
- Confirm DS and Hub pairing works (mentor pre-check)
- Write test plan on board: **one motor at a time** if powered

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Review S003 layout and clearance notes; safety: mentor OK for power; goals |
| 35 | Repair / tune / program | Mount Hub/battery/switch; route and dress wiring; **CAD pair models mount plate** (print vs order note); strain relief |
| 55 | Test prep | Inspect fasteners, shafts, wheel retention; if minimal drive code ready — elevate/restrain chassis and test **each motor individually**; otherwise complete dress and document blocker |
| 20 | Closeout | Record defects and unfinished work; inspection/repair list for S005; explain-back; cleanup |

## Mentor demonstration

Two minutes: show acceptable vs unacceptable wire routing near a spinning wheel. Students fix one route before any enable.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Hub/battery/switch mount; retention re-check |
| Electrical | Motor and power wiring, strain relief, labeling |
| Programming | Deploy minimal test OpMode if repo exists; otherwise document blocker for [#2](https://github.com/The-Allsparks/FORGE/issues/2) |
| Drive team | Call out pinch points during wire dress; assist restraint setup |
| Documentation | Mount location sketch; Onshape plate concept; motor test table or blocker note; inspection list |

## Integrated build or test activity

Individual motor spin tests (restrained) **or** completed wiring with honest blocker documentation. Both are valid exits if evidence matches reality.

## Failure-injection scenario

Mentor disconnects one motor wire before a test. Electrical pair must find open circuit before blaming code.

## Evidence to collect

- Onshape mount-plate concept (Hub/battery/switch)
- Wire routing photos (strain relief visible)
- Individual motor test results (direction, port, mentor initials) **or** blocker note: "No TeamCode repo / no test OpMode — wiring complete, tests deferred to S005"
- Inspection and repair list for S005

## Student explain-back questions

1. Where is the main switch and why?
2. What strain relief did you add and where?
3. Did each motor spin correctly? If not, what is the blocker?
4. What must S005 fix before full system map work?

## Assessment or exit check

Components mounted; wiring dressed; retention inspected; motor tests logged **or** blocker written without exaggeration.

## Portfolio or engineering-notebook artifact

Electrical layout sketch (Control award candidate — passive description only). Inspection list (engineering process). Motor test table or blocker record (honest evidence).

## Competition enablement impact

Wiring only. No competition approval. Control Hub combined-stack acceptance **not** claimed ([FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4) blocked on [#2](https://github.com/The-Allsparks/FORGE/issues/2)).

## Rollback procedure

DS stop. Disconnect battery. Fix wiring before re-enable. Do not deploy untested code to all motors at once.

## Cleanup requirements

Battery disconnected and stored; robot on blocks; Hub powered off; cables un-trip-hazarded.

## Next-session preparation

- S005 (2026-09-01): system map, safety, TRACE evidence, final drivetrain corrections — **not** first assembly
- S006 (2026-09-03): restrained driver baseline
- Label batteries A/B if possible
- Mentors: TRACE desktop test on one laptop for S005 integration block

## Hardware-unavailable fallback

Wire dress on a breadboard mock or second robot. Paper Hub mount sketch. No powered tests — blocker documented.

## Robot-unavailable simulation option

Paper wiring diagram with color codes. Students explain motor port map and disable path without Hub.

## Links to authoritative project documentation

- [learning-paths/onshape-cad.md](../../../learning-paths/onshape-cad.md)
- [docs/safety-and-enablement.md](../../../docs/safety-and-enablement.md)
- [docs/stack-acceptance.md](../../../docs/stack-acceptance.md)
- [docs/student-install.md](../../../docs/student-install.md)
- [docs/team-robot-project.md](../../../docs/team-robot-project.md) — **BLOCKED** on [#2](https://github.com/The-Allsparks/FORGE/issues/2)
- [projects/trace.md](../../../projects/trace.md) — passive prep for S005

## Mentor notes

Do not claim Control Hub acceptance or combined-stack success. Individual motor tests are success; honest blocker is also success. Protect wire dress from "quick enable" pressure. S004 finishes wiring — S005 adds TRACE and system vocabulary on top of an already-built drivetrain.
