# Lab I002 — Combined stack install diagnosis

| Field | Value |
| ----- | ----- |
| Lab ID | I002 |
| Kind | integrated |
| Projects | TRACE, AMPER, MIMIC, ViDAR, BEACON, HELM, ECHO, PEDRO |
| Difficulty | Integration |
| Duration | fits in a 25-minute Meeting A integration block or 35-minute Meeting B repair block |

## Objective

Prove students can add **or refuse** a library without breaking conventional teleop and autonomous. This lab does not compile TeamCode inside FORGE.

## Prerequisites

- [stack-acceptance.md](../../docs/stack-acceptance.md)
- [student-install.md](../../docs/student-install.md)
- [team-robot-project.md](../../docs/team-robot-project.md) — if the URL is still unpublished, run the **paper path** below
- One library install doc open (AMPER install is the packaging reference)

## Safety

No new active flags. No HELM execute. No ECHO match audio. Mentor present if a Hub is powered.

## Procedure

**If a TeamCode repo exists**

1. Confirm teleop drives with all optionals independently disabled.
2. Confirm conventional auto still exists (do not run it on a table without blocks/carpet rules from the session).
3. Add or already-have **one** optional library using its install doc.
4. Compile. If a Hub is available, deploy and run teleop with that library still off.
5. Name the disable path out loud.
6. Record: Gradle wrapper unchanged; FORGE is not a dependency.

**Paper path (no published robot repo — current Allsparks state)**

1. Draw the composition-root diagram from stack-acceptance.md.
2. Write the install order and the disable line for each library.
3. Write the blocker: “compile-checked combined TeleOp is issue #2 / #4.”
4. Do not invent a GitHub URL.

## Observable result

A teammate can disable the optional just discussed in one minute, and can say whether today’s work was Hub-compile evidence or paper only.

## Failure injection

Someone adds FORGE as a Gradle project, or enables HELM “just to see.” Students must reject both.

## Evidence

Notebook: library name, install doc URL, disable command, teleop still works (or paper blocker). Tick Combined stack on the [readiness dashboard](../../season/2026-2027-biobuzz/readiness-dashboard.md) only as `blocked` / paper — not `approved`.

## Explain-back

What is the composition root? What remains if every Allsparks optional is off?

## Rollback / disable

[student-install.md](../../docs/student-install.md) table. Pit copy: [pit-and-inspection.md](../../season/2026-2027-biobuzz/pit-and-inspection.md).

## Fallback if hardware missing

Paper path. AMPER/TRACE desktop tests in their own repos are not combined Hub evidence.

## Authoritative links

- [AMPER install](https://github.com/The-Allsparks/AMPER/blob/main/docs/install.md)
- [conventions.md](../../docs/conventions.md)
- [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4)
