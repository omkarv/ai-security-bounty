import unittest
from src.cve_fetcher import fetch_cves
from src.risk_model import score_cve
from src.report_writer import render_markdown

class TestAIBountyMVP(unittest.TestCase):
    def test_fetch(self):
        data = fetch_cves(2)
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)

    def test_score(self):
        cve = {"cve_id": "CVE-TEST-1", "severity": "High"}
        self.assertTrue(score_cve(cve) >= 4)

    def test_report(self):
        cve = {"cve_id": "CVE-TEST-1", "summary": "test", "severity": "High"}
        md = render_markdown([cve], [4])
        self.assertIn("CVE-TEST-1", md)

if __name__ == '__main__':
    unittest.main()
