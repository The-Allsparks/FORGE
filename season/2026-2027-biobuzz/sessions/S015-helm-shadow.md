---
id: S015
title: "HELM shadow recommendations"
date: 2026-10-22
meeting_type: B
season_phase: reliability-sprint
event_checkpoint: league-1s-2s
status: complete
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
| Calendar date | 2026-10-22 (planning input; Thursday Meeting B) |
| Relative week | Reliability sprint |
| Meeting type | B |
| Season phase | reliability-sprint |
| Event checkpoint | league-1s-2s |
| Difficulty | Developing |

## Driving question

If a selector suggested a different step, would we notice — without letting it drive?

## Student-facing objective

Spend 55 minutes on conventional auto and driver reps. Between reps, compare a **shadow** recommendation to what Pedro (or the fallback auto) actually did. If the HELM shadow API refuses — expected — do the comparison on paper from the S014 tree. HELM does not command motors. Combined-stack Hub evidence is still [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4), not this session.

## Robot outcome

- Unchanged match control path
- Shadow vs actual table in the notebook
- Auto repetition times recorded
- HELM competition status remains disabled

## Prerequisites

- S014 paper tree exists
- Students can explain the conventional auto
- [HELM student path](https://github.com/The-Allsparks/HELM/blob/main/docs/student-learning-path.md) — Phase 4 shadow may be unimplemented; paper is valid
- [responsibility-boundaries.md](https://github.com/The-Allsparks/HELM/blob/main/docs/responsibility-boundaries.md)
- [readiness-gates.md](https://github.com/The-Allsparks/HELM/blob/main/docs/readiness-gates.md) — authority **not met**

## Vocabulary

shadow · observe · conventional fallback · `OFF`

## Safety concerns

- No bounded substitution. No execute
- Unknown / stale vision is not “no game piece”
- Do not skip driving to debug a HELM adapter
- Desktop observe tests are not Control Hub budgets

## Required hardware

Robot for 55-minute reps; blocks or carpet per shop rules; charged batteries.

## Required software

Pedro/fallback auto. Optional `Helm.observe` if present **and** compile-safe without execute adapters. Else notebook only. TRACE records the real auto if installed.

## Preparation required before the meeting

Bring the S014 tree. One laptop with HELM tests if time. Printed disable: mode `OFF`; run Pedro auto.

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Review auto logs; test goal: run conventional auto N times; note where a shadow would differ |
| 35 | Repair / tune / program | Auto tuning and repairs. HELM code only if observe-only. No executor stubs. |
| 55 | Driving / auto reps | Auto and driver reps. Shadow discussion between reps, not instead of reps. |
| 20 | Closeout | Inspection, log review, explain-back, next steps, cleanup |

## Mentor demonstration

Observe record vs human strategy. Show a refused execute. Two minutes.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Repairs as needed |
| Electrical | Battery discipline |
| Programming | Observe or paper; never an executor |
| Drive team | Reps; say what the auto actually does |
| Documentation | Diff table |

## Integrated build or test activity

After three autos, fill: conventional did X; shadow would have said Y; we will still run X. If observe is unavailable, Y is from the paper tree.

## Failure-injection scenario

Treat unknown vision as no piece — students must catch that ([HELM mentor guide](https://github.com/The-Allsparks/HELM/blob/main/docs/mentor-guide.md)).

## Evidence to collect

- Shadow vs actual table
- Auto completion times
- Dashboard HELM: observe/shadow at most, competition **disabled**
- TRACE auto start/end if recording

## Student explain-back questions

1. Did the shadow change the robot?
2. Disable path? (`OFF`; not in the match OpMode.)
3. Why keep conventional auto?
4. What evidence would be required before any authority — and is combined stack acceptance done? (No, unless #4 is checked.)

## Assessment or exit check

Diff table complete. Autos actually run. No execute flags.

## Portfolio or engineering-notebook artifact

Shadow vs actual table. Link HELM docs; do not copy BIOBUZZ point values into FORGE.

## Competition enablement impact

HELM observe/shadow at most; competition disabled. Pedro still owns chassis motion.

## Rollback procedure

Mode `OFF`. Run the Pedro/fallback auto. DS stop remains the e-stop.

## Cleanup requirements

Robot disabled; healthy pack if a weak pack was used; no HELM in the match OpMode.

## Next-session preparation

S016 league prep. Unnumbered days: drive.

## Hardware-unavailable fallback

Paper autos walked. Diff table from a walked route vs the S014 tree.

## Robot-unavailable simulation option

Desktop observe tests plus paper. Say out loud that this is not Hub evidence.

## Links to authoritative project documentation

- [HELM student path](https://github.com/The-Allsparks/HELM/blob/main/docs/student-learning-path.md)
- [responsibility-boundaries.md](https://github.com/The-Allsparks/HELM/blob/main/docs/responsibility-boundaries.md)
- [readiness-gates.md](https://github.com/The-Allsparks/HELM/blob/main/docs/readiness-gates.md)
- [safety.md](https://github.com/The-Allsparks/HELM/blob/main/docs/safety.md)
- [projects/helm.md](../../../projects/helm.md)
- [projects/pedro-pathing.md](../../../projects/pedro-pathing.md)
- [docs/stack-acceptance.md](../../../docs/stack-acceptance.md)

## Mentor notes

If the API refuses shadow, that is correct behavior. Do not stub an executor. Do not treat this session as combined FTC-ready HELM.
