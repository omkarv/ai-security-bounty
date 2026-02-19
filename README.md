# ai-security-bounty

A reusable, ethical framework for discovering and responsibly disclosing security vulnerabilities in AI/ML systems. Outputs Markdown reports and CSV tracking logs suitable for bug bounty submissions.

## What this does

- Fetches CVEs from public feeds (NVD 2.0, MITRE) filtered for AI/ML targets
- Scores findings by severity and exploitability
- Generates structured Markdown disclosure reports
- Tracks submissions across bounty programs in `tracker.csv`

## Quickstart

```bash
python3 -m venv venv && source venv/bin/activate
pip install pytest
PYTHONPATH=. python3 scripts/run_phase1.py   # fetch → score → report
PYTHONPATH=. python3 -m pytest tests/ -v     # run tests
```

## Repo structure

```
src/                  Core pipeline
  cve_fetcher.py        Fetches CVEs from NVD 2.0 API
  risk_model.py         Scores CVEs by severity/exploitability
  report_writer.py      Renders Markdown reports

scripts/
  run_phase1.py         End-to-end runner

tests/
  test_basic.py         Unit tests for all pipeline stages

templates/
  finding-template.md       Per-finding write-up template
  disclosure-report.md      Formal vendor disclosure template

tracker.csv           Log of all findings and disclosure status
references/programs.md  Tiered list of AI bug bounty programs
```

## Target programs

See [`references/programs.md`](references/programs.md) for a tiered list of AI/GenAI bug bounty programs including Google VRP, OpenAI, Microsoft MSRC, Meta, Anthropic, HuggingFace and others.

## Contributing

- All changes go through a PR — `main` is protected
- Feature branches: `feat/<short-description>`
- Run tests before opening a PR: `PYTHONPATH=. python3 -m pytest tests/ -v`

## Ethics

See [`ETHICS.md`](ETHICS.md). No exploit code, no undisclosed vulnerabilities, no credentials — ever.
