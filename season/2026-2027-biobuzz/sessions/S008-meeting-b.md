---
id: S008
title: Post-Kickoff week 4 — integration, wiring, clinic prep
date: 2026-10-09
meeting_type: B
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: complete
difficulty: Competition readiness
projects:
- TRACE
- AMPER
- ViDAR
- BEACON
- ECHO
- PEDRO
active_features: []
compressed_week: 4
forge_gate: G5
---

# S008 — Clinic and scrimmage preparation

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S008 |
| Title | Post-Kickoff week 4 — integration, wiring, clinic prep |
| Calendar date | 2026-10-09 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | Compressed week 4 (G5 Mechanical/electrical completion) |
| Meeting type | B |
| Season phase | kickoff-to-clinic |
| Event checkpoint | clinic |
| Forge gate | G5 |
| Difficulty | Competition readiness |

## Driving question

Is Sparkee mechanically and electrically complete enough for clinic data collection?

## Student-facing objective

Students complete wiring (strain relief, service loops), integrate modules, test MIMIC states as hardware allows, prep clinic test card, and review G5 gate.

## Robot outcome

- Mechanically and electrically integrated robot
- Individual mechanisms under software control
- Clinic test card copied to notebook
- G5 gate pass or starter-bot fallback plan


## Prerequisites

- Clinic date is a **planning input** — verify FIRST Nevada
- [pit-and-inspection.md](../pit-and-inspection.md)
- Blank [event-retrospective](../../../templates/event-retrospective.md) for Saturday
- Official inspection PDF: check [2026–2027 event resources](https://ftc-resources.firstinspires.org/ftc/archive/2027/event) (may still be "coming soon")

## Vocabulary

preflight · pit · inspection · systems validation · freeze (for the event)

## Safety concerns

- Transport and battery rules
- No ECHO match audio
- No HELM authority
- No last-minute active flags
- Event Wi-Fi: follow venue rules; Pedro Panels is a shop tool

## Required hardware

- Full robot, spares, cart, tools, batteries
- Printed pit page and dashboard

## Required software

- Meet-like config: TRACE recorder OK if Hub-proven; AMPER/BEACON passive; ViDAR observe-only or unplugged; ECHO off; HELM off; Pedro/fallback auto

## Preparation required before the meeting

Walk [pit-and-inspection.md](../pit-and-inspection.md). Charge batteries. Confirm official 26–27 inspection document status. Packing list on the board.

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | **G5 target** — mech/electrical complete; clinic 10 Oct is measurement only |
| 35 | Repair / tune / program | Wiring integration: strain relief, service loops, labels; MIMIC smoke test per module as wired |
| 55 | Driving reps | Full mechanism cycles under teleop; practice-inspect failures fixed |
| 20 | Closeout | Clinic test card signed; G5 gate review or fallback plan; pit rollback drill |

## Mentor demonstration

Pit layout and one-minute rollback from [pit-and-inspection.md](../pit-and-inspection.md).

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Fasteners, size/starting pose as the **current** manual requires |
| Electrical | Batteries labeled; Hub visible |
| Programming | Config freeze; TRACE quotas if file sink is on |
| Drive team | Reps and callouts |
| Documentation | Saturday test card copied from pit page |

## Integrated build or test activity

Fill the clinic test card (load, lighting, comms, sag, driver workload, auto, inspect/pit). ECHO cue clarity defaults to **skip**.

## Failure-injection scenario

Mentor hides a battery or a zip-tie bag. Team must catch it in packing/inspect.

## Evidence to collect

- Inspection notes
- Auto rep count
- Packed-list photo
- Rollback drill sign-off

## Student explain-back questions

1. What will we not enable at clinic?
2. Who owns rollback in the pit?
3. What is the conventional auto?
4. How do we collect TRACE without PII?

## Assessment or exit check

Test card complete. Robot can run auto or has a written blocker. Packing list signed.

## Portfolio or engineering-notebook artifact

Clinic test card plus packing list.

## Competition enablement impact

No new approvals. Event statuses frozen as disabled/passive/practice-only per dashboard.

## Rollback procedure

Printed dashboard + pit page. Spare DS. Battery disconnect.

## Cleanup requirements

Pack robot; batteries safe; tools inventoried.

## Next-session preparation

Saturday clinic. Sunday/Monday: copy logs off the Hub before overwrite. S009 retrospective.

## Hardware-unavailable fallback

Tabletop inspect of whatever exists; still write the test card and packing list.

## Robot-unavailable simulation option

Walk pit workflow in the shop with empty boxes. Still time a 55-minute "match" as driver communication practice.

## Links to authoritative project documentation

- [docs/season-process.md](../docs/season-process.md)
- [docs/decision-gates.md](../docs/decision-gates.md)
- [docs/pratt-crosswalk.md](../docs/pratt-crosswalk.md)
- [prototype-test-record.md](../../../templates/prototype-test-record.md)
- [gate-review.md](../../../templates/gate-review.md)
- [pit-and-inspection.md](../pit-and-inspection.md)
- [2026–2027 event resources](https://ftc-resources.firstinspires.org/ftc/archive/2027/event)
- [BEACON preflight](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/preflight.md)
- [TRACE mentor guide](https://github.com/The-Allsparks/TRACE/blob/main/docs/mentor-guide.md)
- [ECHO competition readiness](https://github.com/The-Allsparks/ECHO/blob/main/docs/competition-readiness.md)
- [templates/event-retrospective.md](../../../templates/event-retrospective.md)
- [readiness-dashboard.md](../readiness-dashboard.md)

## Mentor notes

Protect Saturday as measurement. Do not promise wins. Do not enable HELM or ECHO in the parking lot.
