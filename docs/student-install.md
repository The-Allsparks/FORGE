# Student install, diagnose, disable, rollback

This page is the student-facing companion to [stack-acceptance.md](stack-acceptance.md). It is **not** a substitute for each library’s install document. The robot application is the composition root ([team-robot-project.md](team-robot-project.md)). FORGE is not a Gradle dependency.

Parent epic: [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4). Robot project: [The-Allsparks/FtcRobotController](https://github.com/The-Allsparks/FtcRobotController) ([team-robot-project.md](team-robot-project.md)). Combined Hub evidence is still unmeasured.

## Before you add a library

1. The chassis still drives in team teleop.
2. Conventional autonomous still exists (Pedro or the S011 fallback).
3. You can name the disable path for the library you are about to add.
4. You are following **that library’s** install file, not a remembered Gradle snippet.

## Install order (when the robot project exists)

Add one library at a time. After each add: sync Gradle, compile, deploy if a Hub is available, run teleop with the new library **off**.

Recommended order for first contact (optional systems stay disabled):

1. Team FTC SDK project + Pedro (or chosen drive layer)
2. SHIFT (`shift-core` + `shift-ftc`; input layer for BumbleBee teleop — not chassis motion)
3. TRACE (recorder only; Java 11 — do not add until an FTC/Java 8 path exists)
4. AMPER (`amper-core` + `amper-ftc`; [install.md](https://github.com/The-Allsparks/AMPER/blob/main/docs/install.md))
5. MIMIC (Phase 0 observation)
6. BEACON (reports only)
7. ViDAR (teaching OpModes; no motors)
8. HELM (`OFF` / validate / observe only)
9. ECHO last, and only if a supported Driver Hub path exists — otherwise omit

Use the FTC SDK Gradle wrapper. Do not upgrade Gradle because a library asked you to. Prefer composite `includeBuild` while versions are SNAPSHOT or rc. Pins: [stack-acceptance.md](stack-acceptance.md).

## Lifecycle you must be able to point at

In the OpMode (not in FORGE):

| Method | You do |
| ------ | ------ |
| `init` | Build adapters. Fail explicit on missing **required** hardware. Optional libraries degrade. |
| `init_loop` | Driver-visible status. No motion. |
| `start` | Match clock / session start if used. |
| `loop` | Team code commands motors. One observe pass for recorders. |
| `stop` | Zero outputs as team policy. Flush logs. No leaked threads. |

If `init` fails, the OpMode must still be abortable from the Driver Station.

## Diagnose (paper checklist)

Work top-down. Do not start by rewriting architecture.

| Symptom | First checks |
| ------- | ------------ |
| Gradle sync fails | Wrapper version; `includeBuild` path; you did not add FORGE as a dependency |
| Compile error in TeamCode | Library version pin; you imported the FTC adapter module (`amper-ftc`, not desktop-only stubs) |
| OpMode does not appear | `@TeleOp` / `@Autonomous` on the class the SDK will load |
| Robot does not drive after an add | Disable the new library; confirm conventional teleop still exists |
| Loop feels slow | Measure with extras **off**, then add one observer; desktop tests are not Hub budgets |
| Camera / USB disappears | Unplug optional cameras; ViDAR is not required for teleop |
| Logs fill the Hub | TRACE quotas / `TraceMode.OFF` |
| Audio / cues | ECHO mute and `driverEnabled=false`; mute must not stop the robot |

Shared names, units, and telemetry keys: [conventions.md](conventions.md).

## Disable independently

Installing a library must not turn it on.

| System | Disable |
| ------ | ------- |
| SHIFT | omit from the OpMode; run Motor Test / conventional-stick teleop |
| TRACE | `TraceMode.OFF` / do not configure |
| AMPER | `AmperPolicies.disabled()` |
| MIMIC | no actuation flags; omit from loop |
| ViDAR | do not consume detections; unplug camera if the loop dies |
| BEACON | omit reports; never Phase 5 |
| HELM | mode `OFF`; not in the match OpMode |
| ECHO | audio off; `driverEnabled=false` |

Printed pit copy: [pit-and-inspection.md](../season/2026-2027-biobuzz/pit-and-inspection.md).

## Rollback (under one minute)

Same sequence as the pit card:

1. Driver Station stop.
2. Select team teleop. Do not run experimental autos.
3. Disable the optional that misbehaved (table above).
4. Battery disconnect if the robot will not disable.
5. Who: any mentor or the designated drive-coach.

Conventional teleop and conventional autonomous must still run.

## What you must not claim

- “It compiled on my laptop, so it is FTC-ready.”
- “CI passed, so the stack is match-approved.”
- “FORGE says we can enable this.” FORGE never flips a library default to on.

Competition approval stays on the [readiness dashboard](../season/2026-2027-biobuzz/readiness-dashboard.md) and [safety-and-enablement.md](safety-and-enablement.md).
