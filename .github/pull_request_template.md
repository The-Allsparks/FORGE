## Summary

Briefly describe what this PR changes and why.

## Curriculum impact

- [ ] Documentation / architecture only
- [ ] Session added or rewritten
- [ ] Calendar / event dates
- [ ] Enablement or safety policy
- [ ] Validation tooling

## Safety

- [ ] Does **not** add robot runtime code or make robot projects depend on FORGE
- [ ] Does **not** enable unvalidated active features by default
- [ ] Distinguishes disabled / passive / practice-only / approved / frozen
- [ ] No secrets or student PII

## Validation

- [ ] `python tools/validation/validate_curriculum.py` passed locally

## Checklist

- [ ] Deep links point at authoritative project files (no invented APIs)
- [ ] Session agendas still total 120 minutes
- [ ] Hardware and simulation fallbacks remain
- [ ] `calendar.yaml` updated if dates changed
- [ ] Linked related issues / milestones
