# Pratt crosswalk — twelve weeks to FORGE sessions

Maps Brogan M. Pratt's [*A 12 Week FTC Season Plan That Actually Works*](https://www.youtube.com/playlist?list=PLRHdgFNRLyaM6TmNVVHKqVnnyntDDYDNt) to The Allsparks FORGE sessions. Pratt does not endorse FORGE.

**Canonical session files only** — `{ID}-meeting-{type}.md` referenced by [calendar.yaml](../calendar.yaml). Legacy topic-named duplicates are not authoritative.

## Compression overview

| Pratt week | Pratt focus | Allsparks compressed phase | FORGE gate |
| ---------- | ----------- | -------------------------- | ---------- |
| — | (not in Pratt) | Preseason | — |
| 1 | Rules, strategy, ideation, crude prototype | Post-Kickoff week 1 | G1 |
| 2 | Prototype robot, goals, outreach | Post-Kickoff week 1–2 | G1 → G2 |
| 3 | Comparative mechanism prototyping | Post-Kickoff week 2 | G2 |
| 4 | Modular architecture, interfaces | Post-Kickoff week 3 | G3 |
| 5 | Mechanism selection, vision POC | Post-Kickoff week 3 | G3 |
| 6 | Pivot deadline, architecture commit | Post-Kickoff week 3–4 | G3, G4 |
| 7 | Robust module construction | Post-Kickoff week 4 | G4, G5 |
| 8 | Mech/electrical integration | Post-Kickoff week 4 | G5 |
| 9 | Stable handoff, tuning, pathing | Post-Kickoff week 5 | G6 |
| 10 | Auto, driver automation, portfolio | Post-Kickoff week 5 | G6 |
| 11 | Reliability, mock judging, freeze | Post-Kickoff week 6 | G7 |
| 12 | Full match, pit, logistics | Post-Kickoff week 6–7 | G7, G8 |

## Session mapping — preseason

| Session | Date | Pratt equivalent | Compressed phase | Primary deliverable |
| ------- | ---- | ---------------- | ---------------- | ------------------- |
| P001 | 2026-08-17 | — | Preseason | Parts org, safety, sponsor cards started (**complete**) |
| P002 | 2026-08-19 | — | Preseason | Sponsor cards; Strafer chassis start (**scheduled**) |
| P003 | 2026-08-24 | — | Preseason | Rolling drivetrain |
| P004 | 2026-08-26 | — | Preseason | Electrical foundation |
| P005 | 2026-08-31 | — | Preseason | Bring-up, TRACE habit |
| P006 | 2026-09-04 | — | Preseason | Driver baseline |
| P007 | 2026-09-07 | Pratt w2 mechanism lab (early) | Preseason | Reusable mechanism experiments |
| P008 | 2026-09-11 | — | Preseason | Kickoff readiness; student goals baseline |

## Session mapping — competition one (through League 1S/2S)

| Session | Date | Pratt weeks | Compressed week | Gate | Session focus (calendar title) |
| ------- | ---- | ----------- | --------------- | ---- | ------------------------------ |
| K001 | 2026-09-12 | 1 | Week 1 | G1 | BIOBUZZ analysis; MVP; ideation |
| S001 | 2026-09-14 | 1 | Week 1 | G1 | Strategy execution; crude prototypes |
| S002 | 2026-09-18 | 1–2 | Week 1 | G1 | Ideation scale-up; low-fi prototypes |
| S003 | 2026-09-21 | 2–3 | Week 2 | G2 | Comparative mechanism tests |
| S004 | 2026-09-25 | 3 | Week 2 | G2 | Starter vs alternative evidence |
| S005 | 2026-09-28 | 4–5 | Week 3 | G3 | Architecture selection; interfaces |
| S006 | 2026-10-02 | 5–6 | Week 3 | G3 | Pivot deadline; CAD/BOM authorization |
| S007 | 2026-10-05 | 6–7 | Week 4 | G4 | Module fabrication (incremental) |
| S008 | 2026-10-09 | 7–8 | Week 4 | G4–G5 | Integration; wiring; clinic prep |
| — | 2026-10-10 | 8 | Week 4 | G5 | **Clinic/scrimmage** — data collection |
| S009 | 2026-10-12 | 8–9 | Week 5 | G5–G6 | Clinic retro; stable handoff start |
| S010 | 2026-10-16 | 9–10 | Week 5 | G6 | Minimum auto; mechanism tuning |
| S011 | 2026-10-19 | 9–10 | Week 5 | G6 | Reliability testing; portfolio draft |
| S012 | 2026-10-23 | 10–11 | Week 5–6 | G6–G7 | Driver automation (if earned); freeze prep |
| S013 | 2026-10-26 | 11 | Week 6 | G7 | Feature freeze; mock judging |
| S014 | 2026-10-30 | 11–12 | Week 6 | G7 | Full-match simulation; pit rehearsal |
| — | 2026-10-31 | 12 | Week 7 | G8 | **League 1S/2S** — competition simulation |

## Session mapping — post–League 1S/2S (FORGE preserved)

Pratt's series focuses on first competition. FORGE **retains** extended season phases:

| Session range | FORGE phase | Intent |
| ------------- | ----------- | ------ |
| S015–S023 | league-development | Match evidence; calibration; Version 2 on Strafer/fixtures only |
| S024–S031 | adversity-simulations | Failure drills; full-match reps |
| S032–S034, E004 | feature-freeze | Tournament mock; freeze |
| S036–S042, E005 | state-prep | Evidence-supported improvements if advancing |

Retitle cadence sessions in `calendar.yaml` after each event retrospective — do not rename files.

## Library sessions vs gates

Library deep-dives (ViDAR, BEACON, MIMIC, ECHO, HELM) occur **only when** the G3 software contract and K001 mapping table say yes. Default post-G3 schedule:

| Session | Library tie-in | Enablement |
| ------- | -------------- | ---------- |
| S003–S004 | TRACE, passive AMPER, MIMIC paper states | Off/passive |
| S005–S007 | MIMIC on hardware; BEACON passive | Controlled |
| S008 | ViDAR only if G3 requires | Observe-only default |
| S010 | ECHO off-robot lab | Competition-off |
| S012 | HELM vocabulary/shadow | No execute |
| S014+ | Per dashboard | Per [safety-and-enablement.md](../../../docs/safety-and-enablement.md) |

## Issues linked to gates

| Issue | Title | Gate / phase |
| ----- | ----- | -------------- |
| [#23](https://github.com/The-Allsparks/FORGE/issues/23) | Fill S015–S031 post-league weekly goals | post–G8 |
| [#24](https://github.com/The-Allsparks/FORGE/issues/24) | Verify BIOBUZZ award/portfolio limits | Kickoff → G8 |
| [#25](https://github.com/The-Allsparks/FORGE/issues/25) | Assign checklist owners at G8 | G8 |
| [#26](https://github.com/The-Allsparks/FORGE/issues/26) | Student learning-goal baselines at P008 | Preseason → G8 |
| [#27](https://github.com/The-Allsparks/FORGE/issues/27) | Sparkee module docs after G3 | G3 → G5 |
| [#28](https://github.com/The-Allsparks/FORGE/issues/28) | Retime S005–S011 agendas | weeks 3–5 |
| [#29](https://github.com/The-Allsparks/FORGE/issues/29) | Archive legacy duplicate sessions | maintenance |

Full report: [pratt-integration-report.md](../pratt-integration-report.md).

## Maintainer notes

- Add optional front matter `compressed_week:` and `forge_gate:` to sessions when updating content — not enforced by validator today.
- After Kickoff, mentors update `calendar.yaml` titles to match actual mechanism names — keep IDs stable.
- If League 1S/2S date moves, shift gate target dates in [decision-gates.md](decision-gates.md) and this table together.
