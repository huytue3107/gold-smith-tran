#!/usr/bin/env python3
"""
Validate Gold Smith content files for obvious finance-safety risks.

This is a lightweight guardrail, not a legal/compliance review.
Run before publishing or after generating a batch of posts.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PATHS = [ROOT / "posts"]


RISK_PATTERNS = {
    "profit_promise": [
        r"\bbao loi\b",
        r"\bchac thang\b",
        r"\bchac chan co lai\b",
        r"\bkhong the thua\b",
        r"\bnhan doi tai khoan\b",
        r"\bx\d+\s+tai khoan\b",
        r"\b100%\s+(thang|loi)\b",
    ],
    "reckless_leverage": [
        r"\ball[- ]?in\b",
        r"\bfull margin\b",
        r"\bvay tien dau tu\b",
        r"\bthe chap.*dau tu\b",
    ],
    "blind_signal": [
        r"\bmua ngay\b",
        r"\bban ngay\b",
        r"\bvao lenh ngay\b",
        r"\bkeo thom\b",
        r"\btarget\s+\d",
    ],
    "fomo": [
        r"\bco hoi cuoi\b",
        r"\bdoi doi\b",
        r"\bkhong mua se tiec\b",
        r"\bmat co hoi\b",
    ],
}


REQUIRED_SAFETY_HINTS = [
    r"\brui ro\b",
    r"\bquan tri von\b",
    r"\bdiem sai\b",
    r"\bvo hieu\b",
    r"\bkhau vi rui ro\b",
    r"\bcat lo\b",
    r"\bbao toan von\b",
]


def iter_markdown_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    excluded_names = {"readme.md", "_template.md"}
    for path in paths:
        resolved = path if path.is_absolute() else ROOT / path
        if resolved.is_file() and resolved.suffix.lower() == ".md" and resolved.name.lower() not in excluded_names:
            files.append(resolved)
        elif resolved.is_dir():
            files.extend(p for p in sorted(resolved.rglob("*.md")) if p.name.lower() not in excluded_names)
    return sorted(set(files))


def normalize(text: str) -> str:
    text = text.lower().replace("đ", "d")
    decomposed = unicodedata.normalize("NFD", text)
    return "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")


def allowed_context(text: str, match_start: int) -> bool:
    line_start = text.rfind("\n", 0, match_start) + 1
    line_end = text.find("\n", match_start)
    if line_end == -1:
        line_end = len(text)
    line = text[line_start:line_end]

    caution_patterns = [
        r"\bkhong\b.*\b(all[- ]?in|full margin|vay tien)\b",
        r"\bdung\b.*\b(all[- ]?in|full margin|vay tien)\b",
        r"\bket\b.*\b(full margin|don bay)\b",
        r"\brui ro\b.*\b(all[- ]?in|full margin|vay tien)\b",
    ]
    return any(re.search(pattern, line, flags=re.IGNORECASE) for pattern in caution_patterns)


def scan_file(path: Path) -> list[tuple[str, int, str]]:
    text = normalize(path.read_text(encoding="utf-8"))
    findings: list[tuple[str, int, str]] = []

    for category, patterns in RISK_PATTERNS.items():
        for pattern in patterns:
            for match in re.finditer(pattern, text, flags=re.IGNORECASE):
                if allowed_context(text, match.start()):
                    continue
                line = text.count("\n", 0, match.start()) + 1
                findings.append((category, line, match.group(0)))

    finance_terms = ["dau tu", "giao dich", "forex", "vang", "thi truong", "usd", "vn-index"]
    if any(word in text for word in finance_terms):
        has_safety_hint = any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in REQUIRED_SAFETY_HINTS)
        if not has_safety_hint:
            findings.append(("missing_safety_layer", 1, "no risk/diem sai/capital management hint"))

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Gold Smith content safety.")
    parser.add_argument("paths", nargs="*", help="Files or directories to scan. Defaults to posts/.")
    args = parser.parse_args()

    paths = [Path(p) for p in args.paths] if args.paths else DEFAULT_PATHS
    files = iter_markdown_files(paths)

    if not files:
        print("No markdown files found.")
        return 0

    total_findings = 0
    for file in files:
        findings = scan_file(file)
        if not findings:
            continue

        rel = file.relative_to(ROOT)
        print(f"\n{rel}")
        for category, line, snippet in findings:
            total_findings += 1
            print(f"  line {line}: {category}: {snippet}")

    if total_findings:
        print(f"\nSafety validation found {total_findings} issue(s). Review before publishing.")
        return 1

    print(f"Safety validation passed for {len(files)} markdown file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
