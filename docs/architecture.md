# Architecture

FORGE is the season layer above seven Allsparks libraries and Pedro Pathing. It sequences learning and integration. It does not compile into the robot.

## Layer map

```text
Students and mentors
        │
        ▼
FORGE  — season sequence, meetings, evidence, enablement, rollback
        │  (links only; no robot dependency)
        ▼
┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
│  TRACE  │  AMPER  │  MIMIC  │  ViDAR  │ BEACON  │  ECHO   │  HELM   │
│ evidence│  power  │  mech   │  vision │  comms  │  audio  │ intent  │
└─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
        │
        ▼
Pedro Pathing owns chassis motion.
FTC SDK / Control Hub / Driver Station own official control and stop behavior.
```

## Ownership boundary

| FORGE may | FORGE must not |
| --------- | -------------- |
| Point to a project phase, example, or gate | Restate that project's API as if FORGE owned it |
| Require evidence before enablement | Treat repository completion as robot readiness |
| Schedule construction, driving, and labs | Replace driver practice with lectures |
| Record competition status on the dashboard | Flip a library default to "on" from this repo |

## Data that lives here

- `season/*/calendar.yaml` — structured dates and session index
- `season/*/sessions/` — meeting plans
- `season/*/readiness-dashboard.md` — human-editable enablement state
- `projects/` — student-facing maps with deep links
- `tools/curriculum-manifest.json` — machine-readable inventory for validation

## Data that must not live here

- Voltage thresholds, PID constants, HSV ranges, or homing currents (project + robot)
- Game scoring rules after Kickoff (link the official manual; keep local notes in the season folder as team decisions, not as invented rules)
- Student names in committed evidence samples
- Secrets, Wi-Fi credentials, or unredacted logs

## Design choices

1. **One robot, many layers.** Sessions always include construction or driving. Software is taught on the mechanism just built or the test just run.
2. **TRACE is the closeout habit**, not a separate course. See [TRACE student learning path](https://github.com/The-Allsparks/TRACE/blob/main/docs/student-learning-path.md).
3. **Passive before active.** AMPER, BEACON, MIMIC, ViDAR, ECHO, and HELM follow the [enablement ladder](safety-and-enablement.md).
4. **Conventional fallbacks.** A teleop and a Pedro autonomous must keep working with optional systems disabled.
5. **Editable calendar.** Event dates are planning inputs. Verify them if FIRST Nevada publishes a change.
6. **Stale-link tolerance.** Linked repositories will evolve. Validation checks link shape and, where practical, that GitHub paths still exist. Mentors should re-verify after Kickoff using [maintaining-the-schedule.md](maintaining-the-schedule.md).

## Related documents

- [Curriculum model](curriculum-model.md)
- [Safety and enablement](safety-and-enablement.md)
- [Evidence model](evidence-model.md)
- [Research audit](research-audit.md)
