---
id: K001
title: "BIOBUZZ Kickoff analysis and minimum viable robot"
date: 2026-09-12
meeting_type: K
season_phase: kickoff
event_checkpoint: kickoff
status: scheduled
difficulty: Integration
projects: [TRACE, HELM]
active_features: []
---

# K001 — BIOBUZZ Kickoff analysis and minimum viable robot

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | K001 |
| Title | BIOBUZZ Kickoff analysis and minimum viable robot |
| Calendar date | 2026-09-12 (planning input; 4:00–6:00 PM unless Kickoff/event) |
| Relative week | Kickoff |
| Meeting type | K |
| Season phase | kickoff |
| Event checkpoint | kickoff |
| Difficulty | Integration |

## Driving question

What is the smallest robot that can score our highest-ranked cycle legally, be repaired in the pit, and still leave time to drive — and did we **debate** our way there instead of defaulting to the first idea?

## Student-facing objective

Students will extract scoring **and ranking** tasks from **official** Kickoff materials, sketch alliance roles, **brainstorm multiple robot concepts**, start the [kickoff-decision-package.md](../../../templates/kickoff-decision-package.md) (including a not-yet list), **debate** the top options with the [four tests](../docs/guiding-principle.md), draft R0–R2, and edit season dates only in `calendar.yaml` as needed. G1 completes at S002.

## Robot outcome

- Written MVP as R0 + intended R2 ([robot-releases.md](../docs/robot-releases.md))
- Kickoff decision package started (scoring/ranking, alliance sketch, not-yet list, software tiers)
- [Concept brainstorm record](../../../templates/concept-brainstorm.md) with at least three concepts
- [Decision record](../../../templates/decision-record.md) if two or more finalists were compared
- No new active software features; no custom scoring fab at the venue

## Prerequisites

- Official Kickoff broadcast/materials (FIRST)
- [kickoff-replan-guide.md](../kickoff-replan-guide.md)
- Preseason robot and evidence **as they actually exist** — see [preseason-deferred-work.md](../docs/preseason-deferred-work.md). P002–P004 were construction; P005 was V0 rules review; electrical/programming/first movement only if P006 completed them; dial-in and Kickoff worksheets only if P007 completed them
- P005 V0 notes are study notes. **Official Kickoff materials supersede V0**
- [preseason-kickoff-gate.md](../docs/preseason-kickoff-gate.md)
- Do not assume a P007 mechanism-lab data set — that lab was deferred after Kickoff
- Do not assume P008 produced Kickoff worksheets — P008 is the FRC tour

## Vocabulary

minimum viable robot · scoring task · ranking · alliance role · not-yet list · four tests · brainstorm · debate · fallback · planning-input date

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
- Bring P007 Kickoff bag (roles, worksheets, learning goals). Tour notes from P008 are optional inspiration and must be checked for FTC scale
- Print [concept-brainstorm.md](../../../templates/concept-brainstorm.md), [kickoff-decision-package.md](../../../templates/kickoff-decision-package.md), and mapping table from the replan guide
- Re-read [ECHO feasibility-decision.md](https://github.com/The-Allsparks/ECHO/blob/main/docs/feasibility-decision.md) as that document requires after 12 Sep 2026
- Assign debate facilitator and timekeeper

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 15 | Opening | Safety travel/battery; where official rules live; FORGE is not the manual; [four tests](../docs/guiding-principle.md); brainstorm rules (quantity before judgment); **do not build a competition robot tonight to look busy** |
| 25 | Game analysis | Scoring **and ranking** from the manual; alliance-role sketch (what we must not block); students list **official** tasks; no software debate yet |
| 20 | Creative brainstorm | Silent sketch then share: **≥3 distinct robot concepts** on [concept-brainstorm.md](../../../templates/concept-brainstorm.md); wild ideas go on the not-yet list |
| 20 | Structured debate | Top 2–3 concepts: pros/cons, build time, driver workload, four tests; drive team may veto high-cognitive-load cues; mentors do not pick for students |
| 15 | Package + MVP | Rank capabilities; draft not-yet / will-not; lock R0 + intended R2 in one sentence; starter-bot fallback |
| 15 | Software tiers | Fill replan table into [software-sequencing.md](../docs/software-sequencing.md) tiers — MVP vs later vs research; HELM execute never |
| 10 | Closeout | Decision record if comparing finalists; TRACE-style decision events; assign S001 package leftover + crude prototype; calendar edit notes; cleanup |

## Mentor demonstration

Show one example of a team that over-scoped (story, not shame). Show the four tests and the priority order on the board. Two minutes on **how to disagree with data** during debate — commit comes at G3.

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
- Kickoff decision package (partial is OK — S001/S002 finish it)
- Debate notes or photo of comparison table
- Decision record **if** finalists were compared
- Not-yet / will-not list
- Mapping / software-tier table photo
- List of features that stay disabled

## Student explain-back questions

1. What is the MVP (R0 + intended R2) in one sentence?
2. Name one concept you **did not** pick and why (not-yet vs will-not).
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

- S001 is vision **only if** MVP needs it; otherwise construction-heavy with sim geometry
- Order parts for MVP immediately; update Onshape with MVP layout when back in shop

## Hardware-unavailable fallback

Paper/sticky only. Still 120 minutes — brainstorm and debate do not require a robot.

## Robot-unavailable simulation option

Same as fallback — Kickoff is analysis. Use photos of the current drivetrain.

## Links to authoritative project documentation

- [kickoff-replan-guide.md](../kickoff-replan-guide.md)
- [templates/kickoff-decision-package.md](../../../templates/kickoff-decision-package.md)
- [docs/guiding-principle.md](../docs/guiding-principle.md)
- [docs/robot-releases.md](../docs/robot-releases.md)
- [templates/concept-brainstorm.md](../../../templates/concept-brainstorm.md)
- [templates/decision-record.md](../../../templates/decision-record.md)
- [HELM season-strategy.md](https://github.com/The-Allsparks/HELM/blob/main/docs/season-strategy.md)
- [ECHO feasibility](https://github.com/The-Allsparks/ECHO/blob/main/docs/feasibility-decision.md)
- [TRACE student path](https://github.com/The-Allsparks/TRACE/blob/main/docs/student-learning-path.md) (decision events)
- [projects/helm.md](../../../projects/helm.md)

## Mentor notes

Do not let programmers dominate debate. Drive team has veto on cue/planner cognitive load. Preserve S003 comparative-test time. **Creativity block is not fluff** — it feeds the decision record and portfolio. If debate runs long, steal from software tiers, not from brainstorm. Students already saw **Pre-Season V0** rules at P005 — use that as practice, then switch to official text. If the chassis still does not drive, MVP must include finishing a legal drivetrain (R0), not only a scoring mechanism. G1 is **not** finished tonight unless the package is actually complete — S002 is the gate review. P008 was an FRC tour; do not look there for missing Kickoff worksheets.
