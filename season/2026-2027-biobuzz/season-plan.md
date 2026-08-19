# Season plan — 2026–2027 BIOBUZZ

This plan sequences **one robot**. It is not seven courses. Dates: [calendar.yaml](calendar.yaml) (planning inputs; verify if FIRST Nevada changes them).

**First combined-stack acceptance priority:** [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4). FORGE owns the student-facing install matrix, lifecycle ordering, conventions, disable paths, and acceptance teaching ([stack-acceptance.md](../../docs/stack-acceptance.md)). It does not contain TeamCode. Compile-checked combined TeleOp/auto is blocked until a published robot repository exists ([issue #2](https://github.com/The-Allsparks/FORGE/issues/2)). Do not invent a URL. Do not teach later sessions as if the stack already composes on a Control Hub.

Libraries may be treated as **functionally complete for scheduling** after the week of 24 August 2026. That is not hardware validation and not combined FTC readiness.

## Constraints

- Two meetings per week × ~2 hours
- Students build mechanical and electrical systems
- Substantial driver practice
- Reliable conventional autonomous (Pedro Pathing owns chassis motion)
- Advanced libraries support the robot; they do not consume the season
- Combined stack acceptance (install, lifecycle, fallbacks, Hub evidence) outranks deeper standalone library expansion

## Phase map

### Preseason — through 10 September 2026 (P000–P003, S001–S002, P004–P005; last meeting before Kickoff)

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
| **P000** | Requires confirmation | Completed prep: parts organization, safety, sponsor cards started |
| **P001** | 2026-08-19 | Finish sponsor cards; begin Strafer chassis frame |
| **P002** | 2026-08-25 | Mechanically complete rolling chassis (modified drivetrain) |
| **P003** | 2026-08-27 | Safe, serviceable control and power system |
| **S001** | 2026-09-01 | Bring-up one motor at a time; system map; TRACE habit — **not** first assembly |
| **S002** | 2026-09-03 | Driver baseline in all mecanum directions |
| **P004** | 2026-09-08 | Reusable mechanism lab: capstan, tower slide, transport |
| **P005** | 2026-09-10 | Kickoff readiness review; evidence consolidation |

See [learning-paths/onshape-cad.md](../../learning-paths/onshape-cad.md) for optional CAD tied to P001–P003 and S001–S002.

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

S009–S010 fall after Kickoff because a four-hour week cannot also finish a scoring robot. They remain **introduction** sessions, not competition enablement.

### Kickoff — 12 September 2026 (SK01)

- Analyze BIOBUZZ from the official Kickoff materials (do not use FORGE as a rules source)
- **Brainstorm ≥3 robot concepts** and **debate** finalists before MVP lock
- Identify scoring tasks
- Select the minimum viable competition robot
- Map mechanisms, sensors, and software capabilities to the game
- Revise remaining FORGE dates in `calendar.yaml`
- Preserve build and driver-practice time

### Kickoff through 10 October (S009–S016)

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

### 12–31 October (S017–S020 + unnumbered Meeting B practice)

Reliability sprint: repairs, auto repetitions, driver practice. TRACE on. AMPER and BEACON passive. Only tested MIMIC protections. ECHO competition-disabled unless controlled evidence demonstrates benefit. HELM observe-only or static-only. Conventional auto fallback preserved.

### 2 November – 5 December

Use match evidence. Deeper ViDAR calibration, MIMIC lifecycle, AMPER envelope, BEACON recovery exercises, ECHO experiments, HELM shadow. **Drive and auto every week.** Do not treat sibling CI or desktop tests as combined Hub acceptance.

### 7 December – 9 January (S021 + templates)

Full match simulations: depleted battery, missed acquisition, obstructed camera, stale sensors, mechanism failures, comms failures, ambiguous ECHO cues, pit and inspection. Only narrowly bounded validated active behavior. Immediate rollback.

### 11–23 January (S022)

Feature freeze. Full mock competitions. Inspection, judging, pit, driver communication, auto reps. No new active features unless a critical demonstrated problem.

### 25 January – 20 February (S023, contingent)

If advancing to State: two or three evidence-supported improvements. Prioritize driver practice, auto tuning, reliability, judging. Avoid broad architectural changes.

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
| Clinic (10 Oct) | S017 |
| League 1S/2S (31 Oct) | First unnumbered or cadence Meeting A after |
| League 3S/4S (5 Dec) | First Meeting A after |
| League 5S/6S (9 Jan) | First Meeting A after |
| Tournament (22–23 Jan) | First Meeting A after |
| State (19–20 Feb, if advancing) | First Meeting A after |

## Portfolio assembly gates

Track progress with [portfolio-validation.md](../../templates/portfolio-validation.md). Promote candidates every 2–3 weeks via [portfolio-candidate.md](../../templates/portfolio-candidate.md).

| Gate | Target (planning input) |
| ---- | ----------------------- |
| Early skeleton | Before Kickoff / early September (P000–P005 preseason evidence) |
| Pre-scrimmage review | 10 October 2026 |
| Post-league-meet revision | After 31 Oct, 5 Dec, 9 Jan |
| Tournament-ready | 22 January 2027 |
| State-ready | 19 February 2027 (contingent) |
| Final A201 validation | Before each submission |

See [award-and-portfolio-traceability.md](../../docs/award-and-portfolio-traceability.md) for criteria mapping.
