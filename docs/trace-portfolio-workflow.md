# TRACE → portfolio workflow

How exported TRACE data becomes **judge-readable evidence** on a PORTFOLIO page. Judges will not open links, repositories, or external files (A201). The graph or table must stand alone on the printed page.

Use TRACE when measurement **materially improves a decision** — not every session needs a graph.

## When to make a graph

| Make a graph when… | Skip the graph when… |
| ------------------ | -------------------- |
| A number changed a design choice | The session was only construction with no new test |
| You need to show repeatability (N runs) | A photo and one sentence are enough |
| AMPER sag or loop time explains a failure | You have no export yet (use paper timeline instead) |
| Control or auto behavior is the evidence | The robot still needs a wrench — fill the four-line evidence record first |

## Workflow

1. **Select a meaningful test question.** One sentence: "We wanted to know if ___."
2. **Choose the minimum useful signals.** Do not dump every topic onto one figure. Example: one motor current trace + one event marker, not twelve channels.
3. **Record test conditions.** Battery label, mechanism load, field surface, OpMode name, number of runs.
4. **Export the relevant data.** Redacted `.tlog`, CSV, or AdvantageScope-compatible file → team storage, not git. See [TRACE student path](https://github.com/The-Allsparks/TRACE/blob/main/docs/student-learning-path.md).
5. **Produce a readable graph or table.** Screenshot or exported image with labeled axes and units. Prefer 10 pt+ fonts on annotations.
6. **Annotate what happened.** Arrows or captions on the figure: "Here the belt slipped," "Voltage dropped here."
7. **Record the student's conclusion.** One or two sentences in the student's words: "This means we should ___."
8. **Place the result in the portfolio candidate.** Print the figure + caption directly on the page. No QR codes, no "see GitHub."

## Caption template

Copy into the notebook and portfolio:

```text
Question: We asked whether ___.
Conditions: ___ battery, ___ load, ___ runs on ___.
What happened: The ___ line went ___ at ___.
Conclusion: We decided ___ because ___.
```

## Stack roles (keep captions honest)

| Project | Role in this workflow |
| ------- | ----------------------- |
| TRACE | Exports structured telemetry and logs — **recorder**, not commander |
| AMPER | Electrical signals (voltage, current) may appear in the same timeline |
| MIMIC | Mechanism state or fault events may appear as markers |
| Pedro Pathing | Chassis motion / pose if the question is autonomous driving |
| ViDAR / BEACON / ECHO / HELM | Include only if that system was under test |

ECHO is audio driver assistance, not telemetry. TRACE is not the control system.

## Fallback while robot repo is blocked ([#2](https://github.com/The-Allsparks/FORGE/issues/2))

Until Hub exports exist:

- Paper event timeline with timestamps
- Driver Station telemetry screenshot (redacted)
- Ruler/tape-measure photo with labeled values
- Notebook table of N run results

These are valid portfolio evidence if the caption is complete.

## File size reminder

Digital portfolio submissions must be under 15 MB total (A201). Crop figures; avoid full-screen 4K screenshots.

## Related templates

- [Evidence record](../templates/evidence-record.md) — daily session notes
- [Math evidence](../templates/math-evidence.md) — when a calculation supports the figure
- [Portfolio candidate](../templates/portfolio-candidate.md) — promote the best figures every 2–3 weeks
- [Portfolio validation](../templates/portfolio-validation.md) — final A201 checklist
