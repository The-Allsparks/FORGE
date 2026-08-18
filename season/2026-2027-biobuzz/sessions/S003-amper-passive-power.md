---
id: S003
title: "AMPER passive battery and power observations"
date: 2026-09-08
meeting_type: A
season_phase: preseason
event_checkpoint: none
status: complete
difficulty: Foundation
projects: [AMPER, TRACE]
active_features: []
---

# S003 — AMPER passive battery and power observations

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S003 |
| Title | AMPER passive battery and power observations |
| Calendar date | 2026-09-08 (planning input) |
| Relative week | Preseason week 2 |
| Meeting type | A |
| Season phase | preseason |
| Event checkpoint | none |
| Difficulty | Foundation |

## Driving question

When the robot feels "tired," is that a battery, a connector, a mechanical bind, or a guess?

## Student-facing objective

Students will continue drivetrain electrical construction, enable **passive** AMPER (or DS voltage if AMPER is not installed), and connect a voltage dip to a real action without changing motor output.

## Robot outcome

- Battery mount and power wiring improved
- Passive voltage observation path exists **or** a written gap with DS voltage screenshot
- No AMPER Phase 2+ flags

## Prerequisites

- S002 inspection baseline
- Mentor for powered tests
- AMPER install docs if integrating: [install.md](https://github.com/The-Allsparks/AMPER/blob/main/docs/install.md), [quickstart.md](https://github.com/The-Allsparks/AMPER/blob/main/docs/quickstart.md)

## Vocabulary

voltage · sag · current (optional) · passive · XT30 · loop time

## Safety concerns

- Do **not** induce an uncontrolled brownout ([AMPER hardware test card](https://github.com/The-Allsparks/AMPER/blob/main/docs/validation/hardware-test-card.md))
- Wheels off for first AMPER observe
- AMPER Phase 0/1 must not call `setPower` ([AMPER README](https://github.com/The-Allsparks/AMPER/blob/main/README.md))
- Loose power connectors are a hardware fix, not a software tune

## Required hardware

- Drivetrain; labeled battery if possible; Control Hub
- Multimeter optional (mentor)

## Required software

- AMPER `AmperPolicies.passiveDefaults()` **or** DS voltage only
- TRACE events at `Intake/start` substitutes: use `Drive/pulse` if no intake exists
- Team teleop unchanged except observe() call if using AMPER

## Preparation required before the meeting

- Read AMPER Phase 1 exercise (intake/drive/both — adapt to drive-only)
- Confirm composite/install compiles
- Stage cable-management parts

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Sag vs bind vs empty pack; safety: wheels off, no brownout games; assignment: electrical pair owns connectors, programming pair owns passive observe |
| 75 | Construction | Battery retention, Hub power wiring, strain relief, dress cables along S001 channels; continue drivetrain remaining structure |
| 25 | Integration | Add passive AMPER observe once per loop **or** log DS voltage by hand each run. TRACE event when drivers punch forward on blocks. Compare two batteries if labeled |
| 10 | Closeout | Circle the largest drop on CSV or notebook graph; explain-back; dashboard AMPER = ladder 3 if robot-passive else 1; cleanup |

## Mentor demonstration

Show the AMPER README snippet that motors stay team-owned. Point at `AmperPolicies.disabled()` as the off switch. Do not teach Phase 3 state machines today.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Battery mount, guards around connectors |
| Electrical | Seating, labeling packs, Hub power |
| Programming | Passive AMPER or DS voltage table; TRACE overlay |
| Drive team | Repeatable on-blocks "forward pulse" so graphs line up |
| Documentation | Graph sketch: voltage vs time with event marks |

## Integrated build or test activity

[AMPER Phase 1 exercise](https://github.com/The-Allsparks/AMPER/blob/main/docs/power-management/phases.md): run drive (and intake if it exists). Export CSV. Circle the largest voltage drop. Write one sentence: which command started just before the drop?

## Failure-injection scenario

Safe config: misspell a voltage sensor name **or** run with AMPER disabled vs enabled and compare motion. Motion must match. If current sampling is attempted, stop if loop time becomes unusable — record overhead; do not "optimize" by enabling limiting.

## Evidence to collect

- CSV or notebook voltage table
- Loop-time note vs AMPER-off (even qualitative)
- Sentence tying sag to a command
- Hardware test card steps 1–2 if time ([test card](https://github.com/The-Allsparks/AMPER/blob/main/docs/validation/hardware-test-card.md))

## Student explain-back questions

1. What can AMPER not repair?
2. Did AMPER change motor output today? How do you know?
3. Why are placeholder voltage thresholds in AMPER docs not our competition limits?
4. How do you disable AMPER?

## Assessment or exit check

Student points to a sag and a command. Mentor confirms no Phase 2+ enablement.

## Portfolio or engineering-notebook artifact

Voltage vs time sketch with events. Photo of battery mount.

## Competition enablement impact

AMPER **passive** if observe ran on robot; else **disabled**. Automatic limiting stays disabled. Not competition approved.

## Rollback procedure

`AmperPolicies.disabled()` or `measurementOnly()` / omit AMPER from OpMode. Teleop must drive identically.

## Cleanup requirements

Batteries stored at safe charge practice; connectors capped; CSV copied off Hub if any (no PII).

## Next-session preparation

- Bring any simple mechanism (intake roller, servo claw, or even a dummy arm) for S004 snapshots
- If no mechanism, use MIMIC fake hardware on laptops

## Hardware-unavailable fallback

Paper circuit of battery → Hub → motors. Use published DS voltage from a previous run or a mentor demo video. Still complete cable-routing on a mock chassis.

## Robot-unavailable simulation option

Read AMPER Phase 0–1 docs and complete a table of "observes / controls / cannot solve" from [phases.md](https://github.com/The-Allsparks/AMPER/blob/main/docs/power-management/phases.md). Run AMPER unit tests on desktop if Gradle works.

## Links to authoritative project documentation

- [AMPER README](https://github.com/The-Allsparks/AMPER/blob/main/README.md)
- [AMPER phases](https://github.com/The-Allsparks/AMPER/blob/main/docs/power-management/phases.md)
- [AMPER assessment](https://github.com/The-Allsparks/AMPER/blob/main/docs/power-management/assessment.md)
- [Hardware test card](https://github.com/The-Allsparks/AMPER/blob/main/docs/validation/hardware-test-card.md)
- [Validation STATUS](https://github.com/The-Allsparks/AMPER/blob/main/docs/validation/STATUS.md)
- [Examples](https://github.com/The-Allsparks/AMPER/blob/main/examples/README.md)
- [projects/amper.md](../../../projects/amper.md)

## Mentor notes

Allsparks had **no on-robot AMPER dataset** at audit. Do not quote FRC brownout firmware as FTC behavior. If install fails, teach the idea with DS voltage — do not burn the construction block on Gradle.
