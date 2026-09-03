# Pratt *Why Most FTC Teams Fail* — integration report

**Date:** 2 September 2026  
**Scope:** Incorporate applicable findings from Brogan M. Pratt, *Why Most FTC Teams Fail (And How Not To)*, into the 2026–2027 BIOBUZZ FORGE plan for The Allsparks (FTC 36117).  
**Primary source:** Findings enumerated from the video (integration brief). A standalone transcript file was not present in the repository; the brief’s seventeen findings were treated as the extract. Official FIRST rules override the video. Pratt does not endorse FORGE.

This is **not** a replacement of the 19 August twelve-week Pratt integration ([pratt-integration-report.md](pratt-integration-report.md)). That work (G1–G8, compressed weeks, Sparkee modules) is preserved.

Audit matrix: [docs/pratt-why-teams-fail.md](docs/pratt-why-teams-fail.md).

---

## Audit findings (summary)

| Class | Findings |
| ----- | -------- |
| Already explicit | Modular architecture (5); partial automation after reliability (11); mech/software freeze gates (13); Think as process (15) |
| Present but weak | Principle (1); Kickoff analysis (2); fewer tasks (3); CAD vs physical tests (6); full process docs (7); quantified gates (8); reliability design (9); driver-practice weeks (10); degraded drills before league 1 (12); portfolio rubric map (17) |
| Missing | Staged R0–R5 releases (4); disagree-and-commit (14); focused award selection (16) |
| Modified / rejected | Exclusive multi-week driving-only block; universal 20/20; locking awards now; video page-limit numbers; two full robots; hundreds of sketches; zero week-1 physical work; deleting the software vision; treating clinic as freeze |

Evidence for each row is in the audit file.

---

## Recommendations adopted

- Four-test guiding principle, applied at G1–G3, G7, and software promotions
- Kickoff decision package (scoring, ranking, alliance roles, effort/value, ranked capabilities, not-yet list, R0–R2, software tiers)
- Staged releases R0–R5 mapped to clinic (10 Oct) and league (31 Oct)
- Quantified acceptance method with risk-based n (not 20/20)
- Reliability design heuristics on the module contract
- Named competition runway **12–30 Oct** (S009–S014)
- Failure-mode catalog assigned to S011/S013/S014 **and** existing S024–S030
- Four-tier software sequencing (MVR / before league / later / research)
- Disagree-and-commit with a measured reopen path
- Award strategy: Think always-on; Control and Connect as **hypotheses** until Kickoff V1

## Recommendations modified or rejected

| Item | Decision | Why |
| ---- | -------- | --- |
| Several exclusive weeks of only driver practice | Modified to 12–30 Oct (~12 h) plus Meeting B all season | 4 h/week rookies; clinic 10 Oct; G2–G5 still required |
| 20-for-20 (or similar) everywhere | Rejected as a universal gate | Sample-size method; example 7/10 auto remains |
| Lock Control + Connect now | Rejected as a final target | Official V1/Kickoff criteria + Nevada context first |
| Transcript page limits | Rejected | Use V0 **15 pages / 15 MB**; Kickoff re-verify (FORGE#24) |
| No physical work in analysis week | Modified | R0 chassis finish + crude prototypes allowed; custom scoring fab at scale still blocked |
| Delete ViDAR/HELM/ECHO/etc. vision | Rejected | Four-tier roadmap instead |
| Freeze before the 10 Oct clinic | Rejected | Clinic stays data collection; G7 stays 26–30 Oct |

---

## Files changed (high level)

**New canonical docs:** `docs/guiding-principle.md`, `docs/robot-releases.md`, `docs/acceptance-criteria.md`, `docs/software-sequencing.md`, `docs/award-strategy.md`, `docs/failure-mode-drills.md`, `docs/pratt-why-teams-fail.md`

**New template:** `templates/kickoff-decision-package.md`

**This report:** `pratt-why-teams-fail-integration.md`

**Updated process:** `season-plan.md`, `docs/season-process.md`, `docs/decision-gates.md`, `docs/references.md`, `docs/modular-architecture.md`, `docs/pratt-crosswalk.md`, `docs/preseason-kickoff-gate.md`, `kickoff-replan-guide.md`, `calendar.yaml`, `README.md`, `pratt-integration-report.md` (later note only)

**Updated FORGE-wide:** `AGENTS.md`, `README.md`, `docs/curriculum-model.md`, `docs/evidence-model.md`, `docs/award-and-portfolio-traceability.md`, `docs/mentor-guide.md`, `docs/student-guide.md`, `docs/safety-and-enablement.md`, `learning-paths/{programming,drive-team,mechanical}.md`

**Updated templates:** decision-record, prototype-test-record, evidence-record, concept-brainstorm, gate-review, sparkee-module-record, competition/common-repairs

**Updated sessions:** P008 (link), K001, S001, S002, S003, S005, S006, S008, S010, S011, S012, S013, S014, S024, S026, S028, S029, S030

**Dashboard:** status-log entry only — no capability marked complete from this work.

---

## New gates, freezes, tests, and protected practice

| Item | When |
| ---- | ---- |
| Four tests on every authorizing gate | G1–G8 |
| Kickoff package = G1 evidence | K001 start; **S002** pass/fail |
| Architecture commitment + disagree-and-commit | G3 ~2–4 Oct |
| Competition-mechanism freeze (no new modules) | G4 ~5 Oct |
| Clinic | 10 Oct — R0 required; not a freeze |
| Mech/electrical complete | G5 ~9–11 Oct |
| **Protected driver practice** | **12–30 Oct (S009–S014)** |
| Software integration / auto stabilization | G6 12–23 Oct |
| Feature/code freeze | G7 26–30 Oct |
| Quantified tests | G2 ≥3/concept; match-critical 8–12 with distribution; auto k/n example 7/10 |
| Failure drills before league 1 | S011 (one), S013 (two including F6 if auto), S014 (F7 timed pit; F1 if safe) |
| Portfolio draft | S011; print S014; A201 still V0 15 pages |

---

## Effect on minimum viable robot and software

- **MVR is a release, not a wish list.** League 1S/2S requires R0 + R1 (auto or teleop-only) + R2 if a scoring strategy is claimed. R3 is a goal if G3 holds. R4 is measured cycles. R5 is optional and default **none**.
- Elevator, capstan, hopper, ViDAR drive, AMPER limiting, BEACON intervention, HELM, ECHO match audio, and multi-camera are **not** implied first-meet requirements. They sit on the not-yet list until a ranked row and a gate move them.
- Software vision is intact as tiers 3–4. Tier 1 is deploy, teleop, TRACE/paper, auto-or-teleop-only, MIMIC for scored mechanisms that exist.

---

## Effect on award and portfolio preparation

- Think remains a continuous process objective (already strong).
- Control (MCI) and Connect (TA, including Friendly Hobbies / mentors / sponsors) are **working hypotheses**, not a declared season target.
- Innovate or Design remain alternatives if match evidence is stronger there.
- Portfolio: keep the coherent engineering story; add a judge-facing page index; page limits from **V0** (15 content pages, 15 MB), re-verify at Kickoff.

---

## Remaining coach decisions

1. File the YouTube watch URL for *Why Most FTC Teams Fail (And How Not To)* into [docs/references.md](docs/references.md).
2. Confirm first **scored** Nevada event (clinic vs 31 Oct league) — still open from the twelve-week integration.
3. Approve starter-bot fallback if G3/G5 fail.
4. After Kickoff V1 award tables: facilitate the 15-minute award-focus decision (do not treat Control/Connect as locked).
5. Approve any reopen of a G3 decision that would consume the 12–30 Oct runway.
6. Accommodations for student judging presentations (unchanged).
7. Competition enablement per RD001 (not automatic).

---

## Validation performed

- Internal links among new canonical docs and the templates they cite
- K001 agenda still **120** minutes (15+25+20+20+15+15+10)
- S001 / S002 Meeting A/B blocks still 120
- Clinic 10 Oct and league 31 Oct used as planning inputs; no new impossible freeze before G2/G3
- Preseason variance (P002–P005 actuals; P006 first movement, P007 dial-in + Kickoff prep, P008 FRC tour) not overwritten
- Twelve-week Pratt gates G1–G8 retained
- Future sessions not marked complete (K001/S001/S002 set to `scheduled`; other future bodies left as they were except content edits)
- `python tools/validation/validate_curriculum.py` run after edits

## Achievability (4 hours/week rookies)

The plan remains tight. It is honest: clinic is R0 plus stretch, league is R0–R2 (R3 if G3 held), advanced software is gated, and driver practice is a named 18-day window rather than a fictional month of only driving.
