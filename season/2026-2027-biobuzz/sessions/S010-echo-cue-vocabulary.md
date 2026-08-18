---
id: S010
title: "ECHO cue vocabulary and off-robot driver lab"
date: 2026-10-01
meeting_type: B
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: outline
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
| Calendar date | 2026-10-01 (planning input) |
| Relative week | Kickoff-to-clinic |
| Meeting type | B |
| Season phase | kickoff-to-clinic |
| Event checkpoint | clinic |
| Difficulty | Foundation |

## Driving question

Can a sound help a driver without hiding referees or lying about unknown targets?

## Student-facing objective

Off-robot cue lab: pan vs pulse, silence reasons, mute path. Match audio stays off.

## Robot outcome

No robot audio. Drivers still do 55 minutes of normal driving without ECHO.

## Prerequisites

[cue-vocabulary.md](https://github.com/The-Allsparks/ECHO/blob/main/docs/cue-vocabulary.md), [hearing-safety.md](https://github.com/The-Allsparks/ECHO/blob/main/docs/hearing-safety.md), [phase1-desktop](https://github.com/The-Allsparks/ECHO/blob/main/examples/phase1-desktop.md).

## Vocabulary

pan · pulse · silence · mute · GUIDANCE vs WARN

## Safety concerns

Start OS volume low. Stop if ears ring. Mute must not stop a robot (when audio exists). Two-ear isolation is a comms risk. Match audio forbidden.

## Required hardware

Headphones optional; laptops. Robot for driving without ECHO.

## Required software

ECHO desktop training UI; audio flag off by default. `driverEnabled=false` path.

## Preparation required before the meeting

Read hearing-safety aloud plan. Confirm audio defaults off.

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Hearing rules; test goal: identify left/right in training UI then drive the real robot silently |
| 35 | Repair / tune / program | Desktop ECHO exercises + any robot repair. No DS audio wiring. |
| 55 | Driving / auto reps | Normal driver/auto reps with ECHO off. After a set, drivers comment on whether they wanted a cue — capture as question, not approval. |
| 20 | Closeout | Inspection, log review, explain-back, next steps, cleanup |

## Mentor demonstration

Silence vs guidance decision record. Mute control.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Ignore ECHO; keep building later |
| Electrical | No robot speaker work |
| Programming | Desktop tests |
| Drive team | Training UI then silent driving |
| Documentation | Mute-path checklist |

## Integrated build or test activity

Student path items 1–2 and 8 (mute) from [ECHO student path](https://github.com/The-Allsparks/ECHO/blob/main/docs/student-learning-path.md).

## Failure-injection scenario

Excessive cue rate or unknown filled as center pan — students must reject.

## Evidence to collect

Mute demonstration; written silence reasons; no competition enablement.

## Student explain-back questions

1. Why isn't ECHO a vision system?
2. List three silence reasons.
3. How do you mute without killing the robot?
4. Why are anecdotes forbidden for approval?

## Assessment or exit check

Mute path named. Hearing rules restated.

## Portfolio or engineering-notebook artifact

Cue family table copied as a pointer, not a soundboard design.

## Competition enablement impact

ECHO remains disabled for competition and for on-robot audio.

## Rollback procedure

Audio flag off; `driverEnabled=false`; unplug any unofficial speaker experiments (none should exist).

## Cleanup requirements

Volume down; headphones away.

## Next-session preparation

S011 integrated failures.

## Hardware-unavailable fallback

Paper pan left/right with eyes closed using mentor clicks; still valid if no audio.

## Robot-unavailable simulation option

Desktop UI entirely.

## Links to authoritative project documentation

- [ECHO README](https://github.com/The-Allsparks/ECHO/blob/main/README.md)
- [Student path](https://github.com/The-Allsparks/ECHO/blob/main/docs/student-learning-path.md)
- [Cue vocabulary](https://github.com/The-Allsparks/ECHO/blob/main/docs/cue-vocabulary.md)
- [Hearing safety](https://github.com/The-Allsparks/ECHO/blob/main/docs/hearing-safety.md)
- [Competition readiness](https://github.com/The-Allsparks/ECHO/blob/main/docs/competition-readiness.md)
- [phase1-desktop](https://github.com/The-Allsparks/ECHO/blob/main/examples/phase1-desktop.md)
- [projects/echo.md](../../../projects/echo.md)

## Mentor notes

Do not sneak audio onto the Driver Hub. Re-read feasibility after Kickoff.
