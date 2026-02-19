# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

A research framework for discovering, scoring, and responsibly disclosing security vulnerabilities in AI/ML systems. Outputs Markdown/CSV reports suitable for bug bounty submissions. This is methodology and tooling only — no exploit code, no active scanning without authorisation.

## Development Environment

```bash
# First-time setup
python3 -m venv venv
source venv/bin/activate
pip install pytest

# Always run with PYTHONPATH set (src is not an installed package)
PYTHONPATH=/Users/omkarv/Projects/ai-security-bounty python3 -m pytest tests/ -v

# Run the Phase 1 MVP report
PYTHONPATH=/Users/omkarv/Projects/ai-security-bounty python3 scripts/run_phase1.py

# Run a single test
PYTHONPATH=. python3 -m pytest tests/test_basic.py::TestAIBountyMVP::test_score -v
```

## Architecture

```
src/            Core pipeline modules
  cve_fetcher.py    Fetches CVEs (currently mock; to be wired to NVD API / OpenClaw)
  risk_model.py     Scores CVEs by severity (Critical=5, High=4, Medium=3, Low=1)
  report_writer.py  Renders scored CVEs as Markdown

scripts/
  run_phase1.py     Entry point: fetch → score → render → print

tests/
  test_basic.py     Unit tests for all three pipeline stages

templates/          Markdown templates for findings and formal disclosure reports
tracker.csv         Single CSV log of all findings and their disclosure status
findings/           (empty) Drop per-finding Markdown write-ups here post-disclosure
references/
  programs.md       Tiered list of AI/GenAI bug bounty programs with scope and payout info
```

The pipeline is linear: `fetch_cves()` → `score_cve()` → `render_markdown()`. All three functions are thin stubs designed to be swapped out independently.

## OpenClaw Integration (Remote Recon)

OpenClaw is a remote AI agent on an EC2 instance, communicated with via **Browser MCP + Telegram** (`@krabby_om_bot` on Telegram Web).

**Security rules when communicating with OpenClaw:**
- Send only repo contents and task instructions — never local file paths, credentials, SSH keys, or any information about the local machine
- OpenClaw handles CVE fetching from public APIs (NVD etc.) and safe reconnaissance
- Results come back via Telegram and are then integrated into `src/cve_fetcher.py`

Browser MCP is configured for this project in `~/.claude.json` and connects via the Chrome extension on the open Telegram Web session.

## Ethics & Hard Limits (from ETHICS.md)

- Only target programs with an explicit bug bounty or VDP policy (see `references/programs.md`)
- Never commit exploit/PoC code; never commit undisclosed vulnerabilities
- Never test on production systems without explicit authorisation
- Default disclosure timeline: 90 days
- `findings/` and `tracker.csv` are for post-disclosure write-ups only

## Key Vulnerability Classes (AI/ML focus)

Prompt injection · Data leakage (system prompts, training data, PII) · Auth/access control bypass · SSRF via tool use/function calling · Insecure model loading (pickle, safetensors) · Sandbox escape (code interpreter, Spaces) · Rate limiting / resource exhaustion · Supply chain (poisoned weights, malicious plugins)
