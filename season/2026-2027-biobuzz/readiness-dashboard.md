# Readiness dashboard

Update during the last 10–20 minutes of a meeting. One row per capability. Do not add a second tracking system.

**How to edit:** change the markdown table cells. Owners may be roles or initials — not full student names in git if the team prefers privacy.

Ladder levels: 1 desktop · 2 sim/fake · 3 passive robot · 4 controlled hardware · 5 practice field · 6 mock match · 7 scrimmage · 8 competition approval

Competition status: `disabled` · `passive` · `practice-only` · `approved` · `frozen`

**Judging / portfolio readiness** (not a robot enablement flag): `none` · `skeleton` · `candidates mapped` · `draft ready` · `validated`

Opening this file does not approve anything.

**Combined stack (P0):** [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4). Until a published TeamCode repo exists and Hub evidence is recorded, the Combined stack row stays blocked. Desktop CI is not that evidence.

| Capability | Owner / pair | Ladder | Latest evidence | Known risks | Rollback method | Next required test | Competition status |
| ---------- | ------------ | ------ | --------------- | ----------- | --------------- | ------------------ | ------------------ |
| Combined stack | | 1 | paper only; **BLOCKED** on [#2](https://github.com/The-Allsparks/FORGE/issues/2) | no published robot repo; Hub budgets unmeasured | disable each optional independently ([student-install.md](../../docs/student-install.md)) | **blocked** — publish/link TeamCode, then compile-checked TeleOp/auto | disabled |
| Robot mechanical | | 1 | none | unfinished drivetrain | n/a | S001–S002 construction | disabled |
| Electrical | | 1 | none | unvalidated wiring | power disconnect | first power-up with mentor | disabled |
| Driver-control | | 1 | none | no baseline | DS stop | S002 blocks then carpet | disabled |
| Conventional autonomous | | 1 | none | no path yet | run teleop only | S007 simple Pedro path | disabled |
| TRACE | | 1 | none | not Hub-tested | `TraceMode.OFF` | S001 desktop events | passive (goal) |
| AMPER | | 1 | none | not Hub-tested | `AmperPolicies.disabled()` | S003 wheels-off voltage | disabled |
| MIMIC | | 1 | none | Phase 0 only; elevator unknown | flags default / no actuation | S004 fake snapshots | disabled |
| ViDAR | | 1 | none | 4-cam unvalidated | do not consume detections in drive | S005 sim or one camera | disabled |
| BEACON | | 1 | none | no DS early-stop API | omit reports; official stop remains | S006 exercises | disabled |
| HELM | | 1 | none | gates unmet | mode `OFF` | S014 paper trees | disabled |
| ECHO | | 1 | none | match audio not approved | `driverEnabled=false` / no audio flag | S010 desktop, mute path | disabled |
| Inspection | | 1 | none | rookie first inspect | n/a | S012 checklist | disabled |
| Pit workflow | | 1 | none | no timed drill | n/a | clinic + S012 | disabled |
| Judging | | 1 | none | no narrative | n/a | notebook after Kickoff; portfolio skeleton | disabled |
| Driver practice | | 1 | none | insufficient reps | n/a | every Meeting B | disabled |
| Student understanding | | 1 | none | mixed experience | n/a | session explain-backs | disabled |

## Status log (newest first)

| Date | Session | What changed |
| ---- | ------- | ------------ |
| 2026-08-18 | — | Combined stack and team robot repo marked **BLOCKED** on [#2](https://github.com/The-Allsparks/FORGE/issues/2). |
| 2026-08-18 | — | Combined stack row added as first acceptance priority ([FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4)); still blocked on robot repo. |
| 2026-08-17 | — | Dashboard created; all optional systems start disabled or TRACE-passive-as-goal. |

## Approval reminder

Competition approval requires correct behavior, safe failure, no unacceptable loop impact, rollback, student understanding, demonstrated benefit, and repeatability. See [safety-and-enablement.md](../../docs/safety-and-enablement.md).
