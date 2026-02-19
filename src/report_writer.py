#!/usr/bin/env python3
"""report_writer.py
Simple Markdown writer for CVEs and reports."""
from __future__ import annotations

from typing import List, Dict


def render_markdown(cves: List[Dict], scores: List[int]) -> str:
    lines = ["# AI Security Bounty Report", ""]
    for cve, s in zip(cves, scores):
        lines.append(f"## {cve.get('cve_id')} - {cve.get('summary')}")
        lines.append(f"- Severity: {cve.get('severity')} (score {s})")
        lines.append("")
    return "\n".join(lines)
