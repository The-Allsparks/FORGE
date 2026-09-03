# Kickoff replan guide

**Date:** 12 September 2026 — FTC Kickoff, Southern Nevada (planning input; verify).

FORGE does **not** contain BIOBUZZ rules. Use FIRST Kickoff materials and the season Game Manual. P005 reviewed **v0** season rules as study practice only — official Kickoff documents supersede v0. This guide tells the team how to change the schedule without abandoning the robot or compressing software, driving, and judging time.

**After Kickoff:** follow the compressed phase model in [docs/season-process.md](docs/season-process.md), apply the [four tests](docs/guiding-principle.md), and pass **G1 Strategy gate** before custom fabrication at scale ([docs/decision-gates.md](docs/decision-gates.md)). Fill [kickoff-decision-package.md](../../templates/kickoff-decision-package.md) across K001–S002 — Kickoff night does not have to finish every row.

**Process source:** Adapted from Brogan M. Pratt's [*A 12 Week FTC Season Plan That Actually Works*](https://www.youtube.com/playlist?list=PLRHdgFNRLyaM6TmNVVHKqVnnyntDDYDNt) and Pratt, *Why Most FTC Teams Fail (And How Not To)* — see [docs/references.md](docs/references.md). Pratt does not endorse FORGE. Official FIRST rules override both.

## Timebox (fits K001)

Keep construction and a short drive if a robot is on site. Analysis is not a six-hour slide deck.

## Outputs required before leaving Kickoff (G1 start)

Finish the package by **S002** (G1). Kickoff night must produce enough that Monday is not a blank page.

Use the fillable [kickoff-decision-package.md](../../templates/kickoff-decision-package.md). Minimum leaving the venue:

1. [Concept brainstorm record](../../templates/concept-brainstorm.md) with **at least three** distinct robot concepts; target **60–100** visual concepts across four students during post-Kickoff week 1 (scaled from Pratt's process).
2. Scoring **and ranking** notes from the official manual (citations, not invented points).
3. Alliance-role sketch (what we contribute / must not block as a likely weaker partner).
4. Structured **debate notes** on the top two or three concepts (pros, cons, driver workload, build time, four tests).
5. Draft **not yet / will not build** list (ambition lives here, not on Sparkee).
6. Written **minimum viable robot** as R0 + intended R2 ([robot-releases.md](docs/robot-releases.md)).
7. **Starter-bot fallback** identified if custom MVP slips.
8. Initial **risk register** (≥3 risks with owners).
9. [Decision record](../../templates/decision-record.md) if the team compared finalists before MVP lock.
10. Software **tier** draft ([software-sequencing.md](docs/software-sequencing.md)) — not a promise to enable everything.
11. Edits to [calendar.yaml](calendar.yaml) session titles/dates if meetings must move — map to [pratt-crosswalk.md](docs/pratt-crosswalk.md).
12. [Gate review record](../../templates/gate-review.md) for G1 at **S002** (pass / fail / conditional).

S001–S002 add: effort-versus-value table, ranked capability lock, ≥1 low-fidelity game-object proof, dashboard next-test column.

## Mapping exercise

For each scoring task in the official materials:

| Task | Mechanical | Electrical | Teleop | Conventional auto | ViDAR? | MIMIC states? | ECHO? | HELM? |
| ---- | ---------- | ---------- | ------ | ----------------- | ------ | ------------- | ----- | ----- |

If a column is "no" for the MVP, do not schedule a deep-dive that displaces driving. Copy the result into the software-tier table in the decision package.

## Preserve

- Meeting A 75-minute build blocks
- Meeting B 55-minute drive/auto blocks
- TRACE closeout; [prototype-test-record.md](../../templates/prototype-test-record.md) for comparisons
- Conventional auto fallback
- Pedro as chassis owner
- ECHO match-off until evidence
- HELM without authority
- **Decision gates** — missed build gates trigger starter-bot fallback, not stolen programming/driving time
- [Competition runway](docs/robot-releases.md#competition-runway) 12–30 Oct

## Re-read after Kickoff

- [ECHO feasibility-decision.md](https://github.com/The-Allsparks/ECHO/blob/main/docs/feasibility-decision.md)
- [HELM season-strategy.md](https://github.com/The-Allsparks/HELM/blob/main/docs/season-strategy.md) (policy lives in HELM; scoring numbers live in FIRST docs)

## What not to do

- Invent point values in FORGE
- Build a custom scoring mechanism during Kickoff week **to look productive** — cardboard/coroplast interaction proofs and finishing R0 are the allowed physical work
- Enable AMPER limiting, MIMIC homing, ViDAR drive, BEACON intervention, ECHO match audio, or HELM execute because Kickoff was exciting
- Delete S003 comparative tests (or Pedro time) to add a seventh library course
- Treat elevator, capstan, hopper, ViDAR, AMPER, MIMIC, BEACON, TRACE extras, HELM, or ECHO as required for the first competition robot
