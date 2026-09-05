# 2026–2027 BIOBUZZ

Season folder for The Allsparks. Game details are unknown until Kickoff.

**Season process:** Compressed competition-one cycle adapted from Brogan M. Pratt's [*A 12 Week FTC Season Plan That Actually Works*](https://www.youtube.com/playlist?list=PLRHdgFNRLyaM6TmNVVHKqVnnyntDDYDNt), with decision tests from *Why Most FTC Teams Fail (And How Not To)* — [docs/season-process.md](docs/season-process.md), [docs/guiding-principle.md](docs/guiding-principle.md), [docs/decision-gates.md](docs/decision-gates.md), [docs/references.md](docs/references.md). Pratt does not endorse FORGE. Official FIRST rules override Pratt.

**Dates in [calendar.yaml](calendar.yaml) are planning inputs.** Verify them if the FIRST Nevada calendar changes. Regular shop meetings are **4:00–6:00 PM** (Monday Meeting A, Friday Meeting B; Wednesday preseason exceptions use type S). Session **topics** after P005 variance: [preseason-deferred-work.md](docs/preseason-deferred-work.md).

## Session files (fixed paths)

Every numbered meeting uses **`{ID}-meeting-{type}.md`** where `type` is `a` (Monday), `b` (Friday), `s` (Wednesday preseason), `k` (Kickoff), or `e` (event day). Example: [S001-meeting-a.md](sessions/S001-meeting-a.md).

**Do not rename session files** when the topic changes. Edit the `title` field in front matter and in `calendar.yaml` instead. After Kickoff, S001 is typically MVP build; later weeks might retitle the same file to match the mechanism of the week.

| Prefix | Meaning |
| ------ | ------- |
| **P001–P008** | Preseason |
| **K001** | Kickoff |
| **S001+** | Official season |
| **E004, E005** | Event days replacing a regular meeting |

## Start this week

1. Read [season-plan.md](season-plan.md) and [preseason-deferred-work.md](docs/preseason-deferred-work.md)
2. Open [P007-meeting-a.md](sessions/P007-meeting-a.md) — **next meeting (2026-09-07)** — last shop night: finish electrical, programming bring-up, and first movement, then Kickoff worksheets. P006 was a code walkthrough only. Do not open as drivetrain dial-in. Wheels off the floor before any floor driving.
3. Update [readiness-dashboard.md](readiness-dashboard.md) in the last 10–20 minutes

## Priority

working robot → reliable mechanisms → driver practice → conventional autonomous → evidence collection → advanced autonomy

**Integration gate:** [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4) — combined FTC stack acceptance. Robot project: [The-Allsparks/FtcRobotController](https://github.com/The-Allsparks/FtcRobotController).

## First Nevada checkpoints (from calendar.yaml)

| Date | Event |
| ---- | ----- |
| 2026-09-12 | FTC Kickoff, Southern Nevada |
| 2026-10-10 | Clinic / scrimmage |
| 2026-10-31 | League Meets 1S and 2S |
| 2026-12-05 | League Meets 3S and 4S |
| 2027-01-09 | League Meets 5S and 6S |
| 2027-01-22 – 2027-01-23 | League Tournament |
| 2027-02-19 – 2027-02-20 | Nevada State Championship (if advancing) |

## Written sessions

**Preseason:** P001–P008 (construction + V0 rules + P006 code-walkthrough variance recorded; remaining shop time is P007 bring-up/first movement plus Kickoff prep; P008 is the FRC tour — not the original mechanism lab).

**Kickoff:** K001.

**Season:** S001–S042 milestone and cadence sessions; **E004** (League Tournament day 1) and **E005** (State day 1, contingent) replace regular meetings on those dates.

Team robot GitHub: [The-Allsparks/FtcRobotController](https://github.com/The-Allsparks/FtcRobotController). Shop construction and driving still proceed. Hub stack evidence does not. Detail: [team-robot-project.md](../../docs/team-robot-project.md).

Combined-stack teaching: [stack-acceptance.md](../../docs/stack-acceptance.md), [student-install.md](../../docs/student-install.md), [lab I002](../../labs/integrated/I002-stack-install-diagnosis.md).

Pit packing, rollback, and clinic test card: [pit-and-inspection.md](pit-and-inspection.md) (not a substitute for the official FIRST checklist).

Competition checklists: [templates/competition/](../../templates/competition/).

## Award and portfolio traceability

[docs/award-and-portfolio-traceability.md](../../docs/award-and-portfolio-traceability.md) — maps FORGE activities to Think, Innovate, Control, Design, and other judged-award criteria. Focused bets (not yet locked): [docs/award-strategy.md](docs/award-strategy.md). Print the Think table and A201 checklist. Prototype records: [prototype-test-record.md](../../templates/prototype-test-record.md).

## Kickoff replan

After 12 September 2026: [kickoff-replan-guide.md](kickoff-replan-guide.md) and [kickoff-decision-package.md](../../templates/kickoff-decision-package.md). Pass **G1 Strategy gate** before custom fabrication at scale. Apply the [four tests](docs/guiding-principle.md).

## Pratt crosswalk

Session ↔ compressed week ↔ gate mapping: [docs/pratt-crosswalk.md](docs/pratt-crosswalk.md). Failure-mode video audit: [docs/pratt-why-teams-fail.md](docs/pratt-why-teams-fail.md). Integration report: [pratt-why-teams-fail-integration.md](pratt-why-teams-fail-integration.md). Preseason variance: [docs/preseason-deferred-work.md](docs/preseason-deferred-work.md). Staged releases: [docs/robot-releases.md](docs/robot-releases.md).
