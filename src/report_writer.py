#!/usr/bin/env python3
"""report_writer.py
Simple Markdown writer for CVEs and reports."""
from __future__ import annotations

from typing import List, Dict


def render_markdown(cves: List[Dict], scores: List[int]) -> str:
    lines = ["# AI Security Bounty Report", ""]
    for cve, s in zip(cves, scores):
        lines.append(f"## {cve.get('cve_id', 'N/A')}")
        lines.append(f"- **Summary:** {cve.get('summary', 'N/A')}")
        lines.append(f"- **Severity:** {cve.get('severity', 'N/A')} (risk score {s})")
        lines.append(f"- **CVSS Score:** {cve.get('cvss_score', 'N/A')}")
        lines.append(f"- **Published:** {cve.get('published_date', 'N/A')}")
        lines.append("")
    return "\n".join(lines)
