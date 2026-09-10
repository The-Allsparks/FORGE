---
name: github-design-review
description: >-
  Turn a plan or shop decision into a GitHub design-review issue students and
  mentors can accept before implementation. Use when the user asks to file a
  GitHub issue (not Jira), capture a TRACE/FORGE/library plan for team review,
  write a phase or enablement issue, or post a student-learning issue.
---

# GitHub design-review issue

FORGE is curriculum. Issues are how the team **reviews a plan before anyone codes**. GitHub, not Jira.

Do **not** start implementation from the issue until maintainers accept it. Say that in the body.

## Before writing

1. Ask which repo if unclear (FORGE vs TRACE vs ECHO vs BEACON vs FtcRobotController).
2. Show a draft. Post only after the user says to post.
3. Use ASCII punctuation. No em dashes.

## Pick a template

| Repo / kind | Template |
| --- | --- |
| FORGE session, sequence, lab | `.github/ISSUE_TEMPLATE/curriculum.md` — title `[curriculum] ` |
| FORGE competition status / rollback | `.github/ISSUE_TEMPLATE/enablement.md` — title `[enablement] ` |
| TRACE phased library work | TRACE `.github/ISSUE_TEMPLATE/phase_work.md` — title `[phase] ` |
| Other Allsparks library | Same TRACE-style headings even if that repo has no template |

## Required headings

Every design-review issue needs:

1. **Problem** — what students or the robot cannot do today
2. **Student learning objective** — what a student can *do* or *say* after this ships
3. **Scope / out of scope**
4. **Acceptance criteria** — checkboxes
5. **This issue is a design review. Do not start implementation until maintainers accept the plan.**

Also include when they apply:

- **Hardware validation:** none / desktop / Control Hub / robot / match
- **Rollback or disable**
- **Parent epic / roadmap issue**
- FORGE **four tests** (top-ranked need, reliable evidence, team-repairable, protects practice time) for enablement or “should this be on the competition robot?”
- TRACE: architecture impact, validation plan, documentation required

## Voice

- Kid-readable. Short sentences. Name the robot behavior, not the framework buzzword.
- “We learned with the kids…” belongs in a PR later, not as a substitute for a student objective.
- Do not invent APIs, voltage limits, or game rules. Link the owning repo.
- Do not competition-enable because code exists ([FORGE AGENTS.md](../../AGENTS.md)).

## After accept

Implementation is a different task. File or update the issue; do not silently start coding.
