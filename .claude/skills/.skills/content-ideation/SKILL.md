---
name: content-ideation
description: Generate Gold Smith content ideas from market signals, audience pain points, proven packaging, and existing content pillars. Use when asked for content ideas, topic ideas, brainstorming posts, angles, hooks, or a content backlog.
---

# Gold Smith Content Ideation

Generate content ideas for **Gold Smith Tran - Nha Gia Kim Forex**.

Default goal: useful, sharp, safe finance content for Facebook and Threads, with optional repurpose into short video, carousel, infographic, or photo overlay.

## Required Context

Read these before ideating:

1. `CLAUDE.md`
2. `context/strategy.md`
3. `context/icp.md`
4. `context/voice-analysis.md`
5. `.claude/rules/safety.md`
6. `context/operating-model-v2-1.md` when planning a campaign or batch

Optional references:

- `outputs/finance_influencer_videos/README.md` for creator/video idea mining.
- `reference/adam-robinson-writing-style.md` only as packaging reference, never as Gold Smith voice.

## Idea Sources

Split requested ideas across four sources unless the user asks otherwise:

1. **Market Signal**: macro, VND/USD, gold, forex, rates, liquidity, risk events.
2. **Audience Pain**: F0 mistakes, money anxiety, family cash flow, founder runway, fintech behavior.
3. **Proven Packaging**: adapt a hook/body structure that worked elsewhere, but rewrite with Gold Smith substance.
4. **Series Builder**: extend Gold Smith pillars into repeatable weekly series.

## Safety Filter

Reject or rewrite ideas that depend on:

- Profit promises.
- Buy/sell signals without context.
- All-in, full margin, borrowed money.
- Fear-only FOMO.
- Unverified personal claims or fake performance numbers.

Every finance idea should include at least one of:

- Risk.
- Invalidation point / diem sai.
- Capital management.
- Time horizon.
- Reader-specific suitability.

## Output Format

For each idea:

```markdown
### [Idea title]

- **Source:** Market Signal / Audience Pain / Proven Packaging / Series Builder
- **Persona:** F0 / Gen Z-Millennials / Family / Founder-Fintech
- **Pillar:** [Gold Smith pillar]
- **Hook:** [First 1-2 lines]
- **Angle:** [What the post proves]
- **Safety layer:** [Risk/diem sai/capital management]
- **Best format:** Facebook post / Thread / Short video / Carousel / Infographic
- **Repurpose:** [Optional path]
- **CTA:** [Soft CTA]
```

When saving is requested, save to:

```text
outputs/YYYY-MM-DD-content-ideas.md
```

## Quality Bar

Good Gold Smith ideas should feel:

- Specific enough to write now.
- Useful to a real reader with money at risk.
- Sharp without becoming reckless.
- Compatible with `Gold-Smith-fb.md` voice.
- Easy to review through `/review-content-v2`.
