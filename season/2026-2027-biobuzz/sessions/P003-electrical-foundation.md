---
id: P003
title: "Electrical foundation and power path"
date: 2026-08-27
meeting_type: B
season_phase: preseason
event_checkpoint: none
status: complete
difficulty: Foundation
projects: []
active_features: []
---

# P003 — Electrical foundation and power path

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | P003 |
| Title | Electrical foundation and power path |
| Calendar date | 2026-08-27 (planning input; Thursday Meeting B) |
| Meeting type | B |
| Season phase | preseason |
| Event checkpoint | none |
| Difficulty | Foundation |

## Driving question

Is the power path drawn, labeled, and serviceable so S001 can bring up one motor at a time on an elevated chassis?

## Student-facing objective

Students will lay out battery, main switch, and Control Hub positions; verify battery removal, USB access, and switch accessibility; mount components securely; route and label motor and power wiring with strain relief and service loops; protect wiring from wheels, sharp edges, and moving mechanisms; draw the robot's power path; and record defects for S001 — **without floor driving or full motor bring-up today**.

## Robot outcome

- Wired drivetrain ready for S001 controlled bring-up
- Power-path diagram with labeled connections
- Inspection and repair list for S001

## Prerequisites

- P002 rolling drivetrain installed
- Control Hub, battery, main switch, motor controllers or integrated ESC wiring available
- Mentor present for any energized work (limited to continuity or mentor-only pre-checks if needed)

## Vocabulary

strain relief · wire dress · service loop · power path · retention · inspection list

## Safety concerns

- **Mentor present** for any battery connection
- No floor driving today — motor bring-up is S001 on blocks
- Check wheel retention before any future spin
- DS disable path known before first enable in S001
- Protect wiring from wheels and pinch points

## Required hardware

- P002 drivetrain assembly
- Control Hub, battery, main switch, USB cables, motor wires
- Zip ties, tape, grommets or edge protection for strain relief
- Blocks, crate, or stand for future elevated test (S001)

## Required software

- Team notebook
- Optional: Onshape Hub/battery/switch mount plate concept ([onshape-cad.md](../../../learning-paths/onshape-cad.md))

## Preparation required before the meeting

- Charge batteries
- Print inspection checklist (fasteners, shafts, wheel screws, wire routing)
- Confirm DS and Hub pairing works (mentor pre-check only)
- Write S001 bring-up plan on board: **one motor at a time**, elevated

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Review P002 layout and clearance notes; safety; goals; software cap (~30 min/week until Kickoff) |
| 35 | Repair / tune / program | Mount Hub/battery/switch; verify removal and USB access; route and dress wiring; strain relief and service loops |
| 55 | Wire completion | Complete motor and power dress; label ports; **draw power path**; inspect retention; protect routes from wheels — **no floor driving** |
| 20 | Closeout | Record defects; inspection/repair list for S001; explain-back; cleanup |

## Mentor demonstration

Two minutes: show acceptable vs unacceptable wire routing near a spinning wheel. Students fix one route before leaving.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Hub/battery/switch mount; retention re-check |
| Electrical | Motor and power wiring, strain relief, labeling, power-path diagram |
| Programming | Document port map on paper; minimal TeleOp prep only if within software cap |
| Drive team | Call out pinch points during wire dress |
| Documentation | Mount location sketch; wire routing photos; power-path diagram; inspection list |

## Integrated build or test activity

Complete labeled wiring and power-path diagram. Motor spin tests **deferred to S001** unless mentor runs a single restrained check after dress is complete.

## Failure-injection scenario

Mentor asks where battery disconnect happens in an emergency. Student traces power path on diagram without guessing.

## Evidence to collect

- Wire routing photos (strain relief and labels visible)
- Power-path diagram (battery → switch → Hub → motors)
- Inspection and repair list for S001
- Optional: Onshape mount-plate concept

## Student explain-back questions

1. Where is the main switch and why?
2. What strain relief and service loops did you add?
3. Trace the power path from battery to one motor.
4. What must S001 verify before any floor driving?

## Assessment or exit check

Components mounted securely; wiring labeled and dressed; power path drawn; retention inspected; honest S001 prep list written.

## Portfolio or engineering-notebook artifact

Electrical layout and power-path sketch (Control award candidate — passive description only). Inspection list (engineering process).

## Competition enablement impact

Wiring only. No competition approval. Control Hub combined-stack acceptance **not** claimed ([FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4) blocked on [#2](https://github.com/The-Allsparks/FORGE/issues/2)).

## Rollback procedure

Disconnect battery. Fix wiring before S001 enable. Do not treat dressed wiring as proof motors work.

## Cleanup requirements

Battery disconnected and stored; robot on blocks; Hub powered off; cables un-trip-hazarded.

## Next-session preparation

- S001 (2026-09-01): bring-up, system map, TRACE evidence — **not** first assembly
- S002 (2026-09-03): driver baseline on restraint/carpet if S001 complete
- Label batteries A/B if possible
- Review [preseason-software-allocation.md](../docs/preseason-software-allocation.md)

## Hardware-unavailable fallback

Wire dress on a breadboard mock or second robot. Paper Hub mount sketch and power-path diagram.

## Robot-unavailable simulation option

Paper wiring diagram with color codes. Students explain motor port map and disable path without Hub.

## Links to authoritative project documentation

- [learning-paths/onshape-cad.md](../../../learning-paths/onshape-cad.md)
- [docs/safety-and-enablement.md](../../../docs/safety-and-enablement.md)
- [docs/stack-acceptance.md](../../../docs/stack-acceptance.md)
- [docs/student-install.md](../../../docs/student-install.md)
- [docs/team-robot-project.md](../../../docs/team-robot-project.md) — **BLOCKED** on [#2](https://github.com/The-Allsparks/FORGE/issues/2)
- [preseason-software-allocation.md](../docs/preseason-software-allocation.md)

## Mentor notes

P003 finishes wiring — S001 proves motors one at a time. Do not claim Control Hub acceptance. Protect wire dress from "quick enable" pressure. Preseason software stays at ~30 minutes per week until Kickoff.
