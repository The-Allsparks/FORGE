# Pratt integration report — FORGE 2026–2027 BIOBUZZ

**Date:** 19 August 2026  
**Scope:** Incorporate Brogan M. Pratt's twelve-week FTC season process as a compressed, evidence-driven cycle for The Allsparks (FTC 36117).

**Attribution:** Adapted from [Brogan M. Pratt, *A 12 Week FTC Season Plan That Actually Works*](https://www.youtube.com/playlist?list=PLRHdgFNRLyaM6TmNVVHKqVnnyntDDYDNt) and [final-week video](https://www.youtube.com/watch?v=Y4K540aCR0E). Pratt does not endorse FORGE or The Allsparks. See [docs/references.md](docs/references.md).

---

## Files and plans reviewed

| Area | Paths |
| ---- | ----- |
| Season core | `season-plan.md`, `calendar.yaml`, `README.md`, `kickoff-replan-guide.md`, `readiness-dashboard.md`, `pit-and-inspection.md` |
| Preseason docs | `docs/preseason-kickoff-gate.md`, `docs/preseason-software-allocation.md` |
| Sessions | P001–P008, K001, S001–S042, E004/E005 (72 files in `sessions/`; 52 canonical) |
| Architecture | `docs/architecture.md`, `docs/curriculum-model.md`, `docs/stack-acceptance.md`, `docs/safety-and-enablement.md`, `docs/evidence-model.md`, `docs/award-and-portfolio-traceability.md` |
| Templates | All 17 existing + new prototype, gate, student goal, competition checklists |
| Assessments | `assessments/readiness/RD001-competition-approval.md`, rubrics |
| Validation | `tools/curriculum-manifest.json`, `tools/validation/validate_curriculum.py` |
| GitHub issues | FORGE #2, #4, #11–#20 (closed portfolio workflow) |

---

## Existing FORGE elements preserved

- **52-session calendar** with P001–P008, K001, S001–S042, E004/E005 — IDs, dates, filenames unchanged
- **P001 complete record:** parts organization, safety presentation, sponsor cards started
- **P002 scheduled record:** sponsor cards + Strafer chassis (meeting not yet held)
- **Meeting A/B 120-minute blocks** (75 build / 55 drive-auto)
- **Priority order:** working robot → mechanisms → driving → conventional auto → evidence → advanced autonomy
- **FORGE#4** combined stack acceptance; **FORGE#2** robot repo block
- **Enablement ladder** and library ownership (Pedro chassis, HELM no authority)
- **Eight FORGE season phases** after competition one (league-development through state-prep)
- **Portfolio workflow** (#11–#20 implemented), decision/failure/evidence templates
- **Preseason Strafer goal** and mechanism lab (P007) — not speculative BIOBUZZ tower
- **Event retrospectives**, clinic test card, pit rollback

---

## Changes made

### New documentation

| File | Purpose |
| ---- | ------- |
| [docs/season-process.md](docs/season-process.md) | Compressed phase model, Pratt twelve-week reference, software/driver/outreach protections |
| [docs/decision-gates.md](docs/decision-gates.md) | G1–G8 full definitions, acceptance criteria, fallbacks |
| [docs/pratt-crosswalk.md](docs/pratt-crosswalk.md) | Pratt week ↔ session ↔ gate mapping |
| [docs/modular-architecture.md](docs/modular-architecture.md) | Sparkee module contract |
| [docs/two-platform-strategy.md](docs/two-platform-strategy.md) | Strafer / Sparkee / starter / fixture strategy |
| [docs/references.md](docs/references.md) | Pratt citations and adaptation table |

### New templates

| File | Purpose |
| ---- | ------- |
| [templates/prototype-test-record.md](../../templates/prototype-test-record.md) | Standardized prototype/test evidence |
| [templates/gate-review.md](../../templates/gate-review.md) | Gate pass/fail record |
| [templates/student-learning-goal.md](../../templates/student-learning-goal.md) | Personal learning goals |
| [templates/student-progress-review.md](../../templates/student-progress-review.md) | Periodic goal review |
| [templates/competition/*](../../templates/competition/) | 17 competition-readiness checklists |

### Updated files

| File | Change |
| ---- | ------ |
| `season-plan.md` | Pratt attribution, gate summary, compressed weeks 1–7, preserved Nov–Feb phases |
| `calendar.yaml` | S001–S014 titles, `compressed_week`, `forge_gate`; cadence intent text |
| `kickoff-replan-guide.md` | G1 outputs, Pratt citation, gate fallbacks |
| `README.md` | Process links, crosswalk, competition checklists |
| `docs/curriculum-model.md` | Compressed phases in season table |
| `sessions/S001–S014` | Front matter + driving questions/objectives aligned to compressed phases |
| `sessions/P008` | Student learning goal baselines added |
| `tools/update_compressed_sessions.py` | Maintainer script for session alignment |

### Not changed (deferred to issues)

- 20 legacy topic-named session duplicates (content merge/archive)
- S015–S031 generic cadence session **bodies** (titles remain; fill after League 1S/2S retro)
- `curriculum-manifest.json` optional enforcement of `compressed_week` / `forge_gate`
- Legacy library-first agendas inside S005–S011 **activity blocks** (objectives updated; mentors retime activities to gate focus)

---

## Pratt original vs Allsparks adaptation

| Topic | Pratt | Allsparks |
| ----- | ----- | --------- |
| Duration | 12 weeks post-Kickoff | 6–7 weeks to League 1S/2S; 12 weeks preserved as reference |
| Preseason | Minimal | P001–P008 Strafer, evidence, goals, sponsor stewardship |
| Ideation | Hundreds of sketches | 60–100 across four students |
| Mechanism modules | ~4 (DECODE example) | BIOBUZZ-derived module set at G3 |
| Two robots | Full programming + prototype chassis | Strafer platform + starter fallback + fixtures |
| Software | General progression | MVP stack with FORGE#4 enablement gates |
| Week 3 end | Stop unrestricted exploration | G2 Prototype evidence gate |
| Week 5 | Mechanism direction | Absorbed into G3 (week 3 compressed) |
| Week 6 | Pivot deadline | G3 pivot deadline |
| Week 8 | Mech/electrical done | G5 (week 4 compressed) |
| Week 9 | Software handoff | G6 (week 5) |
| Week 11 | Feature freeze | G7 (week 6) |
| Week 12 | Drivers, pit, judging | G7–G8 (weeks 6–7) |
| Post-first-comp | Implied | FORGE S015–S042 phases retained |

Full table: [docs/references.md](docs/references.md).

---

## Complete compressed season timeline

| When | Phase | Sessions | Gate |
| ---- | ----- | -------- | ---- |
| through 11 Sep 2026 | Preseason | P001–P008 | — |
| 12 Sep 2026 | Kickoff | K001 | G1 start |
| 14–20 Sep | Week 1 — Understand and diverge | S001, S002 | G1 |
| 21–27 Sep | Week 2 — Test and compare | S003, S004 | G2 |
| 28 Sep – 4 Oct | Week 3 — Select and commit | S005, S006 | G3 |
| 5–11 Oct | Week 4 — Build and integrate | S007, S008, clinic 10 Oct | G4, G5 |
| 12–25 Oct | Week 5 — Tune and validate | S009–S012 | G6 |
| 26–30 Oct | Week 6 — Freeze and rehearse | S013, S014 | G7 |
| 31 Oct 2026 | Week 7 — Competition simulation | League 1S/2S | G8 |
| Nov 2026 – Feb 2027 | League / adversity / freeze / state | S015–S042 | Event-driven |

---

## Decision gates — acceptance criteria (summary)

See [docs/decision-gates.md](docs/decision-gates.md) for full inputs, evidence, fallbacks, and blocks.

| Gate | Pass requires (summary) |
| ---- | ------------------------ |
| G1 | Strategy matrix, MVP, risk register, ≥1 crude prototype, starter fallback |
| G2 | ≥2 prototype records (≥3 trials), comparative table, exploration stop |
| G3 | Architecture, interfaces, CAD/BOM, pivot deadline, software contract |
| G4 | Freeze on new modules without review |
| G5 | Integrated robot, modules under software control, wiring complete |
| G6 | Stable teleop, minimum auto or teleop-only declared, portfolio draft |
| G7 | Feature freeze, mock judging, full-match sim |
| G8 | RD001 review, checklists rehearsed, packed pit |

---

## Session-to-phase mapping

Authoritative table: [docs/pratt-crosswalk.md](docs/pratt-crosswalk.md).

---

## New and modified GitHub issues

Created during this integration (see repo for numbers):

| Issue | Title | Phase | Blocks |
| ----- | ----- | ----- | ------ |
| [#29](https://github.com/The-Allsparks/FORGE/issues/29) | Archive or merge 20 legacy duplicate session files | maintenance | — |
| [#23](https://github.com/The-Allsparks/FORGE/issues/23) | Fill S015–S031 cadence sessions with post-league weekly goals | league-development | — |
| [#24](https://github.com/The-Allsparks/FORGE/issues/24) | Verify BIOBUZZ award and portfolio limits after Kickoff | kickoff | G8 templates |
| [#25](https://github.com/The-Allsparks/FORGE/issues/25) | Assign competition checklist owners and rehearse at G8 | week 6 | G8 |
| [#26](https://github.com/The-Allsparks/FORGE/issues/26) | Record student learning-goal baselines (P008) | preseason | G1 story |
| [#27](https://github.com/The-Allsparks/FORGE/issues/27) | Populate Sparkee module docs after G3 | week 3 | G5 |
| [#28](https://github.com/The-Allsparks/FORGE/issues/28) | Retime S005–S011 agenda blocks to gate-first activities | week 3–5 | Session fidelity |

---

## Risks and unresolved schedule conflicts

| Risk | Mitigation |
| ---- | ---------- |
| League 1S/2S before 31 Oct | Shift gate dates in `decision-gates.md` and `calendar.yaml` together |
| FORGE#2 robot repo still blocked | Shop build proceeds; Hub compile evidence deferred; software on local TeamCode |
| S005–S011 agendas still mention library labs | Objectives gate-first; mentors prioritize prototype/build per compressed week |
| 6–7 weeks may be insufficient for custom + full stack | Starter-bot fallback at every gate; MVP software contract |
| Four students vs build demand | Rotating roles; pairs; gate fallbacks cut scope |
| Legacy duplicate sessions | Issue tracked; canonical files only in calendar |
| First competition may be clinic (10 Oct) not league | Treat clinic as G5 data collection; G8 may move to clinic if that is first scored event — **coach approval** |

---

## BIOBUZZ facts awaiting Kickoff / rules publication

- Game piece geometry and materials
- Scoring values and ranking points
- Autonomous start positions and requirements
- Size and weight limits (2026–2027)
- Portfolio page limits and format
- Judging presentation duration
- Pit dimensions and inspection checklist (2026–2027)
- Official starter-bot design for BIOBUZZ
- Sparkee module count and names

All marked **unverified** in templates until official FIRST materials publish.

---

## Items requiring coach approval

1. Confirm first **scored** Nevada event date (clinic vs 31 Oct league)
2. Approve gate date shifts if FIRST Nevada calendar changes
3. Approve starter-bot fallback if G3/G5 fail
4. Approve competition enablement per RD001 (not automatic from curriculum)
5. Approve outreach activity selection (one sustained vs many events)
6. Accommodations for student judging presentations

---

## Direct links

### Process

- [docs/season-process.md](docs/season-process.md)
- [docs/decision-gates.md](docs/decision-gates.md)
- [docs/pratt-crosswalk.md](docs/pratt-crosswalk.md)
- [docs/references.md](docs/references.md)
- [season-plan.md](season-plan.md)
- [kickoff-replan-guide.md](kickoff-replan-guide.md)

### Templates

- [templates/prototype-test-record.md](../../templates/prototype-test-record.md)
- [templates/gate-review.md](../../templates/gate-review.md)
- [templates/student-learning-goal.md](../../templates/student-learning-goal.md)
- [templates/competition/](../../templates/competition/)

### Preserved session records

- [sessions/P001-meeting-a.md](sessions/P001-meeting-a.md) — **complete**
- [sessions/P002-meeting-s.md](sessions/P002-meeting-s.md) — **scheduled**

### This week

- [sessions/P002-meeting-s.md](sessions/P002-meeting-s.md)
- [readiness-dashboard.md](readiness-dashboard.md)

---

## Validation

Run: `python tools/validation/validate_curriculum.py`

After adding this report, internal link from `pratt-crosswalk.md` resolves. External link warnings may occur (GitHub rate limits) — not merge blockers per prior practice.
