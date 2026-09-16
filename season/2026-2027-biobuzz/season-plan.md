# Season plan — 2026–2027 BIOBUZZ

This plan sequences **one robot** (competition BumbleBee) on a **compressed competition-one cycle** adapted from Brogan M. Pratt's [*A 12 Week FTC Season Plan That Actually Works*](https://www.youtube.com/playlist?list=PLRHdgFNRLyaM6TmNVVHKqVnnyntDDYDNt), with decision tests from Pratt, *Why Most FTC Teams Fail (And How Not To)*. Pratt does not endorse FORGE or The Allsparks. Official FIRST rules override both. Full process, gates, and attribution: [docs/season-process.md](docs/season-process.md), [docs/references.md](docs/references.md).

**Guiding principle:** [docs/guiding-principle.md](docs/guiding-principle.md) — simplest robot that hits top-ranked cycles reliably, is pit-repairable, and leaves time to program and drive.

Staged releases **R0–R5**: [docs/robot-releases.md](docs/robot-releases.md). These are capability ships, not a requirement to finish every Allsparks software idea before League 1S/2S.

This plan is not seven courses. Dates: [calendar.yaml](calendar.yaml) (planning inputs; verify if FIRST Nevada changes them).

**Team:** four-student rookie team · ~2 h meetings Mon/Fri · first Nevada league window ~31 October 2026 (~6–7 post-Kickoff weeks).

**First combined-stack acceptance priority:** [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4). FORGE owns the student-facing install matrix, lifecycle ordering, conventions, disable paths, and acceptance teaching ([stack-acceptance.md](../../docs/stack-acceptance.md)). It does not contain TeamCode. Compile-checked combined TeleOp/auto is blocked until a published robot repository exists ([issue #2](https://github.com/The-Allsparks/FORGE/issues/2)). Do not invent a URL. Do not teach later sessions as if the stack already composes on a Control Hub.

Libraries may be treated as **functionally complete for scheduling** after the week of 24 August 2026. That is not hardware validation and not combined FTC readiness.

## Decision gates (competition one)

Eight gates protect software, driving, and judging time. Missing a gate triggers scope reduction or starter-bot fallback — not silent overtime on build.

| Gate | Name | Target (planning) |
| ---- | ---- | ----------------- |
| G1 | Strategy | ~20 Sep 2026 |
| G2 | Prototype evidence | ~27 Sep 2026 |
| G3 | Architecture selection | ~4 Oct 2026 |
| G4 | Design freeze | ~5 Oct 2026 |
| G5 | Mechanical/electrical completion | ~11 Oct 2026 |
| G6 | Stable software handoff | ~25 Oct 2026 |
| G7 | Reliability / feature freeze | ~30 Oct 2026 |
| G8 | Competition readiness | ~31 Oct 2026 |

Definitions, acceptance criteria, and fallbacks: [docs/decision-gates.md](docs/decision-gates.md). Review template: [gate-review.md](../../templates/gate-review.md). Session mapping: [docs/pratt-crosswalk.md](docs/pratt-crosswalk.md). Quantified tests: [docs/acceptance-criteria.md](docs/acceptance-criteria.md). Four tests: [docs/guiding-principle.md](docs/guiding-principle.md).

## Constraints

- Two meetings per week × ~2 hours (Monday and Friday, 4:00–6:00 PM; Wednesday preseason exceptions in `calendar.yaml`)
- Students build mechanical and electrical systems
- Substantial driver practice
- Reliable conventional autonomous (Pedro Pathing owns chassis motion)
- Advanced libraries support the robot; they do not consume the season
- Combined stack acceptance (install, lifecycle, fallbacks, Hub evidence) outranks deeper standalone library expansion

## Phase map

### Preseason — through 11 September 2026 (P001–P008; last **shop** meeting is P007; P008 is the FRC tour)

**Revised preseason goal (after P006 variance):** By Kickoff on 12 September 2026, The Allsparks will have construction experience on BumbleBee, V0 rule-reading practice, a first look at existing robot code, **and — if P007 completes it** — an as-built electrical diagram, first programming bring-up, and first controlled movement if no blocking fault is found, plus packed Kickoff analysis materials and an FRC tour. Drivetrain dial-in is leftover at P007 or catch-up at S002. The team will **not** treat ViDAR/AMPER/MIMIC/BEACON/HELM/ECHO or a speculative scoring mechanism as Kickoff prerequisites. Detail: [preseason-deferred-work.md](docs/preseason-deferred-work.md).

Three P002–P004 construction meetings produced real mechanical shop time. They do **not** replace electrical, programming, or driving. P006 code reading does **not** replace a deployed TeleOp. Do not invent a finished rolling chassis.

**Preseason priorities (in order, remaining work):**

1. Safe students and an organized workspace (**P001 done**)
2. Construction record (**P002–P004 done**; as-built detail unverified)
3. Electrical diagram, wiring, programming bring-up, first movement (**P007** — last shop night; P006 did not complete this)
4. Drivetrain dial-in (**P007 leftover only**; otherwise **S002**)
5. Kickoff analysis process (**P007** final block + K001 — must not slip)
6. FRC team tour (**P008** — not shop)
7. Evidence and engineering-notebook habits (**ongoing**)
8. Minimal supporting software (**P007 TeleOp**; P006 was read-only)
9. Reusable mechanism experiments (**deferred to S001/S003 if the game justifies them**)
10. Advanced software only when it directly supports current hardware (**not preseason**)

#### Meetings

| ID | Date | Original plan | Actual or rescoped goal | Status |
| -- | ---- | ------------- | ----------------------- | ------ |
| **P001** | 2026-08-17 | Onboarding, parts organization, safety, sponsor cards started | As planned | Complete |
| **P002** | 2026-08-19 | Finish sponsor cards; begin Strafer chassis frame | Robot / Strafer construction (session 1 of 3) | Complete |
| **P003** | 2026-08-24 | Drivetrain finish; CAD dimension sketches | Robot / Strafer construction (session 2 of 3) | Complete (variance) |
| **P004** | 2026-08-26 | Electrical **and** first Onshape lesson | Robot / Strafer construction (session 3 of 3) | Complete (variance) |
| **P005** | 2026-08-31 | One-motor bring-up; CAD export if ready | BIOBUZZ Pre-Season V0 rules review | Complete (variance) |
| **P006** | 2026-09-04 | Driver baseline in all mecanum directions | Electrical/programming/first movement **planned**; actual was a code walkthrough | Complete (variance) |
| **P007** | 2026-09-07 | Reusable mechanism lab | Finish bring-up and first movement **and** Kickoff preparation (dial-in leftover only) | Scheduled (rescoped) |
| **P008** | 2026-09-11 | Kickoff readiness; P007 experiment review | FRC team tour | Scheduled (rescoped) |

See [learning-paths/onshape-cad.md](../../learning-paths/onshape-cad.md). Custom parts are **possible** if the as-built robot needs them; they are not confirmed P002 accomplishments. First CAD lesson is **not** a P004/P005/P006/P007 shop gate — it is **S003 (21 Sep)**, FRC-hosted. S006 authorizes BOM/fab. Students are beginners — mentor/host pairing, not assumed skill.

#### Software allocation before Kickoff

Direct software work is limited to about **30 minutes per week** (excluding brief evidence capture). Details: [preseason-software-allocation.md](docs/preseason-software-allocation.md).

#### Kickoff decision gate

Tower/capstan/transport proceeds only if official BIOBUZZ requirements justify it. Details: [preseason-kickoff-gate.md](docs/preseason-kickoff-gate.md).

#### Preseason definition of done

Preseason succeeds when the **Kickoff-critical** set is true, with honest blockers written for the rest:

- The Strafer has a documented as-built electrical diagram **or** a named blocker
- Hub port assignments are recorded **or** enable is explicitly forbidden
- The Driver Station can connect, enable, disable, and stop **or** that gap is written
- Each drivetrain motor has been commanded individually **or** blocked in writing
- First controlled movement has been attempted **or** a blocking hardware fault is named (P007; P006 did not)
- Drivetrain dial-in observations exist **or** P007 honestly records that first movement blocked them
- Students can distinguish evidence from assumptions (including V0 vs official rules)
- The notebook captures safety, organization, construction, rules discussion, and decisions
- Kickoff roles, worksheets, and learning-goal baselines are packed (**P007**, not the P008 tour)
- No advanced software is treated as competition-ready without robot evidence
- The team is prepared to choose a minimum viable robot immediately after Kickoff

**Not required before Kickoff:** measured capstan/slide/transport lab, Onshape export, GitHub robot-repo workflow, full mecanum performance baseline, field-centric/odometry/auto, any optional library on the Hub, or finishing Kickoff prep during the FRC tour.

### Kickoff — 12 September 2026 (K001)

- Analyze BIOBUZZ from the official Kickoff materials (do not use FORGE as a rules source; P005 v0 notes are study notes only)
- Fill [kickoff-decision-package.md](../../templates/kickoff-decision-package.md): scoring **and ranking**, alliance roles, effort-versus-value, ranked capabilities, **not yet / will not build**, R0–R2 definition
- **Brainstorm ≥3 robot concepts**; scale visual ideation to **60–100** across four students during week 1
- **Debate** finalists; apply the [four tests](docs/guiding-principle.md); pass **G1 Strategy gate** at S002
- Do **not** start custom scoring fabrication to look productive — S001 is game + brainstorm; crude game-object prototypes wait until G1 has ideas (S002/S004)
- Map software to [software-sequencing.md](docs/software-sequencing.md) tiers (not all libraries at once)
- Revise remaining FORGE dates in `calendar.yaml`
- Preserve build and driver-practice time

Guide: [kickoff-replan-guide.md](kickoff-replan-guide.md).

### Compressed post-Kickoff weeks (S001–S014 → League 1S/2S)

Pratt's twelve weeks compress into six or seven shop weeks before **31 October 2026** (planning input). Software, driving, judging, and reliability time are **protected** by gates.

| Week | Phase | Sessions | Gates | Release target |
| ---- | ----- | -------- | ----- | -------------- |
| 1 | Understand and diverge | K001, S001, S002 | G1 | R0; **S001 = season updates, official game review, brainstorm** (crude proofs wait until ideas exist) |
| 2 | Test and compare | S003, S004 | G2 | **S003 = FRC Onshape**; **S004 = physical G2 evidence** |
| 3 | Select and commit | S005, S006 | G3 | Architecture for R2/R3; S006 CAD/BOM authorization |
| 4 | Build and integrate | S007, S008, clinic 10 Oct | G4, G5 | R0 required at clinic; R1–R2 stretch |
| 5 | Tune and validate | S009–S012 | G6 | R1 required; R3/R4 in progress |
| 6 | Freeze and rehearse | S013, S014 | G7 | R4 measurements; R5 only if earned |
| 7 | Competition simulation | League 1S/2S 31 Oct | G8 | Score with R0–R2 (R3 if G3 held) |

**Competition runway (protected driver practice):** 12–30 October (S009–S014). No elective redesign. Detail: [docs/robot-releases.md](docs/robot-releases.md#competition-runway).

Detail per week: [docs/season-process.md](docs/season-process.md). Prototype evidence: [prototype-test-record.md](../../templates/prototype-test-record.md). Two platforms: [docs/two-platform-strategy.md](docs/two-platform-strategy.md).

**Library sessions** (ViDAR, BEACON, MIMIC, ECHO, HELM) run **only when** the G3 software contract ([docs/software-sequencing.md](docs/software-sequencing.md)) places them in tier 1 or 2 — not by default.

### 10 October clinic / scrimmage

Treat as **data collection and systems validation**, not as a feature debut. Contributes to **G5** integration evidence. Target **R0**; stretch R1–R2. Do not debut R5.

Test: mechanisms under load, inspection and pit, driver workload, conventional auto or fallback, communications recovery, battery sag. ViDAR under field lighting **only if** already on the robot for a tier-2 reason. ECHO cue drills **only if** already evidenced. Failure notes use [failure-mode-drills.md](docs/failure-mode-drills.md) when a fault happens — do not inject unsafe faults at a public event.

### 12–31 October (S009–S014)

Tune, validate, freeze, rehearse — not new mechanisms. This **is** the protected driver-practice window. Reliability sprint aligned to **G6–G8**. TRACE on. AMPER and BEACON passive unless G3 promoted them. Only tested MIMIC protections. ECHO competition-disabled unless controlled evidence demonstrates benefit. HELM observe-only or static-only. Conventional auto fallback preserved. Mock judging, [failure-mode drills](docs/failure-mode-drills.md), and full 2½-minute matches before league meets.

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

If a Monday or Friday has no dedicated milestone content, run [templates/cadence-meeting-a.md](../../templates/cadence-meeting-a.md) or [templates/cadence-meeting-b.md](../../templates/cadence-meeting-b.md) using the fixed `{ID}-meeting-{type}.md` file for that date. Change the session **title** in `calendar.yaml` when the week's mechanism changes — do not rename files.

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

See [award-and-portfolio-traceability.md](../../docs/award-and-portfolio-traceability.md) for criteria mapping. Think is continuous. Do not lock Control/Connect (or alternatives) until the team decision in [docs/award-strategy.md](docs/award-strategy.md).
