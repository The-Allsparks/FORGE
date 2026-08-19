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

### Preseason — through 9 September 2026 (sessions S001–S004; last pre-Kickoff meeting 10 September)

- Build and wire the drivetrain
- Establish reliable driver control
- Run a simple Pedro Pathing route when the chassis can move (S007 continues this after Kickoff if not finished)
- Make TRACE permanent as a closeout habit
- Use AMPER passively
- Introduce MIMIC snapshots
- Mention ViDAR/BEACON/ECHO/HELM so vocabulary exists; dedicated labs are S005–S006 and later
- Teach composition root = OpMode ([student-install.md](../../docs/student-install.md)); paper path of [lab I002](../../labs/integrated/I002-stack-install-diagnosis.md) until the robot repo exists
- HELM has **no** authority

S005–S006 fall after Kickoff because a four-hour week cannot also finish a scoring robot. They remain **introduction** sessions, not competition enablement.

### Kickoff — 12 September 2026 (SK01)

- Analyze BIOBUZZ from the official Kickoff materials (do not use FORGE as a rules source)
- Identify scoring tasks
- Select the minimum viable competition robot
- Map mechanisms, sensors, and software capabilities to the game
- Revise remaining FORGE dates in `calendar.yaml`
- Preserve build and driver-practice time

### Kickoff through 10 October (S005–S012)

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

### 12–31 October (S013–S016 + unnumbered Meeting B practice)

Reliability sprint: repairs, auto repetitions, driver practice. TRACE on. AMPER and BEACON passive. Only tested MIMIC protections. ECHO competition-disabled unless controlled evidence demonstrates benefit. HELM observe-only or static-only. Conventional auto fallback preserved.

### 2 November – 5 December

Use match evidence. Deeper ViDAR calibration, MIMIC lifecycle, AMPER envelope, BEACON recovery exercises, ECHO experiments, HELM shadow. **Drive and auto every week.** Do not treat sibling CI or desktop tests as combined Hub acceptance.

### 7 December – 9 January (S017 + templates)

Full match simulations: depleted battery, missed acquisition, obstructed camera, stale sensors, mechanism failures, comms failures, ambiguous ECHO cues, pit and inspection. Only narrowly bounded validated active behavior. Immediate rollback.

### 11–23 January (S018)

Feature freeze. Full mock competitions. Inspection, judging, pit, driver communication, auto reps. No new active features unless a critical demonstrated problem.

### 25 January – 20 February (S019, contingent)

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
| Clinic (10 Oct) | S013 |
| League 1S/2S (31 Oct) | First unnumbered or cadence Meeting A after |
| League 3S/4S (5 Dec) | First Meeting A after |
| League 5S/6S (9 Jan) | First Meeting A after |
| Tournament (22–23 Jan) | First Meeting A after |
| State (19–20 Feb, if advancing) | First Meeting A after |

## Portfolio assembly gates

Track progress with [portfolio-validation.md](../../templates/portfolio-validation.md). Promote candidates every 2–3 weeks via [portfolio-candidate.md](../../templates/portfolio-candidate.md).

| Gate | Target (planning input) |
| ---- | ----------------------- |
| Early skeleton | Before Kickoff / early September |
| Pre-scrimmage review | 10 October 2026 |
| Post-league-meet revision | After 31 Oct, 5 Dec, 9 Jan |
| Tournament-ready | 22 January 2027 |
| State-ready | 19 February 2027 (contingent) |
| Final A201 validation | Before each submission |

See [award-and-portfolio-traceability.md](../../docs/award-and-portfolio-traceability.md) for criteria mapping.
