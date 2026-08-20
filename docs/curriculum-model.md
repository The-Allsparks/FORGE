# Curriculum model

FORGE teaches one robot. The seven libraries are layers, not seven classes.

## Learning loop

Every session uses the same loop, adapted from the strongest student/mentor patterns in TRACE, HELM, ECHO, AMPER, MIMIC, and BEACON:

1. Driving question
2. Small vocabulary set
3. Short mentor demonstration
4. Student implementation (build, wire, program, drive, or document)
5. Evidence collection
6. Deliberate failure injection
7. Student explain-back
8. Assessment
9. Portfolio artifact
10. Enablement-gate decision
11. Rollback exercise
12. Mentor notes

Students must observe, test, diagnose, or explain. Copying code without a visible result is not sufficient.

## Difficulty labels

| Label | Meaning |
| ----- | ------- |
| Foundation | First contact; vocabulary and observation |
| Developing | Students perform the work with coaching |
| Integration | Two or more systems on the same robot |
| Competition readiness | Evidence, rollback, and match procedure |

Mark activities, not people. Mixed-experience teams should pair across labels.

## Participation paths

Offer these roles inside the same session, then rotate:

- Mechanical
- Electrical
- Programming
- Drive team
- Documentation / portfolio

Do not isolate students permanently by discipline. Cross-training is scheduled in [learning-paths/cross-training.md](../learning-paths/cross-training.md).

## Meeting types

| Type | Purpose | Fixed blocks (minutes) |
| ---- | ------- | ---------------------- |
| A | Build and integrate | 10 + 75 + 25 + 10 = 120 |
| B | Test and practice | 10 + 35 + 55 + 20 = 120 |
| K | Kickoff / event-day workshop | 120, custom blocks listed in the session |

Teaching stays inside the blocks. A mentor demo is short and is followed by student work.

## Season phases (2026–2027)

Defined in [season/2026-2027-biobuzz/season-plan.md](../season/2026-2027-biobuzz/season-plan.md) and dated in `calendar.yaml`.

**Competition-one process** (adapted from Brogan M. Pratt's twelve-week FTC season plan): [season-process.md](../season/2026-2027-biobuzz/docs/season-process.md). Eight **decision gates** (G1–G8) protect software, driving, and judging time.

| Phase | Intent |
| ----- | ------ |
| Preseason | Strafer platform, driver control, TRACE habit, evidence templates, student goals |
| Kickoff | BIOBUZZ analysis; G1 Strategy gate; MVP and fallback |
| Compressed weeks 1–4 | Understand → compare → select → build (G1–G5) |
| Compressed weeks 5–7 | Tune → freeze → rehearse → League 1S/2S (G6–G8) |
| League development | Match evidence; Version 2 on Strafer/fixtures only |
| Adversity simulations | Failures, pit, inspection, bounded active behavior |
| Feature freeze | Mock competition; no new active features |
| State | Two or three evidence-supported improvements if advancing |

## Project teaching intent

Summaries only. Authoritative phase tables live in the project repos.

| Project | FORGE intent |
| ------- | ------------ |
| TRACE | First and always. Evidence, observability, diagnosis. Close every session with it. Do not let paperwork block robot work. |
| AMPER | Passive voltage/current. Connect electrical observations to behavior. No unvalidated automatic power limiting in competition. |
| MIMIC | Connect construction to states and limits. Controlled failure tests before protections go active. |
| ViDAR | Geometry, one camera, then game-relevant detection. Simulation first. Tie vision to a real robot need. |
| BEACON | Passive freshness and recovery vocabulary. Monitoring must not interfere with control. |
| HELM | Vocabulary → static trees → validation → observation → shadow. No chassis authority. Conventional auto remains. |
| ECHO | Cue design and driver workload off-robot first. Immediate mute. Competition-off until benefit is evidenced. |
| Pedro Pathing | Conventional autonomous ownership of chassis motion. |

Combined FTC stack acceptance is a FORGE gate, not a per-library README claim. See [stack-acceptance.md](stack-acceptance.md).

## Session contract

Copy [templates/session.md](../templates/session.md). Required headings are enforced by `tools/validation/validate_curriculum.py`.
