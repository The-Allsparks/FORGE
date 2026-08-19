---
id: S011
title: "Pedro Pathing conventional autonomous"
date: 2026-09-22
meeting_type: A
season_phase: kickoff-to-clinic
event_checkpoint: clinic
status: complete
difficulty: Developing
projects: [PEDRO, TRACE]
active_features: []
---

# S011 — Pedro Pathing conventional autonomous

## Session identity

| Field | Value |
| ----- | ----- |
| Session ID | S011 |
| Title | Pedro Pathing conventional autonomous |
| Calendar date | 2026-09-22 (planning input; Tuesday Meeting A) |
| Relative week | Kickoff-to-clinic week 2 |
| Meeting type | A |
| Season phase | kickoff-to-clinic |
| Event checkpoint | clinic |
| Difficulty | Developing |

## Driving question

Can we complete one simple, repeatable autonomous path without vision, HELM, or ECHO — and still keep building the robot?

## Student-facing objective

Students continue MVP construction, mount or verify localization, and leave with either a short Pedro path they can explain **or** a documented timed drive-forward auto plus a paper path. Official Pedro tuning takes up to a few days; this meeting does not finish every tuner.

## Robot outcome

- Localization hardware mounted or drive-encoder localizer chosen
- One of: (a) Localization Test seen on Panels/dashboard, (b) a two-pose Pedro path run at least twice, or (c) paper path walked + `DriveForward` fallback OpMode
- TRACE events `Auto/start` and `Auto/end` if software is on the Hub; otherwise paper times
- HELM, ECHO, and ViDAR **not** in the auto

## Prerequisites

- Driveable chassis from S002
- Android Studio on at least one mentor laptop ([Pedro does not support OnBot Java or Blocks](https://pedropathing.com/docs/pathing))
- Team robot project — see [team-robot-project.md](../../../docs/team-robot-project.md). If that URL is still empty, install into the local TeamCode the team is actually flashing
- [Pedro Quickstart](https://github.com/Pedro-Pathing/Quickstart) or Pedro added per current docs
- Kickoff MVP list from SK01 (if Kickoff was missed, path is still "leave starting area / park-shaped motion" without invented scoring)

## Vocabulary

path · localization · pose · conventional auto · fallback · tuner (do not finish all today)

## Safety concerns

- First auto: clear floor, exclusion zone, DS stop in a mentor's hand
- Omnidirectional drive required for Pedro; do not force Pedro onto tank
- Gentle bump only during failure injection — no ramming
- Do not "fix" localization by turning on ViDAR
- Robot Wi-Fi for Panels is for the shop; follow event Wi-Fi rules at competition ([Pedro dashboard notes](https://pedropathing.com/docs/pathing/dashboard))

## Required hardware

- Drivetrain; charged battery
- Localization as the team actually has: drive encoders (allowed), dead wheels, Pinpoint, or OTOS — pick one and follow **that** Pedro page
- Tape or cones for a 2–3 waypoint course (about one to two tiles)
- Optional: laptop for Panels at `192.168.43.1:8001` on robot Wi-Fi

## Required software

- Pedro Pathing in the team FTC project
- `Tuning` OpMode from Pedro/Quickstart
- One team `@Autonomous` that is either a tiny Pedro path **or** timed drive-forward
- TRACE events around auto if TRACE is installed; else DS timer
- HELM off; no ViDAR in this OpMode

## Preparation required before the meeting

- Read [Pedro introduction](https://pedropathing.com/docs/pathing) and [tuning overview](https://pedropathing.com/docs/pathing/tuning)
- Open the localizer page that matches hardware: [localization index](https://pedropathing.com/docs/pathing/tuning/localization) (drive encoders are valid)
- Confirm Android Studio opens the robot project
- Stage localization mount hardware
- Tape a short course before students arrive if the field is available

## Exact 120-minute agenda

| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Goal: conventional auto fallback; Pedro owns chassis; we will not finish every tuner today; safety: exclusion zone; assignments |
| 75 | Construction | MVP mechanism remaining work **and** localization mount (or encoder cable dress if using drive encoders). Mechanical pair owns the mount; electrical pair owns wiring per the chosen Pedro localizer page |
| 25 | Integration | Run Localization Test **or** one short path **or** encode the paper path. If Pedro is not compiling, write timed drive-forward auto and walk the paper path. TRACE start/stop events |
| 10 | Closeout | Rep count or blocker; dashboard Conventional autonomous row; explain-back; cleanup |

## Mentor demonstration

Under five minutes: show official constraints (omni drive, some localization, Android Studio). Show where `Constants` / follower setup lives in **their** project if it exists. Do not lecture PIDF vs predictive braking — name that those tuners exist on [tuning](https://pedropathing.com/docs/pathing/tuning) and are homework/next Meeting B.

## Student work

| Path | Work |
| ---- | ---- |
| Mechanical | Localization mount square to the robot; bumpers/skids if needed for auto |
| Electrical | Encoder / Pinpoint / OTOS / drive-encoder wiring as chosen; strain relief |
| Programming | Localizer constants from the official page; tiny path or drive-forward fallback; TRACE events |
| Drive team | Watch every auto; call stop; time completions |
| Documentation | Field sketch with start pose and two waypoints; note which localizer |

## Integrated build or test activity

1. If localization is new: run Pedro `Tuning` → Localization Test. Confirm forward increases `x` and strafe left increases `y` as [Pedro localization](https://pedropathing.com/docs/pathing/tuning/localization) describes — or record that the team has not reached that screen yet.
2. If localization already looks sane: run a two-pose path twice. Success is **repeatability**, not speed.
3. If neither is possible: walk the taped path, write poses on paper, and keep a timed `setPower` forward auto as the emergency fallback.

## Failure-injection scenario

Mentor gives a **gentle** bump mid-path or mid-drive-forward. Students explain whether the robot recovered toward the path (Pedro) or just kept pushing (timed auto). Do not enable vision to compensate.

## Evidence to collect

- Path sketch
- Number of complete runs and times
- Localization notes (jumped / spun / looked right)
- TRACE or paper `Auto/start`–`Auto/end`
- Honest dashboard ladder (likely 4 controlled hardware, not 8)

## Student explain-back questions

1. What happens if HELM is off? (This auto still runs.)
2. Who owns chassis motion?
3. How do you disable this auto in a pit? (Select teleop; do not run the OpMode.)
4. Why is a boring repeatable auto a higher priority than HELM execute or ViDAR-guided drive?
5. Which localizer did we choose, and which Pedro page is the authority for it?

## Assessment or exit check

A student who is not the programmer can retell the path in human words. The team has either repeated runs or a written blocker plus fallback auto.

## Portfolio or engineering-notebook artifact

Field sketch: start, waypoints, which localizer, "ViDAR not used." Photo of localization mount.

## Competition enablement impact

Conventional autonomous moves toward practice-field (ladder 4–5) only if it actually ran. **Not** competition-approved from this session. HELM stays disabled. Pedro is allowed as the chassis follower when the path is the one students can explain.

## Rollback procedure

Select teleop on the DS. Do not run the auto OpMode. If Pedro misbehaves, the timed drive-forward OpMode is the fallback — keep it in the project. Optional systems remain off.

## Cleanup requirements

Robot disabled; battery stored; tape removed if the venue requires it; laptop off robot Wi-Fi before leaving.

## Next-session preparation

- Continue tuners on Meeting B repair time using [tuning](https://pedropathing.com/docs/pathing/tuning) — do not steal driving block for a tuner marathon
- S012 only if Kickoff mapped a vision need; otherwise construction and auto reps
- Write the chosen localizer name on the dashboard "next test" cell

## Hardware-unavailable fallback

Walk the taped (or hallway) path. Students write poses as inches and headings. Encode later. Construction block still builds MVP and a cardboard localization mount.

## Robot-unavailable simulation option

[Pedro Visualizer](https://github.com/Pedro-Pathing/Visualizer) if the team can run it; otherwise paper Bézier/polyline sketch. Programmers read the matching localizer doc. No invented constants in FORGE.

## Links to authoritative project documentation

- [Pedro Pathing site](https://pedropathing.com/)
- [Introduction](https://pedropathing.com/docs/pathing)
- [Tuning](https://pedropathing.com/docs/pathing/tuning)
- [Localization](https://pedropathing.com/docs/pathing/tuning/localization)
- [Drive encoder localizer](https://pedropathing.com/docs/pathing/tuning/localization/drive-encoder)
- [Dashboard / Panels](https://pedropathing.com/docs/pathing/dashboard)
- [PedroPathing repo](https://github.com/Pedro-Pathing/PedroPathing)
- [Quickstart](https://github.com/Pedro-Pathing/Quickstart)
- [Visualizer](https://github.com/Pedro-Pathing/Visualizer)
- [projects/pedro-pathing.md](../../../projects/pedro-pathing.md)
- [docs/team-robot-project.md](../../../docs/team-robot-project.md)
- [ViDAR Pedro integration](https://github.com/The-Allsparks/ViDAR/blob/main/docs/PEDRO_INTEGRATION.md) (do **not** use today)

## Mentor notes

Pedro's own docs say tuning can take days. Protect the 75-minute build. A drive-forward auto that students understand beats a half-tuned follower nobody can roll back. If the team robot GitHub URL is still missing, flash whatever project they actually use and update [team-robot-project.md](../../../docs/team-robot-project.md) after the meeting.
