# Sparkee module records

Per-module documentation for competition Sparkee. Template: [../../../../templates/sparkee-module-record.md](../../../../templates/sparkee-module-record.md).

**Status:** **BLOCKED pre-Kickoff** — module names and interfaces depend on BIOBUZZ ([biobuzz-unverified-facts.md](../biobuzz-unverified-facts.md)).

## After G3 gate

Create one file per approved module:

```
M-drivetrain.md
M-intake.md
M-scorer.md
…
```

Copy [../../../../templates/sparkee-module-record.md](../../../../templates/sparkee-module-record.md) for each. Track in [FORGE#27](https://github.com/The-Allsparks/FORGE/issues/27).

## Candidate modules (placeholders — rename after Kickoff)

| Placeholder ID | Likely role | G3 decision |
| -------------- | ----------- | ----------- |
| M-drivetrain | Mecanum mobility | Required |
| M-intake | Game object acquisition | MVP or starter fallback |
| M-transport | Index / hold | MVP-dependent |
| M-scorer | Primary scoring | MVP or starter fallback |
| M-endgame | Lift / endgame | Only if ranking value justifies |
| M-vision | Cameras / sensors | Per software contract |
| M-power | PDH / wiring | Required |

Do not fabricate custom modules until **G3** passes.
