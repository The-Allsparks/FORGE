#!/usr/bin/env python3
"""Batch updates for FORGE issues #23, #28 (partial)."""
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SESSIONS = ROOT / "season/2026-2027-biobuzz/sessions"
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)

AGENDAS = {
    "S005-meeting-a.md": """| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Review G2 comparative evidence; architecture selection starts today; module list from BIOBUZZ MVP |
| 75 | Construction | Physical module-boundary mockups; interface sketches on Sparkee frame; begin CAD for authorized modules |
| 25 | Integration | Architecture diagram draft; software contract (MVP libraries only); assign module owners |
| 10 | Closeout | Shared-parts table started; explain-back; dashboard update; prep S006 G3 gate |""",
    "S006-meeting-b.md": """| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | **Major-design-pivot deadline** — no new architecture after closeout unless G3 gate review |
| 35 | Repair / tune / program | CAD dimensions; BOM finalize; cut list for week 4 fabrication |
| 55 | Driving reps | Short drivetrain reps on Sparkee or Strafer — do not pause G3 paperwork for tuning debates |
| 20 | Closeout | [Gate review G3](../../../templates/gate-review.md); explicit fallback plan; update `calendar.yaml` titles only |""",
    "S007-meeting-a.md": """| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | **G4 design freeze** — no new modules without gate review; incremental software delivery plan |
| 75 | Construction | Fabricate authorized Sparkee modules; spares for fragile parts |
| 25 | Integration | Deliver first completed module to programming pair; [prototype-test-record](../../../templates/prototype-test-record.md) per module |
| 10 | Closeout | Module handoff log; explain-back; dashboard mechanical row |""",
    "S008-meeting-b.md": """| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | **G5 target** — mech/electrical complete; clinic 10 Oct is measurement only |
| 35 | Repair / tune / program | Wiring integration: strain relief, service loops, labels; MIMIC smoke test per module as wired |
| 55 | Driving reps | Full mechanism cycles under teleop; practice-inspect failures fixed |
| 20 | Closeout | Clinic test card signed; G5 gate review or fallback plan; pit rollback drill |""",
    "S009-meeting-a.md": """| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Clinic retrospective rules: evidence not vibes; no architecture rewrite |
| 75 | Construction | P0 clinic repairs only — fasteners, wiring, binds; no new modules |
| 25 | Integration | [Event retrospective](../../../templates/event-retrospective.md); stable teleop verification on Sparkee |
| 10 | Closeout | Handoff checklist for G6; TRACE clinic story; dashboard P0 list |""",
    "S010-meeting-b.md": """| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Minimum reliable auto before advanced paths; Pedro on **Sparkee mass**, not Strafer assumptions |
| 35 | Repair / tune / program | Pedro path or conventional fallback; mechanism tuning; known-good release tag |
| 55 | Driving reps | Auto repetitions (≥7/10 target) interleaved with teleop scoring cycles |
| 20 | Closeout | Auto log; rollback tag recorded; optional libraries still per software contract |""",
    "S011-meeting-a.md": """| Duration (min) | Block | Activity |
| ---: | --- | --- |
| 10 | Opening | Reliability test plan: ≥10 full-cycle attempts; portfolio draft milestone |
| 75 | Construction | P1 repairs only — no new mechanisms; support reliability testing |
| 25 | Integration | Log cycle success rate; TRACE + human-readable log; portfolio draft section |
| 10 | Closeout | [student-progress-review](../../../templates/student-progress-review.md) if due; dashboard reliability row |""",
}

S015_S031 = {
    "S015": {
        "title": "League 1S/2S retrospective and match evidence",
        "dq": "What did our first league teaches us — and what is Version 2 allowed to explore?",
        "obj": "Students run [event-retrospective.md](../../../templates/event-retrospective.md) for League 1S/2S; map match evidence to dashboard; begin calibration backlog. Version 2 research only on Strafer/fixtures — not Sparkee competition time.",
        "outcome": "- League retrospective complete\n- Match evidence table in notebook\n- P0/P1 repair list with owners\n- Version 2 boundary acknowledged",
    },
    "S016": {
        "title": "Post-league driver and auto reps",
        "dq": "Can drivers execute the scoring cycle we planned — with league pressure still fresh?",
        "obj": "Students run 55-minute driver and minimum-auto repetitions; log failures as actionable issues; no new features.",
        "outcome": "- Driver rep log with post-run feedback\n- Auto success rate recorded\n- No elective robot changes",
    },
    "S017": {
        "title": "Match-evidence mechanism calibration",
        "dq": "Which league failure mode yields the highest-value fix today?",
        "obj": "Students pick one mechanism issue from the retrospective and implement an evidence-backed fix in the 75-minute build block.",
        "outcome": "- One calibration fix shipped and tested\n- Before/after metric recorded\n- Rollback path documented",
    },
    "S018": {
        "title": "Driver and auto reps — league development",
        "dq": "Did yesterday's fix survive repeated cycles?",
        "obj": "Students repeat driver and auto reps; validate S017 fix under load.",
        "outcome": "- Rep count logged\n- Fix validated or rolled back",
    },
    "S019": {
        "title": "Sensor and software calibration from match data",
        "dq": "Does match evidence justify any optional library work this week?",
        "obj": "Students calibrate only sensors/libraries named in the G3 software contract **and** supported by league evidence; otherwise continue mechanism reps.",
        "outcome": "- Calibration record or explicit deferral\n- Dashboard rows updated honestly",
    },
    "S020": {
        "title": "Driver and auto reps — league development",
        "dq": "Are alliance-compatible paths worth the time budget?",
        "obj": "Students run driver/auto reps; add one alternate auto path only if G6 contract and time permit.",
        "outcome": "- Rep log\n- Alternate auto decision recorded",
    },
    "S021": {
        "title": "Version 2 fixture research (Strafer or bench only)",
        "dq": "What should Sparkee 2 test — without stealing reliability time?",
        "obj": "Students prototype next-mechanism ideas on Strafer, fixtures, or spare modules only. Sparkee stays competition configuration.",
        "outcome": "- Version 2 experiment record\n- No Sparkee competition resources diverted",
    },
    "S022": {
        "title": "League-evidence mechanism refinement",
        "dq": "What is the second-highest-value fix before League 3S/4S?",
        "obj": "Students implement one more retrospective-driven mechanism improvement with measured before/after.",
        "outcome": "- Fix shipped and tested\n- Portfolio candidate note if applicable",
    },
    "S023": {
        "title": "League Meets 3S/4S preparation",
        "dq": "Are pit, checklists, and robot ready for the next league window?",
        "obj": "Students rehearse pre/post-match checklists, packing, and assigned pit roles; reliability reps in remaining time.",
        "outcome": "- [competition checklists](../../../templates/competition/) walked once\n- Packing list verified\n- Known-good release tag confirmed",
    },
    "S024": {
        "title": "Adversity drill — depleted battery and sag",
        "dq": "Can we finish a cycle when the battery is tired?",
        "obj": "Students run scripted adversity: low battery or AMPER-observed sag; practice swap and teleop fallback.",
        "outcome": "- Drill script and result logged\n- Battery log practice updated",
    },
    "S025": {
        "title": "Driver and auto reps — adversity window",
        "dq": "Did the battery drill change how we plan match strategy?",
        "obj": "Students run reps applying lessons from S024; no new features.",
        "outcome": "- Rep log with strategy notes",
    },
    "S026": {
        "title": "Adversity drill — missed acquisition",
        "dq": "Can drivers recover when intake fails mid-match?",
        "obj": "Students inject missed acquisition; practice recovery and communication between Driver 1 and Driver 2.",
        "outcome": "- Recovery procedure documented\n- Drill results logged",
    },
    "S027": {
        "title": "Driver and auto reps — adversity window",
        "dq": "Does recovery work under repeated pressure?",
        "obj": "Students repeat reps with acquisition-failure scenarios where safe.",
        "outcome": "- Rep log\n- Recovery success rate",
    },
    "S028": {
        "title": "Adversity drill — obstructed camera and stale sensors",
        "dq": "Can we drive safely when vision or sensors lie?",
        "obj": "Students run manual-override drills; ViDAR observe-only or unplugged per dashboard.",
        "outcome": "- Override procedure verified\n- Dashboard status unchanged unless evidenced",
    },
    "S029": {
        "title": "Adversity drill — mechanism jam and pit repair",
        "dq": "Can we repair the highest-frequency jam under time pressure?",
        "obj": "Students time pit repair for top jam mode; update [common-repairs.md](../../../templates/competition/common-repairs.md).",
        "outcome": "- Timed repair result\n- Spares list updated",
    },
    "S030": {
        "title": "Adversity drill — comms loss and pit procedure",
        "dq": "Can every student run rollback in under one minute?",
        "obj": "Students practice DS stop, teleop-only, and [pit-and-inspection.md](../pit-and-inspection.md) rollback; BEACON vocabulary only — no intervention.",
        "outcome": "- Rollback timed\n- Pit roles confirmed",
    },
    "S031": {
        "title": "League Meets 5S/6S preparation",
        "dq": "Are we ready for January league meets with frozen scope?",
        "obj": "Students rehearse checklists, mock judging refresh, and full-match sim; portfolio revision from league evidence.",
        "outcome": "- Checklists rehearsed\n- Portfolio updated from match evidence\n- Feature freeze still in effect",
    },
}


def replace_agenda(body: str, new_table: str) -> str:
    return re.sub(
        r"(\| Duration \(min\) \| Block \| Activity \|\n\| ---: \| --- \| --- \|\n)(?:\|[^\n]+\n)+",
        new_table + "\n",
        body,
        count=1,
    )


def update_s015_s031() -> None:
    cal_path = ROOT / "season/2026-2027-biobuzz/calendar.yaml"
    cal_text = cal_path.read_text(encoding="utf-8")
    for sid, u in S015_S031.items():
        # Update calendar title in place (preserve YAML comments)
        cal_text = re.sub(
            rf"(  - id: {sid}\n(?:    [^\n]+\n)*?    title: ).+",
            rf"\1{u['title']}",
            cal_text,
            count=1,
        )
        path = SESSIONS / f"{sid}-meeting-{('a' if sid in ('S015','S017','S019','S021','S022','S024','S026','S028','S029','S030') else 'b')}.md"
        # Resolve path from calendar row
        cal = yaml.safe_load(cal_text)
        row = next(r for r in cal["sessions"] if r["id"] == sid)
        path = ROOT / "season/2026-2027-biobuzz" / row["file"]
        text = path.read_text(encoding="utf-8")
        m = FM.match(text)
        fm = yaml.safe_load(m.group(1)) or {}
        fm["title"] = u["title"]
        new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False).strip()
        body = text[m.end() :]
        body = re.sub(r"^# S\d+ —[^\n]+\n", f"# {sid} — {u['title']}\n", body, count=1)
        body = re.sub(r"\| Title \| [^\|]+ \|", f"| Title | {u['title']} |", body, count=1)
        body = re.sub(r"## Driving question\n\n[^\n#]+", f"## Driving question\n\n{u['dq']}", body, count=1)
        body = re.sub(
            r"## Student-facing objective\n\n[^\n#]+",
            f"## Student-facing objective\n\n{u['obj']}",
            body,
            count=1,
        )
        body = re.sub(
            r"## Robot outcome\n\n(?:- [^\n]+\n|[^\n#]+)+",
            "## Robot outcome\n\n" + u["outcome"] + "\n\n",
            body,
            count=1,
        )
        path.write_text("---\n" + new_fm + "\n---\n" + body, encoding="utf-8")
    cal_path.write_text(cal_text, encoding="utf-8")
    print("S015-S031 updated")


def main() -> None:
    for fname, agenda in AGENDAS.items():
        path = SESSIONS / fname
        text = path.read_text(encoding="utf-8")
        m = FM.match(text)
        body = replace_agenda(text[m.end() :], agenda)
        path.write_text(text[: m.end()] + body, encoding="utf-8")
        print("agenda", fname)
    update_s015_s031()


if __name__ == "__main__":
    main()
