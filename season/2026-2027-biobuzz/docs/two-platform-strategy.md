# Two-platform strategy

Adapted from the **principle** behind Brogan M. Pratt's separate programming and prototype chassis ([playlist](https://www.youtube.com/playlist?list=PLRHdgFNRLyaM6TmNVVHKqVnnyntDDYDNt)) — without requiring two fully duplicated competition robots.

## Platforms

| Platform | Role | When used |
| -------- | ---- | --------- |
| **Hybrid Strafer** (preseason build) | Stable software and driver-development platform; Pedro familiarity | Preseason through season; after G7 for Version 2 research |
| **Sparkee** (competition one) | Modular competition robot | Post-G3 fabrication through events |
| **Official starter-bot design** | Scoring baseline and **fallback** | G2 comparison; G3/G5 fallback if custom slips |
| **Bench / fixture rigs** | Mechanism development without blocking Sparkee | G2 exploration; Version 2 after G7 |

## Shared parts inventory

Maintain a table in the engineering notebook (updated at G3 and G4):

| Part / assembly | Strafer | Sparkee | Fixture | Notes |
| --------------- | ------- | ------- | ------- | ----- |
| Mecanum wheel set | | | | |
| Control Hub | | | | One Hub — schedule swaps |
| Battery | | | | |
| Motors (by function) | | | | |
| Custom module X | | | | |

**Rule:** The same physical component cannot be planned in two places simultaneously. If Strafer donates a part to Sparkee, update Strafer status to `non-driving` until replaced.

## Software implications

- Preseason Pedro tuning on Strafer **does not** transfer unchanged to Sparkee mass and geometry — retune at G6 on Sparkee.
- Release tags must record which platform they were tested on.
- Minimum viable stack on Strafer during preseason: SDK deploy, TRACE habit, basic teleop.

## Version 2 research boundary

After Sparkee reaches G7 mechanical/software freeze:

- Strafer, fixtures, or spare modules may host next-mechanism experiments.
- **Forbidden:** Version 2 work that steals time from competition-one reliability, driving, portfolio, or judging before G8.

## Fallback path

If custom modules miss G5:

1. Install official starter-bot scoring assembly on Sparkee drivetrain.
2. Re-run minimum auto and teleop on fallback configuration.
3. Document in gate review and portfolio as scope decision — not failure to disclose.
