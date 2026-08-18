# Pit workflow and inspection (team)

This is **not** the official FIRST inspection checklist. It is The Allsparks packing, rollback, and practice-inspect routine.

Official 2026–2027 inspection documents were listed as **coming soon** on 18 August 2026. Use FIRST's copies when they publish:

- [2026–2027 event resources](https://ftc-resources.firstinspires.org/ftc/archive/2027/event) (inspection checklist / quick reference)
- [2026–2027 team resources](https://ftc-resources.firstinspires.org/ftc/archive/2027/team)
- Current-season shortcut (when live): [Inspection checklist](https://ftc-resources.firstinspires.org/ftc/event/inspection-check)

Until the 26–27 checklist is posted, practice with the **process** (present the whole robot, size, battery, control system) and re-check against the published 26–27 list before any official inspect. Do not treat a prior-season PDF as this year's rules.

## Packing list

- Robot, battery, charger, spare battery if owned
- Driver Hub / DS, gamepads, spare USB cable
- Tools that actually got used this week
- Zip-ties, electrical tape, fasteners bag
- Printed [readiness dashboard](readiness-dashboard.md) statuses
- This page (rollback)

## Software config for events (until dashboard says otherwise)

| System | Event status |
| ------ | ------------ |
| TRACE | passive recorder if Hub evidence exists; else off |
| AMPER | passive or off — **no** limiting |
| MIMIC | observation only unless a tested protection is listed on the dashboard |
| ViDAR | unplugged or observe-only; not driving |
| BEACON | no intervention |
| ECHO | **off** |
| HELM | **off** |
| Pedro conventional auto | the auto we can explain |

## Pit rollback (under one minute)

1. DS stop.
2. Select teleop. Do not run optional autos.
3. If a flag was enabled: set TRACE `OFF` / AMPER disabled / omit ViDAR from teleop / ECHO mute and audio off / HELM `OFF`.
4. Battery disconnect if the robot will not disable.
5. Who can do this: any mentor or the designated drive-coach.

## Clinic test card (10 October is a planning input)

Copy to the notebook. Measure; do not debut features.

| Test | Planned | Result |
| ---- | ------- | ------ |
| Mechanisms under load | | |
| ViDAR under field lighting (if camera is on the robot) | | |
| Communications recovery / official stop | | |
| Battery sag (AMPER passive or DS voltage) | | |
| Driver workload | | |
| ECHO cue clarity | default skip | |
| Conventional autonomous | | |
| Inspection / pit procedure | | |

## Practice inspect (shop)

Use FIRST's list when available. Until then, walk:

1. Whole robot presented; no leftover mechanisms in the bag
2. Starting size with a cube or tape measure — **confirm numbers from the current Game Manual**, not from memory
3. Battery seated, switch reachable, Hub visible
4. Wires strain-relieved; no sharp edges
5. Optional systems match the dashboard

## After the event

Fill [templates/event-retrospective.md](../../templates/event-retrospective.md). Update the dashboard. Do not enable anything because it "worked at clinic" without the [readiness check](../../assessments/readiness/RD001-competition-approval.md).
