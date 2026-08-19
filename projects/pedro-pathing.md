# Pedro Pathing

Pedro Pathing owns **chassis motion**. FORGE schedules a reliable conventional autonomous as a season priority. HELM, ViDAR, and ECHO may observe or advise; they do not replace Pedro as the drivetrain follower.

Authoritative documentation is **not** an Allsparks repository:

- [pedropathing.com](https://pedropathing.com/)
- [Introduction](https://pedropathing.com/docs/pathing)
- [Tuning](https://pedropathing.com/docs/pathing/tuning)
- [Localization](https://pedropathing.com/docs/pathing/tuning/localization)
- [Dashboard](https://pedropathing.com/docs/pathing/dashboard)
- [Pedro-Pathing/PedroPathing](https://github.com/Pedro-Pathing/PedroPathing)
- [Quickstart](https://github.com/Pedro-Pathing/Quickstart)
- [Visualizer](https://github.com/Pedro-Pathing/Visualizer)

## What students learn here

Localization plus path following on an omnidirectional drive. Tuning is required. Official intro: mecanum/x-drive/swerve (not tank), some form of localization, Android Studio.

## FORGE season use

| Period | Intent |
| ------ | ------ |
| Preseason | Driveable chassis; simple path on the practice surface |
| Kickoff–clinic | Conventional auto matched to minimum viable BIOBUZZ robot |
| Always | Auto works with HELM off, ECHO off, ViDAR unused |

## Prerequisites

Built drivetrain, battery discipline, Driver Station basics. Dead wheels / Pinpoint / OTOS / drive encoders as chosen by the team — FORGE does not pick the sensor.

## Hardware / simulation

[Visualizer](https://github.com/Pedro-Pathing/Visualizer) is a separate Pedro project. Shop tuning often uses Panels on robot Wi-Fi ([dashboard docs](https://pedropathing.com/docs/pathing/dashboard)). If the robot is unavailable, students sketch the path on paper and walk it, then encode it when hardware returns. Full follower tuning can take days; FORGE sessions must not consume Meeting B driving to finish every tuner.

## Evidence

Repeated path completion times; TRACE events at auto start/end; notes on localization jumps.

## Safety

Standard motion hazards. Blocks or carpet as the session specifies. Disable path is the DS stop.

## Integration

[ViDAR Pedro integration](https://github.com/The-Allsparks/ViDAR/blob/main/docs/PEDRO_INTEGRATION.md) is optional later. Do not block the first auto on vision.

Audit: [docs/research-audit.md](../docs/research-audit.md)

## Combined stack

Pedro (or the chosen drive layer) owns chassis motion and must keep working with every Allsparks optional independently disabled. Combined FTC readiness of the Allsparks libraries is [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4). See [stack-acceptance.md](../docs/stack-acceptance.md).
