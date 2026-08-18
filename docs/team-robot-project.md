# Team robot project

FORGE does not contain robot code. Students and mentors still need a real FTC SDK / TeamCode project for S002 onward.

## Status (18 August 2026)

Re-checked [The-Allsparks](https://github.com/The-Allsparks) public and listed-private repositories. There is **no** published TeamCode / `FtcRobotController` robot project.

| Candidate | Finding |
| --------- | ------- |
| Org GitHub repos | Libraries, `FORGE`, `ftc-dev-tools`, `ftc-team-analysis`, `SponsorshipPlan` only |
| Local folder `FTC-test` | Contains an `FtcRobotController` tree; **no git remote**; not treated as the production robot repo |

Do not invent a GitHub URL. Do not copy TeamCode into FORGE.

## What mentors should do

1. Create or choose the team's Android Studio robot project (Pedro requires Android Studio, not OnBot Java or Blocks — [Pedro introduction](https://pedropathing.com/docs/pathing)).
2. Put it on GitHub under The-Allsparks if the team wants it versioned, public or private.
3. Replace the placeholder below with the real clone URL and TeamCode path.
4. Keep FORGE out of that project's Gradle dependencies.

## Placeholder (fill when the repo exists)

```text
Robot project URL:    (not published)
Clone:                (not published)
TeamCode path:        TeamCode/src/main/java/org/firstinspires/ftc/teamcode/
Android Studio:       required for Pedro Pathing
```

Install libraries into **that** project using each library's own install docs (AMPER, TRACE, ViDAR, and so on). FORGE only links those docs. Combined order, lifecycle, and disable paths: [stack-acceptance.md](stack-acceptance.md), [student-install.md](student-install.md). AMPER’s multi-module packaging is the starting Gradle reference, not something to copy into FORGE.

Until this URL exists, [FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4) cannot check compile-checked TeleOp/auto or Control Hub budgets. Keep this issue and [#2](https://github.com/The-Allsparks/FORGE/issues/2) open.

## Related

- Tracking issue: [The-Allsparks/FORGE#2](https://github.com/The-Allsparks/FORGE/issues/2)
- Combined stack epic: [The-Allsparks/FORGE#4](https://github.com/The-Allsparks/FORGE/issues/4)
- Pedro Quickstart (if starting from Pedro's template): [Pedro-Pathing/Quickstart](https://github.com/Pedro-Pathing/Quickstart)
- Official SDK: [FIRST-Tech-Challenge/FtcRobotController](https://github.com/FIRST-Tech-Challenge/FtcRobotController)
