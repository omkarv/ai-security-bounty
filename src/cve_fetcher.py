#!/usr/bin/env python3
"""cve_fetcher.py – fetch CVEs from the NVD 2.0 REST API.

Filters by AI/ML/LLM-related keywords.  Returns a list of dicts, each with:
  cve_id, summary, severity, cvss_score, published_date

Reference: https://services.nvd.nist.gov/rest/json/cves/2.0
"""
from __future__ import annotations

import json
from typing import List, Dict, Optional
from urllib import request, parse

NVD_API = "https://services.nvd.nist.gov/rest/json/cves/2.0"

KEYWORDS = ["AI", "LLM", "machine learning", "prompt injection"]


def _build_url(limit: int = 20) -> str:
    """Build the NVD 2.0 query URL with keyword filter."""
    keyword_query = " ".join(KEYWORDS)
    params = {
        "keywordSearch": keyword_query,
        "resultsPerPage": str(limit),
    }
    return f"{NVD_API}?{parse.urlencode(params)}"


def _extract_cvss(metrics: dict) -> tuple[Optional[float], Optional[str]]:
    """Extract the best available CVSS score and severity from NVD 2.0 metrics."""
    # Prefer v3.1, then v3.0, then v2
    for key in ("cvssMetricV31", "cvssMetricV30"):
        entries = metrics.get(key, [])
        if entries:
            cvss_data = entries[0].get("cvssData", {})
            return cvss_data.get("baseScore"), cvss_data.get("baseSeverity")

    entries = metrics.get("cvssMetricV2", [])
    if entries:
        cvss_data = entries[0].get("cvssData", {})
        return cvss_data.get("baseScore"), cvss_data.get("baseSeverity")

    return None, None


def _parse_vulnerability(item: dict) -> Dict:
    """Parse a single NVD 2.0 vulnerability object into our standard dict."""
    cve = item.get("cve", {})
    cve_id = cve.get("id")

    descriptions = cve.get("descriptions", [])
    # Prefer English description
    summary = ""
    for d in descriptions:
        if d.get("lang") == "en":
            summary = d.get("value", "")
            break
    if not summary and descriptions:
        summary = descriptions[0].get("value", "")

    metrics = cve.get("metrics", {})
    cvss_score, severity = _extract_cvss(metrics)

    published_date = cve.get("published")

    return {
        "cve_id": cve_id,
        "summary": summary,
        "severity": severity,
        "cvss_score": cvss_score,
        "published_date": published_date,
    }


def fetch_cves(limit: int = 20) -> List[Dict]:
    """Fetch CVEs from NVD 2.0 with keyword filtering.

    Returns a list of dicts with keys:
        cve_id, summary, severity, cvss_score, published_date
    """
    url = _build_url(limit)
    req = request.Request(url, headers={"Accept": "application/json"})
    with request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    vulnerabilities = data.get("vulnerabilities", [])
    return [_parse_vulnerability(v) for v in vulnerabilities[:limit]]
