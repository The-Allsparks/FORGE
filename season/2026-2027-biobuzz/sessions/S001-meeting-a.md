---
id: S001
title: Post-Kickoff week 1 — strategy execution and crude prototypes
date: 2026-09-14
meeting_type: A
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: complete
difficulty: Integration
projects:
- TRACE
active_features: []
compressed_week: 1
forge_gate: G1
---

# S001 — Post-Kickoff MVP build and season execution

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S001 |
| Title | Post-Kickoff week 1 — strategy execution and crude prototypes |
| Calendar date | 2026-09-14 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | Compressed week 1 (G1 Strategy) |
| Meeting type | A |
| Season phase | kickoff-to-clinic |
| Event checkpoint | clinic |
| Forge gate | G1 |
| Difficulty | Integration |

## Driving question

Did we turn K001 strategy into physical proof — crude prototype plus clear owners — without starting a side quest?

## Student-facing objective

Students execute K001 strategy: build crude game-object interaction prototype(s), confirm mechanism owners, begin strategy matrix refinement, and record evidence vs preseason assumptions.

## Robot outcome

- Crude prototype demonstrating at least one game-object interaction
- Strategy matrix draft updated
- Owner list on [readiness-dashboard.md](../readiness-dashboard.md)
- Progress toward G1 exit (complete G1 at S002 if needed)


## Prerequisites

- [K001-meeting-k.md](K001-meeting-k.md) outputs: MVP, brainstorm, decision record if used
- [kickoff-replan-guide.md](../kickoff-replan-guide.md)
- [preseason-kickoff-gate.md](../docs/preseason-kickoff-gate.md) if tower/capstan/transport is in debate
- Strafer drivetrain from preseason (P002–P006)

## Vocabulary

MVP · owner · planning-input title · evidence vs assumption · rollback

## Safety concerns

- Mentor present for powered tests
- No library enablement because Kickoff was exciting
- DS disable path before any enable

## Required hardware

- MVP mechanism materials from Kickoff list
- Strafer chassis; hand tools; notebook

## Required software

- Minimal TeleOp only if needed for mechanism clearance checks
- TRACE optional for build milestones (≤10 min)

## Preparation required before the meeting

- Print mechanism owner list from K001
- Mentors: identify **one** scoring subsystem for today's 75-minute block
- Read [preseason-software-allocation.md](../docs/preseason-software-allocation.md) — software cap lifts after Kickoff but still serves the robot

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Review K001 MVP, owners, and preseason evidence; safety; **this meeting is about the season robot** |
| 75 | Construction | Build the highest-priority MVP subsystem; integrate with Strafer only as the MVP requires |
| 25 | Integration | TRACE or notebook: record build milestone; update dashboard; **optional:** edit upcoming `calendar.yaml` titles to name this week's mechanism |
| 10 | Closeout | Explain-back: what shipped vs what is still assumption; assign S002 teleop checks |

## Mentor demonstration

Two minutes: show K001 MVP written goal vs one physical part that proves progress today.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Lead the 75-minute construction block |
| Electrical | Power path for new mechanism; labeled wires |
| Programming | TeleOp trim only if blocking mechanical progress |
| Drive team | Clearance checks; call out driver visibility |
| Documentation | Dashboard update; photo of today's subsystem |

## Integrated build or test activity

Construction **is** the session. No ViDAR/HELM/ECHO lecture block today.

## Failure-injection scenario

Mentor asks: "Does this part serve the K001 MVP or a leftover preseason experiment?" Students defend with K001 decision record or park the work.

## Evidence to collect

- Photo of MVP progress
- Dashboard row updates with owners
- Note linking preseason P007 data to today's design choice (if applicable)

## Student explain-back questions

1. What is the MVP scoring action from K001?
2. Who owns each subsystem?
3. What preseason evidence informed today's build?
4. What library stays **off** until the MVP drives?

## Assessment or exit check

Mechanism progress is visible; owners named; no competitor treated a library session as today's priority.

## Portfolio or engineering-notebook artifact

Before/after photo of MVP subsystem with owner initials and K001 task reference.

## Competition enablement impact

None. Build and document only.

## Rollback procedure

Remove untested mechanism additions; return to Strafer-only teleop if integration fails.

## Cleanup requirements

Robot safe; floor clear; tools stored.

## Next-session preparation

- S002: teleop and driver reps on the MVP configuration
- Charge batteries; list teleop blockers

## Hardware-unavailable fallback

Cardboard MVP prototype and full K001 mapping table on paper.

## Robot-unavailable simulation option

Walk through teleop commands and mechanism states without Hub power.

## Links to authoritative project documentation

- [docs/season-process.md](../docs/season-process.md)
- [docs/decision-gates.md](../docs/decision-gates.md)
- [docs/pratt-crosswalk.md](../docs/pratt-crosswalk.md)
- [prototype-test-record.md](../../../templates/prototype-test-record.md)
- [gate-review.md](../../../templates/gate-review.md)
- [kickoff-replan-guide.md](../kickoff-replan-guide.md)
- [preseason-kickoff-gate.md](../docs/preseason-kickoff-gate.md)
- [readiness-dashboard.md](../readiness-dashboard.md)
- [docs/safety-and-enablement.md](../../../docs/safety-and-enablement.md)

## Mentor notes

**Filename stays `S001-meeting-a.md`.** Change the `title` in front matter and calendar when this week's focus shifts. First shop meeting after Kickoff is for **building the season robot**, not a standalone library lab.
