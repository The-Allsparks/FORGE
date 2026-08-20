# Modular architecture — Sparkee

Sparkee is The Allsparks' competition-one robot (FTC 36117). Treat it as **replaceable modules**, not one inseparable mechanism.

Module set is **derived from BIOBUZZ** after Kickoff — do not force four modules because Pratt's DECODE-era example used approximately four.

Process: [season-process.md](season-process.md). Gate G3 locks this document. Attribution: modular thinking aligns with Brogan M. Pratt's [*A 12 Week FTC Season Plan That Actually Works*](https://www.youtube.com/playlist?list=PLRHdgFNRLyaM6TmNVVHKqVnnyntDDYDNt) (adapted; not endorsed).

## Candidate module set (fill after Kickoff)

Replace placeholders with BIOBUZZ-specific names at G3.

| Module | Purpose | Competition-one priority |
| ------ | ------- | ------------------------ |
| Drivetrain | Mecanum mobility, bumpers, frame | **Required** |
| Intake / acquisition | Game object pickup | MVP or starter fallback |
| Transport / indexing / storage | Move objects toward scorer | MVP-dependent |
| Primary scoring mechanism | Score points per manual | MVP or starter fallback |
| Lift / endgame | Endgame or elevation scoring | Only if ranking value justifies time |
| Sensors and vision | Cameras, encoders, limits | Necessary vs optional at G3 |
| Electrical and power distribution | PDH, wiring, battery path | **Required** |
| Software interfaces and driver controls | TeleOp, auto, states | **Required** |

## Per-module documentation contract

Each module above must have a one-page record (notebook or linked doc) containing:

Use [sparkee-module-record.md](../../../templates/sparkee-module-record.md). Store filled copies under [docs/sparkee-modules/](sparkee-modules/) after G3.

| Field | Description |
| ----- | ----------- |
| Mounting interface | Hole pattern, rail spacing, standoff length, alignment features |
| Allowed volume | Max envelope inside frame rules (**verify** 2026–2027 size rules when published) |
| Mass estimate | Measured or scaled; update after integration |
| Motors and servos | Type, ratio, name in config |
| Sensors | Required for this module's states |
| Wiring path and connectors | Route, connector type, service loop length |
| Software class / interface | MIMIC class, HELM intent (if any), Pedro exclusion |
| Required states and transitions | e.g. IDLE → ACQUIRE → HOLD → SCORE |
| Failure behavior | Safe state on sensor loss, jam, comms drop |
| Service access | Tool clearance; which panels remove |
| Replacement time | Target minutes to swap module at pit |
| Dependencies | Other modules this one requires |

## Interface rules

1. **Mechanical:** Modules attach to common rail pattern on Sparkee frame; no module-specific frame hacks without G3 change control.
2. **Electrical:** Each module gets a labeled harness with disconnect at module boundary.
3. **Software:** MIMIC owns mechanism states; Pedro owns chassis; HELM never bypasses MIMIC or Pedro.
4. **Fallback:** Any module may be replaced by official **starter-bot equivalent** if custom version misses G5 — document swap procedure in pit materials.

## Version 2 modules

After G7 feature freeze, next-generation modules may be prototyped on:

- Hybrid Strafer platform
- Bench fixtures
- Spare module mounts

**Rule:** Version 2 work cannot remove students from Sparkee reliability, driving, documentation, or judging prep. See [two-platform-strategy.md](two-platform-strategy.md).

## Evidence

Link module tests to [prototype-test-record.md](../../../templates/prototype-test-record.md) and TRACE logs. Three trials minimum before design reactions; larger counts for reliability claims.
