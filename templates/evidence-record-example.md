# Evidence record — filled example

This is a **redacted fictional example** for mentors and students. Real records go in the team notebook, not in this repository. No real student data, measurements, or mechanism decisions are represented.

---

| Field | Value |
| ----- | ----- |
| Date | 2026-09-22 |
| Session ID | S007 |
| Student owner or participants | Alex M., Jordan T. |
| Capability | Conventional autonomous |
| Ladder level after this evidence | 3 |
| Competition status after this evidence | practice-only |

## What question were we trying to answer?

_We wanted to know if the robot could drive to the scoring zone and come back without drifting._

## What did we think would happen?

_We thought the Pedro path would end within about 2 inches of the start because the field is flat._

## What other options did we consider?

_We also looked at a simple timed drive. We picked Pedro because it corrects for wheel slip and we can reuse the path at different speeds._

## What did we try?

Ran the Pedro path five times on the practice field.

## What did we measure or observe?

_We saw the robot ended 1–4 inches from the start each time. The number was 2.5 inches average._

## Was anything unexpected?

_We did not expect the fourth run to drift 4 inches left. The left rear wheel was loose._

## What did we decide, and why?

_We decided to tighten the wheel and retest next Meeting B because one loose wheel changed the result more than we expected._

## What changed on the robot, CAD, or software?

Tightened left rear wheel. No software change.

## TRACE or other log (redacted path or snippet)

Paper: five run end-positions marked on tape with a ruler.

## Failure injection result

N/A this session.

## Student explain-back (one sentence each)

1. Alex: "The auto was repeatable except when hardware was loose."
2. Jordan: "Pedro owns the chassis, and we can turn it off and drive manually if it breaks."

## Benefit demonstrated? (yes/no + why)

Yes — five repeatable runs. Not match-approved yet (practice-only).

## Rollback exercised? (yes/no)

Yes — Jordan drove teleop-only after the loose-wheel run.

## Known risks

Loose fasteners change auto accuracy.

## Next required test

Five more runs after wheel fix. Then practice with scoring action.

## Award tags

- [x] **A** — Engineering process (we followed question → build → test → learn → change)
- [x] **B** — Lesson applied (something broke or surprised us and we changed the robot)
- [ ] **C** — Comparing choices (we looked at two or more options and picked one)
- [ ] **D** — Math choices (a number helped us decide)
- [ ] Innovate (creative or unique design element)
- [ ] Control (sensor or software feedback improved the robot)
- [ ] Design (elegant, efficient, practical to maintain)
