# Cadence Meeting A — mechanism of the week

Copy into `season/2026-2027-biobuzz/sessions/` only if you need a dated file. For most unnumbered Tuesdays, run this from `templates/` and log the date in the notebook.

Replace `YYYY-MM-DD` and the mechanism name. Agendas must total **120** minutes (10 + 75 + 25 + 10).

Use the [cadence window intent](../season/2026-2027-biobuzz/calendar.yaml) for this date. Combined Hub composition is **blocked** until [issue #2](https://github.com/The-Allsparks/FORGE/issues/2) has a robot URL.

---
id: CA00
title: "Cadence A — mechanism of the week"
date: YYYY-MM-DD
meeting_type: A
season_phase: league-development
event_checkpoint: none
status: complete
difficulty: Developing
projects: [TRACE]
active_features: []
---

# Cadence A — mechanism of the week

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | CA00 (notebook date if unnumbered) |
| Title | Cadence A — mechanism of the week |
| Calendar date | YYYY-MM-DD |
| Relative week | Unnumbered Tuesday |
| Meeting type | A |
| Season phase | from `calendar.yaml` cadence window |
| Event checkpoint | none or next event id |
| Difficulty | Developing |

## Driving question

Can we repair or finish this week’s mechanism and still observe it before we leave?

## Student-facing objective

75 minutes of physical work on the BIOBUZZ (or preseason) mechanism of the week. 25 minutes of TRACE / AMPER / MIMIC **observation** on what was just built. No new active flags. If there is no TeamCode repo, use paper snapshots and photos.

## Robot outcome

Mechanism progressed. One observation (TRACE event, AMPER voltage if wired, or MIMIC paper state). Conventional teleop still the drive plan.

## Prerequisites

[season-plan.md](../season/2026-2027-biobuzz/season-plan.md) unnumbered-meeting rule. Dashboard printed. Robot repo still **blocked** unless [team-robot-project.md](../docs/team-robot-project.md) has a URL.

## Vocabulary

mechanism of the week · observe · disable

## Safety concerns

Mentor present for energized work. No last-minute enablement. Hard stops before software limits.

## Required hardware

Robot, tools, the mechanism of the week.

## Required software

Meet-like config: optionals off or passive. Paper if no robot project.

## Preparation required before the meeting

Name the mechanism on the board. Charge batteries.

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Mechanism name; safety; no new flags; assignments |
| 75 | Construction | Mechanical/electrical work on that mechanism |
| 25 | Integration | TRACE/AMPER/MIMIC observe what was just built, or paper states |
| 10 | Closeout | TRACE evidence, explain-back, dashboard, cleanup |

## Mentor demonstration

How today’s observation maps to a named state or voltage — two minutes.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Mechanism of the week |
| Electrical | Wiring/strain relief for that mechanism |
| Programming | Observe only; paper if #2 still blocked |
| Drive team | Confirm the mechanism does not steal teleop |
| Documentation | Photo + one TRACE/paper sentence |

## Integrated build or test activity

Observe the new mechanism the same day it was built.

## Failure-injection scenario

Missing sensor: record **missing**, not `0`.

## Evidence to collect

Photo; TRACE or paper event; dashboard tick if a capability actually changed (usually no).

## Student explain-back questions

1. What did we build?
2. How do we turn optionals off?
3. Did software change outputs today?
4. Next physical test?

## Assessment or exit check

Mechanism progressed. Observation exists. No new actives.

## Portfolio or engineering-notebook artifact

Photo and state name.

## Competition enablement impact

No change unless the dashboard already had evidence — default: no change.

## Rollback procedure

DS stop. Omit the new observer from teleop. Conventional drive remains.

## Cleanup requirements

Robot safe; fasteners bagged.

## Next-session preparation

Thursday cadence B: drive and auto.

## Hardware-unavailable fallback

Cardboard mechanism + paper states.

## Robot-unavailable simulation option

Paper MIMIC snapshot + TRACE desktop events named after the mock.

## Links to authoritative project documentation

- [season-plan.md](../season/2026-2027-biobuzz/season-plan.md)
- [student-install.md](../docs/student-install.md)
- [projects/trace.md](../projects/trace.md)
- [templates/session.md](session.md)

## Mentor notes

Protect 75 minutes of build. Do not use unnumbered Tuesdays to “finally add HELM.”
