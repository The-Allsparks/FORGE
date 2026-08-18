# BEACON

**Bus and External-link Awareness, Continuity, Observation, and Notification**

Begin as passive communications-health observation. Teach freshness, disconnection, degraded state, and recovery. Never allow monitoring to interfere with control-system operation.

Authoritative repository: [The-Allsparks/BEACON](https://github.com/The-Allsparks/BEACON)

## What students learn here

A loop that still runs is not proof the driver command is fresh. Stick values can be stale. Official FTC stop behavior is the authority for DS loss.

## FORGE season use

| Period | Intent | Competition status target |
| ------ | ------ | ------------------------- |
| Preseason | Vocabulary + exercises (fake clock) | disabled or passive |
| Clinic | Observe comms under venue Wi-Fi | passive |
| League | Failure-domain stories from match evidence | passive |
| Not this season unless gates change | Phase 5 drivetrain safe-stop | disabled |

**Verified gap:** there is no reliable supported public OpMode API for early Driver Station loss detection. Do not teach students to wrap private SDK internals.

## Prerequisites

Paper + unit-test exercises need no robot. Robot reporting needs team-owned `report(...)` later.

## Hardware / simulation

[Student exercises](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/exercises.md). [Passive health monitor example](https://github.com/The-Allsparks/BEACON/blob/main/examples/passive-health-monitor/README.md).

## Evidence

Freshness classification write-ups; preflight optional vs required findings; TRACE/BEACON exports when present.

## Safety

BEACON must not weaken, replace, or circumvent official watchdog/keepalive. Automatic encoder resets and Hub power cycles stay manual.

## Deep links

- [README](https://github.com/The-Allsparks/BEACON/blob/main/README.md)
- [Phases](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/phases.md)
- [Command freshness](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/command-freshness.md)
- [Driver-link](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/driver-link.md)
- [Recovery](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/recovery.md)
- [Preflight](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/preflight.md)
- [Assessment](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/assessment.md)

Audit: [docs/research-audit.md](../docs/research-audit.md)
