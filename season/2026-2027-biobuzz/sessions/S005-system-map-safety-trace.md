---
id: S005
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

# S005 — System map, safety, and TRACE evidence

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S005 |
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

Students will map The Allsparks software layers onto one robot, complete a shop safety and disable-path walkthrough, **correct and finalize** the S003–S004 drivetrain and wiring (not first assembly), review the modified StarterBot layout rationale, and record a TRACE event sequence they can retell without class names.

## Robot outcome

- Drivetrain corrections complete: retention, cable routing, mount refinement, documented design review of modified layout
- TRACE desktop (or robot-event) log from today's integration block tied to **real** inspection items

## Prerequisites

- S001–S004 complete or equivalent: chassis built, modified drivetrain installed, control system substantially wired ([S003](S003-modified-drivetrain-install.md), [S004](S004-control-system-wiring-prep.md))
- Mentor present for any energized equipment
- Team FTC project available on at least one laptop (clone may happen during integration if needed) — **BLOCKED** on [#2](https://github.com/The-Allsparks/FORGE/issues/2) until robot URL published
- TRACE repo clone **or** ability to run TRACE desktop tests ([TRACE README](https://github.com/The-Allsparks/TRACE/blob/main/README.md))

## Vocabulary

measurement · decision · command · event · disable path · layer (not "seven robots")

## Safety concerns

- Pinch points on drivetrain hardware
- No motors powered without mentor OK
- TRACE must not be described as something that moves motors ([TRACE mentor guide](https://github.com/The-Allsparks/TRACE/blob/main/docs/mentor-guide.md))
- No student names or Wi-Fi passwords in logs ([TRACE SECURITY](https://github.com/The-Allsparks/TRACE/blob/main/SECURITY.md))

## Required hardware

- S003–S004 drivetrain and wiring as assembled
- Safety glasses; known e-stop / DS disable location
- Control Hub mounted per S004 sketch

## Required software

- TRACE (desktop tests acceptable)
- Team notebook (paper or digital)
- Onshape — export one custom part for print or order

## Preparation required before the meeting

- Print or open the layer map from [docs/architecture.md](../../../docs/architecture.md)
- Confirm TRACE `.\gradlew.bat test` works on one mentor laptop
- Bring S004 inspection/repair list to the opening block
- Assign mixed pairs (mechanical + programming) before students arrive

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Driving question; vocabulary; safety: glasses, disable path; review S004 blockers; assignments |
| 75 | Construction | **Corrections and finalization** (≈60 min) — retention, cable routing, mount refinement; then **≈15 min Onshape export** for one custom part (print/order checklist). Fix S004 inspection items |
| 25 | Integration | Configure TRACE events (memory sink) tied to real inspection items; export or screenshot event list |
| 10 | Closeout | One student retells order; tick TRACE row on readiness dashboard; cleanup; assign S006 prep |

## Mentor demonstration

Under five minutes: write a match story on the board as four lines (saw / decided / commanded / happened). Then show `Trace.event("Autonomous started")` from the TRACE README quick start. Stop. Students type their own events tied to the chassis they are holding.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Retention, square re-check, fastener fixes from S004 list |
| Electrical | Final cable dress, strain relief, labeling |
| Programming | TRACE configure + events named after real checks — **does not replace** mechanical work |
| Drive team | Practice picking up DS, pointing to stop; verify disable path |
| Documentation | Photo of corrected drivetrain; print/order checklist; copy event list into notebook (redacted) |

## Integrated build or test activity

Every TRACE event must correspond to a physical check the pair just performed. A log of fake events with no chassis work fails the session. Software time **cannot** displace the 75-minute construction block.

## Failure-injection scenario

Scramble the event list (mentor deletes order or shuffles paper cards). Students restore chronological order and explain what is missing if a `Wheel retention check` never appears.

## Evidence to collect

- TRACE memory-sink export or handwritten ordered log
- Photo of drivetrain after corrections
- Print/order checklist for one custom part (owner, material, due date)
- Dashboard note: TRACE ladder = 1 (desktop) or 2 if they used fake-robot wording only

## Student explain-back questions

1. What is the difference between a measurement and an event? (no class names required — [TRACE Phase 0 checkpoint](https://github.com/The-Allsparks/TRACE/blob/main/docs/student-learning-path.md))
2. Which Allsparks project owns chassis motion? (Pedro Pathing)
3. How do you turn TRACE off? (`TraceMode.OFF`)
4. Why is FORGE not a robot library?
5. What did we change from the standard StarterBot layout and why?

## Assessment or exit check

Student retells today's correction work from the event list in order. Mentor marks skills-matrix TRACE foundation. S004 blockers resolved or carried honestly to S006.

## Portfolio or engineering-notebook artifact

Layer sketch: robot in the center; TRACE/AMPER/MIMIC/ViDAR/BEACON/ECHO/HELM/Pedro as labels with one verb each. Photo of drivetrain. S003 decision record attached or summarized.

## Competition enablement impact

TRACE may be listed as **passive goal**. No competition approval. No other project enabled.

## Rollback procedure

Set `TraceMode.OFF` or do not call `Trace.configure`. Robot teleop (when it exists) must run without TRACE.

## Cleanup requirements

Tools away; loose fasteners bagged; laptops not left with Hub passwords on screen; floor clear.

## Next-session preparation

- S006: restrained driver baseline — drivetrain expected ready for blocks-first testing
- Drivers: bring gamepads
- Mentors: blocks or crate for wheels-off drive in S006
- Resolve any S004 motor-test blockers or document them for S006 honest path

## Hardware-unavailable fallback

Inspect and document whatever structure exists. TRACE events named after mock inspections. Review layout rationale on paper.

## Robot-unavailable simulation option

If no FTC project exists: run TRACE desktop tests from the TRACE repo and log events for a **simulated** inspection checklist. Construction block becomes S004 repair list on paper plus wire-routing sketch.

## Links to authoritative project documentation

- [TRACE README](https://github.com/The-Allsparks/TRACE/blob/main/README.md)
- [TRACE student learning path](https://github.com/The-Allsparks/TRACE/blob/main/docs/student-learning-path.md)
- [TRACE mentor guide](https://github.com/The-Allsparks/TRACE/blob/main/docs/mentor-guide.md)
- [TRACE data model](https://github.com/The-Allsparks/TRACE/blob/main/docs/data-model.md)
- [TRACE architecture](https://github.com/The-Allsparks/TRACE/blob/main/docs/architecture.md)
- [projects/trace.md](../../../projects/trace.md)
- [projects/pedro-pathing.md](../../../projects/pedro-pathing.md)
- [docs/stack-acceptance.md](../../../docs/stack-acceptance.md)
- [docs/student-install.md](../../../docs/student-install.md)
- [learning-paths/onshape-cad.md](../../../learning-paths/onshape-cad.md)
- [S003 modified drivetrain](S003-modified-drivetrain-install.md)
- [S004 control wiring](S004-control-system-wiring-prep.md)

## Mentor notes

Protect the 60-minute construction block and the 15-minute Onshape export — both are required. Drivetrain **first assembly happened in S002–S004** — S005 is corrections, export, and TRACE. Never let software displace mechanical debugging.
