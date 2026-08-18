# Research audit

Audit date: **17 August 2026**. Local checkouts of The-Allsparks project repositories were read alongside GitHub. This file records what FORGE should teach, what it must not invent, and which links were verified at audit time.

Linked repositories evolve. If a path 404s, follow [maintaining-the-schedule.md](maintaining-the-schedule.md).

## Organization snapshot

Public Allsparks software libraries used by FORGE:

| Repo | Description (from GitHub) |
| ---- | ------------------------- |
| [ViDAR](https://github.com/The-Allsparks/ViDAR) | Robot-space situational awareness |
| [AMPER](https://github.com/The-Allsparks/AMPER) | Adaptive motor power monitoring |
| [MIMIC](https://github.com/The-Allsparks/MIMIC) | Mechanism lifecycle, motion, calibration, interlock, safety |
| [BEACON](https://github.com/The-Allsparks/BEACON) | Communications health, preflight, safe-state coordination |
| [TRACE](https://github.com/The-Allsparks/TRACE) | Telemetry, event recording, analysis, replay |
| [HELM](https://github.com/The-Allsparks/HELM) | High-level execution and logic manager |
| [ECHO](https://github.com/The-Allsparks/ECHO) | Environmental Cue and Heading Output |

Also in the org, **not** FORGE runtime dependencies: `ftc-dev-tools`, `ftc-team-analysis`, `SponsorshipPlan`.

Pedro Pathing is **not** an Allsparks repository. Authoritative docs: [pedropathing.com](https://pedropathing.com/), [docs introduction](https://pedropathing.com/docs/pathing), [Pedro-Pathing/PedroPathing](https://github.com/Pedro-Pathing/PedroPathing).

Community files: TRACE, AMPER, MIMIC, BEACON, HELM, and ECHO share MIT licenses and Contributor Covenant / SECURITY / CONTRIBUTING patterns. FORGE copies that family (MIT, 2026 The Allsparks FTC Team 36117). ViDAR has LICENSE + CONTRIBUTING; it did not have CODE_OF_CONDUCT.md or SECURITY.md in the audited tree.

## Strongest student/mentor patterns (used by FORGE)

From TRACE, HELM, ECHO, AMPER, MIMIC, and BEACON:

- Phased ladder; do not skip rungs
- Each phase optional, reversible, feature-flagged, disabled by default until evidence
- Short vocabulary; explain-out-loud checkpoint before the next robot enablement
- Passive observation before actuation
- Fake hardware / desktop tests as first-class
- Explicit "what this cannot solve"
- Mentors protect construction, electrical debugging, and conventional autos from framework theater
- Distinguish verified fact vs inference vs hypothesis

TRACE is the primary curriculum reference for evidence closeout. FORGE does not copy TRACE's eight software phases as the season calendar.

## Project records

### TRACE

| Field | Record |
| ----- | ------ |
| Teaches | Measurement vs decision vs command vs event; ordered reconstruction; CSV/.tlog; bounded storage; later replay is gated |
| Prerequisites | Desktop JVM for unit tests; later Control Hub file storage through team adapters |
| Difficulty | Foundation (events) through competition readiness (match recorder). Replay is advanced and fail-closed |
| Hardware | None for Phases 0–1 classroom; Control Hub storage for file sink |
| Simulation | Desktop tests; memory sink |
| Evidence | Events, typed records, CSV, `.tlog`, drop counts |
| Safety | Observational in Phases 0–5; never energizes outputs; no PII in logs; `REPLAY` throws |
| Competition | Recorder may be on; must not command hardware; quotas before events |
| Integration | Records others; must not own vision, pathing, power, mechanisms, or comms |
| Maturity at audit | 0.1.0-SNAPSHOT; Phases 0–3 desktop-validated; **not Control Hub tested** |

Verified links: [README](https://github.com/The-Allsparks/TRACE/blob/main/README.md), [student path](https://github.com/The-Allsparks/TRACE/blob/main/docs/student-learning-path.md), [mentor guide](https://github.com/The-Allsparks/TRACE/blob/main/docs/mentor-guide.md), [architecture](https://github.com/The-Allsparks/TRACE/blob/main/docs/architecture.md), [data model](https://github.com/The-Allsparks/TRACE/blob/main/docs/data-model.md), [integrations](https://github.com/The-Allsparks/TRACE/blob/main/docs/integrations.md), [SECURITY](https://github.com/The-Allsparks/TRACE/blob/main/SECURITY.md), [examples](https://github.com/The-Allsparks/TRACE/blob/main/examples/README.md).

### AMPER

| Field | Record |
| ----- | ------ |
| Teaches | What the robot can measure electrically; why voltage falls; later optional protection is gated |
| Prerequisites | FTC SDK project; Hub voltage; optional motor current |
| Difficulty | Foundation Phases 0–1; later phases selective / research |
| Hardware | Control Hub; optional Expansion Hub; labeled batteries |
| Simulation | Unit tests; no substitute for the hardware test card |
| Evidence | CSV / AdvantageScope export; loop time; sag vs commands |
| Safety | Phase 0/1 must not call `setPower`; do not induce uncontrolled brownout; AMPER cannot fix bad batteries or loose XT30 |
| Competition | Passive only until characterized; no unvalidated limiting |
| Integration | MIMIC may later request grants; AMPER must not write motors |
| Maturity at audit | 0.1.0-rc.1; Phase 0–1 software; **hardware validation not yet run** |

Verified links: [README](https://github.com/The-Allsparks/AMPER/blob/main/README.md), [phases](https://github.com/The-Allsparks/AMPER/blob/main/docs/power-management/phases.md), [assessment](https://github.com/The-Allsparks/AMPER/blob/main/docs/power-management/assessment.md), [quickstart](https://github.com/The-Allsparks/AMPER/blob/main/docs/quickstart.md), [install](https://github.com/The-Allsparks/AMPER/blob/main/docs/install.md), [hardware test card](https://github.com/The-Allsparks/AMPER/blob/main/docs/validation/hardware-test-card.md), [validation status](https://github.com/The-Allsparks/AMPER/blob/main/docs/validation/STATUS.md), [examples](https://github.com/The-Allsparks/AMPER/blob/main/examples/README.md).

### MIMIC

| Field | Record |
| ----- | ------ |
| Teaches | What must be measured for safe mechanisms; ticks are not inches; states vs raw setpoints; later limits/interlocks |
| Prerequisites | Mechanism sensors or fake hardware; adult supervision for motion |
| Difficulty | Foundation Phase 0–1; interlocks need real geometry later |
| Hardware | Not selected for elevator at audit; fake actuators for classroom |
| Simulation | `FakeActuator` / fake hardware in Phase 0 tests |
| Evidence | Snapshots, disagreement metrics (later), no motion in Phase 0 |
| Safety | Software limits do not replace hard stops; no production safety claims |
| Competition | Observation until mechanism-specific tests; protections off |
| Integration | Coexists with Pedro/ViDAR; AMPER clip later; MIMIC still gates mechanically |
| Maturity at audit | 0.1.0-SNAPSHOT; **Phase 0 only implemented**; not robot-validated |

Verified links: [README](https://github.com/The-Allsparks/MIMIC/blob/main/README.md), [phases](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/phases.md), [safety model](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/safety-model.md), [lifecycle](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/lifecycle.md), [interlocks](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/interlocks.md), [assessment](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/assessment.md), [examples](https://github.com/The-Allsparks/MIMIC/blob/main/examples/README.md), [testing](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/testing.md).

### ViDAR

| Field | Record |
| ----- | ------ |
| Teaches | Robot-space range/bearing, frames, one-camera observation, later fusion |
| Prerequisites | FTC SDK, Control Hub, UVC webcam; browser sim needs none |
| Difficulty | Foundation in sim / Discover OpMode; multi-camera is integration |
| Hardware | One camera first; 3–4 cameras need powered USB hub (roadmap) |
| Simulation | Browser simulator (`sim/`, serve scripts) |
| Evidence | Telemetry, Camera Stream overlay, calibration checklist |
| Safety | Discover/Spatial OpModes are no-motors; do not let vision drive until team code is understood |
| Competition | Field lighting validation required; 4-cam not hardware-validated |
| Integration | Optional Pedro consumer; AprilTag scout must not silently own pose |
| Maturity at audit | 0.2.0; sim-tested; Control Hub multi-cam **requires team validation** |

Verified links: [README](https://github.com/The-Allsparks/ViDAR/blob/main/README.md), [TEACHING](https://github.com/The-Allsparks/ViDAR/blob/main/docs/TEACHING.md), [coordinate frames](https://github.com/The-Allsparks/ViDAR/blob/main/docs/COORDINATE_FRAMES.md), [calibration](https://github.com/The-Allsparks/ViDAR/blob/main/docs/CALIBRATION.md), [checklist](https://github.com/The-Allsparks/ViDAR/blob/main/docs/CALIBRATION_CHECKLIST.md), [system design](https://github.com/The-Allsparks/ViDAR/blob/main/docs/SYSTEM_DESIGN.md), [API](https://github.com/The-Allsparks/ViDAR/blob/main/docs/API.md), [Pedro integration](https://github.com/The-Allsparks/ViDAR/blob/main/docs/PEDRO_INTEGRATION.md), [sim](https://github.com/The-Allsparks/ViDAR/blob/main/sim/README-SIM.md).

### BEACON

| Field | Record |
| ----- | ------ |
| Teaches | What "connected" means; freshness vs stick value; failure domains; preflight |
| Prerequisites | Vocabulary can be desktop; robot reports later |
| Difficulty | Foundation Phases 0–2; Phase 5 drivetrain safe-stop **not proven** |
| Hardware | Hubs, DS, cameras as reporting sources — BEACON must not probe/restart in early phases |
| Simulation | Fake clocks, fake health sources, student exercises |
| Evidence | Registry snapshots, preflight findings, later timelines |
| Safety | Must not replace FTC watchdog; no unsupported DS heartbeat APIs; recovery inhibit after reconnect with stick forward |
| Competition | Passive observation; no comms intervention |
| Integration | Consumes health from others; does not own perception/power/mechanisms |
| Maturity at audit | 0.1.0-SNAPSHOT; Phase 0–2 types; flags default off; not hardware-validated |

Verified links: [README](https://github.com/The-Allsparks/BEACON/blob/main/README.md), [phases](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/phases.md), [assessment](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/assessment.md), [exercises](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/exercises.md), [command freshness](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/command-freshness.md), [driver-link](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/driver-link.md), [recovery](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/recovery.md), [preflight](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/preflight.md), [passive example](https://github.com/The-Allsparks/BEACON/blob/main/examples/passive-health-monitor/README.md).

### HELM

| Field | Record |
| ----- | ------ |
| Teaches | Goals, tasks, timeouts, fallbacks; observe; offline validate; later shadow |
| Prerequisites | A conventional auto students can explain; TRACE for later gates |
| Difficulty | Foundation vocabulary; execution is not approved |
| Hardware | None in current scaffold |
| Simulation | Desktop tree walking; not robot execution |
| Evidence | Observe records; validation errors |
| Safety | Never commands motors; lower layers override; default `OFF` |
| Competition | Disabled / observe / validate only |
| Integration | Pedro moves chassis; MIMIC mechanisms; TRACE records |
| Maturity at audit | 0.1.0-SNAPSHOT; Phases 0–2 + simulated walk; physical output refused |

Verified links: [README](https://github.com/The-Allsparks/HELM/blob/main/README.md), [student path](https://github.com/The-Allsparks/HELM/blob/main/docs/student-learning-path.md), [mentor guide](https://github.com/The-Allsparks/HELM/blob/main/docs/mentor-guide.md), [readiness gates](https://github.com/The-Allsparks/HELM/blob/main/docs/readiness-gates.md), [safety](https://github.com/The-Allsparks/HELM/blob/main/docs/safety.md), [intent trees](https://github.com/The-Allsparks/HELM/blob/main/docs/intent-trees.md), [season strategy](https://github.com/The-Allsparks/HELM/blob/main/docs/season-strategy.md), [responsibility boundaries](https://github.com/The-Allsparks/HELM/blob/main/docs/responsibility-boundaries.md).

**Stale-doc gap:** HELM `docs/readiness-gates.md` still reports TRACE as an empty repository (status as of HELM's 17 August 2026 table). TRACE now has a scaffold. FORGE links the gates file anyway and treats HELM authority as **not met**.

### ECHO

| Field | Record |
| ----- | ------ |
| Teaches | Cue is a chosen message; pan vs pulse; silence reasons; mute; driver workload |
| Prerequisites | Desktop JVM; later Driver Hub path is not in-library |
| Difficulty | Foundation desktop; competition audio is gated and currently forbidden |
| Hardware | None for Phase 0–1; hearing safety if audio is on |
| Simulation | Desktop training UI (audio off by default); synthetic bearing scenarios |
| Evidence | Cue decision records; training accuracy is not match proof |
| Safety | Never commands hardware; start quiet; immediate mute; two-ear isolation hides referees |
| Competition | **Not approved.** Re-read feasibility after 12 Sep 2026 |
| Integration | ViDAR/HELM/AMPER/MIMIC/BEACON as cue sources via adapters; TRACE for records |
| Maturity at audit | 0.1.0-SNAPSHOT; CONDITIONAL GO; match audio disabled |

Verified links: [README](https://github.com/The-Allsparks/ECHO/blob/main/README.md), [student path](https://github.com/The-Allsparks/ECHO/blob/main/docs/student-learning-path.md), [competition readiness](https://github.com/The-Allsparks/ECHO/blob/main/docs/competition-readiness.md), [hearing safety](https://github.com/The-Allsparks/ECHO/blob/main/docs/hearing-safety.md), [cue vocabulary](https://github.com/The-Allsparks/ECHO/blob/main/docs/cue-vocabulary.md), [driver training](https://github.com/The-Allsparks/ECHO/blob/main/docs/driver-training.md), [feasibility](https://github.com/The-Allsparks/ECHO/blob/main/docs/feasibility-decision.md), [phase 1 desktop](https://github.com/The-Allsparks/ECHO/blob/main/examples/phase1-desktop.md).

### Pedro Pathing

| Field | Record |
| ----- | ------ |
| Teaches | Localization + Bézier path following for omnidirectional drive |
| Prerequisites | Omnidirectional drive; localization; Android Studio (not OnBot Java/Blocks per official intro) |
| Difficulty | Developing after a driveable chassis; tuning takes practice days |
| Hardware | Drivebase + chosen localization |
| Simulation | Visualizer (external project) |
| Evidence | Repeatable path completion; TRACE events around auto |
| Safety | Standard robot motion hazards; keep a simple auto fallback |
| Competition | Conventional autonomous is a season priority |
| Integration | Chassis owner; ViDAR optional consumer; HELM must not replace it |

Verified links: [site](https://pedropathing.com/), [introduction](https://pedropathing.com/docs/pathing), [tuning](https://pedropathing.com/docs/pathing/tuning), [localization](https://pedropathing.com/docs/pathing/tuning/localization), [GitHub](https://github.com/Pedro-Pathing/PedroPathing), [Quickstart](https://github.com/Pedro-Pathing/Quickstart).

## Gaps (do not invent)

| Gap | Closest authority | FORGE behavior |
| --- | ----------------- | -------------- |
| BIOBUZZ Kickoff manual not published at audit | ECHO research against Competition Manual V0; Kickoff 12 Sep 2026 | Kickoff replan guide; no invented scoring rules |
| No Allsparks on-robot datasets for TRACE/AMPER/MIMIC/BEACON | Each project's README / validation STATUS | Sessions stay passive or simulated until team evidence exists |
| Elevator hardware not selected | [MIMIC elevator-target.md](https://github.com/The-Allsparks/MIMIC/blob/main/docs/mechanism-control/elevator-target.md) | Teach snapshots on whatever simple mechanism exists |
| TRACE Phase 4 adapters not approved | TRACE student path Phase 4 | Correlate with whatever exports exist; do not claim unified flight recorder adapters |
| BEACON Phase 5 DS freshness API not verified | [driver-link.md](https://github.com/The-Allsparks/BEACON/blob/main/docs/communications-health/driver-link.md) | Teach official stop; do not implement faster library stop |
| HELM execute not approved; readiness gates unmet | [readiness-gates.md](https://github.com/The-Allsparks/HELM/blob/main/docs/readiness-gates.md) | Vocabulary, validate, shadow only |
| ECHO Driver Hub / match audio untested | ECHO competition readiness | Simulation and mute drills only |
| SystemCore APIs | Blocked issues in AMPER/MIMIC/BEACON | Out of season scope |
| ViDAR missing some community files | ViDAR README / CONTRIBUTING | Link README; do not claim a ViDAR CoC that is not there |
| Team robot repository not identified in this org audit | Local `FTC-test` exists with no git remote; org has no TeamCode repo as of 18 Aug 2026 | [docs/team-robot-project.md](team-robot-project.md) holds the placeholder; do not forge a URL |

## Scheduling assumption

User/team instruction: treat all seven libraries as functionally complete for **scheduling** after the week of 24 August 2026. That is a planning assumption, not a hardware-validation claim. FORGE still requires evidence before active competition use.
