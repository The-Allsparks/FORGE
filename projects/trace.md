# TRACE

**Telemetry, Recording, Analysis, and Control Events**

TRACE is the season's evidence habit. Introduce it first. Use it in every session closeout. Never let logging replace wrenches or driving.

Authoritative repository: [The-Allsparks/TRACE](https://github.com/The-Allsparks/TRACE)

## What students learn here

The difference between a measurement, a decision, a command, and an event — and how to retell a match from an export.

Ladder (do not skip): Observe → Record → Explain → Correlate → Reconstruct → Replay → Test. Replay is **not** this season's early work.

## FORGE season use

| Period | Intent | Competition status target |
| ------ | ------ | ------------------------- |
| Preseason | Events + one signal (battery or pose) | Passive recorder |
| Through clinic | File sink with quotas once Control Hub evidence exists | Passive |
| League+ | Correlate with AMPER/MIMIC/ViDAR/BEACON using whatever exports exist | Passive |
| Never without TRACE gates | `TraceMode.REPLAY`, hardware commands | disabled |

## Prerequisites

Desktop tests can start with no robot. File recording needs Control Hub storage adapters owned by the team robot project.

## Hardware / simulation

- Simulation: desktop JVM tests and memory sink
- Robot: bounded file sink; treat Hub storage as finite

## Evidence it can produce

Ordered events, CSV, `.tlog`, drop counts. See [data model](https://github.com/The-Allsparks/TRACE/blob/main/docs/data-model.md).

## Safety

Phases 0–5 are observational. TRACE must not command motors. Keep PII and secrets out of logs.

## Enablement notes

A student should explain the current TRACE phase out loud before anyone enables the next mode on a robot ([student learning path](https://github.com/The-Allsparks/TRACE/blob/main/docs/student-learning-path.md)). Hardware validation was **not** performed at the FORGE audit.

## Deep links

- [README](https://github.com/The-Allsparks/TRACE/blob/main/README.md)
- [Student learning path](https://github.com/The-Allsparks/TRACE/blob/main/docs/student-learning-path.md)
- [Mentor guide](https://github.com/The-Allsparks/TRACE/blob/main/docs/mentor-guide.md)
- [Architecture](https://github.com/The-Allsparks/TRACE/blob/main/docs/architecture.md)
- [Integrations](https://github.com/The-Allsparks/TRACE/blob/main/docs/integrations.md)
- [Examples](https://github.com/The-Allsparks/TRACE/blob/main/examples/README.md)
- [SECURITY](https://github.com/The-Allsparks/TRACE/blob/main/SECURITY.md)

Audit: [docs/research-audit.md](../docs/research-audit.md)
