# Quantified acceptance criteria

Do not record "it worked." Record a **claim**, a **test method**, a **sample**, and an **interpretation**.

Canonical test form: [prototype-test-record.md](../../../templates/prototype-test-record.md). This page is the method for choosing sample sizes and thresholds. Do not copy these numbers into every session.

**Strategic influence:** Pratt, *Why Most FTC Teams Fail (And How Not To)* (adapted; not endorsed). Official FIRST inspection and match rules still apply.

## How to set n and the pass line

The Allsparks meet about **four hours per week**. A 20-for-20 reliability trial is rarely possible in one session and is not automatically more scientific than an honest smaller sample.

Set three numbers **before** the test, write them on the board, then run:

| Number | Meaning | How to choose |
| ------ | ------- | ------------- |
| **n** | Planned trials | Fit the remaining block. Typical Meeting B driving block (~55 min) supports **8–12** full cycles if reset is fast, or **3–5** if each trial needs a rebuild. |
| **k** | Successes required | Higher when failure costs the match (jam that needs tools, auto that sets ranking). Lower when the test is comparative (G2). |
| **Stop rule** | When to abort | Safety, game-piece damage, or a failure mode that needs a design change before more trials. |

### Defaults (use unless the team writes a better set)

| Claim type | Default n | Default pass | Notes |
| ---------- | --------- | ------------ | ----- |
| Comparative prototype (G2) | ≥3 per concept | Rank by measurements, not a pass/fail trophy | Already required at G2. |
| Match-critical mechanism (R2/R3) | 8–12 in one sitting | Team sets k (example: 8/10) | Record **all** times, not the best. |
| Autonomous path (R1) | 8–10 consecutive practice runs | Example: 7/10, or declare teleop-only | G6. |
| Repair time | 3 timed pits | Median at or under the target the team wrote | Use [common-repairs.md](../../../templates/competition/common-repairs.md). |
| Degraded operation | 3 trials in the failed configuration | Robot remains driveable and safe | See [failure-mode-drills.md](failure-mode-drills.md). |

**Never** treat one success, a CAD screenshot, or a desktop compile as acceptance.

## Required measurements (pick those that apply)

| Metric | What to record | Why |
| ------ | -------------- | --- |
| Success count | k / n, with failure reasons | Stops "it worked." |
| Cycle-time **distribution** | Every trial; median and range (or min/median/max) | Fastest cycle is a brag, not a match plan. |
| Jam frequency and recovery | Jams per n; time to clear; tools needed | Repairability test. |
| Autonomous success rate | Completes / attempts; where it failed | Ranking and alliance trust. |
| Repair time | Minutes, who did it, spare used | Pit reality. |
| Battery / thermal | Pack ID, sag notes, motor/controller temp if measured | AMPER observes; it does not fix wiring. |
| Degraded performance | Same cycle with sensor covered, motor unplugged (safe), or auto skipped | Match will not be ideal. |

Interpretation is a separate sentence from the raw table: what the numbers mean for G3/G6/G7.

## CAD and theory

CAD, sketches, and calculations **inform** a test; they do not replace it. [Math evidence](../../../templates/math-evidence.md) must say whether the robot matched the number. G3 may authorize fabrication from CAD **after** G2 physical comparison for that mechanism family.

## Mentors

- Stop one-trial design changes.
- Do not raise n mid-test to chase a pass.
- If time expires, report the actual k/n and whether the claim is **unsupported** — that is a valid G2/G6 outcome.
