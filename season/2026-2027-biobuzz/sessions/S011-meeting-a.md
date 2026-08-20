---
id: S011
title: Post-Kickoff week 5 — reliability testing and portfolio draft
date: 2026-10-19
meeting_type: A
season_phase: reliability-sprint
event_checkpoint: league-1s-2s
status: complete
difficulty: Integration
projects:
- TRACE
- AMPER
- MIMIC
- ViDAR
- BEACON
active_features: []
compressed_week: 5
forge_gate: G6
---

# S011 — Integrated failure injection

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S011 |
| Title | Post-Kickoff week 5 — reliability testing and portfolio draft |
| Calendar date | 2026-10-19 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | Compressed week 5 (G6 Stable software handoff) |
| Meeting type | A |
| Season phase | reliability-sprint |
| Event checkpoint | league-1s-2s |
| Forge gate | G6 |
| Difficulty | Integration |

## Driving question

What is our measured reliability — and is the portfolio draft ready for final edit?

## Student-facing objective

Students run repeated full-cycle tests (≥10 attempts), log via TRACE and human-readable log, draft portfolio narrative from season notes.

## Robot outcome

- Reliability metrics recorded honestly
- Portfolio draft substantially complete
- [student-progress-review.md](../../../templates/student-progress-review.md) if due


## Prerequisites

- S001–S002 vocabulary
- [BEACON exercises](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/exercises.md) especially 3
- [failure-domains.md](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/failure-domains.md)
- [AMPER hardware test card](https://github.com/The-Allsparks/AMPER/blob/main/docs/validation/hardware-test-card.md) — no uncontrolled brownout
- TRACE closeout habit

## Vocabulary

correlation · insufficient evidence · domain · timeline

## Safety concerns

- Mentor present. Restrain if motion is involved
- Do **not** induce an uncontrolled brownout
- Do not jam gravity loads
- Weaker pack only if labeled and stopped before damage
- Restore healthy battery and uncover camera before anyone leaves

## Required hardware

- Robot as it will go to clinic
- Lens cap or cloth
- Optional labeled weaker pack
- TRACE/AMPER exports if those are installed

## Required software

- TRACE memory or file sink if present
- Passive AMPER/BEACON if installed
- ViDAR observe-only if a camera is mounted
- Team teleop/auto **unchanged** except logging

## Preparation required before the meeting

Pick **one** fault for the 25-minute block. Write it on the board before students arrive. Construction stays MVP.

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Reliability test plan: ≥10 full-cycle attempts; portfolio draft milestone |
| 75 | Construction | P1 repairs only — no new mechanisms; support reliability testing |
| 25 | Integration | Log cycle success rate; TRACE + human-readable log; portfolio draft section |
| 10 | Closeout | [student-progress-review](../../../templates/student-progress-review.md) if due; dashboard reliability row |

## Mentor demonstration

Show a bad diagnosis: "we were jammed" from mixed symptoms. Point at BEACON exercise 3.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Clinic-critical fasteners and mechanism freedom |
| Electrical | Connector check; battery labeling |
| Programming | Export or copy a short timeline |
| Drive team | If time after construction, a short restrained run — otherwise wait for S008 |
| Documentation | Timeline paragraph |

## Integrated build or test activity

Chosen fault examples (pick one):

1. Cover camera → stale/unknown vision
2. Wheels-off forward pulse on two packs (healthy vs labeled weaker) → sag story, AMPER passive only
3. Stop capturing a MIMIC snapshot while still talking as if the pose is live

Write one paragraph. If you cannot name a single domain, end with `INSUFFICIENT_EVIDENCE`.

## Failure-injection scenario

The integration block **is** the injection. Do not stack three faults.

## Evidence to collect

- Timeline (redacted)
- Dashboard **Known risks** updated
- Restore checklist ticked (battery, lens, disable)

## Student explain-back questions

1. Which domain do you actually have evidence for?
2. What did you not prove?
3. Rollback for TRACE, AMPER, ViDAR, BEACON, MIMIC?
4. Will any optional feature be **on** at clinic? (Default no.)

## Assessment or exit check

Paragraph complete. Robot restored. MVP still the priority.

## Portfolio or engineering-notebook artifact

Failure timeline. Link BEACON domains rather than copying the whole spec. Promote to [failure-record.md](../../../templates/failure-record.md) if the failure will drive a design change.

## Competition enablement impact

No new approvals. Clinic remains systems validation. TRACE Phase 4 adapters may not exist — correlate by hand ([TRACE integrations](https://github.com/The-Allsparks/TRACE/blob/main/docs/integrations.md)).

## Rollback procedure

Dashboard statuses. Uncover camera. Healthy pack in. Optional systems off or passive. DS stop.

## Cleanup requirements

Healthy pack installed; lens uncovered; robot safe; no weaker pack left in the robot.

## Next-session preparation

S008 clinic prep. Print [pit-and-inspection.md](../pit-and-inspection.md) and a blank retrospective.

## Hardware-unavailable fallback

Paper multi-log exercise using BEACON exercises. Label any made-up numbers as **practice only**.

## Robot-unavailable simulation option

TRACE desktop memory sink + BEACON fake-clock exercises.

## Links to authoritative project documentation

- [docs/season-process.md](../docs/season-process.md)
- [docs/decision-gates.md](../docs/decision-gates.md)
- [docs/pratt-crosswalk.md](../docs/pratt-crosswalk.md)
- [prototype-test-record.md](../../../templates/prototype-test-record.md)
- [gate-review.md](../../../templates/gate-review.md)
- [TRACE integrations](https://github.com/The-Allsparks/TRACE/blob/main/docs/integrations.md)
- [BEACON exercises](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/exercises.md)
- [Failure domains](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/failure-domains.md)
- [AMPER phases](https://github.com/The-Allsparks/AMPER/blob/main/docs/power-management/phases.md)
- [AMPER hardware test card](https://github.com/The-Allsparks/AMPER/blob/main/docs/validation/hardware-test-card.md)
- [pit-and-inspection.md](../pit-and-inspection.md)
- [projects/trace.md](../../../projects/trace.md)
- [projects/beacon.md](../../../projects/beacon.md)

## Mentor notes

Do not claim unified flight-recorder adapters. One fault. Restore before closeout.
