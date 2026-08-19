# Create the team robot repository (when ready)

This is a **mentor playbook**. It does **not** create a GitHub repository and does **not** invent a clone URL. Until the URL exists, [FORGE#2](https://github.com/The-Allsparks/FORGE/issues/2) stays **blocked**.

FORGE must never become a Gradle dependency of that project. Combined Hub compile-check lives in that repo (or a named acceptance project), not here ([FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4)).

## Decision (team, not FORGE)

1. Public or private under [The-Allsparks](https://github.com/The-Allsparks).
2. Start from [Pedro-Pathing/Quickstart](https://github.com/Pedro-Pathing/Quickstart) **or** [FIRST-Tech-Challenge/FtcRobotController](https://github.com/FIRST-Tech-Challenge/FtcRobotController) plus Pedro later. Pedro requires **Android Studio**, not OnBot Java or Blocks ([Pedro introduction](https://pedropathing.com/docs/pathing)).
3. Pick a repository name when you create it. Do not write a guessed URL into FORGE first.

Local `FTC-test` is **not** the production robot repo until it has a remote and is recorded below.

## After the repo exists

1. Add a git remote and push.
2. Fill the placeholder in [team-robot-project.md](team-robot-project.md) (URL, clone command, TeamCode path).
3. Confirm `settings.gradle` / `build.gradle` do **not** include FORGE.
4. Use the FTC SDK Gradle wrapper. Do not upgrade Gradle because a library asked you to ([AMPER install](https://github.com/The-Allsparks/AMPER/blob/main/docs/install.md)).
5. Add libraries **one at a time**, default off: [student-install.md](student-install.md).
6. Comment the real URL on [FORGE#2](https://github.com/The-Allsparks/FORGE/issues/2) and close it when the FORGE links are updated.
7. Then #4 can start compile-checked TeleOp/auto and Hub budgets. Those remain blocked until this playbook is finished.

## First OpModes to keep forever

| OpMode | Purpose |
| ------ | ------- |
| Team teleop | Sticks drive the chassis with every optional independently disabled |
| Conventional auto | Pedro or the S007 timed fallback; HELM off |

Do not wait for TRACE/AMPER/ViDAR before those two exist.

## What not to do

- Copy TeamCode into FORGE
- Make the robot project depend on FORGE
- Enable HELM execute, ECHO match audio, AMPER limiting, or ViDAR driving because the repo is new
- Treat sibling library CI as Control Hub evidence
