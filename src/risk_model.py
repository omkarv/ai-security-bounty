#!/usr/bin/env python3
"""risk_model.py
Very small risk scoring stub for CVEs."""
from __future__ import annotations

from typing import Dict


def score_cve(cve: dict) -> int:
    sev = (cve.get("severity") or "Low").lower()
    mapping = {"critical": 5, "high": 4, "medium": 3, "low": 1}
    return mapping.get(sev, 1)


def describe_score(score: int) -> str:
    if score >= 4:
        return "High"
    if score == 3:
        return "Medium"
    return "Low"
