---
name: carousel-creation
description: Create Gold Smith carousel content and generate carousel PDFs using the local script. Use when asked for carousel, slides, swipe post, PDF post, or multi-slide finance content.
---

# Gold Smith Carousel Creation

Create carousel posts for Gold Smith finance education, market psychology, personal finance, and founder/fintech lessons.

## Required Context

Read:

1. `CLAUDE.md`
2. `.claude/rules/design.md`
3. `.claude/rules/safety.md`
4. `context/voice-analysis.md`
5. `reference/carousel-ref/carousel-style-analysis.md` if visual style matters.

## Default Visual Style

- Format: 1080 x 1350px.
- Background: warm off-white.
- Text: black or near-black.
- Accent: restrained gold.
- Mood: finance, minimal, sharp, calm.
- No neon.
- No fake profit screenshots.
- No "YOUR BRAND" placeholders.

The local generator already sets Gold Smith defaults in:

```text
scripts/generate-carousel.py
```

## Slide Structure

Recommended structure:

1. Cover: hard truth or high-signal promise.
2. Context: why the reader usually gets this wrong.
3. Lesson 1.
4. Lesson 2.
5. Lesson 3.
6. Risk / invalidation / diem sai.
7. Practical checklist.
8. CTA slide.

Shorter carousels are fine when the idea is narrow. Do not pad slides.

## Content JSON

Use this shape:

```json
{
  "title": "5 Bai Hoc De F0 Khong Chay Tai Khoan",
  "title_emphasis": "F0",
  "slides": [
    {
      "number": 1,
      "heading": "Dung nham may man voi nang luc",
      "subtitle": "Mot lenh thang khong chung minh he thong dung.",
      "takeaway": "Thi truong thuong thuong nguoi moi bang loi nhuan som."
    }
  ],
  "cta_text": "Theo doi Gold Smith Tran de hoc cach doc thi truong tinh tao hon.",
  "cta_subtitle": "Luu lai neu ban dang xay he thong quan tri von."
}
```

## Generate

```bash
python scripts/generate-carousel.py --json content.json --output posts/slug/carousel.pdf
```

Then rebuild dashboard:

```bash
python scripts/build-dashboard.py
```

## Storage

Preferred:

```text
posts/slug/
|-- post.md
|-- content.json
|-- carousel.pdf
`-- original.md      # only if adapted from reference
```

## Safety Check

Before finalizing:

- No profit promise.
- No direct buy/sell command.
- No all-in/full-margin/vay tien.
- Includes risk, diem sai, or capital management.
- Visual text is readable and not overcrowded.
