---
id: S005
title: "BEACON communications freshness and recovery"
date: 2026-09-28
meeting_type: A
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: complete
difficulty: Foundation
projects: [BEACON, TRACE]
active_features: []
---

# S005 — BEACON communications freshness and recovery

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S005 |
| Title | BEACON communications freshness and recovery |
| Calendar date | 2026-09-28 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | First Meeting B after Kickoff |
| Meeting type | A |
| Season phase | kickoff-to-clinic |
| Event checkpoint | clinic |
| Difficulty | Foundation |

## Driving question

If the loop is still running, does that mean the driver is still in charge?

## Student-facing objective

Students will classify freshness vs stale stick values, practice official disable, keep driving reps, and write a recovery story that does **not** invent a faster-than-FTC stop.

## Robot outcome

- Written freshness classification from [exercise 1](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/exercises.md)
- Drive reps with a planned "stale command" discussion
- BEACON flags remain default off on the robot unless a mentor adds **passive** reports

## Prerequisites

- Driveable chassis from S002+
- BEACON exercises doc open
- [driver-link.md](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/driver-link.md) — mentors must have read this

## Vocabulary

fresh · stale · connected (ambiguous) · official stop · recovery inhibit · insufficient evidence

## Safety concerns

- Restrained robot if unplugging gamepad USB
- Do not wrap private SDK heartbeat APIs ([BEACON README](https://github.com/The-Allsparks/BEACON/blob/main/README.md))
- BEACON must not replace the FTC watchdog
- After reconnect, sticks may still be forward — students must **not** expect library magic to save them today

## Required hardware

- Robot + DS + gamepad
- Restraint
- Optional spare USB cable

## Required software

- Team teleop
- BEACON desktop tests / paper exercise
- TRACE events `DS/stop` `Drive/rep`

## Preparation required before the meeting

- Print freshness policy example from exercise 1
- Confirm students will not enable Phase 5
- Charge batteries

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Review S004 tape-vs-vision note; BEACON passive only; safety: official stop only |
| 75 | Construction | MVP wiring dress; Hub/DS strain relief; complete passive health-monitor read-through if useful |
| 25 | Integration | BEACON exercises 1–2 on laptop or paper; classify stale stick stories — no intervention flags |
| 10 | Closeout | Domain matching; explain-back; dashboard BEACON ladder 1–2; cleanup |

## Mentor demonstration

Hold a stick forward on a **stopped** OpMode or on paper: `y = -1` with `lastValidTimestamp` 300 ms ago. Walk exercise 1. Do not demo private APIs.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Repair anything that failed S004/S002 inspection |
| Electrical | DS cable strain relief; Hub placement |
| Programming | Paper/unit freshness; no intervention flags |
| Drive team | Reps + honest "I don't know" when evidence is insufficient |
| Documentation | Failure-domain table in notebook |

## Integrated build or test activity

Exercises 1, 2, and 5 from [exercises.md](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/exercises.md) (5 can be discussion if no unit test harness). Recovery inhibit: returning comms with stick forward is **not** "resume driving."

## Failure-injection scenario

Restrained robot: DS stop. Optional: unplug gamepad USB. Students classify the domain using [failure-domains.md](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/failure-domains.md). If they want to say "we were jammed," require `INSUFFICIENT_EVIDENCE` instead (exercise 3 idea).

## Evidence to collect

- Written freshness paragraph
- TRACE/DS timestamps around the stop
- Explicit statement: early DS-loss safe-stop is **not implemented** / **not proven**

## Student explain-back questions

1. Why is a running loop not a heartbeat?
2. What stops the robot on official DS loss (FTC stack, not BEACON)?
3. Why might reconnecting with stick forward be dangerous?
4. How do we roll BEACON off? (don't enable flags; omit reports)

## Assessment or exit check

Student refuses to diagnose jamming from a single symptom. Driver completes remaining reps after the fault drill.

## Portfolio or engineering-notebook artifact

Freshness paragraph + domain table. Link BEACON; do not paste the whole spec.

## Competition enablement impact

BEACON **disabled** or **passive** reports only. No comms intervention. Not approved.

## Rollback procedure

Remove BEACON from OpMode. Official DS stop still works. Never ship Phase 5.

## Cleanup requirements

Gamepad reconnection verified; robot disabled; batteries stored.

## Next-session preparation

- S003 Pedro conventional auto — install/tune docs from [pedropathing.com](https://pedropathing.com/docs/pathing) on one laptop
- Keep MVP build list from Kickoff visible

## Hardware-unavailable fallback

All BEACON work from exercises + fake clock stories. Drive block: unpowered push-bot with verbal "stop" drills.

## Robot-unavailable simulation option

BEACON `gradlew test` if available; complete exercises 1–4 on paper. Watch official FTC disconnect troubleshooting conceptually via [BEACON README watchdog section](https://github.com/The-Allsparks/BEACON/blob/main/README.md) — do not invent latency numbers beyond what BEACON cites.

## Links to authoritative project documentation

- [BEACON README](https://github.com/The-Allsparks/BEACON/blob/main/README.md)
- [Phases](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/phases.md)
- [Exercises](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/exercises.md)
- [Command freshness](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/command-freshness.md)
- [Driver-link](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/driver-link.md)
- [Recovery](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/recovery.md)
- [Failure domains](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/failure-domains.md)
- [Passive example](https://github.com/The-Allsparks/BEACON/blob/main/examples/passive-health-monitor/README.md)
- [projects/beacon.md](../../../projects/beacon.md)

## Mentor notes

The teaching win is humility about evidence. If students ask to "make it stop faster," read driver-link.md together and refuse. Protect the 55-minute driving block.
