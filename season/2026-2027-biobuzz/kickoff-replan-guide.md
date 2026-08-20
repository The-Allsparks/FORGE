# Kickoff replan guide

**Date:** 12 September 2026 — FTC Kickoff, Southern Nevada (planning input; verify).

FORGE does **not** contain BIOBUZZ rules. Use FIRST Kickoff materials and the season Game Manual. This guide tells the team how to change the schedule without abandoning the robot or compressing software, driving, and judging time.

**Process source:** Adapted from Brogan M. Pratt's [*A 12 Week FTC Season Plan That Actually Works*](https://www.youtube.com/playlist?list=PLRHdgFNRLyaM6TmNVVHKqVnnyntDDYDNt) — see [docs/references.md](docs/references.md). Pratt does not endorse FORGE.

**After Kickoff:** follow the compressed phase model in [docs/season-process.md](docs/season-process.md) and pass **G1 Strategy gate** before custom fabrication at scale ([docs/decision-gates.md](docs/decision-gates.md)).

## Timebox (fits K001)

Keep construction and a short drive if a robot is on site. Analysis is not a six-hour slide deck.

## Outputs required before leaving Kickoff (G1 Strategy gate)

1. [Concept brainstorm record](../../templates/concept-brainstorm.md) with **at least three** distinct robot concepts; target **60–100** visual concepts across four students during post-Kickoff week 1 (scaled from Pratt's process).
2. Scoring / ranking / penalty / **constraint matrix** from the official manual.
3. Structured **debate notes** on the top two or three concepts (pros, cons, driver workload, build time).
4. Written **minimum viable robot** (drive + one scoring action + place/park as the manual requires).
5. **Starter-bot fallback** identified if custom MVP slips.
6. Initial **risk register** (≥3 risks with owners).
7. [Decision record](../../templates/decision-record.md) if the team compared finalists before MVP lock.
8. Mechanism list with owners ([student-ownership.md](../../templates/student-ownership.md)).
9. Sensors that are *needed* vs *nice*.
10. Software that stays **passive/off** unless it serves the MVP (see [season-process.md](docs/season-process.md#software-protections)).
11. ≥1 low-fidelity physical proof of game-object interaction (week 1 exit).
12. Edits to [calendar.yaml](calendar.yaml) session titles/dates if meetings must move — map to [pratt-crosswalk.md](docs/pratt-crosswalk.md).
13. Updated [readiness-dashboard.md](readiness-dashboard.md) next-test column.
14. [Gate review record](../../templates/gate-review.md) for G1 (pass / fail / conditional).

## Mapping exercise

For each scoring task in the official materials:

| Task | Mechanical | Electrical | Teleop | Conventional auto | ViDAR? | MIMIC states? | ECHO? | HELM? |
| ---- | ---------- | ---------- | ------ | ----------------- | ------ | ------------- | ----- | ----- |

If a column is "no" for the MVP, do not schedule a deep-dive that displaces driving.

## Preserve

- Meeting A 75-minute build blocks
- Meeting B 55-minute drive/auto blocks
- TRACE closeout; [prototype-test-record.md](../../templates/prototype-test-record.md) for comparisons
- Conventional auto fallback
- Pedro as chassis owner
- ECHO match-off until evidence
- HELM without authority
- **Decision gates** — missed build gates trigger starter-bot fallback, not stolen programming/driving time

## Re-read after Kickoff

- [ECHO feasibility-decision.md](https://github.com/The-Allsparks/ECHO/blob/main/docs/feasibility-decision.md)
- [HELM season-strategy.md](https://github.com/The-Allsparks/HELM/blob/main/docs/season-strategy.md) (policy lives in HELM; scoring numbers live in FIRST docs)

## What not to do

- Invent point values in FORGE
- Enable AMPER limiting, MIMIC homing, ViDAR drive, BEACON intervention, ECHO match audio, or HELM execute because Kickoff was exciting
- Delete S003 (Pedro auto) to add a seventh library course
