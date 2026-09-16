# Readiness dashboard

Update during the last 10–20 minutes of a meeting. One row per capability. Do not add a second tracking system.

**How to edit:** change the markdown table cells. Owners may be roles or initials — not full student names in git if the team prefers privacy.

Ladder levels: 1 desktop · 2 sim/fake · 3 passive robot · 4 controlled hardware · 5 practice field · 6 mock match · 7 scrimmage · 8 competition approval

Competition status: `disabled` · `passive` · `practice-only` · `approved` · `frozen`

**Judging / portfolio readiness** (not a robot enablement flag): `none` · `skeleton` · `candidates mapped` · `draft ready` · `validated`

Opening this file does not approve anything.

**Combined stack (P0):** [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4). Robot repo is [FtcRobotController](https://github.com/The-Allsparks/FtcRobotController). Drive ran on a Hub. Combined optional-library budgets still unmeasured.

| Capability | Owner / pair | Ladder | Latest evidence | Known risks | Rollback method | Next required test | Competition status |
| ---------- | ------------ | ------ | --------------- | ----------- | --------------- | ------------------ | ------------------ |
| Combined stack | | 4 | BumbleBee Drive APK on Hub (8 Sep TRACE; 15 Sep redeploy). AMPER current sampling blew loop time. | Optional libs not budgeted together | disable each optional independently ([student-install.md](../../docs/student-install.md)) | Drive-only loop + hub voltage AMPER; no per-motor current | practice-only |
| Robot mechanical | | 4 | P002–P004 construction; Drive on floor 8 Sep and 15 Sep | unknown remainder; scoring mech not started | n/a | Keep inspecting during practice | disabled |
| Electrical | | 3 | Temporary wiring sufficient for Drive. **Not** a competition diagram. | will be rebuilt with the real design | power disconnect | Keep temp path safe; freeze only after G3 | disabled |
| Driver-control | | 4 | All students drove 15 Sep; extra practice 16 Sep; S002 more reps | still few reps vs season | DS stop | S002 55-minute block | practice-only |
| Conventional autonomous | | 1 | none | no path yet | run teleop only | S010 simple Pedro path (S003 is Onshape) | disabled |
| TRACE | | 4 | Hub .tlog 8 Sep; live AdvantageScope 15 Sep | AMPER current in TRACE must stay off Drive | `TraceMode.OFF` | Friday Drive session with voltage-only AMPER | passive |
| AMPER | | 3 | Voltage observe; 8 Sep current sampling 63 ms median | per-motor `getCurrent` too slow | `AmperPolicies.disabled()` | Hub-wide current only; never four drive motors | disabled |
| MIMIC | | 1 | no elevator; BIOBUZZ intake/turret/hood not built | Phase 0 only | flags default / no actuation | Paper states after G1 | disabled |
| ViDAR | | 1 | BIOBUZZ fixtures JSON on `main`; no Hub cameras | 4-cam unvalidated | do not consume detections in drive | One camera after G3 if earned | disabled |
| BEACON | | 1 | none | no DS early-stop API | omit reports; official stop remains | S002 exercises | disabled |
| HELM | | 1 | teleop pose is TRACE/Pedro; HELM consumes snapshot freshness only | gates unmet | mode `OFF` | S010 paper trees | disabled |
| ECHO | | 1 | none | match audio not approved | `driverEnabled=false` / no audio flag | S006 desktop, mute path | disabled |
| Inspection | | 1 | none | rookie first inspect | n/a | S008 checklist | disabled |
| Pit workflow | | 1 | none | no timed drill | n/a | clinic + S008 | disabled |
| Judging | | 1 | P001–P002 sponsor stewardship evidence | no narrative; G1 package empty | n/a | S002 kickoff package | disabled |
| Driver practice | | 4 | All four students drove 15 Sep | still insufficient season reps | n/a | 16 Sep extra; S002 every Meeting B | practice-only |
| Student understanding | | 2 | S001 game review | mixed experience | n/a | S002 G1 explain-backs | disabled |

## Status log (newest first)

| Date | Session | What changed |
| ---- | ------- | ------------ |
| 2026-09-15 | shop | **All students drove.** Extra practice **16 Sep**. Electrical stays **temporary** until a real design. AMPER: hub-wide current, not per-drive. MIMIC: no elevator; intake/color reject, turret, hood, feeder, optional FLOWER tray. HELM: pose monitoring is TRACE/Pedro; snapshot freshness only. |
| 2026-09-14 | S001 | **Complete.** Season updates, official game review, and brainstorm. Crude prototypes wait. Onshape first lesson **S003 (21 Sep)**; G2 comparative tests **S004**. Clinic 24h code freeze named on S008. |
| 2026-09-08 | Hub | BumbleBee Drive TRACE sessions. Drive-only ~18 ms median. AMPER with motor current ~63 ms median (do not repeat). |
| 2026-09-04 | P006 | **Complete (variance)** — code walkthrough only. Electrical, useful programming, motor tests, and first movement did **not** run. Catch-up is P007 (last shop night). |
| 2026-09-02 | — | Pratt *Why Most FTC Teams Fail* findings integrated: four tests, R0–R5, Kickoff package, acceptance method, software tiers, award strategy. See [docs/pratt-why-teams-fail.md](docs/pratt-why-teams-fail.md). Not marked as team-practiced yet. |
| 2026-09-02 | — | **Schedule reconciliation.** P002–P004 = construction (subassembly detail unverified). P005 = BIOBUZZ Pre-Season V0 rules (not bring-up). P006 = electrical/programming/first movement. P007 = drivetrain dial-in + Kickoff prep. P008 = FRC tour. Mechanism lab stays post-Kickoff. See [preseason-deferred-work.md](docs/preseason-deferred-work.md). |
| 2026-08-31 | P005 | **Complete (variance)** — BIOBUZZ Pre-Season V0 rules review. Bring-up, TRACE, wiring, and driving did **not** run. |
| 2026-08-26 | P004 | **Complete (variance)** — Strafer / first-robot construction session 3 of 3. Electrical and Onshape did **not** run. |
| 2026-08-24 | P003 | **Complete (variance)** — Strafer / first-robot construction session 2 of 3. Original drivetrain-finish / CAD-prep did **not** run. |
| 2026-08-19 | — | Onshape first lesson later scheduled as **S003 (21 Sep)** FRC-hosted (was coach prep / S006). Custom parts are possible if the as-built robot needs them — **not** confirmed P002 accomplishments. |
| 2026-08-19 | P002 | **Complete** — Strafer / first-robot construction session 1 of 3. Subassembly detail (motors, cards finished, orders) **unverified**. |
| 2026-08-19 | — | Pratt compressed season process integrated; gates G1–G8; see [docs/season-process.md](docs/season-process.md). |
| 2026-08-19 | P002 | ~~Scheduled~~ — superseded by completion entry above. |
| 2026-08-19 | — | Renumber: P001–P008 preseason, K001 Kickoff, S001+ season; Mon/Fri 4–6 PM; E004/E005 event days. |
| 2026-08-18 | — | Combined stack and team robot repo marked **BLOCKED** on [#2](https://github.com/The-Allsparks/FORGE/issues/2). |
| 2026-08-18 | — | Combined stack row added as first acceptance priority ([FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4)); still blocked on robot repo. |
| 2026-08-17 | — | Dashboard created; all optional systems start disabled or TRACE-passive-as-goal. |

## Approval reminder

Competition approval requires correct behavior, safe failure, no unacceptable loop impact, rollback, student understanding, demonstrated benefit, and repeatability. See [safety-and-enablement.md](../../docs/safety-and-enablement.md).
