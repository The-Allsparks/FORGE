# Staged robot releases

BumbleBee ships as **capability releases**, not as "every idea on the robot by the first event."

Adapt the scoring verbs after Kickoff from the **official** Game Manual. The R0–R5 labels stay; the BIOBUZZ tasks inside them change. Do not treat the examples below as required scoring functions.

Process: [season-process.md](season-process.md) · gates: [decision-gates.md](decision-gates.md) · principle: [guiding-principle.md](guiding-principle.md).

**Strategic influence:** Pratt, *Why Most FTC Teams Fail (And How Not To)* (adapted; not endorsed; not a FIRST rule source).

## Release definitions

| Release | Name | Meaning | Typical first evidence |
| ------- | ---- | ------- | ---------------------- |
| **R0** | Driveable legal chassis | Legal, safe, inspectable, driveable. Battery/switch/Hub path understood. Students can enable, drive, disable. | Preseason P007 as actually completed (P006 was code reading only); remaining gaps closed in week 1 if needed. P008 is the FRC tour |
| **R1** | Autonomous mobility + fallback | Dependable auto movement **or** a written teleop-only fallback. Failed auto does not strand the match plan. | G6 minimum auto **or** declared teleop-only |
| **R2** | Acquire and release | Reliable pickup and release of the **primary** game piece (name it from the manual after Kickoff). | G2 prototype records; G5 module under software control |
| **R3** | Primary score | Reliable scoring of the **primary** objective on the ranked capability list. | G5–G6 measured cycles |
| **R4** | Repeatable match cycles | Full teleop cycles with a recorded distribution (not only the fastest cycle). | G6–G7 reliability log |
| **R5** | Selective extras | Automation or secondary capabilities that pass the [four tests](guiding-principle.md) and [software sequencing](software-sequencing.md) gates. | G7 only if earned |

**Clinic (10 Oct)** is a data-collection event, not an R4/R5 debut. **League 1S/2S (31 Oct)** is the first scored meet in the planning calendar.

## What is not a release requirement

Elevator, capstan, hopper, ViDAR, AMPER limiting, MIMIC homing, BEACON intervention, TRACE Phase 4, HELM, ECHO, and multi-camera systems are **roadmap items**. They enter a release only when the Kickoff ranked list and a gate say so.

## Map to gates (competition one)

| Release | Must not slip past | Honest target for 36117 |
| ------- | ------------------ | ----------------------- |
| R0 | Clinic 10 Oct | **Required** at clinic. If preseason bring-up missed, S001 finishes chassis before any scoring fab. |
| R1 | League 31 Oct | **Required** at league (auto **or** documented teleop-only). Stretch at clinic. |
| R2 | League 31 Oct | **Required** for a scoring strategy. Stretch at clinic if G2 passed. |
| R3 | League 31 Oct | **Goal** if G3 custom path holds; else starter-bot score path. |
| R4 | G7 (30 Oct) | **Goal** — measured cycles in S011–S014. Do not invent numbers. |
| R5 | After G6, only if runway holds | **Optional.** Default is none at League 1S/2S. |

If a release is missed, trigger the matching gate **fallback** (starter-bot, scope cut, teleop-only). Do not steal the [competition runway](#competition-runway).

## Competition runway

Pratt's "several weeks of only driver practice" does not fit a rookie team with ~4 hours/week and a 31 October league. FORGE names the **maximum honest window** and protects it with gates.

Worked **backward** from planning-input dates (verify if FIRST Nevada changes them):

| Milestone | Target | Why this date is honest |
| --------- | ------ | ----------------------- |
| Kickoff analysis (no custom fab at scale) | 12–18 Sep (K001, S001, S002) | G1. Crude prototypes and chassis finish only. |
| Architecture commitment | ~2–4 Oct (S006 / G3) | Last major-pivot deadline before clinic. |
| Competition-mechanism freeze (no new modules) | ~5 Oct (G4) | Week-4 build must finish, not expand. |
| Clinic / scrimmage | **10 Oct** | R0 required; R1–R2 stretch; inspection practice; **not** feature freeze. |
| Mechanical/electrical complete | ~9–11 Oct (S008 / G5) | Day-after-clinic is already tight — do not add modules after S007. |
| Software integration on final mass | 12–23 Oct (S009–S012 / G6) | Retune Pedro on BumbleBee, not Strafer assumptions. |
| Autonomous stabilization | 16–23 Oct (S010–S012) | One reliable path or teleop-only declared. |
| Inspection readiness | S008 + clinic + S014 | Practice the team checklist; official PDF when published. |
| **Protected driver practice** | **12–30 Oct (S009–S014)** | Six sessions (~12 h). Meeting B 55-minute blocks stay driving. No elective redesign. |
| Reliability testing | 19–30 Oct (S011, S013, S014) | Quantified cycles + [failure-mode drills](failure-mode-drills.md). |
| Pit repair practice | S014 (timed) + clinic | Also S029 later in the season. |
| Feature / code freeze | 26–30 Oct (G7) | One shop day before league — freeze **must** hold. |
| Portfolio draft complete enough to edit | 19 Oct (S011) → print 30 Oct | Skeleton already started in preseason. |
| League 1S/2S | **31 Oct** | G8. No elective features at the venue. |

**Protected practice rule:** After G5, Meeting A construction is P0/P1 repair and reliability support only. Meeting B driving is not a build overflow. Version 2 research waits for Strafer/fixtures after G7.

## After League 1S/2S

R5 and Version 2 may grow using match evidence. Releases can advance; they do not reset. New mechanisms still pass the four tests.
