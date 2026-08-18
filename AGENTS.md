# Agent instructions for FORGE

FORGE is the season-orchestration repository for The Allsparks (FTC Team 36117). It is student-facing curriculum, not a robot runtime.

## Non-negotiable constraints

- Do **not** add robot libraries, Gradle modules, or TeamCode here. If the team robot GitHub URL is unknown, update [docs/team-robot-project.md](docs/team-robot-project.md) rather than inventing a clone path.
- Do **not** make ViDAR, AMPER, MIMIC, BEACON, TRACE, HELM, ECHO, or the robot project depend on FORGE.
- Do **not** duplicate project manuals. Link to authoritative files in those repositories.
- Do **not** invent APIs, safety limits, voltage thresholds, or game rules. If a document is missing, link to the closest source and record the gap.
- Do **not** competition-enable a feature because code exists. Enablement requires evidence, safe failure, rollback, student understanding, benefit, and repeatability.
- Pedro Pathing owns chassis motion. HELM must not take chassis authority in this curriculum.
- Preserve Meeting A / Meeting B timing. Every session agenda must total 120 minutes.
- Priority order: working robot → reliable mechanisms → driver practice → conventional autonomous → evidence collection → advanced autonomy.

## Authoritative owners

| Concern | Owner |
| ------- | ----- |
| Source, APIs, install, architecture, project curriculum, project gates | The named project repository |
| Season sequence, meeting plans, integration, onboarding, assessments, readiness, event checkpoints | FORGE |
| Chassis motion | [Pedro Pathing](https://pedropathing.com/) |

## Before editing curriculum

1. Read [docs/architecture.md](docs/architecture.md), [docs/curriculum-model.md](docs/curriculum-model.md), and [docs/safety-and-enablement.md](docs/safety-and-enablement.md).
2. Read the project page under `projects/` for every library the session touches.
3. Prefer deep links already verified in [docs/research-audit.md](docs/research-audit.md).
4. Keep event dates only in `season/2026-2027-biobuzz/calendar.yaml` as the structured source.

## Validation

Run:

```powershell
python tools/validation/validate_curriculum.py
```

Do not merge changes that fail validation.

## Session contract

Every detailed session must include the headings in [templates/session.md](templates/session.md). Distinguish:

- Learning objective
- Robot deliverable
- Evidence required
- Competition-readiness decision
