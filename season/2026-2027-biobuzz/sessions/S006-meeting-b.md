---
id: S006
title: Post-Kickoff week 3 — pivot deadline; CAD and BOM authorization
date: 2026-10-02
meeting_type: B
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: scheduled
difficulty: Developing
projects:
- TRACE
active_features: []
compressed_week: 3
forge_gate: G3
---

# S006 — CAD/BOM authorization and G3 pivot deadline

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

Students complete the CAD/fabrication authorization package, BOM, major-design-pivot deadline declaration, and G3 gate review. **Disagree and commit.** Reject features that do not fit remaining time. First Onshape **login lesson already ran at S003**. Tonight applies that skill to authorize fab after G2 physical comparison. Clinic pit-interview talking points get a short practice in closeout.

## Robot outcome

- G3 gate review passed or fallback activated
- BOM and fabrication package (what we will cut/print/order)
- Pivot deadline recorded — no architectural pivots after today without gate review
- Explicit fallback plan
- CAD used to dimension authorized parts, not to discover a new robot

## Prerequisites

- G2 from S004
- S005 architecture draft
- S003 Onshape screenshot / team document
- [modular-architecture.md](../docs/modular-architecture.md)
- [software-sequencing.md](../docs/software-sequencing.md)
- [guiding-principle.md](../docs/guiding-principle.md)

## Vocabulary

BOM · authorization · pivot deadline · disagree and commit · G3 · fallback

## Safety concerns

- Do not order or cut parts that fail the four tests
- Driving block still has exclusion zone and DS stop
- No last-minute mechanism redesign during reps

## Required hardware

- Drivetrain for the 55-minute drive block
- Laptops with team Onshape document
- Notebook BOM template (part, vendor, qty, why, owner)

## Required software

- Onshape team document
- Team teleop for driving
- TRACE optional

## Preparation required before the meeting

- Open S003 sketches and S004 test records
- Draft BOM rows before students arrive if mentors have vendor links (students still own the why)
- Print [gate-review.md](../../../templates/gate-review.md)
- Charge batteries

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | **Major-design-pivot deadline** — no new architecture after closeout unless G3 gate review. S003 was first CAD; tonight authorizes fab. |
| 35 | Repair / tune / program | CAD dimensions for authorized modules; BOM finalize; cut/print/order list for week 4 fabrication |
| 55 | Driving reps | Short drivetrain reps — do not pause G3 paperwork for tuning debates |
| 20 | Closeout | [Gate review G3](../../../templates/gate-review.md); fallback plan; 5 min pit talking points (robot + team story); update `calendar.yaml` titles only |

## Mentor demonstration

Show one BOM line that is **not** authorized (fails time or four tests) and one that is. CAD screenshot without G2 evidence does not authorize metal.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Dimensions and spare-parts rows |
| Electrical | Sensors/wires on the BOM only if G3 software contract needs them |
| Programming | Software contract stays tier 1 for League 1S/2S unless already decided |
| Drive team | Reps; veto workload |
| Documentation | BOM, G3 record, pit 30-second script start |

## Integrated build or test activity

Authorize or reject each major part. Export STL/DXF only for authorized custom parts that block S007 fabrication.

## Failure-injection scenario

Someone wants a new scoring idea after seeing another team's photo. Correct answer: not-yet list. Pivot requires gate review. Do not add it to the BOM tonight.

## Evidence to collect

- BOM with owners
- G3 gate review
- CAD screenshots of **authorized** parts
- Fallback sentence
- Pit talking-point draft (clinic is 10 Oct)

## Student explain-back questions

1. What are we authorized to fabricate after today?
2. What did we explicitly cut?
3. What happens if a custom part is late?
4. Why is driving still 55 minutes on a paperwork night?
5. Who speaks if judges visit the pit at clinic?

## Assessment or exit check

G3 passed or fallback named. BOM exists. Students can say what they will not build.

## Portfolio or engineering-notebook artifact

BOM + architecture commit. Think C/D. Pit script seed for Connect/team attributes.

## Competition enablement impact

Shop authorization only. No match feature flags.

## Rollback procedure

If G3 fails, fabricate starter-bot path only. Do not place vendor orders for rejected modules.

## Cleanup requirements

Laptops logged out if shared; robot disabled; batteries charging; BOM photographed or copied to team drive.

## Next-session preparation

- S007: module fabrication from this BOM
- Clinic 10 Oct: S008 is the night-before freeze
- Continue Onshape homework only for authorized parts

## Hardware-unavailable fallback

Paper BOM and dimensioned sketches. Driving: unpowered push-bot or hallway walk of cycles.

## Robot-unavailable simulation option

CAD + BOM on laptops. Gamepad dry-run if a Hub exists without a base.

## Links to authoritative project documentation

- [docs/season-process.md](../docs/season-process.md)
- [docs/decision-gates.md](../docs/decision-gates.md)
- [docs/pratt-crosswalk.md](../docs/pratt-crosswalk.md)
- [docs/modular-architecture.md](../docs/modular-architecture.md)
- [docs/software-sequencing.md](../docs/software-sequencing.md)
- [learning-paths/onshape-cad.md](../../../learning-paths/onshape-cad.md)
- [gate-review.md](../../../templates/gate-review.md)
- [S003 Onshape training](S003-meeting-a.md)
- [kickoff-replan-guide.md](../kickoff-replan-guide.md)

## Mentor notes

**Filename stays `S006-meeting-b.md`.** Old file body was ViDAR detection. Do not run a vision lab unless the G3 software contract already placed detection in tier 1 or 2 — and even then it cannot eat the 55-minute drive or the BOM. Protect driving. Clinic judging practice started as a five-minute closeout, not a full mock (that is S013 for league).
