---
id: S001
title: "System map, safety, and TRACE evidence"
date: 2026-09-01
meeting_type: A
season_phase: preseason
event_checkpoint: none
status: complete
difficulty: Foundation
projects: [TRACE]
active_features: []
---

# S001 — System map, safety, and TRACE evidence

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S001 |
| Title | System map, safety, and TRACE evidence |
| Calendar date | 2026-09-01 (planning input; Tuesday Meeting A) |
| Relative week | Preseason week 1 |
| Meeting type | A |
| Season phase | preseason |
| Event checkpoint | none |
| Difficulty | Foundation |

## Driving question

If the robot misbehaves next month, how will we prove what it sensed, what we commanded, and what actually happened?

## Student-facing objective

Students will map The Allsparks software layers onto one robot, complete a shop safety and disable-path walkthrough, begin drivetrain structure, and record a TRACE event sequence they can retell without class names.

## Robot outcome

- Drivetrain frame started (or kit inventory complete if assembly cannot finish)
- Cable-routing path sketched on the chassis
- TRACE desktop (or robot-event) log from today's integration block

## Prerequisites

- Mentor present for any energized equipment
- Team FTC project available on at least one laptop (clone may happen during integration if needed)
- TRACE repo clone **or** ability to run TRACE desktop tests ([TRACE README](https://github.com/The-Allsparks/TRACE/blob/main/README.md))

## Vocabulary

measurement · decision · command · event · disable path · layer (not "seven robots")

## Safety concerns

- Pinch points on drivetrain hardware
- No motors powered without mentor OK
- TRACE must not be described as something that moves motors ([TRACE mentor guide](https://github.com/The-Allsparks/TRACE/blob/main/docs/mentor-guide.md))
- No student names or Wi-Fi passwords in logs ([TRACE SECURITY](https://github.com/The-Allsparks/TRACE/blob/main/SECURITY.md))

## Required hardware

- Drivetrain kit / structure, fasteners, tools
- Safety glasses; known e-stop / DS disable location
- Optional: unpowered Control Hub for placement discussion

## Required software

- TRACE (desktop tests acceptable)
- Team notebook (paper or digital)

## Preparation required before the meeting

- Print or open the layer map from [docs/architecture.md](../../../docs/architecture.md)
- Confirm TRACE `.\gradlew.bat test` works on one mentor laptop
- Stage drivetrain hardware so the 75-minute block is not an unboxing search
- Assign mixed pairs (mechanical + programming) before students arrive

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Driving question; four vocabulary words; safety: glasses, disable path, no powered drive today unless mentor exception; assignments (pairs + documentation rotator) |
| 75 | Construction | Inventory drivetrain kit; assemble frame/plates/wheels as far as hardware allows; mark battery and Hub mounting; sketch wire channels; mentors coach fasteners — no lecture on TRACE internals |
| 25 | Integration | On a laptop at the same table: configure TRACE events (memory sink). Students log `Frame square check`, `Wheel retention check`, `Hub mount sketched` as they finish real inspection items. If TRACE is not cloned, run the same events on paper then type them in the last 10 minutes of this block |
| 10 | Closeout | Export or screenshot the event list; one student retells order; tick TRACE row on the readiness dashboard; cleanup tools; assign S002 prep |

## Mentor demonstration

Under five minutes: write a match story on the board as four lines (saw / decided / commanded / happened). Then show `Trace.event("Autonomous started")` from the TRACE README quick start. Stop. Students type their own events tied to the chassis they are holding.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Frame assembly, wheel retention, square check |
| Electrical | Battery/Hub placement sketch; strain-relief notes (no live wiring required) |
| Programming | TRACE configure + events named after real checks |
| Drive team | Practice picking up DS, pointing to stop; they still help hold structure |
| Documentation | Photo of frame; copy event list into notebook (redacted) |

## Integrated build or test activity

Every TRACE event must correspond to a physical check the pair just performed. A log of fake events with no chassis work fails the session.

## Failure-injection scenario

Scramble the event list (mentor deletes order or shuffles paper cards). Students restore chronological order and explain what is missing if a `Wheel retention check` never appears.

## Evidence to collect

- TRACE memory-sink export or handwritten ordered log
- Photo of drivetrain progress
- Dashboard note: TRACE ladder = 1 (desktop) or 2 if they used fake-robot wording only

## Student explain-back questions

1. What is the difference between a measurement and an event? (no class names required — [TRACE Phase 0 checkpoint](https://github.com/The-Allsparks/TRACE/blob/main/docs/student-learning-path.md))
2. Which Allsparks project owns chassis motion? (Pedro Pathing)
3. How do you turn TRACE off? (`TraceMode.OFF`)
4. Why is FORGE not a robot library?

## Assessment or exit check

Student retells today's chassis work from the event list in order. Mentor marks skills-matrix TRACE foundation.

## Portfolio or engineering-notebook artifact

Layer sketch: robot in the center; TRACE/AMPER/MIMIC/ViDAR/BEACON/ECHO/HELM/Pedro as labels with one verb each. Photo of frame.

## Competition enablement impact

TRACE may be listed as **passive goal**. No competition approval. No other project enabled.

## Rollback procedure

Set `TraceMode.OFF` or do not call `Trace.configure`. Robot teleop (when it exists) must run without TRACE.

## Cleanup requirements

Tools away; loose fasteners bagged; laptops not left with Hub passwords on screen; floor clear.

## Next-session preparation

- Finish any remaining wheel hardware at home only if mentors allow take-home parts; otherwise leave staged for S002
- Drivers: bring gamepads
- Mentors: blocks or crate for wheels-off drive in S002

## Hardware-unavailable fallback

Cardboard or wood mock chassis to scale. Tape wire channels. TRACE events still named after mock inspections (`Corner brace present`).

## Robot-unavailable simulation option

If no FTC project exists: run TRACE desktop tests from the TRACE repo and log events for a **simulated** inspection checklist. Construction block becomes kit sort + CAD/print of drivetrain if available, or assembly of any non-robot structure to practice fasteners.

## Links to authoritative project documentation

- [TRACE README](https://github.com/The-Allsparks/TRACE/blob/main/README.md)
- [TRACE student learning path](https://github.com/The-Allsparks/TRACE/blob/main/docs/student-learning-path.md)
- [TRACE mentor guide](https://github.com/The-Allsparks/TRACE/blob/main/docs/mentor-guide.md)
- [TRACE data model](https://github.com/The-Allsparks/TRACE/blob/main/docs/data-model.md)
- [TRACE architecture](https://github.com/The-Allsparks/TRACE/blob/main/docs/architecture.md)
- [projects/trace.md](../../../projects/trace.md)
- [projects/pedro-pathing.md](../../../projects/pedro-pathing.md)

## Mentor notes

Protect the 75-minute build. Do not recap all seven READMEs. If a student asks about HELM or ECHO, point at the project page and return to the wrench. Never let TRACE become a reason to skip mechanical debugging — that sentence is from the TRACE mentor guide; follow it.
