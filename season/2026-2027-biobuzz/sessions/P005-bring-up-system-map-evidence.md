---
id: P005
title: "Bring-up, system map, and evidence"
date: 2026-08-31
meeting_type: A
season_phase: preseason
event_checkpoint: none
status: complete
difficulty: Foundation
projects: [TRACE]
active_features: []
---

# P005 — Bring-up, system map, and evidence

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | P005 |
| Title | Bring-up, system map, and evidence |
| Calendar date | 2026-09-01 (planning input; Tuesday Meeting A) |
| Relative week | Preseason week 1 |
| Meeting type | A |
| Season phase | preseason |
| Event checkpoint | none |
| Difficulty | Foundation |

## Driving question

If the chassis was built in P002–P004, can we prove—one motor at a time—that measurement, decision, command, and result match reality?

## Student-facing objective

Students will **verify** the assembled Strafer drivetrain (not begin assembly): inspect structure and wiring, elevate the chassis, test one motor at a time, correct ports and directions, demonstrate Driver Station disable, record checks with TRACE or an honest paper timeline, and introduce the software system map without a library lecture.

## Robot outcome

- Every motor operates correctly on the bench (elevated/restrained)
- Motor directions and ports documented
- DS disable demonstrated
- TRACE or paper timeline tied to **actual** bring-up checks
- System-map vocabulary sketched (measurement → decision → command → result)

## Prerequisites

- [P002](P002-chassis-sponsor-cards.md)–[P004](P004-electrical-foundation.md) complete: chassis, rolling drivetrain, wired power path
- Mentor present for all energized tests
- Minimal TeleOp or per-motor test OpMode — or documented blocker ([#2](https://github.com/The-Allsparks/FORGE/issues/2))
- ≤30 min software this week beyond evidence capture ([preseason-software-allocation.md](../docs/preseason-software-allocation.md))

## Vocabulary

bring-up · measurement · decision · command · result · disable path · port · direction

## Safety concerns

- Chassis **elevated or restrained** before any motor spin
- One motor at a time until all verified
- Hair, hoodies, ties away from wheels
- DS disable path tested before multi-motor tests
- No floor driving today — that is P006

## Required hardware

- P002–P004 drivetrain and wiring
- Blocks, crate, or stand; safety glasses
- Control Hub, battery, main switch per P004 layout

## Required software

- Driver Station
- Minimal motor test or TeleOp (≤30 min programming block if missing)
- TRACE desktop or robot events — evidence only, not a library deep-dive

## Preparation required before the meeting

- Charge batteries; print P004 power-path sketch
- Open [docs/architecture.md](../../../docs/architecture.md) layer map
- Assign: inspector pair, motor-test pair, documentation, **≤30 min** programmer cap

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Safety: elevated test only; software cap; goals; review P004 wiring list |
| 75 | Construction | Inspect fasteners, wheel retention, wiring labels; elevate chassis; **one motor at a time** — direction, port, bind check; fix issues; draw/annotate system map on paper |
| 25 | Integration | TRACE or paper events for each motor verified (`Motor/FL verified`, etc.); ≤30 min total if deploying test OpMode |
| 10 | Closeout | Explain-back measurement→result chain; dashboard note; assign P006 prep |

## Mentor demonstration

Under three minutes: one motor enable on blocks — show disable before the wheel spins free. Then students run their own sequence.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Inspection, retention, elevation setup |
| Electrical | Power-path verification, connector seating |
| Programming | Motor test OpMode or port map — **time-boxed** |
| Drive team | Call disable; observe wheel direction |
| Documentation | Motor table: port, direction, mentor initials |

## Integrated build or test activity

One-motor-at-a-time bring-up **is** the session. System map is sketched from what was verified, not from README slides.

## Failure-injection scenario

Mentor swaps two motor labels on the board. Students must catch mismatch before enable.

## Evidence to collect

- Motor verification table (all four corners)
- DS disable test note
- TRACE or paper timeline
- System-map sketch (layers as verbs, not a code dump)
- Blocker record if TeamCode still missing — honest only

## Student explain-back questions

1. What is the difference between a measurement and a command?
2. Which project owns chassis motion? (Pedro Pathing — tuning deferred)
3. How do you disable from the Driver Station?
4. What did P004 leave for today to verify?

## Assessment or exit check

Every motor verified **or** blocker written with owner. Every student can retell measurement→decision→command→result with today's motor example.

## Portfolio or engineering-notebook artifact

Motor bring-up table + system-map sketch (Think topic A). Photo of elevated test setup.

## Competition enablement impact

TRACE passive goal only. No competition approval. Advanced libraries **not** enabled.

## Rollback procedure

DS stop. Disconnect battery if needed. Fix wiring before re-enable. `TraceMode.OFF` if TRACE interferes.

## Cleanup requirements

Battery disconnected; robot on blocks; tools stored.

## Next-session preparation

- P006: full mecanum baseline on restraint/carpet if P005 complete
- Gamepads charged; inspection checklist printed

## Hardware-unavailable fallback

Paper motor port map and inspection on partial chassis. TRACE desktop events named after mock checks.

## Robot-unavailable simulation option

Same as fallback. Do not claim Hub success without hardware.

## Links to authoritative project documentation

- [preseason-software-allocation.md](../docs/preseason-software-allocation.md)
- [TRACE README](https://github.com/The-Allsparks/TRACE/blob/main/README.md)
- [docs/architecture.md](../../../docs/architecture.md)
- [P003 modified drivetrain](P003-modified-drivetrain-install.md)
- [P004 electrical foundation](P004-electrical-foundation.md)

## Mentor notes

**Not** first assembly — P002–P004 already built the chassis. Protect bring-up from becoming a 75-minute Gradle session; cap software at 30 minutes. Drivetrain must be serviceable after today.
