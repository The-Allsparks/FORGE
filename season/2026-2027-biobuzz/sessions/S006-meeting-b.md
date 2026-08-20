---
id: S006
title: Post-Kickoff week 3 — pivot deadline; CAD and BOM authorization
date: 2026-10-02
meeting_type: B
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: complete
difficulty: Developing
projects:
- ViDAR
- TRACE
active_features: []
compressed_week: 3
forge_gate: G3
---

# S006 — ViDAR game-relevant detection

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S006 |
| Title | Post-Kickoff week 3 — pivot deadline; CAD and BOM authorization |
| Calendar date | 2026-10-02 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | Compressed week 3 (G3 Architecture selection) |
| Meeting type | B |
| Season phase | kickoff-to-clinic |
| Event checkpoint | clinic |
| Forge gate | G3 |
| Difficulty | Developing |

## Driving question

Are we authorized to fabricate — and have we passed G3 before major pivots end?

## Student-facing objective

Students complete CAD/fabrication authorization package, BOM, major-design-pivot deadline declaration, and G3 gate review. Reject features that do not fit remaining time.

## Robot outcome

- G3 gate review passed or fallback activated
- BOM and fabrication package
- Pivot deadline recorded — no architectural pivots after today without gate review
- Explicit fallback plan


## Prerequisites

- S001 geometry
- K001 mapping table (vision column)
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

- Re-read K001 vision column. If blank, this session is deferral + driving
- Stage one camera or confirm sim serves
- Charge batteries for auto reps

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | **Major-design-pivot deadline** — no new architecture after closeout unless G3 gate review |
| 35 | Repair / tune / program | CAD dimensions; BOM finalize; cut list for week 4 fabrication |
| 55 | Driving reps | Short drivetrain reps on Sparkee or Strafer — do not pause G3 paperwork for tuning debates |
| 20 | Closeout | [Gate review G3](../../../templates/gate-review.md); explicit fallback plan; update `calendar.yaml` titles only |

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

S005 interlocks on whatever mechanisms exist. Keep S003 auto as the competition fallback.

## Hardware-unavailable fallback

Browser sim. Drive block: unpowered push-bot or hallway walk of the auto.

## Robot-unavailable simulation option

Entire detection work on sim. Driving becomes gamepad dry-run if a Hub exists without a base.

## Links to authoritative project documentation

- [docs/season-process.md](../docs/season-process.md)
- [docs/decision-gates.md](../docs/decision-gates.md)
- [docs/pratt-crosswalk.md](../docs/pratt-crosswalk.md)
- [prototype-test-record.md](../../../templates/prototype-test-record.md)
- [gate-review.md](../../../templates/gate-review.md)
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
