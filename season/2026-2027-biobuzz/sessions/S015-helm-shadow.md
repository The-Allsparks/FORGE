---
id: S015
title: "HELM shadow recommendations"
date: 2026-10-22
meeting_type: B
season_phase: reliability-sprint
event_checkpoint: league-1s-2s
status: outline
difficulty: Developing
projects: [HELM, PEDRO, TRACE]
active_features: []
---
# S015 — HELM shadow recommendations

## Session identity
| Field | Value |
| ----- | ----- |
| Session ID | S015 |
| Title | HELM shadow recommendations |
| Calendar date | 2026-10-22 (planning input) |
| Relative week | Reliability sprint |
| Meeting type | B |
| Season phase | reliability-sprint |
| Event checkpoint | league-1s-2s |
| Difficulty | Developing |

## Driving question

If a selector suggested a different step, would we notice — without letting it drive?

## Student-facing objective

Compare a shadow recommendation to the conventional auto after driving reps. Library shadow API may refuse; then do the comparison on paper.

## Robot outcome

Unchanged. Shadow notes only.

## Prerequisites

S014 tree. HELM student path Phase 4 is not implemented — paper shadow is OK.

## Vocabulary

shadow · observe · conventional fallback

## Safety concerns

No bounded substitution. No execute.

## Required hardware

Robot for 55-minute reps.

## Required software

Helm.observe if present and safe; else notebook.

## Preparation required before the meeting

Bring S014 tree.

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Review auto logs; test goal: run conventional auto N times; note where a shadow would differ |
| 35 | Repair / tune / program | Auto tuning / repairs. HELM code only if observe-only. |
| 55 | Driving / auto reps | Auto and driver reps. Shadow discussion between reps, not instead of reps. |
| 20 | Closeout | Inspection, log review, explain-back, next steps, cleanup |

## Mentor demonstration

Observe record vs human strategy.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Repairs as needed |
| Electrical | Battery discipline |
| Programming | Observe or paper |
| Drive team | Reps |
| Documentation | Diff table |

## Integrated build or test activity

After three autos, fill: conventional did X; shadow would have said Y; we will still run X.

## Failure-injection scenario

Treat unknown vision as no piece — students must catch that.

## Evidence to collect

Diff table; auto times.

## Student explain-back questions

1. Did shadow change the robot?
2. Disable path?
3. Why keep conventional auto?
4. What evidence would be needed before authority?

## Assessment or exit check

Diff table complete. Autos run.

## Portfolio or engineering-notebook artifact

Shadow vs actual table.

## Competition enablement impact

HELM observe/shadow at most; competition disabled.

## Rollback procedure

Mode OFF; run Pedro auto.

## Cleanup requirements

Standard.

## Next-session preparation

S016 league prep. Unnumbered days: drive.

## Hardware-unavailable fallback

Paper autos walked.

## Robot-unavailable simulation option

Desktop observe tests.

## Links to authoritative project documentation

- [HELM student path](https://github.com/The-Allsparks/HELM/blob/main/docs/student-learning-path.md)
- [responsibility-boundaries.md](https://github.com/The-Allsparks/HELM/blob/main/docs/responsibility-boundaries.md)
- [projects/helm.md](../../../projects/helm.md)
- [projects/pedro-pathing.md](../../../projects/pedro-pathing.md)

## Mentor notes

If the API refuses shadow, that is correct behavior. Do not stub an executor.
