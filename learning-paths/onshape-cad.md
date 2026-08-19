# Onshape CAD learning path

The Allsparks use **Onshape** for custom parts that must be **3D-printed, machined, or ordered** (goBILDA, etc.). No student is assumed to know Onshape at season start. Spread learning across **preseason P001–P003 and S001–S002** so CAD keeps pace with the Strafer build — not a separate course that displaces shop time.

**Authoritative tutorials:** [Onshape Learning Center](https://learn.onshape.com/) and [Onshape Help](https://cad.onshape.com/help/). FORGE does not duplicate those lessons; each session assigns one skill to practice on the robot.

## Session map (preseason)

| Session | Onshape focus | Robot tie-in | Exit evidence |
| ------- | ------------- | ------------ | ------------- |
| **P001** | Accounts, mm units, UI tour; measure frame → rail spacing | Strafer chassis as-built | Key dimensions in a Onshape sketch |
| **P002** | Layout sketch: wheel/motor positions, intake clearance zone | Modified drivetrain decision | Updated layout vs standard StarterBot |
| **P003** | Mount plate sketch: Hub, battery, switch | Control-system locations | Plate concept + print vs order note |
| **S001** | Export (STL/DXF) or dimensioned drawing for **one** custom part if shop needs it | Correction bracket or spacer | Print/order checklist with owner |
| **S002** | As-built update: change CAD to match measured baseline | Drivetrain inspection numbers | Revision note in CAD version history |
| **P004–P005** | Optional: envelope sketch for prototype experiments | Capstan/tower/transport fixtures | Link CAD rev to notebook |

If **P001 already ran** without Onshape, mentors run the account + sketch block as the **first 15 minutes of P002** before drivetrain work.

## Foundation (P001)

- Team workspace or shared folders; student accounts under mentor policy
- Millimeters; hole patterns compatible with goBILDA spacing when possible
- Sketch → constrain → extrude; do not skip constraints
- **Not today:** assemblies, drawings, import/export (later sessions)

## Developing (P002–P003)

- Top-down layout on chassis profile
- Clearance zones as sketch regions (intake, servo mount) — link to [decision-record](../templates/decision-record.md)
- Simple plate with holes; name features for pit readability

## Integration (S001–S002)

- Export for shop printer or mentor order submission
- Record material, infill, and **who prints** in the notebook — not in git if it includes addresses
- After driver baseline, fix CAD when reality differs from model (normal engineering)

## Pairing

- **Builder + CAD pair** on the same subsystem each Meeting A
- CAD students still attend safety and inspection blocks
- Programmers may CAD mount plates; they still own TRACE integration minutes during S001

## Award tags

- **C** — layout vs standard StarterBot ([decision-record](../templates/decision-record.md))
- **D** — clearance dimensions drive custom plate design
- **Design / Innovate** — photos of printed part on robot

## What FORGE does not own

- Onshape feature source or version pins
- Printer profiles, slicer settings, or vendor order accounts
- Game-specific mechanism CAD after Kickoff — update in robot repo or team cloud per mentor policy
