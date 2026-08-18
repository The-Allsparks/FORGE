# Student guide

Welcome to FORGE — **Framework for Onboarding, Robotics, Guidance, and Education**.

This repository is the season map for The Allsparks. It tells you what we are building this week, what evidence to collect, and when a software feature is allowed to be more than a passenger.

It is **not** the robot code. Robot code lives in the team's FTC project and in the library repositories. That project URL is recorded in [team-robot-project.md](team-robot-project.md) when the team publishes it.

## How a meeting works

We meet twice a week for two hours.

- **Meeting A** is mostly building and wiring, with a short software integration on what you just built.
- **Meeting B** is mostly testing and driving, with repair and log review.

You will hear short explanations while you work. You will not sit through a long class instead of building.

## What you should be able to do

By the end of a session you should be able to:

1. Say the driving question in one sentence.
2. Point to the robot (or simulation) result.
3. Show evidence — usually a TRACE log, photo, or notebook sketch.
4. Answer the explain-back questions without reading the answer off a slide.
5. Name how to turn an optional feature **off**.

## The libraries (one robot)

| Name | What it helps you notice or do | Default for competition until proven |
| ---- | ------------------------------ | ------------------------------------ |
| TRACE | What happened, in order | On as a recorder, never as a motor commander |
| AMPER | Battery voltage, current, sag | Passive observation |
| MIMIC | Mechanism states and limits | Snapshots / observation until tested |
| ViDAR | Where things are in robot space | Simulation or one camera; no auto authority |
| BEACON | Whether communications look fresh | Passive observation |
| ECHO | Sound cues for the driver | Off / simulation only |
| HELM | Names for goals and fallbacks | Off; vocabulary and shadow only |
| Pedro Pathing | Chassis movement in autonomous | Conventional auto is required |

If a library is confusing, open its page in `projects/` and follow the links. Those repositories are the source of truth.

## Roles

You might be building, wiring, programming, driving, or documenting on a given day. You will rotate. Everyone still helps with evidence and explain-backs.

## Safety

- No energized robot without a mentor present.
- Know the disable / e-stop path before you drive.
- Do not enable a new "smart" feature to see what happens.
- ECHO stays quiet or on a training UI until mentors and drivers agree. If sound is on, start quiet and mute immediately if anyone cannot hear referees or coaches. See [ECHO hearing safety](https://github.com/The-Allsparks/ECHO/blob/main/docs/hearing-safety.md).
- Do not put names, passwords, or Wi-Fi keys in logs.

## Evidence

A working robot that nobody can explain is not ready. A beautiful log of a robot that does not drive is not ready either. We want both: motion and evidence.

Use the session's evidence section. TRACE is the usual tool: [TRACE student learning path](https://github.com/The-Allsparks/TRACE/blob/main/docs/student-learning-path.md).

## If hardware is missing

Every session has a fallback. You still learn the vocabulary, run a simulation or paper exercise, and write the notebook artifact. Then you return to the physical robot as soon as it exists.

## Finding this week's plan

1. [Season README](../season/2026-2027-biobuzz/README.md)
2. [Calendar](../season/2026-2027-biobuzz/calendar.yaml)
3. The session file for today
4. [Readiness dashboard](../season/2026-2027-biobuzz/readiness-dashboard.md) — update it with a mentor in the last minutes
