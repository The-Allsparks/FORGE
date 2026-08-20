---
id: S010
title: Post-Kickoff week 5 — minimum auto and mechanism tuning
date: 2026-10-16
meeting_type: B
season_phase: reliability-sprint
event_checkpoint: league-1s-2s
status: complete
difficulty: Foundation
projects:
- ECHO
- TRACE
active_features: []
compressed_week: 5
forge_gate: G6
---

# S010 — ECHO cue vocabulary and off-robot driver lab

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S010 |
| Title | Post-Kickoff week 5 — minimum auto and mechanism tuning |
| Calendar date | 2026-10-16 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | Compressed week 5 (G6 Stable software handoff) |
| Meeting type | B |
| Season phase | reliability-sprint |
| Event checkpoint | league-1s-2s |
| Forge gate | G6 |
| Difficulty | Foundation |

## Driving question

Can we run one reliable minimum autonomous path before adding anything advanced?

## Student-facing objective

Students build minimum reliable Pedro (or conventional) auto on Sparkee; tune mechanisms; stop major mechanical changes.

## Robot outcome

- Minimum auto runs ≥7/10 in practice or teleop-only declared
- Mechanism tuning log
- Known-good release tag recorded


## Prerequisites

- [cue-vocabulary.md](https://github.com/The-Allsparks/ECHO/blob/main/docs/cue-vocabulary.md)
- [hearing-safety.md](https://github.com/The-Allsparks/ECHO/blob/main/docs/hearing-safety.md)
- [phase1-desktop](https://github.com/The-Allsparks/ECHO/blob/main/examples/phase1-desktop.md)
- [student-learning-path.md](https://github.com/The-Allsparks/ECHO/blob/main/docs/student-learning-path.md) items 1–2 and 8
- Re-read [feasibility-decision.md](https://github.com/The-Allsparks/ECHO/blob/main/docs/feasibility-decision.md) if Kickoff already happened

## Vocabulary

cue · pan · pulse · silence · mute · GUIDANCE vs WARN · `driverEnabled`

## Safety concerns

- Start OS volume low; ECHO gain stays at library default if audio is on at all
- Stop if ears ring, speech is hard, or coaches cannot be heard
- Two-ear isolation hides referees — even in the shop
- Mute must **not** stop the robot (when audio exists later)
- Match audio is forbidden ([competition readiness](https://github.com/The-Allsparks/ECHO/blob/main/docs/competition-readiness.md))

## Required hardware

- Laptops; headphones optional
- Robot for driving **without** ECHO
- No unofficial speakers on the robot

## Required software

- ECHO desktop training UI; **audio flag off by default**
- `driverEnabled=false` path demonstrated in UI or code reading
- Team teleop/auto unchanged

## Preparation required before the meeting

- Mentor reads hearing-safety aloud plan
- Confirm desktop audio defaults off before students arrive
- `gradlew test` in ECHO on one laptop if possible

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Minimum reliable auto before advanced paths; Pedro on **Sparkee mass**, not Strafer assumptions |
| 35 | Repair / tune / program | Pedro path or conventional fallback; mechanism tuning; known-good release tag |
| 55 | Driving reps | Auto repetitions (≥7/10 target) interleaved with teleop scoring cycles |
| 20 | Closeout | Auto log; rollback tag recorded; optional libraries still per software contract |

## Mentor demonstration

Print or show a decision record: silence vs guidance. Show mute. Do not crank gain.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Repair if the robot needs it during the 35-minute block |
| Electrical | No robot speaker work |
| Programming | Desktop tests; list silence reasons from the cue-vocabulary doc |
| Drive team | Training UI (quiet) then silent field driving |
| Documentation | Mute-path checklist in the notebook |

## Integrated build or test activity

ECHO student path: cue is a chosen message; pan owns bearing; mute without killing the robot. ≥8/10 left/right in a quiet room is a **training metric only**, not match evidence.

## Failure-injection scenario

Mentor describes "unknown target, so pan center" or "turn it up to beat the field." Students must reject (unknown ≠ 0; cranking gain is forbidden).

## Evidence to collect

- Mute demonstration
- Three silence reasons (from the authoritative list, not invented)
- Driver question-not-approval note
- No competition enablement

## Student explain-back questions

1. Why isn't ECHO a vision system?
2. List three silence reasons from the ECHO docs.
3. How do you mute without killing the robot?
4. Why are anecdotes forbidden for approval?

## Assessment or exit check

Mute path named. Hearing rules restated. Robot was driven without ECHO.

## Portfolio or engineering-notebook artifact

Pointer to cue families in ECHO docs — do not copy a soundboard design into FORGE as if it were match-approved.

## Competition enablement impact

ECHO **disabled** for competition and for on-robot audio. Ladder may tick 1–2 (desktop) only.

## Rollback procedure

Audio flag off; `driverEnabled=false`; unplug any unofficial speaker (none should exist). Teleop unchanged.

## Cleanup requirements

OS volume down; headphones away; robot disabled.

## Next-session preparation

S007: pick **one** injected fault in advance. Print [pit-and-inspection.md](../pit-and-inspection.md) clinic test card for awareness.

## Hardware-unavailable fallback

Paper left/right with eyes closed (mentor clicks a table). Still valid with no audio.

## Robot-unavailable simulation option

Desktop UI for the whole meeting except a notebook auto walkthrough.

## Links to authoritative project documentation

- [docs/season-process.md](../docs/season-process.md)
- [docs/decision-gates.md](../docs/decision-gates.md)
- [docs/pratt-crosswalk.md](../docs/pratt-crosswalk.md)
- [prototype-test-record.md](../../../templates/prototype-test-record.md)
- [gate-review.md](../../../templates/gate-review.md)
- [ECHO README](https://github.com/The-Allsparks/ECHO/blob/main/README.md)
- [Student path](https://github.com/The-Allsparks/ECHO/blob/main/docs/student-learning-path.md)
- [Cue vocabulary](https://github.com/The-Allsparks/ECHO/blob/main/docs/cue-vocabulary.md)
- [Hearing safety](https://github.com/The-Allsparks/ECHO/blob/main/docs/hearing-safety.md)
- [Competition readiness](https://github.com/The-Allsparks/ECHO/blob/main/docs/competition-readiness.md)
- [Driver training](https://github.com/The-Allsparks/ECHO/blob/main/docs/driver-training.md)
- [Feasibility](https://github.com/The-Allsparks/ECHO/blob/main/docs/feasibility-decision.md)
- [phase1-desktop](https://github.com/The-Allsparks/ECHO/blob/main/examples/phase1-desktop.md)
- [labs/SIM002](../../../labs/simulated/SIM002-echo-desktop.md)
- [projects/echo.md](../../../projects/echo.md)

## Mentor notes

Do not sneak audio onto the Driver Hub. Clinic is not an ECHO debut. Re-read feasibility after Kickoff as that document requires.
