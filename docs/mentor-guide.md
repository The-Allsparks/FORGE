# Mentor guide

## Goal

Students build and drive a working robot. FORGE exists so the Allsparks libraries support that robot instead of replacing the season.

**First integration priority:** [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4) — combined FTC stack acceptance. Do not expand later labs as if AMPER, TRACE, ViDAR, and the rest already compose on a Control Hub. There is still no published TeamCode URL ([issue #2](https://github.com/The-Allsparks/FORGE/issues/2)). Use [stack-acceptance.md](stack-acceptance.md) and [student-install.md](student-install.md).

## How to run a meeting

1. Read the session the night before. Complete the **Preparation required** list.
2. Put the driving question on the board. Do not lecture the vocabulary list; use it while students work.
3. Keep the timer visible. Meeting A construction is 75 minutes. Meeting B driving is 55 minutes. Protect those blocks.
4. Mentor demonstrations stay under five minutes unless the session says otherwise.
5. Students do the work, collect evidence, and explain.
6. End with TRACE (or the named evidence method), an explain-back, a dashboard tick, and cleanup.
7. Write next-session prep on the whiteboard and in the engineering notebook.

## What to protect

- Adult supervision for energized robots, spinning mechanisms, and any failure injection that involves hardware.
- Exclusion zones and a known e-stop / disable path before wheels-on tests.
- Student PII and secrets out of logs (see [TRACE SECURITY.md](https://github.com/The-Allsparks/TRACE/blob/main/SECURITY.md)).
- Conventional teleop and autonomous fallbacks. Optional systems default off or passive.
- Combined-stack honesty. Desktop tests and sibling CI are not Hub evidence.
- Driver practice time. Do not spend Meeting B rewriting architecture.

## Review questions (every enablement discussion)

- Can this be disabled without rewriting subsystem code?
- Does this PR or session command hardware?
- Is the claim Control Hub / field tested, or only desktop tested?
- What is the rollback, and who can perform it in a pit?
- Can a student explain the current phase out loud?

These questions match the TRACE and HELM mentor guides. Project-specific lists:

- [TRACE mentor guide](https://github.com/The-Allsparks/TRACE/blob/main/docs/mentor-guide.md)
- [HELM mentor guide](https://github.com/The-Allsparks/HELM/blob/main/docs/mentor-guide.md)
- [ECHO mentor guide](https://github.com/The-Allsparks/ECHO/blob/main/docs/mentor-guide.md)

## Facilitation by meeting type

**Meeting A.** Construction first. Software integration uses the mechanism or wiring just finished. If hardware is missing, use the session's hardware-unavailable fallback — usually mock-up, drawing, or desktop test — then return to physical work next time.

**Meeting B.** Logs first. One test goal. Repair or tune, then repetitions. Inspection and explain-back at the end.

## Mixed experience

- Pair a developing programmer with a foundation builder on the same mechanism.
- Rotate documentation so the same student is not always "the notebook."
- Drive team still participates in explain-backs. They must be able to say what the robot will do if a cue, warning, or auto fails.

## Paperwork budget

The last 10–20 minutes update the [readiness dashboard](../season/2026-2027-biobuzz/readiness-dashboard.md) and one evidence record. If the robot still needs a wrench, finish the wrench. Capture a photo and a TRACE note rather than writing an essay.

## Kickoff

On 12 September 2026, stop inventing BIOBUZZ tasks. Use [kickoff-replan-guide.md](../season/2026-2027-biobuzz/kickoff-replan-guide.md), then edit `calendar.yaml`. Preserve build and driving time.

## When you are stuck

1. Open the project page in `projects/`.
2. Follow the deep link. Do not guess API behavior.
3. If the link is stale, file a FORGE issue and link the closest README heading.
4. Keep the robot driveable.
