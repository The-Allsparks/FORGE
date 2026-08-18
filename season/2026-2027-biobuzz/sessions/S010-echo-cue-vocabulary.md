---
id: S010
title: "ECHO cue vocabulary and off-robot driver lab"
date: 2026-10-01
meeting_type: B
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: complete
difficulty: Foundation
projects: [ECHO, TRACE]
active_features: []
---

# S010 — ECHO cue vocabulary and off-robot driver lab

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S010 |
| Title | ECHO cue vocabulary and off-robot driver lab |
| Calendar date | 2026-10-01 (planning input; Thursday Meeting B) |
| Relative week | Kickoff-to-clinic week 3 |
| Meeting type | B |
| Season phase | kickoff-to-clinic |
| Event checkpoint | clinic |
| Difficulty | Foundation |

## Driving question

Can a sound help a driver without hiding referees or lying about unknown targets?

## Student-facing objective

Complete an off-robot cue lab (pan vs pulse, silence reasons, mute) while the robot **drives silently**. Match audio stays off. Training accuracy is not competition proof.

## Robot outcome

- No robot speakers, no Driver Hub audio experiment
- 55 minutes of normal teleop/auto with ECHO off
- Written mute path and three silence reasons

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
| 10 | Opening | Hearing rules; test goal: left/right on training UI **then** drive the real robot silently |
| 35 | Repair / tune / program | Desktop ECHO (student path 1–2, 8) plus any robot repair. No DS audio wiring |
| 55 | Driving / auto reps | Normal reps with ECHO off. After a set, one sentence: "Would a cue have helped?" — capture as a **question**, not approval |
| 20 | Closeout | Mute-path checklist; dashboard ECHO stays disabled; explain-back; cleanup |

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

S011: pick **one** injected fault in advance. Print [pit-and-inspection.md](../pit-and-inspection.md) clinic test card for awareness.

## Hardware-unavailable fallback

Paper left/right with eyes closed (mentor clicks a table). Still valid with no audio.

## Robot-unavailable simulation option

Desktop UI for the whole meeting except a notebook auto walkthrough.

## Links to authoritative project documentation

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
