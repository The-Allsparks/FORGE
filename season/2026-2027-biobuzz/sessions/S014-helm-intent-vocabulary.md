---
id: S014
title: "HELM intent-tree vocabulary"
date: 2026-10-20
meeting_type: A
season_phase: reliability-sprint
event_checkpoint: league-1s-2s
status: outline
difficulty: Foundation
projects: [HELM, PEDRO, TRACE]
active_features: []
---
# S014 — HELM intent-tree vocabulary

## Session identity
| Field | Value |
| ----- | ----- |
| Session ID | S014 |
| Title | HELM intent-tree vocabulary |
| Calendar date | 2026-10-20 (planning input) |
| Relative week | Reliability sprint |
| Meeting type | A |
| Season phase | reliability-sprint |
| Event checkpoint | league-1s-2s |
| Difficulty | Foundation |

## Driving question

Can we name the auto we already have as goals, tasks, timeouts, and fallbacks — without giving HELM authority?

## Student-facing objective

Paper intent tree of the conventional auto. Construction continues. HELM mode OFF.

## Robot outcome

Unchanged control. Tree on paper / `Helm.validate` offline if available.

## Prerequisites

Students can explain the conventional auto. [intent-trees.md](https://github.com/The-Allsparks/HELM/blob/main/docs/intent-trees.md), [mentor-guide.md](https://github.com/The-Allsparks/HELM/blob/main/docs/mentor-guide.md).

## Vocabulary

goal · task · timeout · fallback · validate

## Safety concerns

No execute flags. Physical output refused in library; still do not practice 'just enable it.'

## Required hardware

Robot for construction; paper for HELM.

## Required software

HELM desktop validate optional; Pedro auto remains the runner.

## Preparation required before the meeting

Print the current auto steps.

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | HELM is last; gates unmet; construction still wins |
| 75 | Construction | Reliability repairs / MVP remaining. |
| 25 | Integration | Encode paper tree; optional Helm.validate; TRACE not required to be a HELM sink yet. |
| 10 | Closeout | TRACE evidence, explain-back, dashboard, cleanup |

## Mentor demonstration

Refuse 'pick the best spike.' That is later phases.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Repairs |
| Electrical | Repairs |
| Programming | Paper tree / validate |
| Drive team | Confirm the auto they actually run |
| Documentation | Tree photo |

## Integrated build or test activity

Name success/failure for each step. Mark safe terminal conceptually ([HELM safety](https://github.com/The-Allsparks/HELM/blob/main/docs/safety.md)) without claiming Phase 2 replaces MIMIC.

## Failure-injection scenario

Unknown pose confidence — tree must not assume a piece is absent ([HELM mentor guide](https://github.com/The-Allsparks/HELM/blob/main/docs/mentor-guide.md)).

## Evidence to collect

Tree; validate errors if run; dashboard HELM ladder 1.

## Student explain-back questions

1. How do we turn HELM off?
2. Who overrides HELM?
3. Who moves the chassis?
4. Which readiness gates are unmet?

## Assessment or exit check

Tree matches the auto students can drive/explain.

## Portfolio or engineering-notebook artifact

Intent tree.

## Competition enablement impact

HELM stays disabled. Vocabulary only.

## Rollback procedure

Never added to robot. Mode OFF.

## Cleanup requirements

Standard.

## Next-session preparation

S015 shadow — still no execute.

## Hardware-unavailable fallback

Paper tree of a walked auto.

## Robot-unavailable simulation option

Desktop HELM tests.

## Links to authoritative project documentation

- [HELM README](https://github.com/The-Allsparks/HELM/blob/main/README.md)
- [Student path](https://github.com/The-Allsparks/HELM/blob/main/docs/student-learning-path.md)
- [Intent trees](https://github.com/The-Allsparks/HELM/blob/main/docs/intent-trees.md)
- [Readiness gates](https://github.com/The-Allsparks/HELM/blob/main/docs/readiness-gates.md)
- [Safety](https://github.com/The-Allsparks/HELM/blob/main/docs/safety.md)
- [projects/helm.md](../../../projects/helm.md)

## Mentor notes

Gates file may still say TRACE was empty — treat authority as not met regardless.
