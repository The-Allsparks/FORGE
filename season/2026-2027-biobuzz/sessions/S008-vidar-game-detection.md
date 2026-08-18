---
id: S008
title: "ViDAR game-relevant detection"
date: 2026-09-24
meeting_type: B
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: complete
difficulty: Developing
projects: [ViDAR, TRACE]
active_features: []
---

# S008 — ViDAR game-relevant detection

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S008 |
| Title | ViDAR game-relevant detection |
| Calendar date | 2026-09-24 (planning input; Thursday Meeting B) |
| Relative week | Kickoff-to-clinic week 2 |
| Meeting type | B |
| Season phase | kickoff-to-clinic |
| Event checkpoint | clinic |
| Difficulty | Developing |

## Driving question

Does BIOBUZZ actually need a detection today, and can we see that thing under shop lighting without stealing driver practice?

## Student-facing objective

If SK01 mapped a vision need, students run one-camera detection for **that** element and compare to a tape measure. If vision is not MVP, they write the deferral, run sim calibration for 15 minutes of the repair block, and spend the 55-minute block driving and repeating the S007 auto.

## Robot outcome

- Written **vision serves MVP / vision deferred** decision in the notebook
- If serving: Discover/sim screenshot of the Kickoff-named element (not a guessed color)
- Teleop still has **no** vision-to-drive wiring

## Prerequisites

- S005 geometry
- SK01 mapping table (vision column)
- [CALIBRATION.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/CALIBRATION.md) and [CALIBRATION_CHECKLIST.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/CALIBRATION_CHECKLIST.md)
- [TEACHING.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/TEACHING.md)

## Vocabulary

game-relevant · HSV · ROI · confidence · stale · deferred

## Safety concerns

- No motors from vision
- No raw video in git
- Cover lens as a fault — do not stare into bright lights
- USB strain relief; one camera only

## Required hardware

- One webcam **or** sim laptops
- Official-looking game elements **only if Kickoff provided or the team bought the legal set** — do not invent a piece
- Drivetrain for the 55-minute drive block

## Required software

- `VidarDiscoverOpMode` or browser sim
- Team teleop **without** consuming detections
- TRACE optional `Vision/detect` event when a detection is trusted

## Preparation required before the meeting

- Re-read SK01 vision column. If blank, this session is deferral + driving
- Stage one camera or confirm sim serves
- Charge batteries for auto reps

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Review S007 auto log; test goal: detect MVP element **or** confirm vision is deferred; no drive-from-vision |
| 35 | Repair / tune / program | If vision is MVP: calibration checklist items that fit. If deferred: 15 min sim Lesson 4, then mechanism/auto repair. Do not multi-cam |
| 55 | Driving / auto reps | Driver and Pedro/fallback auto repetitions. Vision pair may observe from the sideline — they do not pause driving for HSV debates |
| 20 | Closeout | Screenshot or deferral paragraph; dashboard ViDAR; explain-back; cleanup |

## Mentor demonstration

Show [CALIBRATION_CHECKLIST.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/CALIBRATION_CHECKLIST.md). If Kickoff said vision is optional, say that out loud in the first minute.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Keep camera mount out of mechanism travel; or ignore camera if deferred |
| Electrical | USB reliability |
| Programming | Tune only fields named in ViDAR config docs — do not invent HSV in FORGE |
| Drive team | Reps; veto if vision work tries to take the field |
| Documentation | Before/after or deferral |

## Integrated build or test activity

**If MVP needs detection:** tape-measure vs telemetry/sim range on the Kickoff element. Cover the lens; students must not treat last pose as truth.

**If deferred:** one sim screenshot labeled "practice only, not this season's scoring piece" plus the deferral sentence.

## Failure-injection scenario

Wrong-color object in view (or empty sim scene). Students must not drive at it. If someone wired vision to motors, stop and remove it.

## Evidence to collect

- Decision: serve vs defer
- Screenshot if serving
- Lighting notes (shop ≠ field)
- TRACE event optional

## Student explain-back questions

1. What game need does this serve, or why is it deferred?
2. What is a stale track?
3. Why not four cameras yet?
4. How do we roll vision out of teleop?

## Assessment or exit check

If deferred, the written decision is the pass. If not, a detection is shown as robot-relative range/bearing.

## Portfolio or engineering-notebook artifact

Calibration notes that **point at** ViDAR docs, or a deferral dated today.

## Competition enablement impact

Still not control. Observation at most. Multi-camera stays off.

## Rollback procedure

Unplug camera. Teleop without `VidarSpatial`. Sim closed.

## Cleanup requirements

Elements stored; camera capped; robot disabled.

## Next-session preparation

S009 interlocks on whatever mechanisms exist. Keep S007 auto as the competition fallback.

## Hardware-unavailable fallback

Browser sim. Drive block: unpowered push-bot or hallway walk of the auto.

## Robot-unavailable simulation option

Entire detection work on sim. Driving becomes gamepad dry-run if a Hub exists without a base.

## Links to authoritative project documentation

- [TEACHING.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/TEACHING.md)
- [CALIBRATION.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/CALIBRATION.md)
- [CALIBRATION_CHECKLIST.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/CALIBRATION_CHECKLIST.md)
- [CONFIGURATION.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/CONFIGURATION.md)
- [COORDINATE_FRAMES.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/COORDINATE_FRAMES.md)
- [sim/README-SIM.md](https://github.com/The-Allsparks/ViDAR/blob/main/sim/README-SIM.md)
- [kickoff-replan-guide.md](../kickoff-replan-guide.md)
- [projects/vidar.md](../../../projects/vidar.md)

## Mentor notes

Do not invent BIOBUZZ element names in this file. After Kickoff, write the real name in the notebook, not as a FORGE "rule." Protect the 55-minute drive block.
