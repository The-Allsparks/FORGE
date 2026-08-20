---
id: S007
title: Post-Kickoff week 4 — module fabrication (incremental delivery)
date: 2026-10-05
meeting_type: A
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: complete
difficulty: Developing
projects:
- MIMIC
- TRACE
active_features: []
compressed_week: 4
forge_gate: G4
---

# S007 — MIMIC interlocks

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S007 |
| Title | Post-Kickoff week 4 — module fabrication (incremental delivery) |
| Calendar date | 2026-10-05 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | Compressed week 4 (G4 Design freeze) |
| Meeting type | A |
| Season phase | kickoff-to-clinic |
| Event checkpoint | clinic |
| Forge gate | G4 |
| Difficulty | Developing |

## Driving question

Can we deliver modules incrementally to software instead of waiting for a complete robot?

## Student-facing objective

Students fabricate authorized Sparkee modules; deliver first modules to programming pair; declare G4 design freeze on module set.

## Robot outcome

- ≥1 module fabricated and demonstrated under power
- Incremental software handoff documented
- G4 freeze declaration
- Spares identified for fragile parts


## Prerequisites

- Paper mechanism state names from P007 or post-Kickoff MIMIC work
- [interlocks.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/interlocks.md)
- [safety-model.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/safety-model.md)
- Second mechanism **or** cardboard stand-in. Elevator-specific racking work stays out until hardware exists ([MIMIC assessment](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/assessment.md))

## Vocabulary

interlock · reject · defer · clamp · deadlock · hard stop vs software

## Safety concerns

- Adult supervision. Do **not** test interlocks by crashing hardware
- Gravity loads secured; no "see if it hits"
- Software limits do not replace mechanical stops
- Unpowered for geometry checks unless a mentor is jogging a mechanism slowly with a clear exclusion zone

## Required hardware

- Two mechanisms or one real + cardboard volume
- Hard stops where the design needs them
- Camera/intake as a typical pair if that is the MVP

## Required software

- Notebook table (required)
- Optional: MIMIC desktop tests / fake hardware — no robot actuation flags
- TRACE event `Interlock/would-reject` when students identify an illegal pair (paper is enough)

## Preparation required before the meeting

- Photograph current travel
- Print a blank state×state grid from mechanism state names (update names if Kickoff changed them)
- Read interlocks.md outcomes: reject, defer, clamp, confirmation — do not invent a scheduler

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | **G4 design freeze** — no new modules without gate review; incremental software delivery plan |
| 75 | Construction | Fabricate authorized Sparkee modules; spares for fragile parts |
| 25 | Integration | Deliver first completed module to programming pair; [prototype-test-record](../../../templates/prototype-test-record.md) per module |
| 10 | Closeout | Module handoff log; explain-back; dashboard mechanical row |

## Mentor demonstration

Two unpowered poses that would collide. Write `REJECT` on the board. Thirty seconds of "this is not a global command scheduler" pointing at MIMIC README.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Travel, hard stops, pinch points |
| Electrical | Limit-switch routing if switches exist; otherwise label future ports |
| Programming | Named constraints on paper; not a competing scheduler |
| Drive team | Practice the callout "clear" / "not clear" they will use in teleop later |
| Documentation | Interlock table |

## Integrated build or test activity

For each pair of states, mark legal / illegal. Choose one illegal: would you **reject** the command, **defer** until the other mechanism moves, or **clamp** travel? Cite the interlocks doc, do not invent deadlock loops.

## Failure-injection scenario

Mentor: "Just raise while extended." Students refuse unless the table already names an exception with a mechanical reason. If they comply on hardware, stop the session's powered work.

## Evidence to collect

- Interlock table
- Geometry photo
- Confirmation: MIMIC actuation still off (no write counts if using fake actuators)

## Student explain-back questions

1. Why is this not a global scheduler?
2. What is deadlock, in one sentence?
3. Difference between a software interlock and a hard stop?
4. How do we roll back? (Do not enable Phase 7.)

## Assessment or exit check

Table complete. Construction visibly progressed. No new motor flags.

## Portfolio or engineering-notebook artifact

State×state grid. Link MIMIC interlocks.md as authority.

## Competition enablement impact

MIMIC protections **disabled**. Observation/snapshots only until a later controlled failure test.

## Rollback procedure

Do not enable Phase 7 or homing. Teleop remains manual. Power off mechanisms.

## Cleanup requirements

Mechanisms unpowered and down; no loaded arms left standing.

## Next-session preparation

S006 ECHO is off-robot. Bring hearing-safety willingness. Keep building Friday if Meeting B has repair time.

## Hardware-unavailable fallback

Cardboard overlapping volumes on the table. Same table exercise.

## Robot-unavailable simulation option

MIMIC `gradlew test` / fake hardware plus the paper grid.

## Links to authoritative project documentation

- [docs/season-process.md](../docs/season-process.md)
- [docs/decision-gates.md](../docs/decision-gates.md)
- [docs/pratt-crosswalk.md](../docs/pratt-crosswalk.md)
- [prototype-test-record.md](../../../templates/prototype-test-record.md)
- [gate-review.md](../../../templates/gate-review.md)
- [interlocks.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/interlocks.md)
- [lifecycle.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/lifecycle.md)
- [safety-model.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/safety-model.md)
- [phases.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/phases.md)
- [assessment.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/assessment.md)
- [testing.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/testing.md)
- [projects/mimic.md](../../../projects/mimic.md)

## Mentor notes

If only one mechanism exists, teach the idea and **build the second** in the 75 minutes. Do not fabricate a second elevator. Phase 0 remains the implemented scaffold at audit.
