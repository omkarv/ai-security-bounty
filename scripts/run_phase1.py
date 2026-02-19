#!/usr/bin/env python3
from __future__ import annotations

from src.cve_fetcher import fetch_cves
from src.risk_model import score_cve, describe_score
from src.report_writer import render_markdown


def main():
    cves = fetch_cves(3)
    scores = [score_cve(c) for c in cves]
    md = render_markdown(cves, scores)
    print(md)

if __name__ == "__main__":
    main()
