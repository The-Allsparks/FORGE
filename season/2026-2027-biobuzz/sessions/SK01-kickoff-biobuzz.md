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

What is the smallest robot that can score legally and still leave time to drive — and did we **debate** our way there instead of defaulting to the first idea?

## Student-facing objective

Students will extract scoring tasks from **official** Kickoff materials, **brainstorm multiple robot concepts**, **debate** the top options with evidence and drive-team veto, select a minimum viable robot, map mechanisms to software layers, and edit season dates only in `calendar.yaml` as needed.

## Robot outcome

- Written MVP (drive + one scoring action + required park/place if any)
- [Concept brainstorm record](../../../templates/concept-brainstorm.md) with at least three concepts
- [Decision record](../../../templates/decision-record.md) if two or more finalists were compared
- Mechanism owner list
- No new active software features

## Prerequisites

- Official Kickoff broadcast/materials (FIRST)
- [kickoff-replan-guide.md](../kickoff-replan-guide.md)
- P003, S001, S002, P004, P005 robot and evidence as they actually exist
- [preseason-kickoff-gate.md](../docs/preseason-kickoff-gate.md)

## Vocabulary

minimum viable robot · scoring task · brainstorm · debate · fallback · planning-input date

## Safety concerns

- Crowded Kickoff venues: battery off while transporting
- Do not enable libraries to "try the game"
- HELM season strategy must not copy invented point values into FORGE ([HELM season-strategy.md](https://github.com/The-Allsparks/HELM/blob/main/docs/season-strategy.md))
- Debate must stay respectful — attack ideas, not people

## Required hardware

- Notebook; sticky notes or whiteboard; robot only if already on site
- Official printed or digital game materials

## Required software

- Browser for official FIRST materials
- FORGE `calendar.yaml` on a mentor laptop
- Onshape optional — sketch MVP layout after MVP lock if time in closeout

## Preparation required before the meeting

- Bookmark official Kickoff / Game Manual locations when published
- Print [concept-brainstorm.md](../../../templates/concept-brainstorm.md) and mapping table from the replan guide
- Re-read [ECHO feasibility-decision.md](https://github.com/The-Allsparks/ECHO/blob/main/docs/feasibility-decision.md) as that document requires after 12 Sep 2026
- Assign debate facilitator and timekeeper

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 15 | Opening | Safety travel/battery; where official rules live; FORGE is not the manual; brainstorm rules (quantity before judgment) |
| 25 | Game analysis | Watch/read scoring; students list **official** tasks on sticky notes; no software debate yet |
| 25 | Creative brainstorm | Silent sketch then share: **≥3 distinct robot concepts** on [concept-brainstorm.md](../../../templates/concept-brainstorm.md); wild ideas allowed |
| 20 | Structured debate | Top 2–3 concepts: pros/cons, build time, driver workload; drive team may veto high-cognitive-load cues; mentors do not pick for students |
| 15 | MVP selection | Vote constraints: must drive, buildable before clinic, preserves Meeting B driving time; lock MVP in one sentence |
| 10 | Layer mapping | Fill replan table: which tasks need ViDAR/MIMIC/ECHO/HELM **this season** vs never |
| 10 | Closeout | Decision record if comparing finalists; TRACE-style decision events; assign S009 owners; calendar edit notes; cleanup |

## Mentor demonstration

Show one example of a team that over-scoped (story, not shame). Show the priority order on the board. Two minutes on **how to disagree with data** during debate.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Sketch concepts; estimate build time for each |
| Electrical | Sensors required vs optional per concept |
| Programming | Conventional teleop/auto still required for every concept |
| Drive team | Veto features that explode cognitive load; speak in debate |
| Documentation | Brainstorm form; debate notes; MVP one-pager |

## Integrated build or test activity

If a robot is present, 0 extra software. Optional 5-minute drive to remember the priority. If the venue forbids robots, skip. Optional: start Onshape MVP layout sketch in closeout if laptops available.

## Failure-injection scenario

Mentor adds a fake "we must use all seven libraries" constraint. Students must reject it using the priority order.

## Evidence to collect

- Concept brainstorm record (≥3 concepts)
- Debate notes or photo of comparison table
- Decision record **if** finalists were compared
- MVP one-pager
- Mapping table photo
- List of features that stay disabled

## Student explain-back questions

1. What is the MVP in one sentence?
2. Name one concept you **did not** pick and why.
3. Which official document is the rules source?
4. What stays off until evidence exists?
5. Who owns chassis auto?

## Assessment or exit check

Every student can state the MVP and one rejected alternative. Mentors leave with calendar edit notes.

## Portfolio or engineering-notebook artifact

Brainstorm photo + MVP one-pager + decision record (Think topic C).

## Competition enablement impact

No enablement. Possibly **delay** ECHO/HELM/multi-cam if they do not serve MVP.

## Rollback procedure

If the team over-commits on paper, delete those rows from the mapping table before Monday. Do not change library defaults.

## Cleanup requirements

Recycle printouts with game spoilers if the team cares; pack robot if present.

## Next-session preparation

- S009 is vision **only if** MVP needs it; otherwise construction-heavy with sim geometry
- Order parts for MVP immediately; update Onshape with MVP layout when back in shop

## Hardware-unavailable fallback

Paper/sticky only. Still 120 minutes — brainstorm and debate do not require a robot.

## Robot-unavailable simulation option

Same as fallback — Kickoff is analysis. Use photos of the current drivetrain.

## Links to authoritative project documentation

- [kickoff-replan-guide.md](../kickoff-replan-guide.md)
- [templates/concept-brainstorm.md](../../../templates/concept-brainstorm.md)
- [templates/decision-record.md](../../../templates/decision-record.md)
- [HELM season-strategy.md](https://github.com/The-Allsparks/HELM/blob/main/docs/season-strategy.md)
- [ECHO feasibility](https://github.com/The-Allsparks/ECHO/blob/main/docs/feasibility-decision.md)
- [TRACE student path](https://github.com/The-Allsparks/TRACE/blob/main/docs/student-learning-path.md) (decision events)
- [projects/helm.md](../../../projects/helm.md)

## Mentor notes

Do not let programmers dominate debate. Drive team has veto on cue/planner cognitive load. Preserve S011 Pedro time. **Creativity block is not fluff** — it feeds the decision record and portfolio. If debate runs long, steal from layer mapping, not from brainstorm.
