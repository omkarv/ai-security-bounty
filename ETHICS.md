# Ethics & Safety Guidelines

## Non-negotiables
- **Never publish undisclosed vulnerabilities.** All findings must go through responsible disclosure before any public write-up.
- **Never commit exploit code.** This repo contains methodology, tooling, and write-ups of already-disclosed issues only.
- **Never test on production systems without explicit authorisation.** Use sandboxes, local environments, or explicitly in-scope test targets.
- **Respect disclosure timelines.** Follow the program's stated timeline (typically 90 days). If none stated, default to 90 days.
- **No weaponisation.** Tools here are for discovery and documentation, not attack.

## What belongs in this repo
- Methodology and playbooks
- Reusable tooling (scanners, fetchers, scoring scripts)
- Write-ups of publicly disclosed findings (post-disclosure only)
- Templates for reports, intake, and triage

## What does NOT belong in this repo
- Active/undisclosed vulnerabilities
- Exploit code (PoC or otherwise)
- Credentials, tokens, API keys
- Personally identifiable information
- Screenshots of non-public systems

## Legal
- Only target programs with explicit bug bounty or VDP (vulnerability disclosure program) policies
- Familiarise yourself with each program's rules before testing
- When in doubt, don't test — ask the program first
