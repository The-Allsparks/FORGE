# Lab SIM001 — ViDAR browser simulator

| Field | Value |
| ----- | ----- |
| Lab ID | SIM001 |
| Kind | simulated |
| Projects | ViDAR |
| Difficulty | Foundation |
| Duration | 25 minutes (Meeting A integration) |

## Objective

Read range and bearing without a Control Hub.

## Prerequisites

[sim/README-SIM.md](https://github.com/The-Allsparks/ViDAR/blob/main/sim/README-SIM.md), [TEACHING.md Lesson 4](https://github.com/The-Allsparks/ViDAR/blob/main/docs/TEACHING.md).

## Safety

None physical. Do not treat sim HSV as competition truth.

## Procedure

1. Serve the sim (`serve_sim.ps1` or Python script per ViDAR docs).
2. Start with Mock scene.
3. Read sidebar range.
4. Empty the scene; confirm students do not keep last pose as truth.

## Observable result

Screenshot of overlay + sidebar.

## Failure injection

Empty scene / occluded object.

## Evidence

Screenshot (not video).

## Explain-back

Robot space vs pixels.

## Rollback / disable

Close the browser. Do not copy detections into teleop.

## Fallback if hardware missing

This lab is the fallback.

## Authoritative links

- [ViDAR TEACHING](https://github.com/The-Allsparks/ViDAR/blob/main/docs/TEACHING.md)
