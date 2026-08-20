# FORGE decision gates

Eight gates protect downstream time for software, driving, judging, and reliability. A missed gate **must not** silently consume later work — trigger scope reduction or starter-bot fallback instead.

Process context: [season-process.md](season-process.md). Gate review template: [gate-review.md](../../../templates/gate-review.md).

**Attribution:** Gate timing is adapted from schedule protections in Brogan M. Pratt's [*A 12 Week FTC Season Plan That Actually Works*](https://www.youtube.com/playlist?list=PLRHdgFNRLyaM6TmNVVHKqVnnyntDDYDNt). Pratt does not endorse FORGE.

---

## Gate summary

| Gate | Name | Target (planning) | Blocks until passed |
| ---- | ---- | ----------------- | ------------------- |
| G1 | Strategy | End post-Kickoff week 1 (~20 Sep 2026) | Custom mechanism fabrication at scale |
| G2 | Prototype evidence | End post-Kickoff week 2 (~27 Sep 2026) | Architecture lock; unrestricted exploration |
| G3 | Architecture selection | End post-Kickoff week 3 (~4 Oct 2026) | Full-module fabrication; sensor procurement |
| G4 | Design freeze | Start post-Kickoff week 4 (~5 Oct 2026) | New modules without gate review |
| G5 | Mechanical/electrical completion | End post-Kickoff week 4 (~11 Oct 2026) | Final auto tuning; reliability claims |
| G6 | Stable software handoff | End post-Kickoff week 5 (~25 Oct 2026) | Advanced autonomy; HELM execute; ECHO match |
| G7 | Reliability / feature freeze | End post-Kickoff week 6 (~30 Oct 2026) | Elective features; major mechanical changes |
| G8 | Competition readiness | League 1S/2S (~31 Oct 2026) | Competition enablement approval |

---

## G1 — Strategy gate

### Purpose

Confirm the team understands BIOBUZZ scoring constraints and has a written, student-owned strategy before custom build work displaces driving and software.

### Required inputs

- Official Kickoff / Game Manual materials (FIRST — not FORGE)
- K001 outputs: concept brainstorm (≥3 concepts), debate notes, MVP definition
- Preseason mechanism experiments (P007) labeled evidence vs assumption

### Required evidence

- Scoring / ranking / penalty / constraint matrix
- Prioritized capability list tied to ranking points
- Initial risk register (≥3 risks with owners)
- ≥1 low-fidelity physical proof of game-object interaction OR documented reason the game makes that impossible until parts arrive
- [Concept brainstorm record](../../../templates/concept-brainstorm.md) with 60–100 scaled ideation count across four students (or honest count + plan to reach target)

### Student decision-making responsibilities

- Select MVP scoring path and ranking strategy
- Debate finalists; drive-team veto on workload
- Reject ideas that exceed build/program/drive time

### Mentor role

- Facilitate debate; enforce timeboxes
- Verify manual citations come from official sources
- Block invented point values in FORGE docs

### Acceptance criteria

- Written MVP: drive + one scoring action + required park/place per manual
- Strategy matrix reviewed by all four students
- Fallback starter-bot path identified if custom MVP slips

### Deliverables

- K001 session evidence; updated [readiness-dashboard.md](../readiness-dashboard.md)
- Mapping table from [kickoff-replan-guide.md](../kickoff-replan-guide.md)

### Fallback if missed

- **Scope reduction:** Adopt official starter-bot scoring baseline as Sparkee MVP
- **Time protection:** No custom fabrication beyond drivetrain until G1 passes
- **Recovery meeting:** Extra 30 min strategy block on next Meeting A before build

### Blocks until passed

- Custom scoring mechanism fabrication at scale
- Deep library integration sessions that displace driving
- Sensor purchases beyond drivetrain essentials

---

## G2 — Prototype evidence gate

### Purpose

End unrestricted mechanism exploration with **measured** comparisons — not opinions.

**Pratt protection:** Week 3 ends unrestricted mechanism exploration.

### Required inputs

- G1 strategy and MVP definition
- Starter-bot reference design (official or kit)
- One–two alternative concepts from G1 brainstorm

### Required evidence

- ≥2 [prototype-test-record.md](../../../templates/prototype-test-record.md) entries with **≥3 trials each**
- Comparative summary: acquisition, cycle time, jams, alignment tolerance, packaging, repairability, current draw (where measured)
- [Decision record](../../../templates/decision-record.md) if finalists were close
- Leading concept(s) and explicit **starter-bot fallback** if custom path fails

### Student decision-making responsibilities

- Choose test procedures and hold variables constant
- Record failures honestly
- Rank concepts using team criteria — not mentor preference

### Mentor role

- Coach measurement technique
- Ensure ≥3 trials before reacting to one result
- Stop simultaneous multi-variable changes unless testing integrated config

### Acceptance criteria

- Comparative table complete with measurements, not adjectives
- Unresolved risks listed with owners
- Team can explain why exploration stops here

### Deliverables

- Prototype test records in engineering notebook / repo-linked storage
- Updated risk register

### Fallback if missed

- **Starter-bot fallback:** Commit to official starter scoring mechanism for competition one
- **Bench-only exploration:** Further prototypes on fixtures only — Sparkee build frozen to drivetrain + starter module
- **Time protection:** Architecture gate (G3) delayed max 3 days; then fallback auto-applies

### Blocks until passed

- G3 architecture lock
- Unrestricted new mechanism branches on Sparkee
- Reliability claims about unscored prototypes

---

## G3 — Architecture selection gate

### Purpose

Lock competition-one modular architecture with interfaces sufficient to fabricate and program in remaining weeks.

**Pratt protections:** Week 5 mechanism direction selected; Week 6 major pivot deadline.

### Required inputs

- G2 comparative evidence and leading concept
- [modular-architecture.md](modular-architecture.md) module list derived from BIOBUZZ
- Software contract: which libraries are MVP vs deferred ([season-process.md](season-process.md#software-protections))

### Required evidence

- Approved architecture diagram (modules + interfaces)
- Interface definitions: mechanical mounts, electrical connectors, software classes/states
- CAD or fabrication sketches authorizing build
- Bill of materials (needed parts only)
- Explicit **fallback plan** (starter-bot module swap)
- Major-design-pivot deadline recorded — **no architectural pivots after this gate**

### Student decision-making responsibilities

- Approve module boundaries and cut list
- Decide necessary vs optional sensors
- Sign software contract (what ships at first competition)

### Mentor role

- Procurement and safety review
- Confirm pivot deadline is realistic for Nevada timeline
- Verify shared parts are not double-booked ([two-platform-strategy.md](two-platform-strategy.md))

### Acceptance criteria

- All students can point to each module on diagram
- BOM ordered or in stock for week-4 build
- Features cut for time are written down — not silently dropped

### Deliverables

- Architecture decision record
- Module owner assignments ([student-ownership.md](../../../templates/student-ownership.md))
- Updated `calendar.yaml` **titles** for build weeks

### Fallback if missed

- **Starter-bot architecture:** Replace custom modules with official starter scoring assembly
- **Single-mechanism scope:** One acquisition + one score path only; defer endgame/lift
- **Time protection:** G4 opens on schedule — new modules require written scope cut elsewhere

### Blocks until passed

- Full Sparkee module fabrication beyond drivetrain
- Nonessential sensor procurement
- ViDAR/HELM/ECHO competition enablement

---

## G4 — Design freeze gate

### Purpose

Stop new modules and interface churn so integration can finish.

### Required inputs

- G3 approved architecture
- Fabrication in progress on authorized modules

### Required evidence

- Written freeze declaration with date
- List of in-flight modules and expected completion dates
- Any change requests since G3 — approved or rejected with reason

### Student decision-making responsibilities

- Reject new features unless traded for removed scope
- Approve exception requests only with time budget shown

### Mentor role

- Enforce freeze during build blocks
- Escalate safety exceptions immediately

### Acceptance criteria

- No unapproved new modules on Sparkee
- Interface changes documented as ECO-level decisions

### Deliverables

- Gate review record
- Dashboard updated: mechanical status

### Fallback if missed

- **Scope cut:** Remove lowest-priority module from competition-one
- **Starter swap:** Install starter-bot module for frozen incomplete subsystem

### Blocks until passed

- Integration sign-off (G5)
- "Final" CAD releases

---

## G5 — Mechanical/electrical completion gate

### Purpose

Confirm Sparkee is mechanically and electrically complete so software tuning uses final mass and geometry.

**Pratt protection:** Week 8 completes mechanical and electrical integration.

### Required inputs

- G4 frozen module set
- Wiring plan with strain relief and service loops

### Required evidence

- Each module demonstrated under power (individual tests)
- Complete robot: all planned competition-one modules mounted
- Wiring checklist: connectors labeled, moving-mechanism protection, ESD practices followed
- Spares list for fragile/custom parts
- Repair access verified — target module swap times recorded

### Student decision-making responsibilities

- Sign off each module test
- Identify remaining defects as P0/P1/P2

### Mentor role

- Safety inspect wiring and battery path
- Confirm no shared Strafer parts are missing from Sparkee ([two-platform-strategy.md](two-platform-strategy.md))

### Acceptance criteria

- Robot is competition-presentable mechanically (may be untuned)
- No exposed unsafe wiring
- P0 defects have owners and target dates before G6

### Deliverables

- Module test records
- Updated pit spares list ([templates/competition/](../../../templates/competition/))

### Fallback if missed

- **Software handoff delay:** G6 blocked — only minimum teleop on completed subsystems
- **Starter module:** Replace incomplete subsystem with starter-bot assembly
- **Time protection:** Programming and driving time **protected** — no silent extension of build into Meeting B blocks

### Blocks until passed

- Final Pedro localization tuning on Sparkee
- Reliability statistics for full robot
- G6 stable software handoff

---

## G6 — Stable software handoff gate

### Purpose

Hand a **stable** Sparkee to sustained software, auto, and driver work.

**Pratt protection:** Week 9 hands stable robot to software.

### Required inputs

- G5 complete robot
- Software contract from G3
- Known-good deployment process and release tag

### Required evidence

- Minimum reliable autonomous routine (Pedro or conventional fallback)
- Stable teleop with controller map documented
- MIMIC states for scored mechanisms (minimum viable)
- TRACE logs from repeated tests
- Measured reliability: cycle success rate over ≥10 attempts (honest count)
- Portfolio draft substantially complete (skeleton + robot narrative + process evidence)

### Student decision-making responsibilities

- Declare minimum auto "good enough" vs time for alternates
- Approve driver automation only with demonstrated reliability

### Mentor role

- Verify release tag and rollback path
- Block HELM execute and ECHO match enablement here

### Acceptance criteria

- Drivers can run full scoring cycle in teleop without mentor intervention
- Auto completes minimum path ≥7/10 in practice (or documented fallback to teleop-only)
- No major mechanical changes scheduled

### Deliverables

- Software release checklist completed
- Portfolio draft milestone ([portfolio-validation.md](../../../templates/portfolio-validation.md) early pass)

### Fallback if missed

- **Teleop-only competition:** Disable auto at event; focus driver reps
- **Reduce auto scope:** Single path, no alternate alliance paths
- **Time protection:** G7 still occurs on calendar — elective software cut

### Blocks until passed

- Advanced autonomy features
- HELM execute / ECHO match audio
- Competition approval (G8) for auto-dependent strategy

---

## G7 — Reliability / feature freeze gate

### Purpose

End speculative features; reserve remaining time for drivers, judging, pit, and critical fixes.

**Pratt protection:** Week 11 feature/code freeze.

### Required inputs

- G6 handoff complete
- Reliability test log

### Required evidence

- Written feature/code freeze declaration
- Full 2½-minute practice match completed (or documented field constraint)
- Mock judging session completed — all four students spoke
- Failure-injection drills: at least two scenarios from [season-process.md](season-process.md#post-kickoff-week-6-freeze-and-rehearse)
- Open defect list: only P0/P1 allowed post-freeze

### Student decision-making responsibilities

- Vote on freeze scope
- Prioritize P0 fixes vs driver time

### Mentor role

- Enforce freeze; approve only critical fixes with regression test
- Coach mock judging without authoring student narrative

### Acceptance criteria

- No elective features in active development
- Critical fixes documented with regression notes
- Portfolio draft ready for final edit

### Deliverables

- Feature freeze record
- Mock judging feedback notes

### Fallback if missed

- **Hard cut:** Disable all optional libraries at event ([student-install.md](../../../docs/student-install.md))
- **Teleop-first:** Remove auto from competition plan
- **Time protection:** G8 focuses on pit/checklists only — no build

### Blocks until passed

- G8 competition enablement for optional systems
- Version 2 / next-gen mechanism research on Sparkee

---

## G8 — Competition readiness gate

### Purpose

Confirm the team is packed, rehearsed, documented, and safe to compete.

**Pratt alignment:** Week 12 — drivers, reliability, judging, pit, logistics.

### Required inputs

- G7 freeze in effect
- [RD001-competition-approval.md](../../../assessments/readiness/RD001-competition-approval.md)

### Required evidence

- All [competition checklists](../../../templates/competition/) assigned and walked once
- Known-good release tag verified on robot DS
- Battery selection/change log practiced
- Pre/post-match checklists timed under pressure
- Portfolio and pit materials printable
- Transportation, food, student arrival plan
- Every student can explain robot, process, outreach, personal learning

### Student decision-making responsibilities

- Run checklists; own pit roles
- Present at mock judging; Q&A

### Mentor role

- Final safety sign-off
- Coach approval per RD001 — not automatic

### Acceptance criteria

- RD001 criteria reviewed — honest pass/fail per row
- Rollback under one minute demonstrated ([pit-and-inspection.md](../pit-and-inspection.md))
- Starter-bot fallback parts packed if custom modules are fragile

### Deliverables

- Completed RD001 assessment
- Packed pit bins per packing list

### Fallback if missed

- **Compete teleop-only** with starter-bot fallback configuration
- **Withdraw optional systems:** ViDAR, ECHO, HELM, advanced auto disabled
- **Event-as-practice:** Treat League 1S/2S as data collection if readiness fails — retrospective required

### Blocks until passed

- `approved` competition status on [readiness-dashboard.md](../readiness-dashboard.md) for optional systems
- Enabling AMPER limiting, MIMIC homing, ViDAR drive, BEACON intervention, ECHO match audio, HELM execute

---

## Gate review procedure

1. Schedule 15–20 minutes at end of Meeting B in gate week (or K001 closeout for G1).
2. Fill [gate-review.md](../../../templates/gate-review.md).
3. If **fail:** execute fallback column; update dashboard; notify coach if scope cut affects competition strategy.
4. Log in readiness dashboard status log.
5. Link gate evidence to GitHub issue if recovery work is needed (see season issue tracker).
