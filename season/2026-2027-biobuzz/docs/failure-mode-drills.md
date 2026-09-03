# Failure-mode and degraded-operation drills

Match robots fail in boring ways. Practice those ways **on purpose**, with a mentor, then record the result.

Canonical record: [failure-record.md](../../../templates/failure-record.md). Acceptance: [acceptance-criteria.md](acceptance-criteria.md). Safety: [safety-and-enablement.md](../../../docs/safety-and-enablement.md).

**Strategic influence:** Pratt, *Why Most FTC Teams Fail (And How Not To)* (adapted; not endorsed). Do not create an illegal or unsafe condition to "simulate" a drill.

## Safety (non-negotiable)

- Mentor present. Known disable path before the fault.
- No uncontrolled brownout. No gravity-load jams to "test" software.
- Do not disable a drivetrain motor by damaging hardware — unplug **one** motor at the controller **only** if the robot is blocked/restrained and students understand the remaining drive.
- Restore a healthy configuration before anyone leaves.

## Catalog

| ID | Fault | What students practice | Earliest honest session |
| -- | ----- | ---------------------- | ----------------------- |
| F1 | Loss of one drivetrain motor | Drive, rotate, and return to pit on three motors if safe | S013 or S014 (restrained first) |
| F2 | Jammed game piece | DS stop → clear → reset mechanism state → timed restart | S011 (one drill); S029 (deeper) |
| F3 | Sensor or vision failure | Cover camera / unplug limit; complete cycle on backup plan | S011 or S013; S028 |
| F4 | Communications interruption | What DS shows; do not invent BEACON commands; restart procedure | S013; S030 |
| F5 | Mechanism indexing failure | Safe state; skip score; still drive | S011 if hardware exists |
| F6 | Autonomous failure + fallback | Missed auto → teleop plan without arguing | S010 declare; S013 run |
| F7 | Time-limited pit repair | One P0 repair under a visible timer | S014; S029 |
| F8 | Depleted battery / sag | Swap pack; log; finish a cycle | Clinic notes; S024 |

G7 requires **at least two** catalog items before League 1S/2S ([decision-gates.md](decision-gates.md#g7--reliability--feature-freeze-gate)). Clinic (10 Oct) may collect opportunistic faults; do not debut new mechanisms there.

## Competition-one assignments (do not duplicate the catalog in every session)

| Session | Required drill |
| ------- | -------------- |
| S008 / clinic | Inspection + opportunistic F8 notes only |
| S011 | **One** of F2, F3, or F5 (write the choice on the board) |
| S013 | **Two** remaining items; include F6 if auto is in the plan |
| S014 | F7 timed pit; F1 only if restrained test already passed |
| S024–S030 | Deeper set after league evidence (titles already in `calendar.yaml`) |

## Pass criteria (default)

Three trials in the degraded configuration **or** one honest abort with a written reason. Robot remains safe. Students can explain the fallback in one sentence. File a failure record even if the drill was easy.
