---
id: SK01
title: "BIOBUZZ Kickoff analysis and minimum viable robot"
date: 2026-09-12
meeting_type: K
season_phase: kickoff
event_checkpoint: kickoff
status: complete
difficulty: Integration
projects: [TRACE, HELM]
active_features: []
---

# SK01 — BIOBUZZ Kickoff analysis and minimum viable robot

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | SK01 |
| Title | BIOBUZZ Kickoff analysis and minimum viable robot |
| Calendar date | 2026-09-12 (planning input — verify FIRST Nevada) |
| Relative week | Kickoff |
| Meeting type | K |
| Season phase | kickoff |
| Event checkpoint | kickoff |
| Difficulty | Integration |

## Driving question

What is the smallest robot that can score legally and still leave time to drive?

## Student-facing objective

Students will extract scoring tasks from **official** Kickoff materials, choose a minimum viable robot, map mechanisms to software layers, and edit season dates only in `calendar.yaml` as needed.

## Robot outcome

- Written MVP (drive + one scoring action + required park/place if any)
- Mechanism owner list
- No new active software features

## Prerequisites

- Official Kickoff broadcast/materials (FIRST)
- [kickoff-replan-guide.md](../kickoff-replan-guide.md)
- S001–S004 robot as it actually exists

## Vocabulary

minimum viable robot · scoring task · fallback · planning-input date

## Safety concerns

- Crowded Kickoff venues: battery off while transporting
- Do not enable libraries to "try the game"
- HELM season strategy must not copy invented point values into FORGE ([HELM season-strategy.md](https://github.com/The-Allsparks/HELM/blob/main/docs/season-strategy.md))

## Required hardware

- Notebook; robot only if already on site
- Official printed or digital game materials

## Required software

- Browser for official FIRST materials
- FORGE `calendar.yaml` on a mentor laptop

## Preparation required before the meeting

- Bookmark official Kickoff / Game Manual locations when published
- Print the mapping table from the replan guide
- Re-read [ECHO feasibility-decision.md](https://github.com/The-Allsparks/ECHO/blob/main/docs/feasibility-decision.md) as that document requires after 12 Sep 2026

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 15 | Opening | Safety travel/battery; where official rules live; FORGE is not the manual |
| 40 | Game analysis | Watch/read scoring; students list tasks on sticky notes; no software debate yet |
| 30 | MVP selection | Vote constraints: must drive, must be buildable in remaining weeks, must leave Meeting B driving time |
| 20 | Layer mapping | Fill replan table: which tasks need ViDAR/MIMIC/ECHO/HELM **this season** vs never |
| 15 | Closeout | TRACE-style event list of decisions; assign S005 owners; note calendar edits; cleanup |

## Mentor demonstration

Show one example of a team that over-scoped (story, not shame). Show the priority order on the board. Two minutes.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Estimate what can be built before clinic |
| Electrical | Sensors required vs optional |
| Programming | Conventional teleop/auto still required |
| Drive team | Veto features that explode cognitive load |
| Documentation | MVP one-pager |

## Integrated build or test activity

If a robot is present, 0 extra software. Optional 5-minute drive to remember the priority. If the venue forbids robots, skip.

## Failure-injection scenario

Mentor adds a fake "we must use all seven libraries" constraint. Students must reject it using the priority order.

## Evidence to collect

- MVP one-pager
- Mapping table photo
- List of features that stay disabled

## Student explain-back questions

1. What is the MVP in one sentence?
2. Which official document is the rules source?
3. What stays off until evidence exists?
4. Who owns chassis auto?

## Assessment or exit check

Every student can state the MVP. Mentors leave with calendar edit notes.

## Portfolio or engineering-notebook artifact

MVP one-pager. Sticky-note photo.

## Competition enablement impact

No enablement. Possibly **delay** ECHO/HELM/multi-cam if they do not serve MVP.

## Rollback procedure

If the team over-commits on paper, delete those rows from the mapping table before Monday. Do not change library defaults.

## Cleanup requirements

Recycle printouts with game spoilers if the team cares; pack robot if present.

## Next-session preparation

- S005 is vision **only if** MVP needs it; otherwise construction-heavy with sim geometry
- Order parts for MVP immediately

## Hardware-unavailable fallback

Paper/sticky only. Still 120 minutes.

## Robot-unavailable simulation option

Same as fallback — Kickoff is analysis. Use photos of the current drivetrain.

## Links to authoritative project documentation

- [kickoff-replan-guide.md](../kickoff-replan-guide.md)
- [HELM season-strategy.md](https://github.com/The-Allsparks/HELM/blob/main/docs/season-strategy.md)
- [ECHO feasibility](https://github.com/The-Allsparks/ECHO/blob/main/docs/feasibility-decision.md)
- [TRACE student path](https://github.com/The-Allsparks/TRACE/blob/main/docs/student-learning-path.md) (decision events)
- [projects/helm.md](../../../projects/helm.md)

## Mentor notes

Do not let programmers dominate. Drive team has veto on cue/planner cognitive load. Preserve S007 Pedro time.
