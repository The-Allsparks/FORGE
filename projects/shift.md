# SHIFT

**Semantic Human Input Framework**

SHIFT maps operator sticks to named intents. TeamCode commands the robot. SHIFT is not a drivetrain library.

Authoritative repository: [The-Allsparks/SHIFT](https://github.com/The-Allsparks/SHIFT)

## What students learn here

Sticks become named intents. SHIFT does not `setPower`. If SHIFT is omitted, run Motor Test / conventional-stick teleop.

## FORGE season use

| Period | Intent | Competition status target |
| ------ | ------ | ------------------------- |
| Preseason | Drive teleop input layer | input layer; not a drivetrain library |
| Kickoff-clinic | Same named intents on the season robot | input layer |
| Always | Omit SHIFT and fall back to Motor Test | conventional sticks |

SHIFT is the preseason Drive teleop input layer. It is not a drivetrain library. Pedro (or team mixers) owns chassis motion.

## Prerequisites

Team FTC project install ([INSTALL.md](https://github.com/The-Allsparks/SHIFT/blob/main/docs/INSTALL.md)). Gamepad on the Driver Station.

## Hardware / simulation

Desktop JSON and unit tests can start with no robot. Drive teleop needs a Control Hub and gamepads.

## Evidence

Named intent names on the Driver Station or in TRACE. Motor Test still drives when SHIFT is omitted.

## Safety

SHIFT does not `setPower`. TeamCode is the only place that writes motors. Omit SHIFT and run Motor Test if the input layer misbehaves.

## Deep links

- [README](https://github.com/The-Allsparks/SHIFT/blob/main/README.md)
- [Install](https://github.com/The-Allsparks/SHIFT/blob/main/docs/INSTALL.md)
- [Teaching path](https://github.com/The-Allsparks/SHIFT/blob/main/docs/TEACHING.md)
- [Architecture](https://github.com/The-Allsparks/SHIFT/blob/main/docs/architecture.md)
- [Integrations](https://github.com/The-Allsparks/SHIFT/blob/main/docs/integrations.md)
- [Hub evidence 2026-09-08](https://github.com/The-Allsparks/SHIFT/blob/main/docs/audits/hub-evidence-2026-09-08.md)

Audit: [docs/research-audit.md](../docs/research-audit.md)

## Combined stack

SHIFT is the operator-intent layer. Combined FTC readiness is [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4). Sibling P0: [SHIFT#8](https://github.com/The-Allsparks/SHIFT/issues/8). See [stack-acceptance.md](../docs/stack-acceptance.md) and [conventions.md](../docs/conventions.md).
