# ViDAR

**Robot-space situational awareness**

Teach geometry, cameras, detections, localization, uncertainty, and field validation. Do not consume early-season build time. Prefer simulation and one-camera exercises. Tie vision to an actual robot or game need.

Authoritative repository: [The-Allsparks/ViDAR](https://github.com/The-Allsparks/ViDAR)

## What students learn here

Vision is a sensor. The product is range, bearing, and tracks in robot space — not raw pixels.

## FORGE season use

| Period | Intent | Competition status target |
| ------ | ------ | ------------------------- |
| Preseason | Browser sim and/or one camera Discover OpMode | simulation / passive |
| Kickoff–clinic | Game-relevant detection only if BIOBUZZ needs it | practice-only |
| Clinic | Field lighting test | evidence for later |
| League | Deeper calibration | as evidenced |
| Never early | Multi-camera fusion as a season goal | disabled until one camera is boringly reliable |

Pedro Pathing remains optional as a consumer ([PEDRO_INTEGRATION.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/PEDRO_INTEGRATION.md)). ViDAR OpModes in the teaching path are **no motors**.

## Prerequisites

Browser sim: laptop. Robot: Control Hub + named UVC webcam. See [TEACHING.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/TEACHING.md).

## Hardware / simulation

[sim/README-SIM.md](https://github.com/The-Allsparks/ViDAR/blob/main/sim/README-SIM.md). Four-camera Control Hub operation **requires team validation**.

## Evidence

Camera Stream overlay, telemetry range/bearing, calibration checklist photos, TRACE events when adapters exist.

## Safety

Stale tracks must not be treated as current field truth. AprilTag scout observations must not silently rewrite pose (ViDAR README). Cover the lens as a failure injection — do not stare into lasers or unmounted spinning robots.

## Deep links

- [README](https://github.com/The-Allsparks/ViDAR/blob/main/README.md)
- [Teaching path](https://github.com/The-Allsparks/ViDAR/blob/main/docs/TEACHING.md)
- [Coordinate frames](https://github.com/The-Allsparks/ViDAR/blob/main/docs/COORDINATE_FRAMES.md)
- [Calibration](https://github.com/The-Allsparks/ViDAR/blob/main/docs/CALIBRATION.md)
- [Calibration checklist](https://github.com/The-Allsparks/ViDAR/blob/main/docs/CALIBRATION_CHECKLIST.md)
- [System design](https://github.com/The-Allsparks/ViDAR/blob/main/docs/SYSTEM_DESIGN.md)
- [API](https://github.com/The-Allsparks/ViDAR/blob/main/docs/API.md)

Audit: [docs/research-audit.md](../docs/research-audit.md)

## Combined stack

ViDAR is optional. Teaching OpModes are no-motors. Combined FTC readiness is [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4). Sibling P0: [ViDAR#33](https://github.com/The-Allsparks/ViDAR/issues/33). See [stack-acceptance.md](../docs/stack-acceptance.md) and [conventions.md](../docs/conventions.md) (frames).
