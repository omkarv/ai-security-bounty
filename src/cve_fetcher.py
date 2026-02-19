#!/usr/bin/env python3
"""cve_fetcher.py
Minimal, non-destructive CVE fetcher scaffold.
This is intentionally a stub to be filled with real feed integrations later."""
from __future__ import annotations

from typing import List


def fetch_cves(limit: int = 5) -> List[dict]:
    # Placeholder: return mock CVE-like dicts
    return [
        {"cve_id": "CVE-2024-0001", "summary": "Mock CVE for demo", "severity": "Medium"},
        {"cve_id": "CVE-2024-0002", "summary": "Another demo CVE", "severity": "Low"},
    ][:limit]
