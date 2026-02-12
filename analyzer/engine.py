#!/usr/bin/env python3
"""
CYFSA Document Analyzer Engine (Educational) v2.1
Ontario jurisdiction only. This tool emits EDUCATIONAL FLAGS — not legal advice.

Notes:
- This is a small, transparent rules + pattern demo.
- It does NOT decide legal validity, consent, authenticity, or outcomes.
- Quotes are truncated to <= 25 words.
"""

import re
import json
import hashlib
import datetime
from dataclasses import dataclass, asdict
from typing import Dict, List, Any, Optional


@dataclass
class Flag:
    severity: str
    category: str
    quote: str
    explanation: str
    source_citation: str
    suggestion: str
    rule_id: str


class CYFSADocumentAnalyzer:
    def __init__(self, rules_path: str = "analyzer/rules.json"):
        with open(rules_path, "r", encoding="utf-8") as f:
            self.rules = json.load(f)

    @staticmethod
    def _sanitize(text: str) -> str:
        text = re.sub(r"\s+", " ", text).strip()
        return text

    @staticmethod
    def _truncate_words(s: str, max_words: int = 25) -> str:
        words = s.split()
        if len(words) <= max_words:
            return s
        return " ".join(words[:max_words]) + " …"

    def _context_quote(self, text: str, start: int, end: int) -> str:
        lo = max(0, start - 40)
        hi = min(len(text), end + 80)
        return self._truncate_words(text[lo:hi], 25)

    def analyze(self, document_text: str) -> Dict[str, Any]:
        raw = self._sanitize(document_text)
        txt = raw.lower()

        flags: List[Flag] = []

        # Out-of-jurisdiction guardrail
        for pat in self.rules.get("patterns", {}).get("out_of_jurisdiction", []):
            if re.search(pat, txt, re.IGNORECASE):
                flags.append(Flag(
                    severity="RED",
                    category="Jurisdiction",
                    quote=self._truncate_words(raw, 25),
                    explanation="Non-Ontario jurisdiction content detected. This analyzer is Ontario-only.",
                    source_citation="Jurisdiction guardrail (project policy)",
                    suggestion="Remove non-Ontario material or analyze separately with correct jurisdiction.",
                    rule_id="out_of_jurisdiction"
                ))
                break

        # Hearsay patterns (educational)
        for pat in self.rules.get("patterns", {}).get("hearsay", []):
            for m in re.finditer(pat, raw, re.IGNORECASE):
                flags.append(Flag(
                    severity="ORANGE",
                    category="Evidence quality",
                    quote=self._context_quote(raw, m.start(), m.end()),
                    explanation="Potential hearsay phrasing. Educational note: uncorroborated hearsay often has lower weight.",
                    source_citation=self.rules["citations"]["hearsay_general"]["source"],
                    suggestion="Identify the original source and look for a direct record or sworn statement.",
                    rule_id="evidence_hearsay"
                ))

        counts = {"RED": 0, "ORANGE": 0, "YELLOW": 0}
        for f in flags:
            counts[f.severity] += 1

        status = "Procedurally unclear (educational flags present)"
        if counts["RED"] == 0 and counts["ORANGE"] == 0:
            status = "No pattern-based flags detected (NOT a legal conclusion)"

        audit = {
            "timestamp_utc": datetime.datetime.utcnow().isoformat() + "Z",
            "ruleset_version": self.rules["analyzer_metadata"]["version"],
            "jurisdiction": self.rules["analyzer_metadata"]["jurisdiction"],
            "document_hash16": hashlib.sha256(raw[:2000].encode("utf-8", errors="ignore")).hexdigest()[:16],
        }

        return {
            "document_type": "unknown",
            "total_flags": counts,
            "procedural_status": status,
            "flags": [asdict(f) for f in flags],
            "audit_trail": audit,
            "disclaimer": self.rules["compliance_safeguards"]["disclaimer_required"],
        }


def main():
    sample = "Neighbour reported child was unsupervised. Parent allegedly has substance abuse issues."
    analyzer = CYFSADocumentAnalyzer()
    print(json.dumps(analyzer.analyze(sample), indent=2))


if __name__ == "__main__":
    main()
