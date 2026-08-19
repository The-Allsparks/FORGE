---
id: S018
title: "Tournament feature freeze"
date: 2027-01-13
meeting_type: A
season_phase: feature-freeze
event_checkpoint: league-tournament
status: complete
difficulty: Competition readiness
projects: [TRACE, PEDRO]
active_features: []
---

# S018 — Tournament feature freeze

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S018 |
| Title | Tournament feature freeze |
| Calendar date | 2027-01-13 (planning input; Meeting A) |
| Relative week | 11–23 January window |
| Meeting type | A |
| Season phase | feature-freeze |
| Event checkpoint | league-tournament |
| Difficulty | Competition readiness |

## Driving question

What is frozen, and how do we inspect, judge, and still practice?

## Student-facing objective

Declare a feature freeze. Practice inspect and a short judging story. Keep conventional auto. No new active features unless a **critical demonstrated problem** is already on the dashboard. Freeze is not combined-stack acceptance ([FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4)).

## Robot outcome

- Frozen config tagged in the notebook
- Practice-inspect notes
- Judging one-pager (problem, test, evidence — not seven logos)

## Prerequisites

- Tournament 22–23 January is a **planning input** — verify FIRST Nevada
- [pit-and-inspection.md](../pit-and-inspection.md)
- [learning-paths/documentation.md](../../../learning-paths/documentation.md)
- Official inspection list when published: [2026–2027 event resources](https://ftc-resources.firstinspires.org/ftc/archive/2027/event)
- Open-bug list (most will wait)

## Vocabulary

feature freeze · critical demonstrated problem · frozen

## Safety concerns

- No experimental flags
- No HELM authority
- No ECHO match audio unless already approved with evidence (default: off)
- Inspection hazards: size, sharp edges, batteries

## Required hardware

Competition robot; inspection tools; printed dashboard and pit page.

## Required software

Frozen OpModes. TRACE may still record. Optionals match frozen dashboard statuses.

## Preparation required before the meeting

List of open bugs. Most wait. Write freeze rules on the board: no new actives; exception requires a demonstrated match-blocking problem and mentor + driver agreement.

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Freeze rules; what counts as critical; HELM does not drive |
| 75 | Construction | Inspection items; pit; mechanical reliability only |
| 25 | Integration | Judging dry-run (short) + config tag; TRACE still records |
| 10 | Closeout | TRACE evidence, explain-back, dashboard frozen, cleanup |

## Mentor demonstration

One-minute story for judges: problem, test, evidence — not seven library logos.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Inspect |
| Electrical | Inspect |
| Programming | Tag freeze in notebook; no new adapters |
| Drive team | Short drive only if time — more on Meeting B templates |
| Documentation | Judging one-pager |

## Integrated build or test activity

Walk practice inspect. Ten-minute judging answers. Tag the frozen config (which OpModes, which flags).

## Failure-injection scenario

Judge asks “does HELM drive the robot?” Correct answer is no unless the dashboard says otherwise (it should not).

## Evidence to collect

- Freeze tag
- Inspection notes
- Judging one-pager
- Dashboard statuses marked `frozen` where applicable

## Student explain-back questions

1. What is frozen?
2. What is the exception process?
3. Conventional auto?
4. Rollback still printed?

## Assessment or exit check

Freeze written. Inspection attempted. Robot still conventional-auto capable.

## Portfolio or engineering-notebook artifact

Judging one-pager plus freeze tag. Run [portfolio-validation.md](../../../templates/portfolio-validation.md) tournament-ready gate.

## Competition enablement impact

Frozen statuses on the dashboard. Do not unfreeze for cleverness. Combined stack remains an open epic unless #4 is checked with Hub evidence.

## Rollback procedure

Still required and printed. Frozen config is the known-good. DS stop first.

## Cleanup requirements

Robot safe; inspection notes filed; no leftover experimental OpModes selected on the DS.

## Next-session preparation

Meeting B templates: mock competition reps through tournament.

## Hardware-unavailable fallback

Judging and freeze on paper. Packing list review.

## Robot-unavailable simulation option

Q&A practice for judging.

## Links to authoritative project documentation

- [learning-paths/documentation.md](../../../learning-paths/documentation.md)
- [templates/judging-one-pager.md](../../../templates/judging-one-pager.md)
- [readiness-dashboard.md](../readiness-dashboard.md)
- [docs/safety-and-enablement.md](../../../docs/safety-and-enablement.md)
- [docs/stack-acceptance.md](../../../docs/stack-acceptance.md)
- [pit-and-inspection.md](../pit-and-inspection.md)
- [projects/trace.md](../../../projects/trace.md)
- [projects/pedro-pathing.md](../../../projects/pedro-pathing.md)

## Mentor notes

22–23 January tournament — verify. Do not unfreeze because a library merged a P0. Sibling CI is not combined Hub acceptance.
