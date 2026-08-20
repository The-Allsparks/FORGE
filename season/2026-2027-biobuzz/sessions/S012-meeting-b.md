---
id: S012
title: Post-Kickoff week 5 — driver automation if earned; G6 gate review
date: 2026-10-23
meeting_type: B
season_phase: reliability-sprint
event_checkpoint: league-1s-2s
status: complete
difficulty: Competition readiness
projects:
- TRACE
- PEDRO
- AMPER
- BEACON
active_features: []
compressed_week: 5
forge_gate: G6
---

# S012 — League meet 1S/2S preparation

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S012 |
| Title | Post-Kickoff week 5 — driver automation if earned; G6 gate review |
| Calendar date | 2026-10-23 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | Compressed week 5 (G6 Stable software handoff) |
| Meeting type | B |
| Season phase | reliability-sprint |
| Event checkpoint | league-1s-2s |
| Forge gate | G6 |
| Difficulty | Competition readiness |

## Driving question

Did we earn driver automation — and does G6 pass with a stable robot?

## Student-facing objective

Students add driver assists only if demonstrably reliable; complete G6 gate review; prep league meet checklists.#4](https://github.com/The-Allsparks/FORGE/issues/4)).

## Robot outcome

- G6 gate review recorded
- Driver automation list (or explicit none)
- [competition checklists](../../../templates/competition/) owners assigned


## Prerequisites

- 31 October 1S/2S is a **planning input** — verify FIRST Nevada
- Printed [readiness-dashboard.md](../readiness-dashboard.md)
- [pit-and-inspection.md](../pit-and-inspection.md)
- [student-install.md](../../../docs/student-install.md) disable table
- Official inspection PDF status: [2026–2027 event resources](https://ftc-resources.firstinspires.org/ftc/archive/2027/event)

## Vocabulary

frozen · passive · approved (none expected) · rollback

## Safety concerns

- No last-minute active flags
- No HELM, no ECHO match audio
- Transport and battery rules
- Do not add a library at the venue

## Required hardware

Competition robot; spares; batteries on charge; printed pit page and dashboard.

## Required software

Meet OpModes. Optional systems off or passive per dashboard. Pedro/fallback auto.

## Preparation required before the meeting

Print dashboard. Charge batteries. Confirm inspection document status. Packing list on the board.

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Meet is not a debut; assignments; safety; nothing new enables |
| 35 | Repair / tune / program | Reliability only — inspect, fasten, strain-relieve, pack |
| 55 | Driving reps | Driver and auto reps; pit rollback drill; TRACE quotas |
| 20 | Closeout | [Gate review G6](../../../templates/gate-review.md); assign [checklist owners](../../../templates/competition/owner-assignment.md); dashboard freeze note; cleanup |

## Mentor demonstration

Pit rollback: disable flags in one minute using the printed table. Students repeat it.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Inspect and pack |
| Electrical | Batteries, strain relief, Hub visible |
| Programming | Config check; no new adapters |
| Drive team | Short drive only if construction finishes early — otherwise Friday |
| Documentation | Meet card |

## Integrated build or test activity

Rollback drill for each optional on the dashboard ([lab I002](../../../labs/integrated/I002-stack-install-diagnosis.md) paper path if the robot repo is still missing). Record who can disable in the pit.

## Failure-injection scenario

Someone enables HELM or ECHO “just to try” at the meet. Mentor stops the meet config. Students must explain why.

## Evidence to collect

- Meet configuration page
- Rollback drill sign-off
- Packed-list photo
- Dashboard statuses frozen for the event (not “approved”)

## Student explain-back questions

1. What is on in matches?
2. What is the conventional auto if Pedro Pathing misbehaves?
3. Who rolls back, and in what order?
4. What will we measure Saturday — and what will we refuse to debut?

## Assessment or exit check

Rollback drill passed. Pack list complete. No new actives.

## Portfolio or engineering-notebook artifact

Meet configuration page. Link pit card.

## Competition enablement impact

Freeze current statuses. Do not approve new actives. Combined stack remains blocked unless #4 is actually evidenced.

## Rollback procedure

Dashboard plus printed [pit-and-inspection.md](../pit-and-inspection.md) steps. DS stop first.

## Cleanup requirements

Pack. Robot safe for transport. Spare battery labeled.

## Next-session preparation

After meets: unnumbered templates until S013. Use match evidence. Drive Friday if this Monday was too build-heavy.

## Hardware-unavailable fallback

Config on a laptop; packing list; tabletop rollback drill.

## Robot-unavailable simulation option

Tabletop pit drill with printed disable table.

## Links to authoritative project documentation

- [docs/season-process.md](../docs/season-process.md)
- [docs/decision-gates.md](../docs/decision-gates.md)
- [docs/pratt-crosswalk.md](../docs/pratt-crosswalk.md)
- [prototype-test-record.md](../../../templates/prototype-test-record.md)
- [gate-review.md](../../../templates/gate-review.md)
- [safety-and-enablement.md](../../../docs/safety-and-enablement.md)
- [student-install.md](../../../docs/student-install.md)
- [stack-acceptance.md](../../../docs/stack-acceptance.md)
- [readiness-dashboard.md](../readiness-dashboard.md)
- [projects/trace.md](../../../projects/trace.md)
- [projects/amper.md](../../../projects/amper.md)
- [projects/beacon.md](../../../projects/beacon.md)
- [projects/pedro-pathing.md](../../../projects/pedro-pathing.md)

## Mentor notes

31 Oct 1S/2S — verify calendar. Do not treat league as the first combined-stack compile. Keep #2 open until a real robot URL exists.
