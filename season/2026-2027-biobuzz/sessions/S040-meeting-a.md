---
id: S040
title: "State preparation"
date: 2027-02-08
meeting_type: A
season_phase: state-prep
event_checkpoint: state-championship
status: complete
difficulty: Competition readiness
projects: [TRACE, PEDRO]
active_features: []
---

# S040 — State preparation

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S040 |
| Title | State preparation |
| Calendar date | 2027-02-08 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | If advancing; 25 January–20 February |
| Meeting type | A |
| Season phase | state-prep |
| Event checkpoint | state-championship |
| Difficulty | Competition readiness |

## Driving question

Which two or three evidenced improvements are worth State — and what do we refuse?

## Student-facing objective

Pick at most three improvements that already have evidence. Prioritize driving, auto, reliability, and judging. Refuse architecture rewrites, HELM execute, and ECHO match audio without evidence. Do not use State as the first combined-stack compile ([FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4)).

## Robot outcome

- Chosen list (≤3) and refused list in the notebook
- State candidate config (usually the tournament freeze plus the chosen deltas)
- Conventional auto still capable

## Prerequisites

- Advancement. If not advancing, convert to celebration / offseason notes and skip this plan
- State 19–20 February is a **planning input** — verify FIRST Nevada
- Tournament retrospective and dashboard
- [season-plan.md](../season-plan.md) State window

## Vocabulary

evidenced improvement · no broad architecture · refuse

## Safety concerns

- Same as freeze plus fatigue
- No last-minute untested actives
- Adult supervision for any chosen hardware change

## Required hardware

Robot as returned from tournament.

## Required software

Only chosen deltas — or none. TRACE still records.

## Preparation required before the meeting

Bring dashboard and tournament retrospective. Pre-write a rejected shiny idea so the opening is a decision.

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Two or three only; drive/auto/reliability/judging first; refuse architecture |
| 75 | Construction | The chosen mechanical reliability items (or none) |
| 25 | Integration | Only chosen software deltas; TRACE evidence plan; or judging Q&A if no software delta |
| 10 | Closeout | TRACE evidence, explain-back, dashboard, cleanup |

## Mentor demonstration

Show a rejected shiny idea (HELM execute, four-camera ViDAR, ECHO at State). Two minutes.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Chosen repairs |
| Electrical | Chosen electrical |
| Programming | Chosen tiny delta or none |
| Drive team | Will get Meeting B reps |
| Documentation | State story; refused list |

## Integrated build or test activity

Write the list of refused changes. Re-approve a chosen item only if it already meets the enablement ladder.

## Failure-injection scenario

Someone proposes HELM execute or ECHO match audio without evidence — refuse. Someone proposes adding FORGE as a Gradle dependency — refuse.

## Evidence to collect

- Chosen list (≤3) with evidence pointers
- Refused list
- Dashboard updates only for chosen items
- Confirmation that conventional auto still exists

## Student explain-back questions

1. What are the two or three changes?
2. What is refused?
3. Conventional auto?
4. Rollback if a chosen delta fails at State?

## Assessment or exit check

Lists exist. Robot still conventional-auto capable. No broad unfreeze.

## Portfolio or engineering-notebook artifact

State plan page: chosen, refused, judging story. Run [portfolio-validation.md](../../../templates/portfolio-validation.md) state-ready gate if advancing.

## Competition enablement impact

Do not broadly unfreeze. Re-approve only the chosen items if they meet the ladder. Combined stack still requires Hub evidence, not hope.

## Rollback procedure

Tournament frozen config is the fallback. Printed pit card still applies.

## Cleanup requirements

Robot safe; refused-list posted so the next meeting does not reopen it.

## Next-session preparation

Meeting B templates through State: drive, auto, judging.

## Hardware-unavailable fallback

Planning only. Judging Q&A. Refused list still written.

## Robot-unavailable simulation option

Judging Q&A and paper auto walk.

## Links to authoritative project documentation

- [season-plan.md](../season-plan.md)
- [calendar.yaml](../calendar.yaml)
- [docs/safety-and-enablement.md](../../../docs/safety-and-enablement.md)
- [docs/stack-acceptance.md](../../../docs/stack-acceptance.md)
- [readiness-dashboard.md](../readiness-dashboard.md)
- [projects/trace.md](../../../projects/trace.md)
- [projects/pedro-pathing.md](../../../projects/pedro-pathing.md)

## Mentor notes

Contingent on advancement. Verify State dates. Avoid architecture. Sibling P0 merges are not a reason to unfreeze.
