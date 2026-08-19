---
id: S013
title: "Full match simulation"
date: 2026-10-26
meeting_type: A
season_phase: reliability-sprint
event_checkpoint: league-1s-2s
status: complete
difficulty: Competition readiness
projects: [TRACE, AMPER, MIMIC, ViDAR, BEACON, ECHO, HELM, PEDRO]
active_features: []
---

# S013 — Full match simulation

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S013 |
| Title | Full match simulation |
| Calendar date | 2026-10-26 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | Adversity window |
| Meeting type | A |
| Season phase | reliability-sprint |
| Event checkpoint | league-1s-2s |
| Difficulty | Competition readiness |

## Driving question

Can we finish a match when the battery is tired, the camera is blocked, and a cue is wrong?

## Student-facing objective

Run a **scripted** mock with only narrowly bounded, already-validated behavior. Practice mute/disable in under five seconds. Immediate rollback if anything optional fails its benefit test. This session tests the team, not a claim that the combined stack is FTC-ready ([stack-acceptance.md](../../../docs/stack-acceptance.md)).

## Robot outcome

- Survives the mock, or fails with a written rollback
- Annotated script in the notebook
- Dashboard rows updated (disable anything that failed)

## Prerequisites

- League evidence already on the dashboard
- Expand the script the week before with the team’s **real** faults
- [ECHO hearing safety](https://github.com/The-Allsparks/ECHO/blob/main/docs/hearing-safety.md) if any audio will be used (default: skip audio)
- [BEACON recovery](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/recovery.md) — observation vocabulary only
- [AMPER hardware test card](https://github.com/The-Allsparks/AMPER/blob/main/docs/validation/hardware-test-card.md) — do not induce uncontrolled brownout

## Vocabulary

mock match · depleted · stale · mute · rollback

## Safety concerns

- Script faults. Mentor present
- No uncontrolled brownout
- ECHO off unless already evidenced — if on, include bad-cue mute; mute must not stop the robot
- HELM still not in charge
- Covered camera, not staring into lights
- Mechanism faults must be **safe** (no gravity-load jams to “test MIMIC”)

## Required hardware

Robot; weaker labeled pack if owned; lens cover; spare healthy battery; pit layout space.

## Required software

Meet-like config. Optionals off or passive unless dashboard already says practice-only with evidence.

## Preparation required before the meeting

Script on the board, for example: T=0 auto, T=30 cover camera, T=60 missed acquire, T=90 mute/disable optionals. Assign driver, coach, programmer, pit.

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Script and safety; HELM still not in charge; clinic/league evidence only |
| 75 | Construction | Fix anything the last meet broke; pit layout; battery swap drill |
| 25 | Integration | Run the scripted mock (short). If a full mock needs 55 minutes, keep this block as pit reset and move the full mock to Friday Meeting B |
| 10 | Closeout | TRACE evidence, explain-back, dashboard, cleanup |

## Mentor demonstration

How to mute/disable in under five seconds ([student-install.md](../../../docs/student-install.md)). Students repeat.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Pit reset |
| Electrical | Battery swap drill |
| Programming | Watch logs live; call stale vs missing |
| Drive team | Play the match |
| Documentation | Script results |

## Integrated build or test activity

Run the scripted mock in the 25-minute block **or** a shortened version (auto + one fault + rollback). Full timed mock belongs on Meeting B if construction must stay 75 minutes. Do not skip driving this week.

## Failure-injection scenario

Obstructed camera, stale sensor story, official stop, ambiguous ECHO if present, safe mechanism fault. Students must keep conventional teleop.

## Evidence to collect

- Annotated script
- TRACE export if recording
- Dashboard updates
- Rollback time (target: under one minute)

## Student explain-back questions

1. What did we roll back?
2. Did drivers still function with optionals off?
3. Did conventional auto still exist?
4. Did any active feature fail its benefit test?

## Assessment or exit check

Mock completed or blocker documented. Healthy pack reinstalled.

## Portfolio or engineering-notebook artifact

Script annotated with times and rollback notes.

## Competition enablement impact

Disable anything that failed. Do not add authority. Combined stack is still not match-approved because a mock happened.

## Rollback procedure

Practiced live: DS stop, teleop, disable table, battery disconnect if needed.

## Cleanup requirements

Healthy pack installed; robot safe; lens cover off the camera for storage.

## Next-session preparation

Continue adversity window with templates through 9 January. S034 freeze.

## Hardware-unavailable fallback

Tabletop match with timers and paper faults. Still practice the disable table.

## Robot-unavailable simulation option

Driver + programmer at a table with logs. Say this is not Hub loop-time evidence.

## Links to authoritative project documentation

- [season-plan.md](../season-plan.md)
- [ECHO hearing safety](https://github.com/The-Allsparks/ECHO/blob/main/docs/hearing-safety.md)
- [BEACON recovery](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/recovery.md)
- [docs/safety-and-enablement.md](../../../docs/safety-and-enablement.md)
- [docs/student-install.md](../../../docs/student-install.md)
- [docs/stack-acceptance.md](../../../docs/stack-acceptance.md)

## Mentor notes

If the 75-minute build and a full mock cannot both fit, split to Friday. Do not skip driving. Do not treat a successful mock as AMPER Phase 2, MIMIC actuation, BEACON recovery, HELM execute, ECHO match audio, or ViDAR motion authority.
