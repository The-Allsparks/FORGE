---
id: S014
title: Post-Kickoff week 6 — full-match simulation and pit rehearsal
date: 2026-10-30
meeting_type: B
season_phase: reliability-sprint
event_checkpoint: league-1s-2s
status: complete
difficulty: Foundation
projects:
- HELM
- PEDRO
- TRACE
active_features: []
compressed_week: 6
forge_gate: G7
---

# S014 — HELM intent-tree vocabulary

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S014 |
| Title | Post-Kickoff week 6 — full-match simulation and pit rehearsal |
| Calendar date | 2026-10-30 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | Compressed week 6 (G7–G8 prep) |
| Meeting type | B |
| Season phase | reliability-sprint |
| Event checkpoint | league-1s-2s |
| Forge gate | G7 |
| Difficulty | Foundation |

## Driving question

Can we run a full 2½-minute match and pit cycle under pressure?

## Student-facing objective

Students run complete match simulations (nonideal conditions where safe), rehearse pit checklists, timed battery change, prep G8 readiness.

## Robot outcome

- Full-match simulation completed
- Pre/post-match checklists timed
- Pit packing walkthrough
- G8 prep or RD001 draft


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
| 10 | Opening | Full 2½-minute match simulation rules; pit roles; no elective changes |
| 35 | Repair / tune / program | Final P0 fixes only; verify [owner-assignment.md](../../../templates/competition/owner-assignment.md); timed battery change |
| 55 | Driving reps | Complete match sims under nonideal conditions (congestion, failed auto recovery where safe) |
| 20 | Closeout | Pre/post-match checklists timed; pit packing walkthrough; G8 / [RD001](../../../assessments/readiness/RD001-competition-approval.md) prep |

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

- [docs/season-process.md](../docs/season-process.md)
- [docs/decision-gates.md](../docs/decision-gates.md)
- [docs/pratt-crosswalk.md](../docs/pratt-crosswalk.md)
- [prototype-test-record.md](../../../templates/prototype-test-record.md)
- [gate-review.md](../../../templates/gate-review.md)
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
