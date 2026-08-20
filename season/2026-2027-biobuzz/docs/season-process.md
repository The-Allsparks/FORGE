# Season process — compressed competition-one cycle

**Adapted from** Brogan M. Pratt's [*A 12 Week FTC Season Plan That Actually Works*](https://www.youtube.com/playlist?list=PLRHdgFNRLyaM6TmNVVHKqVnnyntDDYDNt). Pratt does not endorse FORGE or The Allsparks. See [references.md](references.md) for attribution and adaptation notes.

## Team context

| Factor | Value |
| ------ | ----- |
| Team | The Allsparks, FTC 36117 |
| Students | Four rookies; oldest ~12, youngest ~5th grade |
| Meetings | ~2 hours, twice per week (Mon Meeting A, Fri Meeting B) |
| Kickoff | 12 September 2026 (planning input) |
| First Nevada competition window | League 1S/2S **31 October 2026** (planning input) — ~6–7 post-Kickoff weeks |
| Competition robot name | **Sparkee** (modular; see [modular-architecture.md](modular-architecture.md)) |

## Pratt's original twelve-week structure (preserved for reference)

Pratt's series describes one week per row. Schedule protections are **essential** — do not skip them when compressing.

| Pratt week | Original focus | Essential protection |
| ---------- | -------------- | -------------------- |
| 1 | Rules, scoring, strategy, research, ideation, crude prototype | — |
| 2 | Prototype robot, programming chassis, student goals, outreach planning | — |
| 3 | Comparative mechanism prototyping | **Week 3 ends unrestricted mechanism exploration** |
| 4 | Modular architecture, subsystem interfaces, sensor planning | — |
| 5 | Mechanism selection, refinement, conditional vision proof-of-concept | **Week 5 selects primary mechanism direction** |
| 6 | Major-design-pivot deadline; competition-one architecture commitment | **Week 6 ends major architectural pivots for first competition** |
| 7 | Construction of robust, maintainable competition modules | — |
| 8 | Final mechanical, electrical, and wiring integration | **Week 8 completes mechanical and electrical integration** |
| 9 | Stable robot handoff; mechanism tuning; pathing calibration | **Week 9 hands stable robot to software** |
| 10 | Autonomous routines, driver automation, portfolio, next-gen research | — |
| 11 | Reliability testing, mock judging, feature/code freeze | **Week 11 ends with feature/code freeze** |
| 12 | Full-match driver practice, pit prep, checklists, spares, portfolio, logistics | **Week 12 reserved for drivers, reliability, judging, pit — not speculative features** |

Pratt's final-week guidance: [How to Win Your Next FTC Competition](https://www.youtube.com/watch?v=Y4K540aCR0E).

## Allsparks compression map

Pratt weeks **stack** into fewer calendar weeks. Protections land on **dates and gates**, not on Pratt week numbers.

| Compressed phase | Approx. dates | Pratt weeks absorbed | FORGE gate |
| ---------------- | ------------- | -------------------- | ---------- |
| [Preseason](#preseason) | through 11 Sep 2026 | Pratt assumes Kickoff = week 1; we front-load chassis, safety, evidence | — |
| [Post-Kickoff week 1 — Understand and diverge](#post-kickoff-week-1-understand-and-diverge) | 12–20 Sep 2026 | 1–2 (partial) | **G1 Strategy** |
| [Post-Kickoff week 2 — Test and compare](#post-kickoff-week-2-test-and-compare) | 21–27 Sep 2026 | 2–3 (partial) | **G2 Prototype evidence** |
| [Post-Kickoff week 3 — Select and commit](#post-kickoff-week-3-select-and-commit) | 28 Sep – 4 Oct 2026 | 3–4–5 (compressed) | **G3 Architecture selection** |
| [Post-Kickoff week 4 — Build and integrate](#post-kickoff-week-4-build-and-integrate) | 5–11 Oct 2026 | 6–7–8 (compressed) | **G4 Design freeze** · **G5 Mech/electrical complete** |
| [Post-Kickoff week 5 — Tune and validate](#post-kickoff-week-5-tune-and-validate) | 12–25 Oct 2026 | 9–10 (partial) | **G6 Stable software handoff** |
| [Post-Kickoff week 6 — Freeze and rehearse](#post-kickoff-week-6-freeze-and-rehearse) | 26–30 Oct 2026 | 11–12 (partial) | **G7 Reliability / feature freeze** |
| [Post-Kickoff week 7 — Competition simulation](#post-kickoff-week-7-competition-simulation-if-available) | 31 Oct 2026+ | 12 | **G8 Competition readiness** |
| Post–League 1S/2S | Nov 2026 – Feb 2027 | Version 2 research; league evidence | FORGE league-development phases |

Session-level mapping: [pratt-crosswalk.md](pratt-crosswalk.md).

---

## Preseason

**Goal:** Capable team, reliable hybrid Strafer platform, evidence habits — not a speculative BIOBUZZ scoring robot.

| Deliverable | Detail |
| ----------- | ------ |
| Hybrid Strafer drivetrain | Modified goBILDA Strafer / 2026–2027 Starter Bot platform |
| Safe wiring and battery practices | P004 electrical foundation |
| SDK, version control, deployment, logging | ~30 min/week software cap — [preseason-software-allocation.md](preseason-software-allocation.md) |
| Pedro Pathing familiarity | Preseason tuning does **not** transfer unchanged to final Sparkee mass/geometry |
| Minimum viable software stack | TRACE habit first; others passive or off |
| Driver conventions and basic driving | P006 driver baseline |
| Templates and documentation habits | Prototype records, decision records, photos — [templates/](../../../templates/) |
| Student learning goals and baselines | [student-learning-goal.md](../../../templates/student-learning-goal.md) |
| Sponsor stewardship, inventory, safety | P001–P002 completed work preserved |

**Preseason definition of done:** [season-plan.md](../season-plan.md#preseason--through-11-september-2026-p001p008-last-shop-meeting-before-kickoff).

---

## Post-kickoff week 1: Understand and diverge

**Pratt alignment:** Weeks 1–2 (rules, strategy, ideation, crude prototype).

| Activity | Detail |
| -------- | ------ |
| Manual study | Read and annotate official BIOBUZZ competition manual |
| Strategy matrix | Scoring, ranking, penalty, and constraint matrix |
| MVP strategies | Minimum viable scoring and ranking-point paths |
| Research | Official starter robots; comparable prior-game mechanisms |
| Visual ideation | **60–100** concepts across four students (scaled from Pratt's hundreds) |
| Low-fidelity prototypes | Cardboard, coroplast, temporary channel — at least one game-object interaction proof |
| Drivable chassis | Maintain drivable platform throughout |

**Exit gate (G1 — Strategy):** Documented game strategy, prioritized capabilities, initial risk register, ≥1 physical game-object interaction proof. See [decision-gates.md](decision-gates.md#g1--strategy-gate).

**Sessions:** K001, S001, S002.

---

## Post-kickoff week 2: Test and compare

**Pratt alignment:** Weeks 2–3 (prototype robot, comparative mechanism prototyping).

| Activity | Detail |
| -------- | ------ |
| Comparative tests | Official starter solution vs one–two credible alternatives |
| Measurements | Acquisition success, misalignment tolerance, cycle time, compression, jams, object damage, current draw, packaging, repairability |
| Software start | Minimum autonomous movement; basic mechanism-state software |
| Interfaces | Confirm subsystem boundaries and required interfaces |
| Outreach and goals | Sustained outreach start; student goal progress recorded |

**Pratt protection:** Unrestricted mechanism exploration **ends** at this phase boundary (Pratt week 3).

**Exit gate (G2 — Prototype evidence):** Comparative evidence, leading concepts, starter-bot fallback identified, unresolved-risk list. Template: [prototype-test-record.md](../../../templates/prototype-test-record.md).

**Sessions:** S002 (continued), S003, S004.

---

## Post-kickoff week 3: Select and commit

**Pratt alignment:** Weeks 4–5–6 compressed (architecture, mechanism selection, pivot deadline).

| Activity | Detail |
| -------- | ------ |
| Architecture selection | Evidence-driven competition-one architecture |
| Modular boundaries | Mechanical, electrical, software, sensor, wiring interfaces |
| Sensor decisions | Necessary vs optional |
| CAD and packaging | Enough to authorize fabrication |
| Pivot deadline | **Major design pivots end here** for first competition (Pratt week 6) |
| Scope rejection | Cut features that do not fit build, program, drive, or test time |

**Pratt protection:** **Primary mechanism direction selected** (Pratt week 5).

**Exit gate (G3 — Architecture selection):** Approved architecture, interface definitions, CAD/fabrication package, BOM, software contract, explicit fallback plan.

**Sessions:** S005, S006.

---

## Post-kickoff week 4: Build and integrate

**Pratt alignment:** Weeks 6–7–8 compressed (modules, integration).

| Activity | Detail |
| -------- | ------ |
| Module fabrication | Robust, maintainable Sparkee modules |
| Incremental software delivery | Modules to software as built — do not wait for whole robot |
| Wiring | Strain relief, service loops, moving-mechanism protection, ESD awareness |
| Instrumentation | MIMIC mechanism classes; TRACE/AMPER as hardware appears |
| Maintainability | Repair access; rapid module replacement; spares for fragile parts |

**Pratt protection:** **Mechanical and electrical integration complete** by phase end (Pratt week 8).

**Exit gates:** **G4 Design freeze** (no new modules without gate review) · **G5 Mechanical/electrical completion**.

**Sessions:** S007, S008, clinic (10 Oct).

---

## Post-kickoff week 5: Tune and validate

**Pratt alignment:** Weeks 9–10 (stable handoff, auto, portfolio).

| Activity | Detail |
| -------- | ------ |
| Mechanical freeze | Stop major mechanical changes |
| Pathing tuning | Final mass and geometry on Sparkee — not Strafer assumptions |
| Autonomous | Minimum reliable auto first; alliance-compatible alternate path if time |
| Driver automation | Only when workload drops and reliability is demonstrated |
| Testing | Repeated mechanism and full-robot tests; TRACE + human-readable log |
| Portfolio | Draft engineering portfolio and judging narrative |

**Pratt protection:** **Stable robot handed to software** (Pratt week 9).

**Exit gate (G6 — Stable software handoff):** Competition-capable robot, reliable minimum auto, stable teleop, measured reliability, substantially complete portfolio draft.

**Sessions:** S009, S010, S011, S012.

---

## Post-kickoff week 6: Freeze and rehearse

**Pratt alignment:** Weeks 11–12 (freeze, mock judging, full-match practice).

| Activity | Detail |
| -------- | ------ |
| Feature freeze | Speculative mechanical and software features frozen |
| Allowed changes | Critical defect, safety, reliability, usability only |
| Full matches | Complete 2½-minute practice matches |
| Adversity | Congestion, defense, disabled robots, failed sensors, degraded drivetrain (where safe) |
| Mock judging | Five-minute presentations; all four students speak |
| Logistics | Pit organization, spares, tools, batteries, chargers, transport, food, documents |

**Pratt protection:** **Feature/code freeze** (Pratt week 11). **Week 12 activities** begin here because timeline is compressed.

**Exit gate (G7 — Reliability / feature freeze):** Feature freeze declared; reliability metrics recorded; mock judging completed.

**Sessions:** S013, S014.

---

## Post-kickoff week 7: Competition simulation (if available)

**Pratt alignment:** Week 12 (competition lifecycle rehearsal).

| Activity | Detail |
| -------- | ------ |
| Full lifecycle | Pre-match through post-match checklists |
| Repairs | Battery replacement; common fixes under time pressure |
| Releases | Code backups; known-good release tags verified |
| Reliability | Repeat auto and driver trials |
| Materials | Finalize and print portfolio and pit materials |
| Rule | **No elective feature additions** |

**Exit gate (G8 — Competition readiness):** [RD001-competition-approval.md](../../../assessments/readiness/RD001-competition-approval.md) review passed.

**Event:** League 1S/2S (31 Oct 2026, planning input).

---

## Two-platform strategy

See [two-platform-strategy.md](two-platform-strategy.md). Summary:

- **Strafer (preseason platform):** Software, driver conventions, Pedro familiarity
- **Official starter-bot design:** Scoring baseline and fallback
- **Bench/fixture rigs:** Mechanism development without blocking Sparkee
- **Version 2 research:** After Sparkee mechanical freeze only — cannot steal competition-one resources

## Software protections

Software progresses **throughout** the season — not after fabrication.

| Capability | Minimum for first competition | Defer if time-constrained |
| ---------- | ----------------------------- | ------------------------- |
| FTC SDK + deployment | Required | — |
| GitHub + release tags | Required | — |
| Controller mapping | Required | — |
| TRACE structured logs | Required | — |
| MIMIC mechanism states | Required for scored mechanisms | Advanced interlocks |
| Pedro Pathing | Minimum reliable auto | Alternate paths |
| AMPER | Passive observation | Active limiting |
| BEACON | Safe-state / freshness awareness | Active intervention |
| ViDAR | Only if strategy + measurable value | Multi-camera |
| HELM | After basic mechanism reliability | Execute authority (never) |
| ECHO | Only if driver workload drops | Match audio |

Combined stack acceptance: [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4). Hub evidence blocked until [FORGE#2](https://github.com/The-Allsparks/FORGE/issues/2).

## Driver development

| Phase | Practice |
| ----- | -------- |
| Preseason | Basic mecanum; controller layout evaluation |
| Early season | Short practice end of each meeting |
| After integration | Task-specific repetition |
| After software handoff | Full cycles and full matches |
| Final week | 2½-minute simulations under nonideal conditions |

Include: congestion, defensive pressure, alliance coordination, failed-auto recovery, sensor/manual override, degraded drivetrain (safe tests), Driver 1/Driver 2 communication, match strategy, post-run feedback as actionable issues.

**Protect the final full week from elective robot changes.**

## Outreach, Sustain, and judging

The Allsparks is lighter in Outreach/Sustain — activities start **preseason**:

- One measurable personal learning goal per student ([student-learning-goal.md](../../../templates/student-learning-goal.md))
- Skill baselines and periodic progress ([student-progress-review.md](../../../templates/student-progress-review.md))
- Sponsor contact records; thank-you cards; progress updates
- Audiences: local families, sponsors/partners, FIRST Nevada, other rookie FTC/FLL teams
- One repeatable community activity over many disconnected appearances
- Robotics Mixer and community events as coherent impact story
- Master season-notes document → portfolio source
- Portfolio drafting **before** robot is finished
- Mock judging: all four students; accommodations for comfortable authentic participation

**Unverified until official rules publish:** award names, portfolio page limits, judging times, pit dimensions. Do not hard-code DECODE-era values.

## Four-student rotating roles

No permanent build/program/outreach silos:

- Rotating responsibility model; pairs for focused work
- Everyone conversant with complete robot and team story
- Rotate documentation and test-recording duties
- Mechanical work must not monopolize all four students
- Mentor checkpoints — mentors facilitate; **students decide**
- Distinguish student decisions from mentor safety, scheduling, procurement support

## Competition-readiness artifacts

Templates in [templates/competition/](../../../templates/competition/). Assign owners at G8 prep. Checklists must be short enough for competition pressure; separate every-match vs occasional maintenance items.

## Priority order (unchanged)

working robot → reliable mechanisms → driver practice → conventional autonomous → evidence collection → advanced autonomy

## After League 1S/2S

FORGE **preserves** later phases (league-development, adversity-simulations, feature-freeze, state-prep) for meets in Nov–Feb 2027. Version 2 mechanism research uses Strafer, fixtures, or spare modules **only after** G7 freeze — never at the expense of reliability, driving, documentation, or judging.
