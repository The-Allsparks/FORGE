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

## Session closeout (10–20 minutes)

1. Export or photograph the log (no PII, no secrets).
2. One student retells what happened in order.
3. Update one row on the [readiness dashboard](../season/2026-2027-biobuzz/readiness-dashboard.md).
4. File or photograph the notebook artifact.
5. Name the rollback if anything new was enabled.

Use [templates/evidence-record.md](../templates/evidence-record.md). Do not create a parallel logging standard.

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

## Retention

Keep match and clinic logs on team storage, not in git. Commit only redacted snippets needed to teach.
