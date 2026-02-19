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

KEYWORDS = [
    "large language model",
    "prompt injection",
    "machine learning model",
    "ChatGPT",
    "OpenAI",
    "TensorFlow",
    "PyTorch",
    "Hugging Face",
    "artificial intelligence model",
    "generative AI",
]


def _build_url(keyword: str, limit: int = 20) -> str:
    """Build the NVD 2.0 query URL for a single keyword."""
    params = {
        "keywordSearch": keyword,
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

    # Derive severity from CVSS score if not provided (common for older CVEs)
    if severity is None and cvss_score is not None:
        if cvss_score >= 9.0:
            severity = "CRITICAL"
        elif cvss_score >= 7.0:
            severity = "HIGH"
        elif cvss_score >= 4.0:
            severity = "MEDIUM"
        else:
            severity = "LOW"

    return {
        "cve_id": cve_id,
        "summary": summary,
        "severity": severity,
        "cvss_score": cvss_score,
        "published_date": published_date,
    }


def fetch_cves(limit: int = 20) -> List[Dict]:
    """Fetch CVEs from NVD 2.0, querying each keyword separately and deduplicating.

    NVD treats multiple words in keywordSearch as AND, so we search each
    keyword individually and merge results by cve_id.

    Returns a list of dicts with keys:
        cve_id, summary, severity, cvss_score, published_date
    """
    seen: dict[str, Dict] = {}
    per_keyword = max(limit, 20)

    for keyword in KEYWORDS:
        url = _build_url(keyword, per_keyword)
        req = request.Request(url, headers={"Accept": "application/json"})
        try:
            with request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except Exception:
            continue

        for item in data.get("vulnerabilities", []):
            parsed = _parse_vulnerability(item)
            cve_id = parsed.get("cve_id")
            if cve_id and cve_id not in seen:
                seen[cve_id] = parsed

    return list(seen.values())[:limit]
