# Preseason software allocation

Until Kickoff (12 September 2026), extra software courses stay off. **P006 is the exception:** creating the FTC project, hardware configuration, hardware map, and a minimal robot-centric TeleOp is Kickoff-critical and may use most of that meeting’s programming block. That does **not** reopen a weekly library curriculum.

After P006, P007 software is **dial-in only** (directions, mix, speed limit, deadband). GitHub TeamCode workflow stays blocked on [#2](https://github.com/The-Allsparks/FORGE/issues/2).

Use software only for immediate robot needs:

- Minimal drivetrain TeleOp
- Robot configuration
- Motor-direction verification
- Driver input testing
- Basic telemetry
- TRACE events tied to **actual** physical tests
- Passive voltage observation where useful

## Project treatment before Kickoff

| Project | Preseason treatment |
| ------- | ------------------- |
| TRACE | Short evidence habit tied to real tests |
| AMPER | Passive voltage observations only |
| MIMIC | Paper states or simple limit-switch experiment |
| Pedro | Defer follower tuning until the drivetrain is reliable |
| ViDAR | Hardware placement discussion only |
| BEACON | Vocabulary or passive observation only |
| ECHO | Off-robot experiment if spare time exists |
| HELM | System-map vocabulary only; no authority |

No advanced library is competition-ready without robot evidence. See [stack-acceptance.md](../../../docs/stack-acceptance.md).
