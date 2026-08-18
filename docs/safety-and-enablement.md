# Safety and enablement

FORGE does not certify any library as match-safe. Each project states its own maturity. This document is the **season rule** for turning features on.

## Priority

working robot → reliable mechanisms → driver practice → conventional autonomous → evidence collection → advanced autonomy

If an advanced feature threatens an earlier item, it stays disabled.

## Enablement ladder

Track each capability independently on the [readiness dashboard](../season/2026-2027-biobuzz/readiness-dashboard.md).

| Level | Name | Typical evidence |
| ----- | ---- | ---------------- |
| 1 | Desktop test | Unit tests or training UI; no robot |
| 2 | Simulation or fake hardware | Browser sim, fake clocks, fake actuators |
| 3 | Passive robot observation | Recorders on; motors unchanged by the library |
| 4 | Controlled hardware test | Wheels off / restrained; adult supervision |
| 5 | Practice-field test | Repeatable on the practice field |
| 6 | Full mock match | Timed match with pit and disable path |
| 7 | Scrimmage or lower-risk event | Clinic or league meet with rollback ready |
| 8 | Competition approval | Written mentor + driver decision |

## Competition status

| Status | Meaning |
| ------ | ------- |
| disabled | Not on the competition robot |
| passive | Observes and logs; does not change outputs |
| practice-only | Allowed at practice; off for matches |
| approved | May run in matches under the documented bounds |
| frozen | No further changes except critical demonstrated problems |

## Competition approval requires all of

- Correct behavior
- Safe failure behavior
- No unacceptable drive-loop impact
- Clear rollback procedure
- Student understanding (explain-back)
- Demonstrated benefit
- Repeatability

Opening a GitHub repository, merging a pull request, completing a FORGE session, or passing **desktop** CI is **not** approval. Combined Control Hub evidence lives under [stack-acceptance.md](stack-acceptance.md) / [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4).

## Project defaults for this season

Until the dashboard says otherwise:

| Capability | Starting status | Do not |
| ---------- | --------------- | ------ |
| TRACE | passive recorder (target: always-on observation) | Command motors or enable replay |
| AMPER | passive | Enable automatic power limiting in matches |
| MIMIC | observation / snapshots | Enable homing, limits, or interlocks without a failure test |
| ViDAR | simulation or one-camera observation | Let vision command the drivetrain |
| BEACON | passive | Let monitoring restart devices or fight the FTC stop |
| ECHO | disabled on robot; desktop/sim OK | Competition audio without driver-benefit evidence |
| HELM | observe / vocabulary only | Give HELM chassis or match authority |
| Pedro conventional auto | developing toward approved | Replace it with HELM execution |

Authoritative safety texts (do not paraphrase as if they were weaker than the source):

- [TRACE mentor guide / never command hardware](https://github.com/The-Allsparks/TRACE/blob/main/docs/mentor-guide.md)
- [AMPER phases](https://github.com/The-Allsparks/AMPER/blob/main/docs/power-management/phases.md)
- [MIMIC safety model](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/safety-model.md)
- [BEACON driver-link limits](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/driver-link.md)
- [HELM safety](https://github.com/The-Allsparks/HELM/blob/main/docs/safety.md)
- [HELM readiness gates](https://github.com/The-Allsparks/HELM/blob/main/docs/readiness-gates.md)
- [ECHO competition readiness](https://github.com/The-Allsparks/ECHO/blob/main/docs/competition-readiness.md)
- [ECHO hearing safety](https://github.com/The-Allsparks/ECHO/blob/main/docs/hearing-safety.md)

## Rollback

Every session that touches an optional active feature must name:

1. The flag, config, or OpMode change that disables it
2. Who can do that in a pit
3. The conventional behavior that remains

If students cannot perform the rollback, the feature is not practice-ready.

Student-facing disable table: [student-install.md](student-install.md). Pit copy: [pit-and-inspection.md](../season/2026-2027-biobuzz/pit-and-inspection.md).

## Failure injection

Deliberate faults are teaching tools. Rules:

- Mentor present for hardware faults
- Prefer fake clocks, unplugged named sensors in a **safe config**, covered cameras, and stale log playback
- Do not intentionally induce an uncontrolled brownout ([AMPER hardware test card](https://github.com/The-Allsparks/AMPER/blob/main/docs/validation/hardware-test-card.md))
- Do not jam gravity loads to "see if MIMIC catches it"
- Stop on ringing ears, lost referee audio, or unexpected motion

## Adult supervision

Required for: first power-up, drivetrain on blocks, mechanism bring-up, any Phase 2+ AMPER/MIMIC flag, field tests, and event days.
