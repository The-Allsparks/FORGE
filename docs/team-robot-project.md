# Team robot project

FORGE does not contain robot code. Students and mentors use the published FTC SDK / TeamCode project for P006 onward.

## Status: published (5 September 2026)

Robot repository: [The-Allsparks/FtcRobotController](https://github.com/The-Allsparks/FtcRobotController). Fork of [FIRST-Tech-Challenge/FtcRobotController](https://github.com/FIRST-Tech-Challenge/FtcRobotController) at tag [v11.2.1](https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases/tag/v11.2.1). Default branch: `bumblebee`. Tracking: [FORGE#2](https://github.com/The-Allsparks/FORGE/issues/2).

| Candidate | Finding |
| --------- | ------- |
| Org GitHub | [The-Allsparks/FtcRobotController](https://github.com/The-Allsparks/FtcRobotController) — BumbleBee TeamCode |
| Local folder `FtcRobotController` | Sibling of SHIFT / AMPER; clone of the org fork |
| Local folder `FTC-test` | Earlier SDK 11.2.0 working tree; not the published robot repo |

Do not copy TeamCode into FORGE. Do not add FORGE as a Gradle dependency of the robot project.

## Clone

```text
Robot project URL:    https://github.com/The-Allsparks/FtcRobotController
Clone:                git clone https://github.com/The-Allsparks/FtcRobotController.git
TeamCode path:        TeamCode/src/main/java/org/firstinspires/ftc/teamcode/
Android Studio:       Narwhal 3 Feature Drop or later (v11.2.1 requirement)
Default branch:       bumblebee
```

Sibling `includeBuild` (while SHIFT/AMPER/TRACE are unpublished SNAPSHOT/rc):

```gradle
includeBuild('../SHIFT')
includeBuild('../AMPER')
includeBuild('../TRACE')
```

Install libraries into **that** project using each library's own install docs. Combined order, lifecycle, and disable paths: [stack-acceptance.md](stack-acceptance.md), [student-install.md](student-install.md). AMPER’s multi-module packaging is the starting Gradle reference, not something to copy into FORGE.

[FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4) can start compile-checked TeleOp/auto against this repo. Control Hub budgets are still unmeasured.

## Related

- Tracking issue: [The-Allsparks/FORGE#2](https://github.com/The-Allsparks/FORGE/issues/2)
- Create playbook: [create-robot-project.md](create-robot-project.md)
- Combined stack epic: [The-Allsparks/FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4)
- Official SDK tag: [v11.2.1](https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases/tag/v11.2.1)
- Pedro Quickstart (later): [Pedro-Pathing/Quickstart](https://github.com/Pedro-Pathing/Quickstart)
