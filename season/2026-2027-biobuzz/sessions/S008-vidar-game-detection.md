---
id: S008
title: "ViDAR game-relevant detection"
date: 2026-09-24
meeting_type: B
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: outline
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
| Calendar date | 2026-09-24 (planning input) |
| Relative week | Kickoff-to-clinic |
| Meeting type | B |
| Season phase | kickoff-to-clinic |
| Event checkpoint | clinic |
| Difficulty | Developing |

## Driving question

Does BIOBUZZ actually need a detection today, and can we see it under shop lighting?

## Student-facing objective

If Kickoff mapped a vision need, students tune one-camera detection for that element. If not, they practice sim calibration and spend driving time on the MVP.

## Robot outcome

Detection screenshot for the MVP element, or a written 'vision not MVP' decision.

## Prerequisites

S005 geometry. [CALIBRATION.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/CALIBRATION.md). Kickoff mapping table.

## Vocabulary

HSV · ROI · confidence · game-relevant

## Safety concerns

No motors from vision. No raw video in git.

## Required hardware

One camera or sim laptop; game elements if Kickoff provided them.

## Required software

Discover OpMode or sim; season JSON only as ViDAR docs specify — do not invent HSV in FORGE.

## Preparation required before the meeting

Re-read Kickoff vision column. Stage elements.

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Review S007 auto log; test goal: detect MVP element or confirm vision is deferred |
| 35 | Repair / tune / program | Calibration checklist items that fit 35 min. Mechanism repair otherwise. |
| 55 | Driving / auto reps | Driver and auto reps. Vision pair may observe from the sideline — they do not pause driving for HSV debates. |
| 20 | Closeout | Inspection, log review, explain-back, next steps, cleanup |

## Mentor demonstration

Show calibration checklist page. Do not multi-cam.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Keep camera mount out of mechanism travel |
| Electrical | USB reliability |
| Programming | Tune only documented fields |
| Drive team | Reps |
| Documentation | Before/after screenshots |

## Integrated build or test activity

[CALIBRATION_CHECKLIST.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/CALIBRATION_CHECKLIST.md) as far as one camera allows.

## Failure-injection scenario

Wrong-color object in view. Students must not drive at it.

## Evidence to collect

Screenshot; lighting notes; TRACE event optional.

## Student explain-back questions

1. What game need does this serve?
2. What is stale?
3. Why not four cameras yet?
4. Rollback?

## Assessment or exit check

If vision is deferred, that decision is the pass. If not, a detection is shown and explained.

## Portfolio or engineering-notebook artifact

Calibration notes pointing at ViDAR docs, not copied tables.

## Competition enablement impact

Still not control. practice-only observation at most.

## Rollback procedure

Unplug camera; teleop without ViDAR.

## Cleanup requirements

Elements stored; camera capped.

## Next-session preparation

S009 interlocks on whatever mechanisms exist.

## Hardware-unavailable fallback

Sim with season-colored objects.

## Robot-unavailable simulation option

Browser sim Lesson 4.

## Links to authoritative project documentation

- [TEACHING.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/TEACHING.md)
- [CALIBRATION.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/CALIBRATION.md)
- [CALIBRATION_CHECKLIST.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/CALIBRATION_CHECKLIST.md)
- [CONFIGURATION.md](https://github.com/The-Allsparks/ViDAR/blob/main/docs/CONFIGURATION.md)
- [projects/vidar.md](../../../projects/vidar.md)

## Mentor notes

Expand this outline with Kickoff-specific element names after 12 Sep. Do not invent them here.
