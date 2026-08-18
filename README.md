# FORGE

**Framework for Onboarding, Robotics, Guidance, and Education**

Season curriculum, meeting plans, integration labs, readiness gates, and student learning paths for [The Allsparks](https://github.com/The-Allsparks) FTC software ecosystem.

FORGE is a **curriculum and season-orchestration** repository. It is **not** a runtime robot library and must not become a dependency of the robot code.

Built by **[The Allsparks](https://github.com/The-Allsparks)** (FTC Team **#36117**).

> **Disclaimer:** FORGE is community-developed and unofficial. It is **not** affiliated with or endorsed by FIRST, REV Robotics, Pedro Pathing, or other referenced vendors. Event dates are planning inputs and must be verified if the FIRST Nevada calendar changes. Teams must verify legality against the current-season FTC Game Manual.

---

## What FORGE owns

- Season-level sequencing
- Session-by-session meeting plans
- Cross-project integration
- Student onboarding
- Mentor facilitation guidance
- Assessments and explain-backs
- Evidence requirements
- Readiness tracking
- Event checkpoints
- Hardware and simulation fallback activities
- Competition enablement and rollback decisions

## What FORGE does not own

The individual repositories remain authoritative for source code, APIs, installation, technical architecture, safety constraints, detailed project-specific curriculum, and project-specific enablement gates.

| Project | Role on the robot |
| ------- | ----------------- |
| [ViDAR](https://github.com/The-Allsparks/ViDAR) | Spatial vision, perception, and localization |
| [AMPER](https://github.com/The-Allsparks/AMPER) | Electrical and power-system observation |
| [MIMIC](https://github.com/The-Allsparks/MIMIC) | Mechanism lifecycle, state, and safety |
| [BEACON](https://github.com/The-Allsparks/BEACON) | Communications health and recovery |
| [TRACE](https://github.com/The-Allsparks/TRACE) | Structured logging, evidence, and replay |
| [HELM](https://github.com/The-Allsparks/HELM) | High-level behavior and intent coordination |
| [ECHO](https://github.com/The-Allsparks/ECHO) | Sound-based directional guidance for the driver |
| [Pedro Pathing](https://pedropathing.com/) | Chassis motion |

Do not construct seven independent courses. Teach these as related layers of one robot.

---

## Current status

**First combined-stack acceptance priority:** [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4). A library that compiles on a desktop is not an FTC-ready stack. See [docs/stack-acceptance.md](docs/stack-acceptance.md). Do not invent a TeamCode URL ([issue #2](https://github.com/The-Allsparks/FORGE/issues/2)).

| Item | Status |
| ---- | ------ |
| Season | 2026–2027 BIOBUZZ (game details unknown until Kickoff) |
| Foundation | Session contract, calendar, complete sessions S001–S019 and SK01 |
| Combined stack acceptance | **Open P0.** Install matrix and conventions documented; compile-checked Hub evidence blocked on the robot project |
| Competition enablement | All optional advanced features start **disabled** or **passive** |
| Hardware validation of linked libraries | **Not claimed.** See each project README |

**Library completion for scheduling:** treat ViDAR, AMPER, MIMIC, BEACON, TRACE, HELM, and ECHO as functionally complete after the week of **24 August 2026**. That is not combined Control Hub acceptance. Remaining season work is onboarding, integration, calibration, testing, and field validation.

---

## Team constraints

The Allsparks are a small rookie FTC team.

- Two meetings per week, about two hours each
- Students must build the physical robot
- Students must learn mechanical and electrical construction
- The team needs substantial driver practice
- The team needs a reliable conventional autonomous
- Advanced libraries must support the robot rather than consume the season

**Priority order**

working robot → reliable mechanisms → driver practice → conventional autonomous → evidence collection → advanced autonomy

Combined FTC stack acceptance ([#4](https://github.com/The-Allsparks/FORGE/issues/4)) is the integration gate in front of any claim that those libraries already compose on a robot.

---

## Start here

| Audience | Start |
| -------- | ----- |
| Students | [docs/student-guide.md](docs/student-guide.md) |
| Mentors | [docs/mentor-guide.md](docs/mentor-guide.md) |
| This season | [season/2026-2027-biobuzz/README.md](season/2026-2027-biobuzz/README.md) |
| Combined stack gate | [docs/stack-acceptance.md](docs/stack-acceptance.md) |
| Student install / disable | [docs/student-install.md](docs/student-install.md) |
| Robot code (not this repo) | [docs/team-robot-project.md](docs/team-robot-project.md) |
| First meeting | [season/2026-2027-biobuzz/sessions/S001-system-map-safety-trace.md](season/2026-2027-biobuzz/sessions/S001-system-map-safety-trace.md) |
| Readiness | [season/2026-2027-biobuzz/readiness-dashboard.md](season/2026-2027-biobuzz/readiness-dashboard.md) |
| Event dates | [season/2026-2027-biobuzz/calendar.yaml](season/2026-2027-biobuzz/calendar.yaml) |

---

## Weekly cadence

**Meeting A — build and integrate** (120 minutes)

- 10 minutes: goals, vocabulary, safety, and assignments
- 75 minutes: mechanical/electrical construction
- 25 minutes: software integration on what was just built
- 10 minutes: TRACE evidence, student explain-back, documentation, and cleanup

**Meeting B — test and practice** (120 minutes)

- 10 minutes: review previous logs and define the test goal
- 35 minutes: repair, tuning, calibration, or programming
- 55 minutes: driving and autonomous repetitions
- 20 minutes: inspection, log review, student explain-back, and next steps

Teaching happens inside those blocks. Do not add a long independent lecture.

---

## Enablement ladder

No advanced feature becomes competition-active merely because its code is complete.

1. Desktop test
2. Simulation or fake hardware
3. Passive robot observation
4. Controlled hardware test
5. Practice-field test
6. Full mock match
7. Scrimmage or lower-risk event
8. Competition approval

Details: [docs/safety-and-enablement.md](docs/safety-and-enablement.md).

---

## Repository map

```text
docs/           How FORGE works (architecture, teaching model, safety)
season/         This year's calendar, sessions, and readiness
projects/       Deep links into each library (not copies of those manuals)
learning-paths/ Mechanical, electrical, programming, drive, documentation
labs/           Integrated, simulated, and hardware labs
assessments/    Rubrics, explain-backs, readiness checks
templates/      Reusable session, lab, and evidence forms
tools/          Manifest and validation
```

---

## Validate locally

```powershell
python -m pip install -r tools/validation/requirements.txt
python tools/validation/validate_curriculum.py
```

---

## Continue the work

Open issues and milestones are the handoff. **Next:** keep [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4) as the combined-stack epic; keep [#2](https://github.com/The-Allsparks/FORGE/issues/2) open until a real robot URL exists. Do not expand sessions as if the stack already composes on a Control Hub. Schedule maintenance: [docs/maintaining-the-schedule.md](docs/maintaining-the-schedule.md).

## License

MIT — same open-source license family as the other Allsparks libraries. See [LICENSE](LICENSE).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), [SECURITY.md](SECURITY.md), and [AGENTS.md](AGENTS.md).
