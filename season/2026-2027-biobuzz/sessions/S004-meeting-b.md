---
id: S004
title: Post-Kickoff week 2 — starter vs alternative evidence (G2 gate)
date: 2026-09-25
meeting_type: B
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: complete
difficulty: Foundation
projects:
- ViDAR
- TRACE
active_features: []
compressed_week: 2
forge_gate: G2
---

# S004 — ViDAR camera geometry and one-camera observation

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S004 |
| Title | Post-Kickoff week 2 — starter vs alternative evidence (G2 gate) |
| Calendar date | 2026-09-25 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | Compressed week 2 (G2 Prototype evidence) |
| Meeting type | B |
| Season phase | kickoff-to-clinic |
| Event checkpoint | clinic |
| Forge gate | G2 |
| Difficulty | Foundation |

## Driving question

Do we have measured evidence to stop unrestricted exploration and commit to a leading direction?

## Student-facing objective

Students complete starter vs alternative comparison, fill comparative summary, pass or fail G2 with [gate-review.md](../../../templates/gate-review.md), and run driver reps.

## Robot outcome

- G2 gate review recorded
- Comparative evidence table complete
- Leading concept(s) and starter-bot fallback explicit
- Unresolved risk list updated


## Prerequisites

- K001 minimum viable robot list (if Kickoff was missed, use a placeholder "drive + one intake" and replan)
- Laptop for [sim README](https://github.com/The-Allsparks/ViDAR/blob/main/sim/README-SIM.md)
- Optional: Control Hub + `Webcam 1`

## Vocabulary

robot space · range · bearing · frame · stale track · one camera first

## Safety concerns

- USB strain relief; powered hub only if using multiple cameras later (not today)
- No-motor ViDAR OpModes — do not wire detections to drive
- Camera pointing: no climbing on robots
- Privacy: do not commit raw video ([TRACE storage rules](https://github.com/The-Allsparks/TRACE/blob/main/SECURITY.md) apply to vision files too)

## Required hardware

- One UVC webcam **or** none (sim)
- Mount materials; continue MVP mechanism hardware
- Control Hub if using Discover OpMode

## Required software

- ViDAR sim **or** `VidarDiscoverOpMode`
- TRACE event `Vision/observe` when a detection is trusted
- Team teleop unchanged

## Preparation required before the meeting

- Try `.\scripts\serve_sim.ps1` once before students arrive ([TEACHING Lesson 4](https://github.com/The-Allsparks/ViDAR/blob/main/docs/TEACHING.md))
- Name the Kickoff object students should care about — **only if** the manual needs it. If vision does not serve MVP, keep this session on geometry with a colored ball and say so
- Stage mount hardware

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Robot-space vs pixels; Kickoff MVP reminder; safety: no motor from vision; assignments |
| 35 | Repair / tune / program | Camera mount prototype + USB dress; sim or Discover setup; fix S002 teleop blockers if any |
| 55 | Driving reps | Driver rotations; tape-measure vs telemetry checks between reps; TRACE one trusted observation event |
| 20 | Closeout | Screenshot; explain-back; dashboard ViDAR ladder 2 or 3; cleanup |

## Mentor demonstration

Hold a game element at a known distance. Show sim overlay **or** Camera Stream circle. Say "size range vs floor range" only as far as TEACHING Lesson 1. No fusion lecture.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | MVP + camera mount that can be removed |
| Electrical | USB routing and strain relief |
| Programming | Discover/sim; do not consume detections in teleop |
| Drive team | Tape-measure partner for the ranging check |
| Documentation | Photo of mount; calibration note "not field-validated" |

## Integrated build or test activity

Lesson 1 or 4 from [TEACHING.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/TEACHING.md): see a detection, estimate inches, compare to tape.

## Failure-injection scenario

Cover the lens (or switch sim to empty scene). Students must report unknown/stale — not last known pose as truth.

## Evidence to collect

- Tape vs ViDAR number
- Sim or DS screenshot
- Note that 4-camera Hub operation is **not** validated ([ViDAR README](https://github.com/The-Allsparks/ViDAR/blob/main/README.md))

## Student explain-back questions

1. What frame is this range in?
2. Why start with one camera?
3. Who is allowed to move the chassis using this number today? (Nobody — observation only)
4. What should the robot do if the track is old?

## Assessment or exit check

Student explains a detection as robot-relative, not "the blob is on the left of the screen."

## Portfolio or engineering-notebook artifact

Sketch: camera, robot origin, element, range/bearing arrows. Link [COORDINATE_FRAMES.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/COORDINATE_FRAMES.md) as the authority — do not redraw the whole spec.

## Competition enablement impact

ViDAR **disabled** for control. Simulation or passive observation only. Not approved. Multi-camera off.

## Rollback procedure

Do not call `VidarSpatial` from teleop. Use stock drive. Unplug camera if it tanks loop time.

## Cleanup requirements

Camera capped; USB unstrained; robot unpowered.

## Next-session preparation

- Keep camera mount removable
- S005 BEACON integration continues on S006 if needed

## Hardware-unavailable fallback

Browser sim + cardboard mount. Construction block still builds MVP without vision hardware.

## Robot-unavailable simulation option

Entire integration on sim. Construction uses Kickoff cardboard prototype of the scoring mechanism.

## Links to authoritative project documentation

- [docs/season-process.md](../docs/season-process.md)
- [docs/decision-gates.md](../docs/decision-gates.md)
- [docs/pratt-crosswalk.md](../docs/pratt-crosswalk.md)
- [prototype-test-record.md](../../../templates/prototype-test-record.md)
- [gate-review.md](../../../templates/gate-review.md)
- [ViDAR README](https://github.com/The-Allsparks/ViDAR/blob/main/README.md)
- [TEACHING.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/TEACHING.md)
- [COORDINATE_FRAMES.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/COORDINATE_FRAMES.md)
- [CALIBRATION.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/CALIBRATION.md)
- [sim/README-SIM.md](https://github.com/The-Allsparks/ViDAR/blob/main/sim/README-SIM.md)
- [projects/vidar.md](../../../projects/vidar.md)

## Mentor notes

If Kickoff showed vision is optional for MVP, say that out loud and keep the 75 minutes on the scoring mechanism. Do not chase four cameras.
