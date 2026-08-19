# Season plan — 2026–2027 BIOBUZZ

This plan sequences **one robot**. It is not seven courses. Dates: [calendar.yaml](calendar.yaml) (planning inputs; verify if FIRST Nevada changes them).

**First combined-stack acceptance priority:** [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4). FORGE owns the student-facing install matrix, lifecycle ordering, conventions, disable paths, and acceptance teaching ([stack-acceptance.md](../../docs/stack-acceptance.md)). It does not contain TeamCode. Compile-checked combined TeleOp/auto is blocked until a published robot repository exists ([issue #2](https://github.com/The-Allsparks/FORGE/issues/2)). Do not invent a URL. Do not teach later sessions as if the stack already composes on a Control Hub.

Libraries may be treated as **functionally complete for scheduling** after the week of 24 August 2026. That is not hardware validation and not combined FTC readiness.

## Constraints

- Two meetings per week × ~2 hours (Monday and Friday, 4:00–6:00 PM; Wednesday preseason exceptions in `calendar.yaml`)
- Students build mechanical and electrical systems
- Substantial driver practice
- Reliable conventional autonomous (Pedro Pathing owns chassis motion)
- Advanced libraries support the robot; they do not consume the season
- Combined stack acceptance (install, lifecycle, fallbacks, Hub evidence) outranks deeper standalone library expansion

## Phase map

### Preseason — through 11 September 2026 (P001–P008; last shop meeting before Kickoff)

**Revised preseason goal:** By Kickoff on 12 September 2026, The Allsparks will have a reliable Strafer drivetrain, safe and organized build practices, basic driver-control proficiency, a repeatable code deployment and robot bring-up process, measured experiments for capstan/lift/ball-transport concepts, engineering evidence for rapid post-Kickoff decisions, and a prepared process for selecting the minimum viable BIOBUZZ robot. The team will **not** fabricate a final tower, hopper, or game-piece system before learning actual game requirements.

**Preseason priorities (in order):**

1. Safe students and an organized workspace
2. Reliable driving chassis
3. Electrical installation and diagnosis
4. Driver practice
5. Reusable mechanism experiments
6. Evidence and engineering-notebook habits
7. Minimal supporting software
8. Advanced software only when it directly supports current hardware

#### Meetings

| ID | Date | Primary goal |
| -- | ---- | ------------ |
| **P001** | 2026-08-17 | Onboarding, parts organization, safety, sponsor cards started |
| **P002** | 2026-08-19 | Finish sponsor cards; begin Strafer chassis frame |
| **P003** | 2026-08-24 | Mechanically complete rolling chassis (modified drivetrain) |
| **P004** | 2026-08-26 | Safe, serviceable control and power system |
| **P005** | 2026-08-31 | Bring-up one motor at a time; system map; TRACE habit — **not** first assembly |
| **P006** | 2026-09-04 | Driver baseline in all mecanum directions |
| **P007** | 2026-09-07 | Reusable mechanism lab: capstan, tower slide, transport |
| **P008** | 2026-09-11 | Kickoff readiness review; evidence consolidation |

See [learning-paths/onshape-cad.md](../../learning-paths/onshape-cad.md) for optional CAD tied to P002–P004 and P005–P006.

#### Software allocation before Kickoff

Direct software work is limited to about **30 minutes per week** (excluding brief evidence capture). Details: [preseason-software-allocation.md](docs/preseason-software-allocation.md).

#### Kickoff decision gate

Tower/capstan/transport proceeds only if official BIOBUZZ requirements justify it. Details: [preseason-kickoff-gate.md](docs/preseason-kickoff-gate.md).

#### Preseason definition of done

Preseason succeeds when:

- The Strafer drives reliably in all mecanum directions
- Every student can safely enable, drive, and disable it
- Every student can identify drivetrain and power-path components
- Wiring is labeled, retained, and serviceable
- The team has measured capstan, slide, and transport behavior
- Students can distinguish evidence from assumptions
- Prototype components remain reusable
- The notebook captures safety, organization, sponsor stewardship, construction, failures, and decisions
- No advanced software is treated as competition-ready without robot evidence
- The team is prepared to choose a minimum viable robot immediately after Kickoff

S001–S008 fall after Kickoff because a four-hour week cannot also finish a scoring robot. They remain **introduction** sessions, not competition enablement.

### Kickoff — 12 September 2026 (K001)

- Analyze BIOBUZZ from the official Kickoff materials (do not use FORGE as a rules source)
- **Brainstorm ≥3 robot concepts** and **debate** finalists before MVP lock
- Identify scoring tasks
- Select the minimum viable competition robot
- Map mechanisms, sensors, and software capabilities to the game
- Revise remaining FORGE dates in `calendar.yaml`
- Preserve build and driver-practice time

### Kickoff through 10 October (S001–S008)

- Prioritize the minimum viable BIOBUZZ robot
- TRACE active as recorder
- AMPER records voltage/current passively
- MIMIC defines mechanism states and limits on paper / snapshots; protections off unless tested
- ViDAR begins relevant detection work without stealing construction
- BEACON observes communications health
- ECHO simulation or controlled drills
- HELM describes or simulates autonomous intent
- Conventional teleop and autonomous fallbacks exist

### 10 October clinic / scrimmage

Treat as **data collection and systems validation**, not as a feature debut.

Test: mechanisms under load, ViDAR under field lighting, communications recovery, battery sag, driver workload, ECHO cue clarity **if** it was used in a drill, conventional auto, inspection and pit.

### 12–31 October (S009–S013 + numbered cadence slots)

Reliability sprint: repairs, auto repetitions, driver practice. TRACE on. AMPER and BEACON passive. Only tested MIMIC protections. ECHO competition-disabled unless controlled evidence demonstrates benefit. HELM observe-only or static-only. Conventional auto fallback preserved.

### 2 November – 5 December (S014–S023)

Use match evidence. Deeper ViDAR calibration, MIMIC lifecycle, AMPER envelope, BEACON recovery exercises, ECHO experiments, HELM shadow. **Drive and auto every week.** Numbered cadence sessions fill gaps between milestone labs.

### 7 December – 9 January (S024–S031)

Full match simulations and failure drills: depleted battery, missed acquisition, obstructed camera, stale sensors, mechanism failures, comms failures, ambiguous ECHO cues, pit and inspection. Only narrowly bounded validated active behavior. Immediate rollback.

### 11–23 January (S032–S034, E004)

Feature freeze. Full mock competitions. Inspection, judging, pit, driver communication, auto reps. **E004** replaces the regular meeting on League Tournament day 1 (2027-01-22). No new active features unless a critical demonstrated problem.

### 25 January – 20 February (S036–S042, E005 contingent)

If advancing to State: two or three evidence-supported improvements. **E005** replaces the regular meeting on State Championship day 1 (2027-02-19) if the team competes. Prioritize driver practice, auto tuning, reliability, judging.

## Construction and driving time

Every Meeting A keeps 75 minutes of physical work. Every Meeting B keeps 55 minutes of driving/auto reps. Software teaching is inside those blocks plus the short integration/repair windows.

## Unnumbered meetings

If a Tuesday or Thursday has no `S0xx` row, run:

- Meeting A: BIOBUZZ mechanism of the week + 25 minutes of TRACE/AMPER/MIMIC on that mechanism
- Meeting B: log review + repair + 55 minutes of driver/auto reps + inspection closeout

Use [templates/cadence-meeting-a.md](../../templates/cadence-meeting-a.md) and [templates/cadence-meeting-b.md](../../templates/cadence-meeting-b.md). Copy [templates/session.md](../../templates/session.md) only if you need a new numbered file.

## Event retrospectives

After every match event, run [event-retrospective.md](../../templates/event-retrospective.md) on the first Meeting A back:

| Event | When |
| ----- | ---- |
| Clinic (10 Oct) | S009 |
| League 1S/2S (31 Oct) | S012 or first cadence Meeting A after |
| League 3S/4S (5 Dec) | S023 or first Meeting A after |
| League 5S/6S (9 Jan) | S031 or first Meeting A after |
| Tournament (22–23 Jan) | E004 (competition day — no duplicate shop meeting) |
| State (19–20 Feb, if advancing) | E005 (competition day — no duplicate shop meeting) |

## Portfolio assembly gates

Track progress with [portfolio-validation.md](../../templates/portfolio-validation.md). Promote candidates every 2–3 weeks via [portfolio-candidate.md](../../templates/portfolio-candidate.md).

| Gate | Target (planning input) |
| ---- | ----------------------- |
| Early skeleton | Before Kickoff / early September (P001–P008 preseason evidence) |
| Pre-scrimmage review | 10 October 2026 |
| Post-league-meet revision | After 31 Oct, 5 Dec, 9 Jan |
| Tournament-ready | 22 January 2027 |
| State-ready | 19 February 2027 (contingent) |
| Final A201 validation | Before each submission |

See [award-and-portfolio-traceability.md](../../docs/award-and-portfolio-traceability.md) for criteria mapping.
