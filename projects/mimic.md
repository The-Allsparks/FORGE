# MIMIC

**Mechanism Integration, Motion, Interlocks, and Calibration**

Connect mechanism construction to explicit states and limits. Teach lifecycle, interlocks, safe transitions, and recovery. Require controlled failure tests before protections become active.

Authoritative repository: [The-Allsparks/MIMIC](https://github.com/The-Allsparks/MIMIC)

## What students learn here

Software must know units, direction, and freshness before it may move a mechanism. Encoder ticks are not a physical pose until calibration exists.

## FORGE season use

| Period | Intent | Competition status target |
| ------ | ------ | ------------------------- |
| Preseason | Snapshots on fake hardware or a simple mechanism | observation |
| Kickoff–clinic | Name states for whatever BIOBUZZ mechanisms exist | observation |
| Reliability | Only **tested** protections enabled | practice-only or disabled |
| League | Lifecycle exercises under load | as evidenced |

At audit, **Phase 0 only** is implemented. Elevator hardware was **not selected**. Do not schedule racking/anti-racking work until the physical design exists.

## Prerequisites

Fake hardware for classroom. Real sensors for robot observation. Adult supervision for any motion.

## Hardware / simulation

[Examples](https://github.com/The-Allsparks/MIMIC/blob/main/examples/README.md) and Phase 0 fake actuators. Software limits do not replace hard stops ([safety model](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/safety-model.md)).

## Evidence

Immutable snapshots; later disagreement graphs; written state diagram in the notebook. Phase 0 write counts on fake actuators stay 0.

## Safety

No production safety claims. Incorrect homing, units, direction, or gearing can damage hardware. Gravity loads need mechanical design, not hope.

## Deep links

- [README](https://github.com/The-Allsparks/MIMIC/blob/main/README.md)
- [Phases](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/phases.md)
- [Lifecycle](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/lifecycle.md)
- [Interlocks](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/interlocks.md)
- [Assessment](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/assessment.md)
- [Testing](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/testing.md)

Audit: [docs/research-audit.md](../docs/research-audit.md)

## Combined stack

MIMIC is optional. Phase 0 observation is the season default. Combined FTC readiness is [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4). Sibling P0: [MIMIC#34](https://github.com/The-Allsparks/MIMIC/issues/34). See [stack-acceptance.md](../docs/stack-acceptance.md).
