---
id: S017
title: "Full match simulation"
date: 2026-12-08
meeting_type: A
season_phase: adversity-simulations
event_checkpoint: league-5s-6s
status: outline
difficulty: Competition readiness
projects: [TRACE, AMPER, MIMIC, ViDAR, BEACON, ECHO, HELM, PEDRO]
active_features: []
---
# S017 — Full match simulation

## Session identity
| Field | Value |
| ----- | ----- |
| Session ID | S017 |
| Title | Full match simulation |
| Calendar date | 2026-12-08 (planning input) |
| Relative week | Adversity window |
| Meeting type | A |
| Season phase | adversity-simulations |
| Event checkpoint | league-5s-6s |
| Difficulty | Competition readiness |

## Driving question

Can we finish a match when the battery is tired, the camera is blocked, and a cue is wrong?

## Student-facing objective

Timed mock match with scripted faults. Only narrowly bounded validated active behavior. Immediate rollback.

## Robot outcome

Survives the mock or fails with a written rollback.

## Prerequisites

League evidence already in dashboard. Expand this outline the week before with the team's real faults.

## Vocabulary

mock match · depleted · stale · mute

## Safety concerns

Script faults. No uncontrolled brownout. ECHO off unless already evidenced — if on, include bad-cue mute test.

## Required hardware

Robot; weaker labeled pack; lens cover; spare battery.

## Required software

Meet-like config.

## Preparation required before the meeting

Script: T=0 auto, T=30 cover camera, T=60 missed acquire, T=90 mute/disable optional systems.

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Script and safety; HELM still not in charge |
| 75 | Construction | Fix anything the last meet broke; pit layout. |
| 25 | Integration | Run the scripted mock (may spill a few minutes from construction if mentors agree — prefer keeping 75 min build/pit practice as physical pit reset). |
| 10 | Closeout | TRACE evidence, explain-back, dashboard, cleanup |

## Mentor demonstration

How to mute/disable in under five seconds.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Pit reset |
| Electrical | Battery swap drill |
| Programming | Watch logs live |
| Drive team | Play the match |
| Documentation | Script results |

## Integrated build or test activity

Full script. If construction must stay 75 min, run a shortened mock in the 25-minute integration block and schedule a Thursday Meeting B for the full 55+ mock.

## Failure-injection scenario

Obstructed camera, stale sensor story, comms stop, ambiguous ECHO if present, mechanism fault (safe).

## Evidence to collect

Script sheet; TRACE; dashboard.

## Student explain-back questions

1. What did we roll back?
2. Did drivers still function?
3. Auto fallback?
4. Any active feature that failed its benefit test?

## Assessment or exit check

Mock completed or blocker documented.

## Portfolio or engineering-notebook artifact

Script annotated.

## Competition enablement impact

Disable anything that failed. Do not add authority.

## Rollback procedure

Practiced live.

## Cleanup requirements

Healthy pack installed; robot safe.

## Next-session preparation

Continue adversity window with templates through 9 Jan. S018 freeze.

## Hardware-unavailable fallback

Tabletop match with timers and paper faults.

## Robot-unavailable simulation option

Driver + programmer at a table with logs.

## Links to authoritative project documentation

- [season-plan.md](../season-plan.md)
- [ECHO hearing safety](https://github.com/The-Allsparks/ECHO/blob/main/docs/hearing-safety.md)
- [BEACON recovery](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/recovery.md)
- [docs/safety-and-enablement.md](../../../docs/safety-and-enablement.md)

## Mentor notes

If the 75-minute build and a full mock cannot both fit, the outline already splits to Thursday. Do not skip driving.
