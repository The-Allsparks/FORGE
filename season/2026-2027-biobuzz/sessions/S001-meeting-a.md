---
id: S001
title: Post-Kickoff week 1 — strategy execution and crude prototypes
date: 2026-09-14
meeting_type: A
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: scheduled
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

Did we finish the Kickoff package and prove the top-ranked cycle with a **crude** prototype — without fabricating a custom scoring robot to look busy?

## Student-facing objective

Students execute K001 strategy: complete leftover [kickoff-decision-package.md](../../../templates/kickoff-decision-package.md) rows (ranking, effort/value, not-yet list), finish **R0** if the chassis is not yet driveable, and build **low-fidelity** game-object interaction prototype(s) for the top-ranked capability only. Custom scoring fabrication at scale stays blocked until G1 (S002).

## Robot outcome

- Crude prototype demonstrating at least one game-object interaction (cardboard/coroplast/temporary channel)
- Kickoff package rows that K001 left blank
- Owner list on [readiness-dashboard.md](../readiness-dashboard.md)
- Progress toward G1 exit (complete G1 at S002)
- R0 chassis work **if** enable is still blocked


## Prerequisites

- [K001-meeting-k.md](K001-meeting-k.md) outputs: MVP, brainstorm, decision package, decision record if used
- [kickoff-replan-guide.md](../kickoff-replan-guide.md)
- [guiding-principle.md](../docs/guiding-principle.md)
- [preseason-kickoff-gate.md](../docs/preseason-kickoff-gate.md) if tower/capstan/transport is in debate
- Strafer drivetrain from preseason **as actually completed** (P002–P007; see [preseason-deferred-work.md](../docs/preseason-deferred-work.md)). Do not assume a P007 mechanism lab, a P008 shop meeting, or a full original-P006 driver baseline. P008 was the FRC tour.

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
| 10 | Opening | Review K001 MVP, four tests, not-yet list; safety; **custom scoring fab is still blocked** |
| 75 | Construction | If the chassis still cannot be enabled safely, **finish R0 first**. Otherwise: low-fi prototype of the **top-ranked** capability only (cardboard/coroplast/temporary channel). Do not start a multi-stage elevator/capstan/hopper because it looks productive. |
| 25 | Integration | Finish decision-package rows (ranking, effort/value); TRACE or notebook; dashboard |
| 10 | Closeout | Explain-back: what shipped vs assumption vs not-yet; assign S002 G1 review |

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

Mentor asks: "Does this part serve the K001 ranked list or a leftover preseason experiment?" Students defend with the decision package or park the work.

## Evidence to collect

- Photo of MVP progress
- Dashboard row updates with owners
- Note linking preseason **construction / V0 / first-movement** evidence to today's design choice (there is no P007 mechanism-lab data set; original lab may be reused this week / S003 **if** the official game needs those principles)

## Student explain-back questions

1. What is the MVP scoring action from K001?
2. Who owns each subsystem?
3. What preseason evidence informed today's build? (construction + V0 rules + first movement — not a fake mechanism lab)
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

**Filename stays `S001-meeting-a.md`.** Change the `title` in front matter and calendar when this week's focus shifts. First shop meeting after Kickoff is for **building the season robot**, not a standalone library lab. If preseason never finished enablement, this 75-minute block is the last acceptable chassis catch-up — then return to K001 MVP. Original P007 capstan/slide/transport stations may be reused here **only** if the official game needs those principles; retarget to real game pieces ([preseason-kickoff-gate.md](../docs/preseason-kickoff-gate.md)).
