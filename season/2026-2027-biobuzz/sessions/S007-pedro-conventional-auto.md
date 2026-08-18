---
id: S007
title: "Pedro Pathing conventional autonomous"
date: 2026-09-22
meeting_type: A
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: outline
difficulty: Developing
projects: [PEDRO, TRACE]
active_features: []
---
# S007 — Pedro Pathing conventional autonomous

## Session identity
| Field | Value |
| ----- | ----- |
| Session ID | S007 |
| Title | Pedro Pathing conventional autonomous |
| Calendar date | 2026-09-22 (planning input) |
| Relative week | Kickoff-to-clinic |
| Meeting type | A |
| Season phase | kickoff-to-clinic |
| Event checkpoint | clinic |
| Difficulty | Developing |

## Driving question

Can we complete one simple, repeatable autonomous path without vision, HELM, or ECHO?

## Student-facing objective

Students continue MVP construction and encode or tune a conventional Pedro path they can explain.

## Robot outcome

A simple auto that runs with optional systems off, or a documented blocker with a paper path.

## Prerequisites

Driveable chassis. [Pedro introduction](https://pedropathing.com/docs/pathing). Android Studio per Pedro docs (not OnBot Java/Blocks).

## Vocabulary

path · localization · conventional auto · fallback

## Safety concerns

First auto on a clear practice surface; exclusion zone; DS stop. Do not give HELM chassis authority.

## Required hardware

Drivetrain; localization hardware the team chose; battery.

## Required software

Pedro Pathing per official docs; TRACE auto start/stop events; HELM off.

## Preparation required before the meeting

Open pedropathing.com docs and Quickstart on one laptop. Tape a 2–3 waypoint course.

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Goal: conventional auto fallback; safety; assignments |
| 75 | Construction | MVP mechanism + drivetrain remaining work. Localization mount if missing. |
| 25 | Integration | Pedro constants/path on the robot if it drives; otherwise paper path + Visualizer if available. |
| 10 | Closeout | TRACE evidence, explain-back, dashboard, cleanup |

## Mentor demonstration

Show official intro constraints (omni drive, localization, Android Studio). Two minutes.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Localization mount, bumper/skid if needed |
| Electrical | Encoder/Pinpoint/OTOS wiring as chosen |
| Programming | Path + TRACE events |
| Drive team | Watch auto; call stop |
| Documentation | Path sketch |

## Integrated build or test activity

Run the path N times or walk it. Success is repeatability, not speed.

## Failure-injection scenario

Bump the robot mid-path (gentle, mentor). Students explain whether localization recovered. Do not 'fix' by enabling vision.

## Evidence to collect

Rep count, TRACE auto events, localization notes.

## Student explain-back questions

1. What happens if HELM is off?
2. Who owns chassis motion?
3. How do you disable the auto?
4. Why is this the season priority over HELM execute?

## Assessment or exit check

Student explains the path in human words. Auto or walkthrough completed.

## Portfolio or engineering-notebook artifact

Field sketch with waypoints.

## Competition enablement impact

Conventional autonomous ladder toward practice-field. Not HELM. Not competition approved until repeatable.

## Rollback procedure

Select teleop. Pedro auto OpMode not used. Optional systems remain off.

## Cleanup requirements

Robot disabled; tape removed if needed.

## Next-session preparation

S008 only if MVP needs detection; otherwise keep construction.

## Hardware-unavailable fallback

Walk the path; encode later.

## Robot-unavailable simulation option

Pedro Visualizer if the team can run it; otherwise paper.

## Links to authoritative project documentation

- [Pedro Pathing site](https://pedropathing.com/)
- [Introduction](https://pedropathing.com/docs/pathing)
- [PedroPathing repo](https://github.com/Pedro-Pathing/PedroPathing)
- [Quickstart](https://github.com/Pedro-Pathing/Quickstart)
- [projects/pedro-pathing.md](../../../projects/pedro-pathing.md)

## Mentor notes

Do not block this session on ViDAR. If Pedro install fails, keep a timed drive-forward auto as emergency fallback and record the gap.
