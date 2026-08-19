---
id: S014
title: "HELM intent-tree vocabulary"
date: 2026-10-30
meeting_type: B
season_phase: reliability-sprint
event_checkpoint: league-1s-2s
status: complete
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
| Calendar date | 2026-10-30 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | Reliability sprint |
| Meeting type | B |
| Season phase | reliability-sprint |
| Event checkpoint | league-1s-2s |
| Difficulty | Foundation |

## Driving question

Can we name the auto we already have as goals, tasks, timeouts, and fallbacks — without giving HELM any authority?

## Student-facing objective

Keep repairing the robot. On paper (and optional desktop `Helm.validate`), describe the **existing** conventional auto. HELM mode stays `OFF`. Pedro still moves the chassis.

## Robot outcome

- Unchanged control code path for matches
- Paper intent tree that matches the auto students can explain
- Optional validate errors discussed — not an executor

## Prerequisites

- Students can explain the S003 (or later) conventional auto
- [intent-trees.md](https://github.com/The-Allsparks/HELM/blob/main/docs/intent-trees.md)
- [mentor-guide.md](https://github.com/The-Allsparks/HELM/blob/main/docs/mentor-guide.md)
- [readiness-gates.md](https://github.com/The-Allsparks/HELM/blob/main/docs/readiness-gates.md) — treat authority as **not met**
- [safety.md](https://github.com/The-Allsparks/HELM/blob/main/docs/safety.md)

## Vocabulary

goal · task · timeout · fallback · validate · `OFF`

## Safety concerns

- No execute flags. Physical output is refused in the library; still do not practice "just enable it"
- HELM does not replace MIMIC, BEACON, AMPER, or Pedro
- Unknown vision is not "no game piece"

## Required hardware

- Robot for the 75-minute reliability/MVP work
- Paper or whiteboard for HELM

## Required software

- Optional HELM desktop validate
- Pedro/fallback auto remains what would run in a match
- TRACE records the real auto if installed — HELM does not need to be a sink yet

## Preparation required before the meeting

Print the current auto steps from the notebook. Clone HELM and run tests on one laptop if time.

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | HELM intent vocabulary; gates unmet; construction still wins; no execute |
| 35 | Repair / tune / program | Draft and encode the paper intent tree; optional `Helm.validate` setup |
| 55 | Driving / auto reps | Compare tree to actual auto and teleop during reps — not instead of reps |
| 20 | Closeout | Photo of tree; dashboard HELM ladder 1 disabled; explain-back; cleanup |

## Mentor demonstration

Refuse "just make it pick the best spike." That is later phases in the HELM student path. Two minutes.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Repairs |
| Electrical | Repairs |
| Programming | Paper tree / optional validate |
| Drive team | Confirm the auto they actually run |
| Documentation | Tree photo |

## Integrated build or test activity

For each auto step: name the goal, success, timeout, fallback. Mark a conceptual safe terminal using HELM safety language **without** claiming Phase 2 validation replaces hardware interlocks.

## Failure-injection scenario

"Pose confidence unknown — so there is no piece." Students must catch that ([HELM mentor guide](https://github.com/The-Allsparks/HELM/blob/main/docs/mentor-guide.md)).

## Evidence to collect

- Intent tree
- Validate errors if run
- Dashboard HELM: ladder 1, status disabled

## Student explain-back questions

1. How do we turn HELM off? (`OFF`; it was never in the match OpMode.)
2. Who overrides HELM?
3. Who moves the chassis?
4. Which readiness gates are unmet? (Point at the gates doc; do not argue with a stale "TRACE empty" row — TRACE exists, authority still is not approved.)

## Assessment or exit check

Tree matches the auto a non-programmer can explain. Robot repairs progressed.

## Portfolio or engineering-notebook artifact

Intent tree. Link HELM docs; do not copy season point values into FORGE or HELM core.

## Competition enablement impact

HELM stays **disabled**. Vocabulary only.

## Rollback procedure

Never added to the robot. Mode `OFF`. Run Pedro/fallback auto.

## Cleanup requirements

Robot disabled; papers photographed; no execute flags in TeamCode.

## Next-session preparation

S011 shadow — still no execute. Friday Meeting B: auto reps.

## Hardware-unavailable fallback

Paper tree of a walked auto.

## Robot-unavailable simulation option

HELM desktop tests plus paper tree.

## Links to authoritative project documentation

- [HELM README](https://github.com/The-Allsparks/HELM/blob/main/README.md)
- [Student path](https://github.com/The-Allsparks/HELM/blob/main/docs/student-learning-path.md)
- [Mentor guide](https://github.com/The-Allsparks/HELM/blob/main/docs/mentor-guide.md)
- [Intent trees](https://github.com/The-Allsparks/HELM/blob/main/docs/intent-trees.md)
- [Readiness gates](https://github.com/The-Allsparks/HELM/blob/main/docs/readiness-gates.md)
- [Safety](https://github.com/The-Allsparks/HELM/blob/main/docs/safety.md)
- [Season strategy](https://github.com/The-Allsparks/HELM/blob/main/docs/season-strategy.md)
- [projects/helm.md](../../../projects/helm.md)
- [projects/pedro-pathing.md](../../../projects/pedro-pathing.md)

## Mentor notes

Gates file may still say TRACE was empty. Treat **authority** as not met regardless. Do not skip to execute because the paper tree looks tidy.
