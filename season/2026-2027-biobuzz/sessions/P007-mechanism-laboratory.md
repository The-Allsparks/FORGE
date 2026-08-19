---
id: P007
title: "Reusable mechanism laboratory"
date: 2026-09-07
meeting_type: A
season_phase: preseason
event_checkpoint: none
status: complete
difficulty: Foundation
projects: [TRACE]
active_features: []
---

# P007 — Reusable mechanism laboratory

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | P007 |
| Title | Reusable mechanism laboratory |
| Calendar date | 2026-09-08 (planning input; Tuesday Meeting A) |
| Relative week | Preseason week 2 |
| Meeting type | A |
| Season phase | preseason |
| Event checkpoint | none |
| Difficulty | Foundation |

## Driving question

Which capstan, slide, and transport ideas actually work on measured loads—without building a speculative BIOBUZZ robot?

## Student-facing objective

Students will run **standalone experiments** for capstan line behavior, one tower slide stage, and surgical-tube belt transport—recording measured results, failures, and assumptions. Prototypes must stay **reusable**; do not permanently modify the Strafer drivetrain for throwaway game mechanisms.

## Robot outcome

- Capstan data: drum diameter, line material, wrap count, slip/load notes
- Tower data: one slide stage friction, twist, cascade routing, tension balance
- Transport data: belt spacing, compression, angle, speed vs squash-ball or substitute objects
- No final tower, hopper, or game-piece system committed

## Prerequisites

- P006 baseline **or** documented chassis blocker (experiments still run off-robot)
- Capstan drum, line, slide hardware, surgical tubing, squash balls or substitutes
- [preseason-kickoff-gate.md](../docs/preseason-kickoff-gate.md) — experiments inform Kickoff; they do not decide the game

## Vocabulary

capstan · cascade · compression · assumption · reusable prototype · measured load

## Safety concerns

- Eye protection when lines under tension snap
- Keep fingers clear of winding capstan
- Slide tests: support load; no climbing on prototypes
- Belt tests: low speed; stop on jam

## Required hardware

- Capstan kit parts (drum, line, anchors, known weights)
- One slide stage + line routing hardware
- Two surgical-tube round belts, rollers or pulleys, squash balls or substitutes
- Scale or known masses (mentor)
- **Separate from Strafer** — bench rigs only

## Required software

- Notebook only; optional TRACE events for load tests (≤10 min)
- No ViDAR/MIMIC/Pedro on these rigs

## Preparation required before the meeting

- Stage three bench stations; assign station owners
- Print [decision-record.md](../../../templates/decision-record.md) headers for later Kickoff use
- Confirm parts return to labeled bins after session

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Goal: measured principles, not BIOBUZZ robot; safety; station rotation |
| 75 | Construction | **Rotate stations (~25 min each):** capstan load/slip; tower slide load/friction; transport acquisition/jam tests |
| 25 | Integration | Tabulate results: proven / assumption / open question; photo each rig; optional TRACE event per load test |
| 10 | Closeout | Explain-back; store reusable parts; prep P008 summary |

## Mentor demonstration

Show one failed line termination vs one secure termination. Two minutes.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Run assigned station; measure and record |
| Electrical | Only if station uses a motor — one motor, low speed |
| Programming | ≤10 min TRACE labels if used |
| Drive team | Assist loads; call stops |
| Documentation | Data tables per experiment |

## Integrated build or test activity

Measured load or travel numbers are required—not "it seemed fine."

## Failure-injection scenario

Mentor removes tension from one cascade line. Team must explain unequal routing symptom.

## Evidence to collect

- Capstan table (drum, wraps, line, load, slip Y/N)
- Tower table (friction, twist, service access)
- Transport table (spacing, compression, object, retain/jam)
- Photos of each rig
- List: proven facts vs assumptions vs open questions

## Student explain-back questions

1. One thing proven today with a number.
2. One assumption still unverified.
3. Why did we **not** bolt this to the Strafer yet?
4. What will Kickoff need to tell us before building a tower?

## Assessment or exit check

All three experiment types attempted; data tables exist; parts returned to reusable storage.

## Portfolio or engineering-notebook artifact

Experiment tables (Think C/D). Photos (Innovate/Design candidates). Link forward to [preseason-kickoff-gate.md](../docs/preseason-kickoff-gate.md).

## Competition enablement impact

None. No BIOBUZZ mechanism enabled.

## Rollback procedure

Disassemble bench rigs; no permanent robot changes to revert.

## Cleanup requirements

Parts inventoried; line disposed safely; floor clear.

## Next-session preparation

- P008: summarize experiments; Kickoff role assignments
- Keep prototype bins labeled

## Hardware-unavailable fallback

Paper calculations + video of commercial capstan/elevator/belt for discussion — still fill assumption column honestly.

## Robot-unavailable simulation option

Same as fallback. Strafer not required for P007.

## Links to authoritative project documentation

- [preseason-kickoff-gate.md](../docs/preseason-kickoff-gate.md)
- [templates/decision-record.md](../../../templates/decision-record.md)
- [templates/math-evidence.md](../../../templates/math-evidence.md)
- [season-plan.md](../season-plan.md)

## Mentor notes

Stop any "let's finish the hopper before Kickoff" scope creep. If a student says "this is our robot," redirect to **evidence for decisions**. Strafer stays the team's reliable platform.
