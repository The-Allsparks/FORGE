# Preseason schedule variance and deferred work

**Recorded:** 2 September 2026 (after P005).  
**Revised:** 2 September 2026 — P006–P008 rescoped to: first movement at P006, drivetrain dial-in plus Kickoff prep at P007, FRC tour at P008.  
**Revised:** 4 September 2026 (after P006) — P006 was a **code walkthrough**; electrical, useful programming, and first movement did **not** run. Those move to [P007](../sessions/P007-meeting-a.md). Dial-in is leftover only. P008 remains the FRC tour.

This file is the FORGE tracker so displaced work is **moved, deferred, or marked conditional**, not silently deleted.

Do not treat the original P002–P008 agendas as having run as written. Historical session files record **planned versus actual**. [P007](../sessions/P007-meeting-a.md)–[P008](../sessions/P008-meeting-b.md) are **rescoped around actual progress**, not shifted forward by four meetings.

## What actually happened

| Session | Date | Original plan | Confirmed actual | Classification |
| ------- | ---- | ------------- | ---------------- | -------------- |
| [P001](../sessions/P001-meeting-a.md) | 2026-08-17 | Onboarding, parts organization, safety, sponsor cards started | As planned | **Completed** |
| [P002](../sessions/P002-meeting-s.md) | 2026-08-19 | Finish sponsor cards; begin Strafer chassis frame | Robot / Strafer construction (session 1 of 3) | **Completed construction.** Subassembly detail unverified |
| [P003](../sessions/P003-meeting-a.md) | 2026-08-24 | Finish drivetrain; CAD dimension sketches; push-test if rolling | Robot / Strafer construction (session 2 of 3) | **Completed construction.** Original finish outcomes not recorded as done |
| [P004](../sessions/P004-meeting-s.md) | 2026-08-26 | Electrical foundation **and** first Onshape lesson | Robot / Strafer construction (session 3 of 3) | **Completed construction.** Electrical and CAD did not run |
| [P005](../sessions/P005-meeting-a.md) | 2026-08-31 | One-motor bring-up, system map, TRACE/paper evidence | Reviewed BIOBUZZ **Pre-Season V0** rules | **Completed rules review.** Bring-up, TRACE, wiring, and driving did not run |
| [P006](../sessions/P006-meeting-b.md) | 2026-09-04 | Electrical diagram, programming bring-up, first movement (was driver baseline) | Read through some existing code; no useful programming | **Completed code walkthrough.** Electrical, hardware config, TeleOp, motor tests, and first movement did not run |

P002–P004 together are **three meetings of first-robot construction**: assembly, alignment, fastening, and build continuation. That is more mechanical shop time than the original P002-only chassis start. It is **not** evidence that the drivetrain is complete, rolling, wired, programmed, or inspectable. Motor counts, wheel completion, guards, and parts orders are **not confirmed in FORGE**.

## Indirect progress (supported, not over-claimed)

Three construction meetings plus P001 onboarding likely produced:

- Kit-part identification and fastener practice
- Tool use and pinch-point awareness beyond the P001 presentation
- Informal role rotation while building
- A physically more advanced chassis than an unopened kit — **amount unknown until P007 inspects it**

P006 code reading produced first contact with FTC / robot source, not a deployable TeleOp.

P005 rules review produced something the original preseason scheduled only at Kickoff:

- First contact with BIOBUZZ Pre-Season V0 text
- Practice discussing rules as a team
- A list of items to **reverify** when the Kickoff manual is released

That **does not** replace official Kickoff materials. V0 notes are study notes. The Game Manual and Kickoff documents win.

## Kickoff-critical vs movable

Remaining preseason time: **P007 (7 Sep shop — last shop night), P008 (11 Sep FRC tour)**, then [K001](../sessions/K001-meeting-k.md) on 12 Sep.

Do not cram multiple full meetings of displaced work into one two-hour session.

| Outcome | Kickoff-critical? | Disposition |
| ------- | ----------------- | ----------- |
| Inspect what three construction meetings actually produced | **Yes** (safety) | Opening of [P007](../sessions/P007-meeting-a.md) — P006 did not inspect metal |
| Basic electronics, wiring, and as-built electrical diagram | **Yes** | **P007** (was P004, then P006; neither ran it) |
| Driver Station and robot-controller familiarity | **Yes** | **P007** |
| Basic Java / FTC SDK orientation and hardware map | **Yes** | **P007** (minimal TeleOp, not a software course). P006 only read existing code |
| First controlled movement | **Yes** (if no blocking fault) | **P007** — goal, not a tuned baseline |
| Drivetrain dial-in (directions, mix, speed limit, deadband, practice) | **Useful** | **P007 leftover only** after first movement. Else [S002](../sessions/S002-meeting-b.md) |
| Kickoff game-analysis process, roles, worksheets, learning-goal baselines | **Yes** | **P007** final 30–45 minutes (was P008). P008 cannot recover this |
| Rule-reading practice | **Yes** | **Started at P005**; official materials at K001; V0 must be reverified |
| Engineering documentation habits | **Yes** | Continue every closeout |
| FRC team tour (learning / Connect) | **Scheduled 11 Sep** | [P008](../sessions/P008-meeting-b.md) — not shop, not Kickoff class |
| Clear student roles without silos | **Yes** | Rotating paths in P007; K001 analysis roles at P007; tour observations at P008 |
| Tool, battery, and pit safety | **Yes** | P001 general safety done; battery/enable at P007 |
| GitHub / Onshape / session-record / decision workflow | **Partial** | Session records continue. Onshape and robot GitHub are **not** Kickoff gates |
| Reusable capstan / slide / transport lab | **No** | Deferred after Kickoff — see below |
| First Onshape lesson and STL export | **No** | **S003 (21 Sep)** FRC-hosted class; export when a part blocks build. S006 is BOM/fab authorization |
| TRACE library deep-dive | **No** | Paper notes at P007; library remains evidence-only |
| ViDAR, AMPER, MIMIC, BEACON, HELM, ECHO, controller wrapper | **No** | Staged roadmap; not preseason deployables |
| Field-centric drive, odometry, autonomous, polished controls | **No** | After P007 / post-Kickoff as earned |
| Full measured driver baseline | **Useful, not a Kickoff gate** | Not a P007 claim. First post-Kickoff Meeting B ([S002](../sessions/S002-meeting-b.md)) if P007 only reaches first movement or is blocked |

## Displaced original material (do not delete)

### Electrical foundation and power path (was P004, then P006)

**Still required before enable.** Now the opening of P007 construction (last shop night). Keep: Hub/battery/switch, labels, strain relief, power-path diagram, emergency disconnect explain-back. Drop from preseason: treating wiring as Control Hub stack acceptance.

### One-motor bring-up, SDK, and first movement (was P005, then P006)

**Still required.** Now P007 construction (programming + restrained tests + slow floor if safe). P006 only read existing code — that does **not** count. Keep: wheels-off-floor first, one motor at a time, port/direction table, DS disable, minimal robot-centric TeleOp. Drop from preseason: CAD export during bring-up; TRACE as a library lesson; field-centric / odometry / auto.

### Driver baseline / chassis reliability (was original P006, then P007 dial-in)

**Deferred further.** First movement is now P007. Dial-in (mix, speed limit, deadband, practice) is P007 leftover **only if** the robot already moves. A polished measured baseline is **not** a Kickoff gate. If P007 is blocked or only reaches first movement, S002 Meeting B driving time is the catch-up — do not pretend P007 produced a baseline.

### Reusable mechanism laboratory (was P007)

**Deferred after Kickoff — not placed in P008.** Pratt’s process puts comparative mechanism work after the game is known. Original three stations (capstan load/slip, one slide stage, surgical-tube transport) remain useful as a **post-Kickoff experiment design**, retargeted at official game pieces.

Reuse **conditionally** at:

- [S001](../sessions/S001-meeting-a.md) only as sketches during brainstorm **if** the official game needs those principles
- [S004](../sessions/S004-meeting-b.md) comparative tests with [prototype-test-record.md](../../../templates/prototype-test-record.md) (S003 is Onshape)
- Later cadence sessions if G1/G2 keep those principles on the ranked list

Do **not** bolt speculative BIOBUZZ mechanisms onto the Strafer before K001. The [preseason-kickoff-gate.md](preseason-kickoff-gate.md) still applies. Do **not** force this lab into the FRC tour.

### Kickoff readiness review (was P008)

**Moved to P007** (integration + closeout). Keep: Kickoff worksheet, K001 roles, fact/assumption/idea split, MVP thinking, [student-learning-goal.md](../../../templates/student-learning-goal.md) baselines ([FORGE#26](https://github.com/The-Allsparks/FORGE/issues/26)). Remove the original dependency on P007 experiment tables.

### FRC team tour (now P008)

**New use of the 11 September slot.** Event/tour session: observations, questions, thank-you, reflection. Host details stay **outside git**. Inspiring FRC practices must be checked for FTC scale, rules, hardware, budget, and team capacity.

### First Onshape lesson and custom-part export (was P004–P005)

**Converted to coach preparation + post-Kickoff FRC class.** Custom plates/guards remain **possible** if the as-built robot needs them. They are not confirmed P002 accomplishments in FORGE.

- Mentors: create the team Onshape doc and student accounts **after Appendix F consent** ([onshape-cad.md](../../../learning-paths/onshape-cad.md))
- Do **not** spend P007 shop time on CAD before first movement
- First shop CAD lesson: **[S003](../sessions/S003-meeting-a.md) (21 Sep)** with the P008 FRC host
- [S006](../sessions/S006-meeting-b.md) authorizes BOM/fab — it is not a beginner login night
- STL/DXF export: when a custom part actually blocks build, not on a fixed preseason date
- G2 comparative tests: **[S004](../sessions/S004-meeting-b.md)** if S003 is full-team CAD

### Paper dimensioned sketches for CAD (was P003)

**Incomplete unless the notebook already has them.** P007 as-built measurements can replace the missed P003 dimension sheet. CAD is not a P007 exit check.

## Shortened, combined, coach-prep, or dropped

| Item | Action | Why |
| ---- | ------ | --- |
| Full original P003 remaining-drivetrain agenda | **Inspect at P007**, finish only what blocks wiring or safe motion | Three construction meetings may have done some of it; P006 did not inspect metal |
| P004 electrical + P004 Onshape in one meeting | **Split** — electrical at P007; Onshape off the critical path | Wiring is a prerequisite for movement; CAD is not |
| P005 bring-up + original P006 driver baseline as two full meetings | **Compressed into P007 construction** after P006 was only a code walkthrough | Two hours cannot also be a mechanism lab, a tour class, or a full dial-in |
| P006 electrical/programming/first movement | **Did not run** — code walkthrough only; work moved to P007 | Recorded 4 Sep 2026 |
| P007 three-station mechanism lab | **Moved after Kickoff** (S004 if game-justified; S001 sketches only) | Game unknown at the time; S003 is FRC Onshape; P008 is the FRC tour |
| P008 Kickoff readiness as a full meeting | **Moved to P007** | P008 is the tour; K001 is the next day |
| GitHub robot-project workflow | **Coach prep** until [#2](https://github.com/The-Allsparks/FORGE/issues/2) | Cannot teach a blocked TeamCode URL; local FTC project still used at P007 |
| ViDAR / AMPER / MIMIC / BEACON / HELM / ECHO / wrapper | **Dropped from preseason shop time** | Roadmap, not Kickoff readiness |
| Pedro follower tuning | **Unchanged — still post-Kickoff** | Chassis must exist and drive first |
| Repeating P001 safety presentation | **Not repeated** | Done; add battery/enable rules only |

## Offset from three construction meetings

Useful readiness that **does** offset some delay:

- Students have spent ~six hours building, not only hearing a chassis lecture
- P001 organization plus three build meetings is real mechanical onboarding
- P005 rules discussion means Kickoff analysis is not the team’s first time reading rules
- P006 code reading is first contact with FTC source — **not** a deployed TeleOp

What those meetings **do not** offset:

- Electrical, DS/RC, SDK deploy, or driving
- A documented inspectable configuration
- Mechanism evidence for BIOBUZZ
- Onshape skill
- Kickoff worksheets (those still need P007)

## Post-Kickoff time still protected

Do not steal S001–S014 for leftover preseason software courses. After K001 the team still needs:

- Strategy and minimum viable robot definition (K001–S002 / G1). **S001 (14 Sep)** is season updates, official game review, and brainstorm — not fabrication
- Season-robot construction (S002+ after G1; crude tests at S004)
- First Onshape lesson (**S003**, FRC-hosted)
- Programming and driving (every Meeting B)
- Testing and iteration (G2–G7)

If P007 first movement fails, S001 construction may finish R0 chassis — then return to K001 MVP. If P007 dial-in never starts, S002’s 55-minute driving block is catch-up, not a second mechanism lab.

## Coach input still required

FORGE cannot invent:

1. As-built robot state after P004 (motors, wheels, mounts, guards, any wiring)
2. Whether any motor-mount, narrowing, or side-guard parts were ordered or have arrived
3. Whether P002 finished sponsor thank-you cards (P001 only confirms they **started**)
4. Whether a minimal TeleOp will build and deploy on a mentor laptop before P007
5. FRC tour host, location, personnel, and photo policy (keep out of git)
6. Whether extra shop time exists outside P007 (P006 did not produce bring-up; P008 is the tour)

## Related files

- [season-plan.md](../season-plan.md)
- [readiness-dashboard.md](../readiness-dashboard.md)
- [preseason-software-allocation.md](preseason-software-allocation.md)
- [preseason-kickoff-gate.md](preseason-kickoff-gate.md)
- [pratt-crosswalk.md](pratt-crosswalk.md)
