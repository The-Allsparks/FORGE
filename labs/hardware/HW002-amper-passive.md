# Lab HW002 — AMPER passive observe

| Field | Value |
| ----- | ----- |
| Lab ID | HW002 |
| Kind | hardware |
| Projects | AMPER, TRACE |
| Difficulty | Developing |
| Duration | 25 minutes |

## Objective

Graph voltage against a known command without changing motors.

## Prerequisites

[hardware test card](https://github.com/The-Allsparks/AMPER/blob/main/docs/validation/hardware-test-card.md) steps 1–2. Wheels off.

## Safety

No uncontrolled brownout. Adult supervision.

## Procedure

Follow AMPER Phase 1 exercise adapted to drive-only. Circle the largest sag. Write the command that started just before it.

## Observable result

CSV or notebook graph.

## Failure injection

AMPER disabled vs enabled; motion must match.

## Evidence

CSV snippet (redacted).

## Explain-back

What AMPER cannot repair.

## Rollback / disable

`AmperPolicies.disabled()`.

## Fallback if hardware missing

DS voltage table by hand.

## Authoritative links

- [AMPER phases](https://github.com/The-Allsparks/AMPER/blob/main/docs/power-management/phases.md)
