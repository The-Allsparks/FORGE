#!/usr/bin/env python3
"""One-shot: align S001-S014 session bodies with compressed phase model."""
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
cal = yaml.safe_load((ROOT / "season/2026-2027-biobuzz/calendar.yaml").read_text(encoding="utf-8"))
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)
LINKS = """- [docs/season-process.md](../docs/season-process.md)
- [docs/decision-gates.md](../docs/decision-gates.md)
- [docs/pratt-crosswalk.md](../docs/pratt-crosswalk.md)
- [prototype-test-record.md](../../../templates/prototype-test-record.md)
- [gate-review.md](../../../templates/gate-review.md)"""

UPDATES = {
    "S001": {
        "h1": "S001 — Post-Kickoff week 1 — strategy execution and crude prototypes",
        "title": "Post-Kickoff week 1 — strategy execution and crude prototypes",
        "week": "Compressed week 1 (G1 Strategy)",
        "dq": "Did we turn K001 strategy into physical proof — crude prototype plus clear owners — without starting a side quest?",
        "obj": "Students execute K001 strategy: build crude game-object interaction prototype(s), confirm mechanism owners, begin strategy matrix refinement, and record evidence vs preseason assumptions.",
        "outcome": "- Crude prototype demonstrating at least one game-object interaction\n- Strategy matrix draft updated\n- Owner list on [readiness-dashboard.md](../readiness-dashboard.md)\n- Progress toward G1 exit (complete G1 at S002 if needed)",
    },
    "S002": {
        "h1": "S002 — Post-Kickoff week 1 — ideation scale-up and low-fi prototypes",
        "title": "Post-Kickoff week 1 — ideation scale-up and low-fi prototypes",
        "week": "Compressed week 1 (G1 Strategy)",
        "dq": "Did we generate enough ideas (60–100 scaled) and finish G1 with a documented strategy before custom fabrication scales up?",
        "obj": "Students scale visual ideation, finish low-fidelity prototypes, complete G1 Strategy gate review, and run short driver reps on drivable chassis.",
        "outcome": "- Ideation count recorded (target 60–100 across team)\n- [Gate review G1](../../../templates/gate-review.md) completed\n- Risk register started\n- Starter-bot fallback documented",
    },
    "S003": {
        "h1": "S003 — Post-Kickoff week 2 — comparative mechanism tests",
        "title": "Post-Kickoff week 2 — comparative mechanism tests",
        "week": "Compressed week 2 (G2 Prototype evidence)",
        "dq": "Which mechanism moves game objects reliably — and can we prove it with measurements, not opinions?",
        "obj": "Students run comparative mechanism tests with [prototype-test-record.md](../../../templates/prototype-test-record.md) (≥3 trials each); begin minimum autonomous movement only if G3 software contract will require it.",
        "outcome": "- ≥1 completed prototype test record with ≥3 trials\n- Starter-bot reference test scheduled or complete\n- Drivable chassis maintained\n- Variables held constant documented",
    },
    "S004": {
        "h1": "S004 — Post-Kickoff week 2 — starter vs alternative evidence (G2 gate)",
        "title": "Post-Kickoff week 2 — starter vs alternative evidence (G2 gate)",
        "week": "Compressed week 2 (G2 Prototype evidence)",
        "dq": "Do we have measured evidence to stop unrestricted exploration and commit to a leading direction?",
        "obj": "Students complete starter vs alternative comparison, fill comparative summary, pass or fail G2 with [gate-review.md](../../../templates/gate-review.md), and run driver reps.",
        "outcome": "- G2 gate review recorded\n- Comparative evidence table complete\n- Leading concept(s) and starter-bot fallback explicit\n- Unresolved risk list updated",
    },
    "S005": {
        "h1": "S005 — Post-Kickoff week 3 — architecture selection and interfaces",
        "title": "Post-Kickoff week 3 — architecture selection and interfaces",
        "week": "Compressed week 3 (G3 Architecture selection)",
        "dq": "What modular Sparkee architecture fits our evidence — and what are we explicitly cutting?",
        "obj": "Students select competition-one architecture, define module boundaries and interfaces per [modular-architecture.md](../docs/modular-architecture.md), and draft software contract (MVP libraries only).",
        "outcome": "- Architecture diagram with module interfaces\n- Software contract draft\n- Module owners assigned\n- Shared-parts table started ([two-platform-strategy.md](../docs/two-platform-strategy.md))",
    },
    "S006": {
        "h1": "S006 — Post-Kickoff week 3 — pivot deadline; CAD and BOM authorization",
        "title": "Post-Kickoff week 3 — pivot deadline; CAD and BOM authorization",
        "week": "Compressed week 3 (G3 Architecture selection)",
        "dq": "Are we authorized to fabricate — and have we passed G3 before major pivots end?",
        "obj": "Students complete CAD/fabrication authorization package, BOM, major-design-pivot deadline declaration, and G3 gate review. Reject features that do not fit remaining time.",
        "outcome": "- G3 gate review passed or fallback activated\n- BOM and fabrication package\n- Pivot deadline recorded — no architectural pivots after today without gate review\n- Explicit fallback plan",
    },
    "S007": {
        "h1": "S007 — Post-Kickoff week 4 — module fabrication (incremental delivery)",
        "title": "Post-Kickoff week 4 — module fabrication (incremental delivery)",
        "week": "Compressed week 4 (G4 Design freeze)",
        "dq": "Can we deliver modules incrementally to software instead of waiting for a complete robot?",
        "obj": "Students fabricate authorized Sparkee modules; deliver first modules to programming pair; declare G4 design freeze on module set.",
        "outcome": "- ≥1 module fabricated and demonstrated under power\n- Incremental software handoff documented\n- G4 freeze declaration\n- Spares identified for fragile parts",
    },
    "S008": {
        "h1": "S008 — Post-Kickoff week 4 — integration, wiring, clinic prep",
        "title": "Post-Kickoff week 4 — integration, wiring, clinic prep",
        "week": "Compressed week 4 (G5 Mechanical/electrical completion)",
        "dq": "Is Sparkee mechanically and electrically complete enough for clinic data collection?",
        "obj": "Students complete wiring (strain relief, service loops), integrate modules, test MIMIC states as hardware allows, prep clinic test card, and review G5 gate.",
        "outcome": "- Mechanically and electrically integrated robot\n- Individual mechanisms under software control\n- Clinic test card copied to notebook\n- G5 gate pass or starter-bot fallback plan",
    },
    "S009": {
        "h1": "S009 — Post-Kickoff week 5 — clinic retrospective and software handoff",
        "title": "Post-Kickoff week 5 — clinic retrospective and software handoff",
        "week": "Compressed week 5 (G6 Stable software handoff)",
        "dq": "What did clinic prove — and is Sparkee stable enough for sustained software and driver work?",
        "obj": "Students run [event-retrospective.md](../../../templates/event-retrospective.md) for clinic; begin G6 handoff: minimum teleop stable, Pedro tuning on Sparkee mass (not Strafer assumptions).",
        "outcome": "- Clinic retrospective complete\n- P0 repair list from clinic\n- Stable teleop verified on Sparkee\n- Handoff checklist started",
    },
    "S010": {
        "h1": "S010 — Post-Kickoff week 5 — minimum auto and mechanism tuning",
        "title": "Post-Kickoff week 5 — minimum auto and mechanism tuning",
        "week": "Compressed week 5 (G6 Stable software handoff)",
        "dq": "Can we run one reliable minimum autonomous path before adding anything advanced?",
        "obj": "Students build minimum reliable Pedro (or conventional) auto on Sparkee; tune mechanisms; stop major mechanical changes.",
        "outcome": "- Minimum auto runs ≥7/10 in practice or teleop-only declared\n- Mechanism tuning log\n- Known-good release tag recorded",
    },
    "S011": {
        "h1": "S011 — Post-Kickoff week 5 — reliability testing and portfolio draft",
        "title": "Post-Kickoff week 5 — reliability testing and portfolio draft",
        "week": "Compressed week 5 (G6 Stable software handoff)",
        "dq": "What is our measured reliability — and is the portfolio draft ready for final edit?",
        "obj": "Students run repeated full-cycle tests (≥10 attempts), log via TRACE and human-readable log, draft portfolio narrative from season notes.",
        "outcome": "- Reliability metrics recorded honestly\n- Portfolio draft substantially complete\n- [student-progress-review.md](../../../templates/student-progress-review.md) if due",
    },
    "S012": {
        "h1": "S012 — Post-Kickoff week 5 — driver automation if earned; G6 gate review",
        "title": "Post-Kickoff week 5 — driver automation if earned; G6 gate review",
        "week": "Compressed week 5 (G6 Stable software handoff)",
        "dq": "Did we earn driver automation — and does G6 pass with a stable robot?",
        "obj": "Students add driver assists only if demonstrably reliable; complete G6 gate review; prep league meet checklists.",
        "outcome": "- G6 gate review recorded\n- Driver automation list (or explicit none)\n- [competition checklists](../../../templates/competition/) owners assigned",
    },
    "S013": {
        "h1": "S013 — Post-Kickoff week 6 — feature freeze and mock judging",
        "title": "Post-Kickoff week 6 — feature freeze and mock judging",
        "week": "Compressed week 6 (G7 Reliability / feature freeze)",
        "dq": "Can all four students explain our robot and process — and have we frozen speculative features?",
        "obj": "Students declare G7 feature/code freeze, run mock judging (5 min + Q&A), conduct failure-injection drills, allow only P0/P1 fixes.",
        "outcome": "- G7 freeze declaration\n- Mock judging feedback for all four students\n- Open defect list prioritized",
    },
    "S014": {
        "h1": "S014 — Post-Kickoff week 6 — full-match simulation and pit rehearsal",
        "title": "Post-Kickoff week 6 — full-match simulation and pit rehearsal",
        "week": "Compressed week 6 (G7–G8 prep)",
        "dq": "Can we run a full 2½-minute match and pit cycle under pressure?",
        "obj": "Students run complete match simulations (nonideal conditions where safe), rehearse pit checklists, timed battery change, prep G8 readiness.",
        "outcome": "- Full-match simulation completed\n- Pre/post-match checklists timed\n- Pit packing walkthrough\n- G8 prep or RD001 draft",
    },
}


def main() -> None:
    for row in cal["sessions"]:
        sid = row["id"]
        if sid not in UPDATES:
            continue
        u = UPDATES[sid]
        path = ROOT / "season/2026-2027-biobuzz" / row["file"]
        text = path.read_text(encoding="utf-8")
        m = FM.match(text)
        if not m:
            print("skip no fm", sid)
            continue
        body = text[m.end() :]
        body = re.sub(r"^# S\d+ —[^\n]+\n", u["h1"] + "\n", body, count=1)
        body = re.sub(r"\| Title \| [^\|]+ \|", f"| Title | {u['title']} |", body, count=1)
        body = re.sub(r"\| Relative week \| [^\|]+ \|", f"| Relative week | {u['week']} |", body, count=1)
        gate = row.get("forge_gate", "—")
        if "| Forge gate |" not in body:
            body = body.replace("| Difficulty |", f"| Forge gate | {gate} |\n| Difficulty |", 1)
        body = re.sub(r"## Driving question\n\n[^\n#]+", f"## Driving question\n\n{u['dq']}", body, count=1)
        body = re.sub(
            r"## Student-facing objective\n\n[^\n#]+",
            f"## Student-facing objective\n\n{u['obj']}",
            body,
            count=1,
        )
        body = re.sub(
            r"## Robot outcome\n\n(?:- [^\n]+\n)+",
            "## Robot outcome\n\n" + u["outcome"] + "\n\n",
            body,
            count=1,
        )
        if "season-process.md" not in body:
            body = body.replace(
                "## Links to authoritative project documentation\n\n",
                "## Links to authoritative project documentation\n\n" + LINKS + "\n",
            )
        path.write_text(text[: m.end()] + body, encoding="utf-8")
        print("updated", sid)


if __name__ == "__main__":
    main()
