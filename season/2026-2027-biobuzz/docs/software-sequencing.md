# Software sequencing

The Allsparks software vision stays intact. Competition-one **scope** is gated. Libraries are not simultaneous requirements for the first robot.

**Does not delete:** ViDAR, AMPER, MIMIC, BEACON, TRACE, HELM, ECHO, Pedro Pathing, or driver-assistance research. It **orders** them.

Principle: [guiding-principle.md](guiding-principle.md). Enablement: [safety-and-enablement.md](../../../docs/safety-and-enablement.md). Combined stack: [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4). TeamCode URL: [issue #2](https://github.com/The-Allsparks/FORGE/issues/2) (blocked).

**Strategic influence:** Pratt, *Why Most FTC Teams Fail (And How Not To)* — partial automation only after base mechanisms work (adapted; not endorsed).

## Four tiers

Every library row lives in **exactly one** tier for competition one until a gate moves it. G3 records the contract. Promoting a row requires the four tests plus Hub evidence when the claim is "runs on the robot."

### 1 — Required for the minimum viable competition robot

| Capability | Why it is required | Notes |
| ---------- | ------------------ | ----- |
| FTC SDK deploy, OpMode select, INIT, start, stop | Cannot inspect or drive | First contact P007 as actually completed |
| Drive teleop + documented controller map | R0 | |
| Known-good release / rollback | Pit | Local TeamCode until [#2](https://github.com/The-Allsparks/FORGE/issues/2) |
| TRACE (or paper timeline) on real tests | Evidence, Think | Recorder only |
| Conventional auto **or** written teleop-only | R1 | Pedro owns chassis motion when used |
| MIMIC states for **scored** mechanisms that exist | Safe mechanism operation | Not a reason to invent mechanisms |

### 2 — Valuable before the first league meet (if earned)

Promote only when the base mechanism already meets [acceptance-criteria.md](acceptance-criteria.md).

| Capability | Promotion trigger |
| ---------- | ----------------- |
| AMPER **passive** voltage/current observation | Wiring exists; no limiting |
| BEACON **passive** freshness vocabulary | Does not command recovery |
| MIMIC interlocks / limits on scored mechanisms | Hardware present; homing still optional |
| Driver assistance that removes a **demonstrated** teleop mistake | S012 / G6 — "if earned" |
| Inspection and software-release checklists | S008–S014 |

### 3 — Later-season enhancement (after League 1S/2S unless G6 already passed)

| Capability | Gate |
| ---------- | ---- |
| Alternate auto paths / alliance-specific autos | After one reliable path |
| ViDAR detections consumed by drive or auto | Strategy + measured value + stale-vision fallback |
| AMPER **active** limiting | Envelope understood; wiring healthy |
| BEACON **intervention** | After passive use in matches |
| Additional driver automation | Does not raise cognitive load |

### 4 — Research or offseason (not League 1S/2S requirements)

| Capability | Rule |
| ---------- | ---- |
| HELM **execute** / chassis authority | **Never** in this curriculum. Pedro owns motion. |
| ECHO match audio | Off until ECHO feasibility + hearing safety + workload evidence |
| Multi-camera ViDAR | Placement discussion only until one camera is useful |
| TRACE unified cross-library adapters | TRACE Phase 4 in the TRACE repo |
| HELM intent trees with match authority | Paper / shadow / validate only |
| Advanced MIMIC homing as a season goal | Only if the mechanism requires it and R2 already works |

Preseason treatment (through 11 Sep) remains [preseason-software-allocation.md](preseason-software-allocation.md) (~30 min/week). After Kickoff, software time grows but still **serves the current release**, not the full roadmap.

## Driver assistance

Partial automation (aim assists, intake presets, auto-transfer) is **R5**. It is allowed only when:

1. The mechanism already passes its R2/R3 acceptance sample.
2. Drivers can complete the cycle **without** the assist (fallback).
3. The assist reduces measured workload or error rate — not "because the library exists."

## Session rule

Library deep-dives (ViDAR, BEACON, ECHO, HELM) run **only when** the G3 contract places that library in tier 1 or 2. Calendar titles for S005–S014 already name gates; legacy library headings inside those files are secondary. Mentors retime to the gate ([FORGE#28](https://github.com/The-Allsparks/FORGE/issues/28)).
