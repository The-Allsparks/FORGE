# Cadence Meeting B — drive, auto, inspect

Copy into `season/2026-2027-biobuzz/sessions/` only if you need a dated file. For most unnumbered Thursdays, run this from `templates/` and log the date in the notebook.

Replace `YYYY-MM-DD`. Agendas must total **120** minutes (10 + 35 + 55 + 20).

Combined Hub composition is **blocked** until [issue #2](https://github.com/The-Allsparks/FORGE/issues/2) has a robot URL. Driving still happens on whatever robot exists in the shop.

---
id: CB00
title: "Cadence B — drive, auto, inspect"
date: YYYY-MM-DD
meeting_type: B
season_phase: league-development
event_checkpoint: none
status: complete
difficulty: Developing
projects: [TRACE, PEDRO]
active_features: []
---

# Cadence B — drive, auto, inspect

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | CB00 (notebook date if unnumbered) |
| Title | Cadence B — drive, auto, inspect |
| Calendar date | YYYY-MM-DD |
| Relative week | Unnumbered Thursday |
| Meeting type | B |
| Season phase | from `calendar.yaml` cadence window |
| Event checkpoint | none or next event id |
| Difficulty | Developing |

## Driving question

What is today’s one test goal, and can we get 55 minutes of reps?

## Student-facing objective

Review last logs. Repair or tune for 35 minutes. Drive and conventional auto for 55 minutes. Inspect and explain-back in the last 20. Do not debut optionals.

## Robot outcome

Repetition times in the notebook. Conventional auto still the auto. Dashboard driver-practice row updated.

## Prerequisites

Last meeting’s TRACE/paper notes. [pit-and-inspection.md](../season/2026-2027-biobuzz/pit-and-inspection.md) if an event is inside two weeks.

## Vocabulary

one test goal · reps · inspect

## Safety concerns

Blocks or carpet as shop rules. DS stop known. No experimental flags.

## Required hardware

Robot, batteries, gamepads.

## Required software

Team teleop and conventional auto. Optionals off or passive.

## Preparation required before the meeting

Write the test goal on the board (example: 10 driver cycles + 5 autos).

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Last logs; one test goal; safety |
| 35 | Repair / tune / program | Only what blocks today’s reps |
| 55 | Driving / auto reps | Teleop and conventional auto; no HELM execute |
| 20 | Closeout | Inspection, log review, explain-back, next steps, cleanup |

## Mentor demonstration

How to call a stale log vs a missing log — one minute.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Repair if it blocks driving |
| Electrical | Battery discipline |
| Programming | Tune only the conventional auto/teleop |
| Drive team | Reps |
| Documentation | Times + dashboard |

## Integrated build or test activity

The 55-minute rep block **is** the activity.

## Failure-injection scenario

Cover camera or unplug an optional. Drivers must still teleop.

## Evidence to collect

Rep counts/times; TRACE or paper; inspection notes.

## Student explain-back questions

1. What was the test goal?
2. Conventional auto still?
3. Rollback?
4. What gets repaired next Tuesday?

## Assessment or exit check

Reps happened or a written blocker. No new actives.

## Portfolio or engineering-notebook artifact

Times table. Fill the [evidence record](evidence-record.md) (at least Date, Question, Observation, Decision, Next test). Check award tags if a lesson or comparison happened.

## Competition enablement impact

No change.

## Rollback procedure

DS stop. Teleop. Disable table in [student-install.md](../docs/student-install.md).

## Cleanup requirements

Healthy pack installed; robot safe.

## Next-session preparation

Next numbered session or cadence A.

## Hardware-unavailable fallback

Walk the auto. Gamepad practice on a table robot if wheels-off is required.

## Robot-unavailable simulation option

Paper auto + judging Q&A. Still 55 minutes of *something* that is driving-shaped (walk, strategy, gamepad on blocks).

## Links to authoritative project documentation

- [season-plan.md](../season/2026-2027-biobuzz/season-plan.md)
- [projects/pedro-pathing.md](../projects/pedro-pathing.md)
- [pit-and-inspection.md](../season/2026-2027-biobuzz/pit-and-inspection.md)
- [templates/session.md](session.md)

## Mentor notes

If programmers want a new library, the answer is cadence A integration (25 min) or “blocked on #2,” not this 55-minute block.
