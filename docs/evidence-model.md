# Evidence model

FORGE uses evidence so students can explain the robot and so mentors can refuse premature enablement.

## What counts as evidence

| Kind | Typical source | Good for |
| ---- | -------------- | -------- |
| Ordered events | TRACE `Trace.event` / export | Match story |
| Time series | TRACE records, AMPER CSV | Sag, loop time, pose |
| Snapshot | MIMIC mechanism snapshot, ViDAR telemetry screenshot | State at one moment |
| Health report | BEACON registry / preflight | Fresh vs stale |
| Decision record | HELM observe/validate output, ECHO cue decision | Why something happened or stayed silent |
| Physical | Photo of wiring, inspection checklist, notebook sketch | Construction and inspection |
| Human | Driver comment captured after a drill (not a vibe-based enablement) | Workload, cue clarity |

TRACE is the default recorder. It must not become a second control system. See [TRACE data model](https://github.com/The-Allsparks/TRACE/blob/main/docs/data-model.md) and [TRACE architecture](https://github.com/The-Allsparks/TRACE/blob/main/docs/architecture.md).

## Session closeout (about 5–10 minutes)

1. Export or photograph the log (no PII, no secrets).
2. One student retells what happened in order.
3. Fill the [evidence record](../templates/evidence-record.md) — at minimum: Date, Question, Observation, Decision, Next test. Check any award tags (A/B/C/D) that apply.
4. Update one row on the [readiness dashboard](../season/2026-2027-biobuzz/readiness-dashboard.md).
5. File or photograph the notebook artifact.
6. Name the rollback if anything new was enabled.

If the robot still needs a wrench, fill the four-line minimum and take a photo. Do not skip the record entirely — a short note is better than nothing for later portfolio assembly.

Do not create a parallel logging standard.

## Privacy

Follow [TRACE SECURITY.md](https://github.com/The-Allsparks/TRACE/blob/main/SECURITY.md):

- Do not store raw camera video in this repository
- Do not record student names, emails, Wi-Fi passwords, tokens, or secrets
- Sanitize file names

## What evidence is not

- A green CI build on a library
- A completed FORGE session checkbox without a robot or simulation result
- A single anecdote ("it felt faster") as ECHO or HELM approval — see [ECHO student path, experiment design](https://github.com/The-Allsparks/ECHO/blob/main/docs/student-learning-path.md)

## Cross-project correlation

Later in the season, students should be able to lay AMPER sag, MIMIC state, ViDAR staleness, and BEACON freshness on the same TRACE timeline. That adapter work is a **TRACE Phase 4 approval gate** in the TRACE repo. FORGE may *ask* for correlated stories using whatever exports exist; it must not claim unified adapters until TRACE says they exist.

Gap recorded in [research-audit.md](research-audit.md).

## Where information lives

Do not copy the same paragraph into several systems. Promote by reference (session date + photo filename + TRACE export id), then rewrite once into the portfolio.

| Store | What goes here | System of record? |
| ----- | -------------- | ----------------- |
| Evidence record / paper notebook | Session notes, sketches, decisions, award tags | **Yes** for daily engineering story |
| GitHub issues | Curriculum / process bugs, feature requests | Yes for FORGE process |
| TRACE exports | `.tlog`, CSV, AdvantageScope-compatible files | Team storage (not git); redacted snippets in notebook |
| Photos and videos | Robot changes, mechanism tests, pit observations | Team storage; stills printed into portfolio as needed |
| CAD history | Design iterations | CAD tool or robot repo, not FORGE |
| Test records | Decision records, math evidence, failure records | Notebook + templates in this repo |
| Portfolio candidates | Promoted shortlist of strongest evidence | Team storage or notebook index; [portfolio-candidate.md](../templates/portfolio-candidate.md) |
| Final portfolio | Printed or digital 15-page submission | Team storage; validated against [A201 checklist](award-and-portfolio-traceability.md) and [portfolio-validation.md](../templates/portfolio-validation.md) |

## TRACE → portfolio

When a measurement materially improves a decision, follow [trace-portfolio-workflow.md](trace-portfolio-workflow.md). Not every session needs a graph.

## Retention

Keep match and clinic logs on team storage, not in git. Commit only redacted snippets needed to teach.
