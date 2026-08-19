# Maintaining the schedule

Event dates and session dates live in [season/2026-2027-biobuzz/calendar.yaml](../season/2026-2027-biobuzz/calendar.yaml). That file is the structured source. Prose may quote dates but must not be the only copy.

## Planning-input warning

FIRST Nevada dates in this repository were entered as **planning inputs** on 17 August 2026. If the published calendar changes, update `calendar.yaml` first, then the season README, session front matter, and readiness notes.

## After Kickoff (12 September 2026)

1. Follow [kickoff-replan-guide.md](../season/2026-2027-biobuzz/kickoff-replan-guide.md).
2. Do not delete drivetrain, TRACE, or driver-practice sessions to make room for seven library deep-dives.
3. Map mechanisms to BIOBUZZ tasks. Drop or delay HELM authority, multi-camera ViDAR, and ECHO match audio if they do not serve the minimum viable robot.
4. Do not treat Kickoff as combined-stack Hub acceptance. Re-check [stack-acceptance.md](stack-acceptance.md) pins if FIRST publishes a new season SDK.
5. Re-read [ECHO feasibility decision](https://github.com/The-Allsparks/ECHO/blob/main/docs/feasibility-decision.md) against the Kickoff manual, as that document itself requires.
6. Run `python tools/validation/validate_curriculum.py`.

## When a linked document moves

1. Validation may fail on a GitHub path 404.
2. Update the link to the new path, or to the closest README heading.
3. Add a one-line gap note in [research-audit.md](research-audit.md) if the new location is weaker than the old one.
4. Do not invent replacement technical guidance in FORGE.

## Adding or splitting sessions

See [CONTRIBUTING.md](../CONTRIBUTING.md). Update:

- `calendar.yaml`
- `tools/curriculum-manifest.json`
- `season-plan.md` if the phase intent changes
- the readiness dashboard if a new capability row is needed

## Cadence reminder

Two meetings per week × two hours. Students still have to build the robot. If the outline is overfull, cut advanced software, not driving and construction.
