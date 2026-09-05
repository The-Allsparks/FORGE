# Readiness dashboard

Update during the last 10–20 minutes of a meeting. One row per capability. Do not add a second tracking system.

**How to edit:** change the markdown table cells. Owners may be roles or initials — not full student names in git if the team prefers privacy.

Ladder levels: 1 desktop · 2 sim/fake · 3 passive robot · 4 controlled hardware · 5 practice field · 6 mock match · 7 scrimmage · 8 competition approval

Competition status: `disabled` · `passive` · `practice-only` · `approved` · `frozen`

**Judging / portfolio readiness** (not a robot enablement flag): `none` · `skeleton` · `candidates mapped` · `draft ready` · `validated`

Opening this file does not approve anything.

**Combined stack (P0):** [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4). Robot repo is published. Hub evidence is still unmeasured. Desktop compile is not that evidence.

| Capability | Owner / pair | Ladder | Latest evidence | Known risks | Rollback method | Next required test | Competition status |
| ---------- | ------------ | ------ | --------------- | ----------- | --------------- | ------------------ | ------------------ |
| Combined stack | | 1 | desktop compile of BumbleBee Drive on [FtcRobotController](https://github.com/The-Allsparks/FtcRobotController); Hub budgets unmeasured | Hub untested | disable each optional independently ([student-install.md](../../docs/student-install.md)) | P007 deploy + conventional teleop on a Hub | disabled |
| Robot mechanical | | 1 | P002–P004 construction (**as-built unverified**); P006 did not inspect | unknown remainder after three build meetings | n/a | **P007** — inspect during wiring/bring-up | disabled |
| Electrical | | 1 | none (P004 wiring did not run; P006 did not run it either) | unvalidated wiring | power disconnect | **P007** diagram and wiring | disabled |
| Driver-control | | 1 | none (P006 was code reading only) | no first movement yet | DS stop | **P007** restrained then slow floor; dial-in leftover or **S002** | disabled |
| Conventional autonomous | | 1 | none | no path yet | run teleop only | S003 simple Pedro path | disabled |
| TRACE | | 1 | none | not Hub-tested | `TraceMode.OFF` | P007 paper notes; library later | passive (goal) |
| AMPER | | 1 | none | not Hub-tested | `AmperPolicies.disabled()` | passive voltage in S001+ if useful | disabled |
| MIMIC | | 1 | none | Phase 0 only | flags default / no actuation | paper states post-Kickoff (original P007 lab deferred) | disabled |
| ViDAR | | 1 | none | 4-cam unvalidated | do not consume detections in drive | S001 sim or one camera | disabled |
| BEACON | | 1 | none | no DS early-stop API | omit reports; official stop remains | S002 exercises | disabled |
| HELM | | 1 | none | gates unmet | mode `OFF` | S010 paper trees | disabled |
| ECHO | | 1 | none | match audio not approved | `driverEnabled=false` / no audio flag | S006 desktop, mute path | disabled |
| Inspection | | 1 | none | rookie first inspect | n/a | S008 checklist | disabled |
| Pit workflow | | 1 | none | no timed drill | n/a | clinic + S008 | disabled |
| Judging | | 1 | P001–P002 sponsor stewardship evidence | no narrative | n/a | notebook; portfolio skeleton | disabled |
| Driver practice | | 1 | none | insufficient reps | n/a | every Meeting B | disabled |
| Student understanding | | 1 | none | mixed experience | n/a | session explain-backs | disabled |

## Status log (newest first)

| Date | Session | What changed |
| ---- | ------- | ------------ |
| 2026-09-04 | P006 | **Complete (variance)** — code walkthrough only. Electrical, useful programming, motor tests, and first movement did **not** run. Catch-up is P007 (last shop night). |
| 2026-09-02 | — | Pratt *Why Most FTC Teams Fail* findings integrated: four tests, R0–R5, Kickoff package, acceptance method, software tiers, award strategy. See [docs/pratt-why-teams-fail.md](docs/pratt-why-teams-fail.md). Not marked as team-practiced yet. |
| 2026-09-02 | — | **Schedule reconciliation.** P002–P004 = construction (subassembly detail unverified). P005 = BIOBUZZ Pre-Season V0 rules (not bring-up). P006 = electrical/programming/first movement. P007 = drivetrain dial-in + Kickoff prep. P008 = FRC tour. Mechanism lab stays post-Kickoff. See [preseason-deferred-work.md](docs/preseason-deferred-work.md). |
| 2026-08-31 | P005 | **Complete (variance)** — BIOBUZZ Pre-Season V0 rules review. Bring-up, TRACE, wiring, and driving did **not** run. |
| 2026-08-26 | P004 | **Complete (variance)** — Strafer / first-robot construction session 3 of 3. Electrical and Onshape did **not** run. |
| 2026-08-24 | P003 | **Complete (variance)** — Strafer / first-robot construction session 2 of 3. Original drivetrain-finish / CAD-prep did **not** run. |
| 2026-08-19 | — | Onshape remains coach prep / S006. Custom parts are possible if the as-built robot needs them — **not** confirmed P002 accomplishments. |
| 2026-08-19 | P002 | **Complete** — Strafer / first-robot construction session 1 of 3. Subassembly detail (motors, cards finished, orders) **unverified**. |
| 2026-08-19 | — | Pratt compressed season process integrated; gates G1–G8; see [docs/season-process.md](docs/season-process.md). |
| 2026-08-19 | P002 | ~~Scheduled~~ — superseded by completion entry above. |
| 2026-08-19 | — | Renumber: P001–P008 preseason, K001 Kickoff, S001+ season; Mon/Fri 4–6 PM; E004/E005 event days. |
| 2026-08-18 | — | Combined stack and team robot repo marked **BLOCKED** on [#2](https://github.com/The-Allsparks/FORGE/issues/2). |
| 2026-08-18 | — | Combined stack row added as first acceptance priority ([FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4)); still blocked on robot repo. |
| 2026-08-17 | — | Dashboard created; all optional systems start disabled or TRACE-passive-as-goal. |

## Approval reminder

Competition approval requires correct behavior, safe failure, no unacceptable loop impact, rollback, student understanding, demonstrated benefit, and repeatability. See [safety-and-enablement.md](../../docs/safety-and-enablement.md).
