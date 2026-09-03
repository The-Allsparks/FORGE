# Pratt *Why Most FTC Teams Fail* — audit and adaptation

Working matrix for integrating Brogan M. Pratt, *Why Most FTC Teams Fail (And How Not To)*, into FORGE for The Allsparks (FTC 36117), 2026–2027 BIOBUZZ.

This is **not** an official FIRST source. Game Manual, Q&A, and inspection rules override it. Pratt does not endorse FORGE. The twelve-week process already in [pratt-crosswalk.md](pratt-crosswalk.md) is a **different** Pratt series; do not collapse the two.

**Date of audit:** 2 September 2026. Evidence is from repository files as of that date (including preseason variance). This file is the audit trail; operational rules live in the linked canonical docs.

## Classifications

| Code | Meaning |
| ---- | ------- |
| **E** | Already explicit |
| **W** | Present but weak or implied |
| **M** | Missing |
| **R** | Inapplicable or intentionally rejected / modified |

## Finding matrix

| # | Finding | Class | Evidence (before this integration) | FORGE action |
| - | ------- | ----- | ---------------------------------- | ------------ |
| 1 | Guiding principle: simplicity, reliability, field repairability, time for programming and driver practice | **W** | Priority order in [season-plan.md](../season-plan.md), [AGENTS.md](../../../AGENTS.md); Meeting B 55 min; G1–G8 in [decision-gates.md](decision-gates.md) protect time. No four-test principle that **blocks** a feature. | Adopt [guiding-principle.md](guiding-principle.md); apply at G1–G3, G7, software promotions. |
| 2 | Analyze game and rules before committing: full manual, scoring, ranking, alliance roles, high-value/low-effort, multiple approaches, ranked capabilities, explicit not-yet/will-not, no build-to-look-busy | **W** | [K001](../sessions/K001-meeting-k.md), [kickoff-replan-guide.md](../kickoff-replan-guide.md), G1 strategy matrix; P005 v0 rules. Missing ranking vs scoring, alliance roles, effort/value table, not-yet list as an artifact, explicit anti-busywork rule. | [kickoff-decision-package.md](../../../templates/kickoff-decision-package.md); S001 crude prototypes only. |
| 3 | Fewer tasks done consistently vs every game function | **W** | MVP sentence (drive + one score + park); starter fallback. Not stated as a consistency rule. | Ranked list + not-yet list; R0–R3 before R5. |
| 4 | Staged minimum-viable robot releases | **M** | Gates G1–G8 are process gates, not capability releases. | [robot-releases.md](robot-releases.md) R0–R5. |
| 5 | Modular architecture; swap without rebuilding the robot | **E** | [modular-architecture.md](modular-architecture.md), [two-platform-strategy.md](two-platform-strategy.md), G3. | Keep; add reliability design rules on that page. |
| 6 | Physical prototypes and real tests before treating CAD as validated | **W** | G1 crude prototype; G2 ≥3 trials; G3 CAD authorization. Not stated that CAD ≠ validation. | [acceptance-criteria.md](acceptance-criteria.md) CAD section; G2 before G3 fab. |
| 7 | Document the full engineering process (problem, alternatives, sources, criteria, math, method, raw results, interpretation, failure, decision) | **W** | Split across evidence, decision, prototype, math, failure templates. No sources/prior-art field; interpretation mixed with observations. | Completeness map in [evidence-model.md](../../../docs/evidence-model.md); fields added to templates. |
| 8 | Quantified acceptance gates, not "it worked" | **W** | ≥3 trials; G6 ≥10 attempts and 7/10 auto. No method for choosing n on a 4 h/week team; no cycle-time distribution. | [acceptance-criteria.md](acceptance-criteria.md). Keep 7/10 as an example, not a universal 20/20. |
| 9 | Design for reliability (rigidity, fewer DOF, short travel, fewer transfers, fewer SPOFs, accessible repair, spares, degraded operation) | **W** | G5 repair access, spares, strain relief. Missing design heuristics. | Section on [modular-architecture.md](modular-architecture.md). |
| 10 | Protect several weeks for driver practice; stop continuous redesign | **W** | Meeting B throughout; G7 last week. Pratt's multi-week exclusive practice is **impossible** here. | Named runway **12–30 Oct** in [robot-releases.md](robot-releases.md#competition-runway). |
| 11 | Partial automation only after base mechanisms work | **E** | S012 "if earned"; G6 driver automation rule; [season-process.md](season-process.md) software table. | Restate as R5 + [software-sequencing.md](software-sequencing.md). |
| 12 | Test degraded and failure conditions (motor loss, jam, sensor, comms, indexing, auto fallback, timed pit) | **W** | Week-6 list; S024–S030 **after** league 1 (December). G7 "two scenarios." Competition-one path under-specified. | [failure-mode-drills.md](failure-mode-drills.md) assigned to S011/S013/S014. |
| 13 | Mechanical and software freeze before competitions | **E** | G4, G5, G7, G8. Clinic correctly **not** a freeze. G7 is one day before league — tight but already the plan. | Keep dates; do not invent an earlier freeze that would skip G2/G3. |
| 14 | Disagree and commit; controlled reopen with new evidence | **M** | Debate + student decisions; decision-record "later validation." No commit language or reopen procedure. | [decision-gates.md](decision-gates.md#disagree-and-commit). |
| 15 | Think as a universal judged-award process objective | **E** | [award-and-portfolio-traceability.md](../../../docs/award-and-portfolio-traceability.md); A/B/C/D tags on templates. | Keep; [award-strategy.md](award-strategy.md) says Think is not optional. |
| 16 | Focused award objectives, not every award equally | **M** | Traceability maps all awards; no selection process. | [award-strategy.md](award-strategy.md) hypothesis (Control / Connect) **after** official criteria — not a premature lock. |
| 17 | Portfolio evidence organized so judges find rubric rows quickly | **W** | Think topics, Control checklist, candidates. No judge-facing page index. | Award-strategy page index + cover/page-1 map. |

## Modified or rejected (intentional)

| Pratt-adjacent idea | FORGE decision | Why |
| ------------------- | -------------- | --- |
| Several exclusive weeks of only driving before the first event | **Modified** to 12–30 Oct (~12 h) plus Meeting B all season | 6–7 post-Kickoff weeks × 4 h; clinic on 10 Oct. Exclusive multi-week practice would cancel G2–G5. |
| Hardcoded 20/20 (or similar) everywhere | **Rejected** as a universal gate | Sample size method in acceptance-criteria.md. |
| Declare a final award target now | **Rejected** | Official V1/Kickoff criteria and Nevada context first. |
| Transcript page-limit numbers | **Rejected** | Use V0 **15 pages / 15 MB** in traceability; re-verify Kickoff. |
| Two full competition robots | **Already modified** (prior integration) | Strafer + Sparkee + fixtures. |
| Hundreds of sketches | **Already modified** | 60–100 across four students. |
| Zero physical work in week 1 | **Modified** | Chassis finish (R0) and crude game-object prototypes allowed; custom scoring fab at scale still blocked until G1. |
| Delete the software vision | **Rejected** | Four-tier sequencing instead. |
| Treat clinic as the freeze event | **Rejected** | Clinic remains data collection (existing plan). |

## Canonical documents (do not duplicate)

| Topic | File |
| ----- | ---- |
| Four tests | [guiding-principle.md](guiding-principle.md) |
| R0–R5 and runway | [robot-releases.md](robot-releases.md) |
| Sample sizes and metrics | [acceptance-criteria.md](acceptance-criteria.md) |
| Kickoff outputs | [kickoff-decision-package.md](../../../templates/kickoff-decision-package.md) |
| Software tiers | [software-sequencing.md](software-sequencing.md) |
| Awards | [award-strategy.md](award-strategy.md) |
| Failure drills | [failure-mode-drills.md](failure-mode-drills.md) |
| Twelve-week Pratt series (different source) | [pratt-crosswalk.md](pratt-crosswalk.md) |
