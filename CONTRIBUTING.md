# Contributing to FORGE

FORGE is maintained by [The Allsparks](https://github.com/The-Allsparks) (FTC Team 36117) as the season curriculum and integration program for the team's FTC software ecosystem.

FORGE stands for **Framework for Onboarding, Robotics, Guidance, and Education**.

## What this repository is

Curriculum, meeting plans, integration labs, readiness tracking, and student learning paths.

## What this repository is not

A runtime robot library. Do not add Java/Gradle robot code here. Do not make robot projects depend on FORGE. The TeamCode project is tracked in [docs/team-robot-project.md](docs/team-robot-project.md) — fill the URL there; do not invent one. When the team is ready to create that repo, follow [docs/create-robot-project.md](docs/create-robot-project.md). Combined-stack acceptance teaching lives in [docs/stack-acceptance.md](docs/stack-acceptance.md); compile-checked examples belong in the robot repo ([FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4)).

## Setup

```powershell
git clone https://github.com/The-Allsparks/FORGE.git
cd FORGE
python -m pip install -r tools/validation/requirements.txt
python tools/validation/validate_curriculum.py
```

## Rules of engagement

1. **Do not duplicate** large amounts of documentation from ViDAR, AMPER, MIMIC, BEACON, TRACE, HELM, ECHO, or Pedro Pathing. Link to the authoritative file.
2. If a needed target document does not exist, link to the closest authoritative location and record the gap in [docs/research-audit.md](docs/research-audit.md). Do not invent technical guidance.
3. Distinguish **verified fact**, **engineering inference**, and **untested hypothesis**.
4. Never describe an FRC capability as a current FTC capability without a primary source.
5. Do not enable a feature in a session plan merely because its repository exists or its code compiles.
6. Every detailed session must follow [templates/session.md](templates/session.md) and total **exactly 120 minutes**.
7. Preserve robot construction and driver practice. Teaching happens inside build, integration, test, and review blocks.
8. Do not commit secrets, Wi-Fi passwords, tokens, or student PII.
9. Keep dates in [season/2026-2027-biobuzz/calendar.yaml](season/2026-2027-biobuzz/calendar.yaml). Do not bury the only copy of event dates in prose.
10. Run the validator before requesting review.
11. Combined FTC stack acceptance ([FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4)) outranks standalone curriculum expansion that assumes the libraries already compose on a robot.

## Pull requests

- Prefer small, reviewable PRs after this foundation.
- Include motivation, season-phase impact, student/mentor impact, and safety notes.
- Update the readiness dashboard and calendar when session dates or enablement status change.
- Use `Closes #<issue>` only when the PR fully resolves that issue.
- Keep architecture or enablement-policy changes in **draft** PRs until a mentor reviews them.

## Adding a session

1. Copy [templates/session.md](templates/session.md).
2. Name it `season/2026-2027-biobuzz/sessions/S0XX-short-title.md`.
3. Add the session to `calendar.yaml` and `tools/curriculum-manifest.json`.
4. Keep Meeting A and Meeting B block times exact.
5. Include hardware-unavailable and robot-unavailable fallbacks.
6. Run `python tools/validation/validate_curriculum.py`.

## Line endings

The repository stores LF line endings (see [.gitattributes](.gitattributes)).

## License

Contributions are accepted under the MIT License ([LICENSE](LICENSE)). No CLA is required.
