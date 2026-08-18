# AMPER

**Adaptive Motor Power and Energy Regulation**

AMPER gives the robot situational awareness of its electrical system. Begin passively. Teach voltage, current, battery sag, and power limits by graphing what the robot already does.

Authoritative repository: [The-Allsparks/AMPER](https://github.com/The-Allsparks/AMPER)

## What students learn here

What the Control Hub can actually measure; what causes voltage to fall; why AMPER cannot repair bad batteries, loose XT30, or mechanical binds.

## FORGE season use

| Period | Intent | Competition status target |
| ------ | ------ | ------------------------- |
| Preseason | Passive observe if wired; otherwise desktop + paper | passive or disabled |
| Clinic | Record sag under realistic load | passive |
| League | Power-envelope graphs; still no unvalidated limiting | passive |
| Later | Phase 2+ only after hardware test card evidence | practice-only until approved |

## Prerequisites

Team FTC project install ([install.md](https://github.com/The-Allsparks/AMPER/blob/main/docs/install.md)). Wheels-off for first current sampling.

## Hardware / simulation

- Hardware test card is mandatory before claiming loop-time cost ([hardware test card](https://github.com/The-Allsparks/AMPER/blob/main/docs/validation/hardware-test-card.md))
- Do **not** intentionally induce an uncontrolled brownout

## Evidence

CSV / match summary; min/max voltage; sag aligned with mechanism start events; loop time vs AMPER-off baseline.

## Safety

Phase 0/1 never call `setPower` / `setVelocity`. Placeholder voltage thresholds in AMPER docs are **not** universal FTC truth — do not copy them into FORGE as team limits.

## Deep links

- [README](https://github.com/The-Allsparks/AMPER/blob/main/README.md)
- [Phases](https://github.com/The-Allsparks/AMPER/blob/main/docs/power-management/phases.md)
- [Assessment](https://github.com/The-Allsparks/AMPER/blob/main/docs/power-management/assessment.md)
- [Quickstart](https://github.com/The-Allsparks/AMPER/blob/main/docs/quickstart.md)
- [Validation status](https://github.com/The-Allsparks/AMPER/blob/main/docs/validation/STATUS.md)
- [Examples](https://github.com/The-Allsparks/AMPER/blob/main/examples/README.md)

Audit: [docs/research-audit.md](../docs/research-audit.md)
