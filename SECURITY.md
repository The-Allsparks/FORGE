# Security Policy

## Supported versions

| Version | Supported |
| ------- | --------- |
| main / 0.1.x curriculum | Yes |

FORGE is a curriculum and season-orchestration repository. It does not ship robot runtime code. Security still matters because session plans, evidence records, and linked logs can expose students, credentials, or unsafe enablement advice.

## Reporting a vulnerability

Please do **not** open a public issue for security problems that could put robots, students, or machines at risk.

Prefer:

1. GitHub Security Advisories for this repository (when available), or
2. A private email contact published by the maintainers

Include:

- A description of the issue
- Steps to reproduce
- Impact assessment (for example: enablement guidance that would command hardware unsafely, credentials in evidence files, student names in published logs)

## Safety expectations for this project

FORGE intentionally:

- Is **not** a robot library and must not become a dependency of robot code
- Treats each Allsparks project repository as authoritative for APIs, architecture, and project-specific enablement
- Requires evidence before any optional system becomes competition-active
- Distinguishes **disabled**, **passive**, **practice-only**, **approved**, and **frozen**
- Avoids storing student-identifying information, Wi-Fi passwords, tokens, or secrets in the repository, issues, or sample logs

If you discover a session plan that tells students to enable unvalidated motor intervention, skip a project safety gate, or commit credentials, treat it as a safety defect.

## Secrets

Never store passwords, Wi-Fi credentials, API keys, tokens, or student PII in the repository, issues, pull requests, or exported evidence. Sanitize file names and paths. Redact Driver Station screenshots before they are committed.
