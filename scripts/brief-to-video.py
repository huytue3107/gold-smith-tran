#!/usr/bin/env python3
"""
Convert a Gold Smith Facebook post (markdown) into a Remotion video brief (JSON).

Usage:
    python scripts/brief-to-video.py posts/2026-04-28-ty-gia-usd.md \
        --persona F0 --pillar "Mot phut doc thi truong"

Output: remotion/briefs/<slug>.json

The script extracts hook/context/takeaway/cta heuristically from the post,
then writes a JSON file matching remotion/src/compositions/market-reading/schema.ts.

IMPORTANT: Generated brief is a DRAFT. User must review for:
- Hook ≤120 char, sharp, no clickbait.
- Context ≤220 char, fits 20s of voice-over.
- Takeaway ≤180 char, memorable.
- CTA ≤80 char, soft.
- Safety: no profit promise, no blind signal, no FOMO.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from datetime import date


ROOT = Path(__file__).resolve().parents[1]
BRIEFS_DIR = ROOT / "remotion" / "briefs"


def slug_from_path(path: Path) -> str:
    stem = path.stem
    if path.parent != ROOT / "posts":
        stem = path.parent.name
    return re.sub(r"[^a-z0-9-]", "-", stem.lower()).strip("-")


def extract_first_paragraph(text: str, max_len: int) -> str:
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip() and not p.strip().startswith("#")]
    if not paragraphs:
        return ""
    candidate = paragraphs[0]
    return candidate[:max_len].rstrip()


def extract_post_text(content: str) -> str:
    match = re.search(r"##\s*Post Text\s*\n+(.*?)(?:\n##|\Z)", content, flags=re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return content


def build_draft_brief(post_path: Path, persona: str, pillar: str) -> dict:
    content = post_path.read_text(encoding="utf-8")
    post_text = extract_post_text(content)

    paragraphs = [p.strip() for p in post_text.split("\n\n") if p.strip() and not p.strip().startswith("#")]

    hook = paragraphs[0][:120] if paragraphs else "TBD hook"
    context = paragraphs[1][:220] if len(paragraphs) > 1 else "TBD context"
    takeaway = paragraphs[-2][:180] if len(paragraphs) > 2 else paragraphs[-1][:180] if paragraphs else "TBD takeaway"
    cta = "Luu lai truoc khi vao lenh tiep theo."

    cta_match = re.search(r"(luu lai|theo doi|binh luan|inbox|tham gia)[^.\n]{0,60}", post_text, flags=re.IGNORECASE)
    if cta_match:
        cta = cta_match.group(0).strip()[:80]

    slug = slug_from_path(post_path)

    return {
        "slug": slug,
        "date": date.today().isoformat(),
        "persona": persona,
        "pillar": pillar,
        "hook": hook,
        "context": context,
        "takeaway": takeaway,
        "cta": cta,
        "brandMark": "GOLD SMITH TRAN — NHA GIA KIM FOREX",
        "safetyDisclaimer": "Khong phai khuyen nghi dau tu. Quan tri von la viec cua ban.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert post markdown to Remotion brief JSON.")
    parser.add_argument("post", help="Path to post markdown")
    parser.add_argument("--persona", required=True, choices=["F0", "GenZ-Millennial", "PhuNu-GiaDinh", "Founder-Fintech"])
    parser.add_argument("--pillar", required=True, help="Content pillar name")
    parser.add_argument("--output", help="Output brief path (default: remotion/briefs/<slug>.json)")
    args = parser.parse_args()

    post_path = Path(args.post)
    if not post_path.is_absolute():
        post_path = ROOT / post_path
    if not post_path.exists():
        print(f"ERROR: post not found: {post_path}", file=sys.stderr)
        return 1

    brief = build_draft_brief(post_path, args.persona, args.pillar)

    output_path = Path(args.output) if args.output else BRIEFS_DIR / f"{brief['slug']}.json"
    if not output_path.is_absolute():
        output_path = ROOT / output_path

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(brief, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Draft brief written: {output_path.relative_to(ROOT)}")
    print("REVIEW REQUIRED:")
    print("  - Hook (≤120 char): sharp, no clickbait")
    print("  - Context (≤220 char): fits 20s voice-over")
    print("  - Takeaway (≤180 char): memorable, single sentence")
    print("  - CTA (≤80 char): soft, single goal")
    print("  - Safety: no profit promise, no signal, no FOMO")
    print("\nNext:")
    print(f"  cd remotion && npx remotion render src/index.ts MarketReading out/{brief['slug']}.mp4 --props=briefs/{brief['slug']}.json")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
