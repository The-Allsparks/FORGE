# Combined stack acceptance

**This is the first combined-stack acceptance priority for FORGE.** Parent epic: [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4).

A library that compiles on a desktop is not an FTC-ready stack. Combined readiness exists only when students can install supported libraries in a normal FTC SDK robot project, follow the OpMode lifecycle, disable each optional system independently, keep conventional teleop and autonomous working, and record Control Hub evidence. Opening this document is not that evidence.

FORGE still does **not** contain robot code and must not become a Gradle dependency of the robot project. The composition root is the team's OpMode / robot application ([team-robot-project.md](team-robot-project.md), [issue #2](https://github.com/The-Allsparks/FORGE/issues/2)).

## Status (18 August 2026)

**Blocked by [FORGE#2](https://github.com/The-Allsparks/FORGE/issues/2):** no published robot / TeamCode repository. Paper teaching in this file is not Hub evidence. Playbook when the team is ready: [create-robot-project.md](create-robot-project.md).

| Gate | Status |
| ---- | ------ |
| Canonical robot / TeamCode repository | **BLOCKED** on #2. No published Allsparks robot repo. Do not invent a URL. |
| Pinned install matrix (this file) | **Paper done.** Re-verify at Kickoff if the season SDK changes |
| Lifecycle ordering | **Paper done** below; not Hub-timed |
| Composition root = OpMode | **Paper done** |
| Student install / disable / rollback | **Paper done** ([student-install.md](student-install.md)) |
| Shared conventions | **Paper done** ([conventions.md](conventions.md)); Hub collision-check still blocked |
| Sibling P0 epics linked | **Done** (table below) |
| Combined-stack teaching in sessions | **Paper done** (S001, I002, later sessions refuse Hub claims) |
| Compile-checked combined TeleOp / auto | **BLOCKED** on #2 |
| Conventional fallbacks demonstrated on a Hub | **BLOCKED** on #2 |
| Combined Control Hub budgets | **BLOCKED** on #2 |
| Combined “FTC-ready” claim | **Forbidden** until #4 Hub acceptance is checked |

## Sibling P0 epics

| Repository | Epic |
| ---------- | ---- |
| FORGE | https://github.com/The-Allsparks/FORGE/issues/4 |
| AMPER | https://github.com/The-Allsparks/AMPER/issues/41 |
| MIMIC | https://github.com/The-Allsparks/MIMIC/issues/34 |
| TRACE | https://github.com/The-Allsparks/TRACE/issues/31 |
| BEACON | https://github.com/The-Allsparks/BEACON/issues/42 |
| HELM | https://github.com/The-Allsparks/HELM/issues/44 |
| ViDAR | https://github.com/The-Allsparks/ViDAR/issues/33 |
| ECHO | https://github.com/The-Allsparks/ECHO/issues/17 |

Do not treat a sibling green CI job as combined stack acceptance.

## Ownership (composition root)

```text
FTC OpMode / robot application   ← only composition root
        │
        ├── Pedro Pathing     chassis motion
        ├── TRACE             record (never command)
        ├── AMPER             observe power (passive until gated)
        ├── MIMIC             mechanism snapshots (no actuation until gated)
        ├── ViDAR             observations (no motors in teaching OpModes)
        ├── BEACON            health reports (no watchdog replacement)
        ├── HELM              OFF / observe / validate only
        └── ECHO              optional; disabled; never commands hardware
```

No library may become the robot composition root. Adapters belong in TeamCode.

## Install matrix (planning pins)

Re-verify at Kickoff if FIRST publishes a new season SDK. AMPER’s install doc was verified against **FTC SDK 11.2.0** (DECODE) on 2026-08-17. BIOBUZZ may require a newer SDK; do not freeze 11.2.0 as a game-year claim.

| Library | Version at 17–18 Aug 2026 audit | Install authority | Default on the robot |
| ------- | -------------------------------- | ----------------- | -------------------- |
| AMPER | `0.1.0-rc.1` (`amper-core` + `amper-ftc`) | [AMPER install](https://github.com/The-Allsparks/AMPER/blob/main/docs/install.md) | off / passive |
| TRACE | `0.1.0-SNAPSHOT` | [TRACE README](https://github.com/The-Allsparks/TRACE/blob/main/README.md) | off until configured; observational |
| MIMIC | `0.1.0-SNAPSHOT` | [MIMIC README](https://github.com/The-Allsparks/MIMIC/blob/main/README.md) | Phase 0 observation |
| BEACON | `0.1.0-SNAPSHOT` | [BEACON README](https://github.com/The-Allsparks/BEACON/blob/main/README.md) | flags default off |
| HELM | `0.1.0-SNAPSHOT` | [HELM README](https://github.com/The-Allsparks/HELM/blob/main/README.md) | `OFF` |
| ViDAR | `0.2.0` | [ViDAR TEACHING](https://github.com/The-Allsparks/ViDAR/blob/main/docs/TEACHING.md) | observe-only OpModes |
| ECHO | `0.1.0-SNAPSHOT` | [ECHO README](https://github.com/The-Allsparks/ECHO/blob/main/README.md) | disabled; not a required dependency |
| Pedro Pathing | current public docs | [pedropathing.com](https://pedropathing.com/docs/pathing) | conventional auto |

**Gradle:** use the FTC SDK wrapper. Do not upgrade Gradle because a library asked you to ([AMPER install](https://github.com/The-Allsparks/AMPER/blob/main/docs/install.md)). Prefer composite `includeBuild` while artifacts are SNAPSHOT/rc.

**ECHO** is optional. Do not add it to TeamCode until a supported Driver Hub path exists and [competition readiness](https://github.com/The-Allsparks/ECHO/blob/main/docs/competition-readiness.md) is re-read after Kickoff.

## Lifecycle ordering (student-facing)

TeamCode owns the calls. Libraries do not replace OpMode methods.

| Phase | Robot application | Optional libraries |
| ----- | ----------------- | ------------------ |
| `init` | HardwareMap, construct adapters, fail closed on missing **required** devices | Construct/configure. AMPER `initialize()` pattern. TRACE configure. Do not move mechanisms. HELM stays OFF. |
| `init_loop` | Driver-visible status; alliance/config | Publish health/preflight **advisory** only (BEACON). No motion. |
| `start` | Match clock | AMPER `start()` / TRACE session start if used. |
| `loop` | Read inputs, command motors **from team code**, one observe pass | TRACE cycle; AMPER `observe()` once; MIMIC snapshot; ViDAR `update()`; BEACON reports. HELM must not command. ECHO off. |
| `stop` | Zero outputs as team policy + official stop | AMPER `stop()` / TRACE flush. No leaked writer threads. |
| Init failure | OpMode must still be abortable | Missing optional library → degrade; missing required Hub/motor → fail explicit, do not invent 0.0 |
| Repeated transitions | INIT→START→STOP→INIT again | No leaked cameras, file sinks, or static singletons that fight the next OpMode |

Authoritative examples stay in the library repos (AMPER quickstart, ViDAR teaching OpModes, TRACE README). FORGE does not duplicate their Java.

## Conventional fallbacks (required)

These must run with **every** Allsparks optional independently disabled:

1. Team teleop (sticks drive the chassis).
2. Conventional autonomous (Pedro or a timed drive-forward fallback from S011).

Failure of TRACE, AMPER, ViDAR, BEACON, MIMIC observation, HELM, or ECHO must not prevent those two modes unless a **required** safety stop from FIRST/REV already would.

## Disable paths (pit)

| System | Disable |
| ------ | ------- |
| TRACE | `TraceMode.OFF` / do not configure |
| AMPER | `AmperPolicies.disabled()` |
| MIMIC | no actuation flags; omit from loop |
| ViDAR | do not consume detections; unplug camera if loop dies |
| BEACON | omit reports; never Phase 5 |
| HELM | mode `OFF`; not in match OpMode |
| ECHO | audio off; `driverEnabled=false` |

Printed copy lives in [pit-and-inspection.md](../season/2026-2027-biobuzz/pit-and-inspection.md).

## Combined Hub budgets

Not measured. Do not claim loop-time cost from desktop tests. When the robot project exists, record: loop ms with all optionals off vs TRACE+AMPER passive vs +one camera. AMPER’s [hardware test card](https://github.com/The-Allsparks/AMPER/blob/main/docs/validation/hardware-test-card.md) is the electrical slice only.

## What FORGE sessions may claim

Sessions may teach install, lifecycle, disable, and diagnosis. They must not say the stack is match-ready because CI passed or because this file exists.

Work still blocked as combined FTC readiness ([#4](https://github.com/The-Allsparks/FORGE/issues/4)): AMPER Phase 2+, MIMIC active control, BEACON recovery actuation, HELM execute, ECHO match audio, ViDAR commanding motion.
