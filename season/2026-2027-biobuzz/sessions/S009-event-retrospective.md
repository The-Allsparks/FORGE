---
id: S009
title: "Clinic retrospective and reliability sprint"
date: 2026-10-12
meeting_type: A
season_phase: reliability-sprint
event_checkpoint: clinic
status: complete
difficulty: Integration
projects: [TRACE]
active_features: []
---

# S009 — Clinic retrospective and reliability sprint

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S009 |
| Title | Clinic retrospective and reliability sprint |
| Calendar date | 2026-10-13 (planning input; Tuesday Meeting A) |
| Relative week | First meeting after clinic |
| Meeting type | A |
| Season phase | reliability-sprint |
| Event checkpoint | clinic |
| Difficulty | Integration |

## Driving question

What broke, what we measured, and what we will not rewrite?

## Student-facing objective

Fill the event retrospective from clinic evidence (not vibes). Start the highest-priority mechanical or electrical repair. Keep TRACE closeout. Do not treat a clinic that “mostly drove” as combined-stack acceptance ([stack-acceptance.md](../../../docs/stack-acceptance.md)).

## Robot outcome

- Retrospective filled from [event-retrospective.md](../../../templates/event-retrospective.md)
- Repair #1 started (fastener, wire, mechanism bind, or battery seating — not a new architecture)
- Dashboard rows updated from clinic measurements
- Conventional teleop and auto still the match plan

## Prerequisites

- Clinic happened, or cancel this session and convert to practice
- Logs copied off the Hub before overwrite; redacted
- [pit-and-inspection.md](../pit-and-inspection.md) clinic test card from Saturday
- [readiness-dashboard.md](../readiness-dashboard.md)

## Vocabulary

keep · drop · delay · reliability sprint · evidence not vibes

## Safety concerns

- Repair hazards; energized work only with a mentor
- Do not “just enable” an optional that seemed interesting at clinic
- ECHO stays off; HELM stays off
- Combined Hub budgets were not proven by showing up at clinic

## Required hardware

Robot as returned from clinic; tools; labeled bags for broken parts; laptop for logs.

## Required software

Redacted TRACE/AMPER exports if any were collected. Meet config remains passive/disabled per the pit card.

## Preparation required before the meeting

Copy logs off the Hub. Print or open the clinic test card. List keep / drop / delay on the board before students arrive so the 10-minute opening is a decision, not a debate.

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Retrospective rules: evidence not vibes; clinic was measurement; no architecture rewrite |
| 75 | Construction | Repair #1 from the list. Fasteners, wiring, binds. Not a new library. |
| 25 | Integration | Fill retrospective; update dashboard from clinic data; TRACE story of one match or scrim |
| 10 | Closeout | TRACE evidence, explain-back, dashboard, cleanup |

## Mentor demonstration

How to fill keep / drop / delay without shaming students. Two minutes. Then they write.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Repair #1 |
| Electrical | Repair #1 if electrical; otherwise support mechanical |
| Programming | Log triage; do not add HELM/ECHO |
| Drive team | What was hard to drive; what to keep in the auto |
| Documentation | Retrospective + dashboard |

## Integrated build or test activity

Complete the retrospective template. For each optional system: keep (still passive), drop (off for the sprint), or delay (not this month). Combined stack row stays **blocked** unless issue #4 evidence actually exists — clinic attendance is not that evidence.

## Failure-injection scenario

Logs are missing. That is the failure. Write the process fix (who copies the Hub, when, where redacted files live). Do not invent a match story.

## Evidence to collect

- Completed retrospective
- Repair photo
- Dashboard updates (clinic measurements vs starting status)
- TRACE retell of one run, or a written “no log” process fix

## Student explain-back questions

1. One keep, one drop, one delay — with evidence.
2. Did any optional system change what the robot did, or only what we recorded?
3. Was rollback used at clinic?
4. What is the next test, and is it a Hub compile-check or a wrench?

## Assessment or exit check

Retrospective filled. Repair underway. No new active flags. Combined-stack claims remain honest.

## Portfolio or engineering-notebook artifact

Retrospective in the notebook. Link clinic test card results.

## Competition enablement impact

Tighten: ECHO off, HELM off, only tested MIMIC protections if any were already on the dashboard. Do not approve AMPER limiting, ViDAR driving, or BEACON intervention because clinic happened.

## Rollback procedure

Restore the clinic-passive config from [pit-and-inspection.md](../pit-and-inspection.md). `TraceMode.OFF` if logs are the problem. Conventional teleop remains.

## Cleanup requirements

Broken parts bagged and labeled; robot safe; Hub not left in a debug OpMode.

## Next-session preparation

Unnumbered Meeting B: driving and auto reps. S010 HELM vocabulary without stealing repairs.

## Hardware-unavailable fallback

Retrospective from photos and memory. Cardboard repair planning for the missing mechanism. TRACE paper events for the process fix.

## Robot-unavailable simulation option

Log review only. Construction block becomes pit-cart / packing repair if the robot is in pieces at a mentor’s house.

## Links to authoritative project documentation

- [templates/event-retrospective.md](../../../templates/event-retrospective.md)
- [docs/evidence-model.md](../../../docs/evidence-model.md)
- [docs/stack-acceptance.md](../../../docs/stack-acceptance.md)
- [projects/trace.md](../../../projects/trace.md)
- [readiness-dashboard.md](../readiness-dashboard.md)

## Mentor notes

Reliability sprint through 31 October. Do not start HELM execute because clinic was humbling. Do not expand integration as if the stack already composes on a Control Hub ([FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4)).
