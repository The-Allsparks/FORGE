# Shared integration conventions

Student-facing contracts for combining Allsparks libraries. Libraries remain authoritative for types and APIs. This table exists so TeamCode does not invent a second dialect.

If a library’s README disagrees, **the library wins**. File a FORGE issue to update this page.

Parent: [stack-acceptance.md](stack-acceptance.md) / [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4).

## Principles

- Prefer adapters in the robot application over compile-time edges between every library.
- Installing a library must not activate it.
- Unknown, stale, and missing are not `0`, `false`, or “no game piece.”
- TRACE records; it does not command.
- Pedro (or the chosen drive layer) owns chassis motion.
- HELM never commands motors.
- ECHO never commands hardware.

## Convention table

| Topic | Convention | Authority |
| ----- | ---------- | --------- |
| Composition root | FTC OpMode / robot application | [stack-acceptance.md](stack-acceptance.md) |
| Time | Monotonic clock for robot-loop age; do not mix wall clock into unit tests | TRACE clock; BEACON fake clock; ECHO FakeClock examples |
| Sample age | `now − observation` / last-valid timestamp; stale ≠ connected | BEACON command-freshness; ECHO stale → silence; MIMIC snapshot liveness |
| Validity | Missing / unsupported / unknown explicit; never silent `0.0` volts or ticks-as-inches | AMPER phases; MIMIC units |
| Confidence / health | Report degraded/unknown; do not invent healthy | BEACON health states; ViDAR confidence; HELM unavailable capability |
| Units | Named units in records (volts, mm, rad) | TRACE data model; MIMIC MechanismUnits; ViDAR robot-space |
| Frames | Explicit robot vs field; ViDAR observations are robot-space unless documented otherwise | [ViDAR COORDINATE_FRAMES](https://github.com/The-Allsparks/ViDAR/blob/main/docs/COORDINATE_FRAMES.md) |
| Snapshots | Immutable; do not mutate last snapshot in place | MIMIC Phase 0; HELM world snapshot docs |
| Telemetry namespaces | `Project/Name` style (`Battery/Voltage`, `Drive/Pose`) | TRACE schema; AMPER DS lines |
| TRACE events | Human-readable, no PII, no secrets | [TRACE SECURITY](https://github.com/The-Allsparks/TRACE/blob/main/SECURITY.md) |
| Fault codes | Library reason codes; `INSUFFICIENT_EVIDENCE` rather than “jammed” | BEACON exercises |
| Config validation | Fail explicit on missing **required** hardware; optional devices degrade | AMPER init; BEACON preflight optional vs required |
| Feature flags | Default off; independent disable | Every project README |

## Dependency graph (required)

```text
TeamCode (OpMode)
  → TRACE (optional)
  → AMPER (optional)
  → MIMIC (optional)
  → ViDAR (optional)
  → BEACON (optional; consumes reports, does not own subsystems)
  → HELM (optional; must not compile-require execute adapters)
  → ECHO (optional; last, disabled)
  → Pedro Pathing (chassis)

FORGE ↛ robot classpath
Library A ↛ Library B compile dependency unless a published adapter exists
```

TRACE Phase 4 adapters are a **TRACE approval gate**, not a FORGE default.

## Telemetry collision check (when the robot project exists)

Before claiming a combined TeleOp:

1. List DS keys from TRACE, AMPER, ViDAR, BEACON.
2. No two libraries write the same key with different meaning.
3. Prefix with project name if collision appears.

Until that list is captured on a Hub, this check is **not done**.
