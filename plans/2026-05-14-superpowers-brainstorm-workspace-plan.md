# Gold Smith Tran Workspace Plan - Superpowers Workshop

**Date:** 2026-05-14
**Status:** P0 implemented
**Goal:** Turn Gold Smith from a content file workspace into a weekly operating system for finance content across Facebook, Threads, short-form video, research, visuals, safety, and analytics.

## 1. Superpowers Frame

This plan uses "Superpowers" as a planning lens, not as an external plugin.

The workspace should develop six core powers:

1. **Strategy Power** - know who the content is for, why it matters, and what pillar it serves.
2. **Research Power** - turn market signals, transcript references, and influencer videos into safe content angles.
3. **Writing Power** - produce Facebook/Threads posts with Gold Smith voice.
4. **Video Power** - convert strong ideas into 15/30/45/60/90s scripts.
5. **Safety Power** - block profit promises, blind signals, FOMO, all-in/full-margin language, and unverified claims.
6. **Learning Power** - track what was published, what worked, and what should be repeated.

## 2. Current State

### Strong Assets

- `Gold-Smith-fb.md` - master voice for Facebook/Threads.
- `Gold-Smith-video.md` - dedicated short-form video voice and script structure.
- `1000_hook_short_form_tai_chinh.md` - hook bank for finance video and post openings.
- `context/operating-model-v2-1.md` - NEXUS-lite operating model.
- `.claude/agents/` - specialist agents for strategy, safety, voice, visual, evidence, analytics, experiment tracking.
- `.claude/commands/` - operational commands for content creation, review, market intelligence, and weekly review.
- `reference/Scripts/` - transcript bank for studying finance/video content.
- `outputs/finance_influencer_videos/` - collected influencer video reference dataset.
- `scripts/validate-content-safety.py` - local safety guardrail.
- `scripts/build-dashboard.py` - local dashboard generator.

### Gaps

- No single weekly command center file tying ideas, posts, scripts, experiments, and dashboard status together.
- Transcript/reference assets are large but not yet scored or mapped into Gold Smith pillars.
- Video assets are now strong, but there is no standard video script template in `posts/` or `outputs/`.
- Dashboard still shows posts, not a full content pipeline with persona/platform/status/experiment fields.
- `context/metrics.md` still has many `TBD` values, so learning loop cannot yet make real performance decisions.
- `context/context.exe` was removed during P0 cleanup.

## 3. Brainstorm Output

### A. Strategy Power

Build a weekly "Content Mission Brief" that chooses:

- 1 market theme.
- 1 F0 pain point.
- 1 personal finance/family angle.
- 1 founder/fintech angle.
- 1 repurpose target.

Output target:

- `outputs/YYYY-MM-DD-weekly-mission.md`

Suggested command:

- `/weekly-content-review-v2`
- `/market-intelligence-v2`

### B. Research Power

Turn `reference/Scripts/` and `outputs/finance_influencer_videos/` into a scored idea source.

Each reference should be mapped by:

- Creator/source.
- Topic.
- Hook type.
- Persona.
- Gold Smith pillar.
- Safety risk.
- Reusable angle.
- Suggested output format.

Output target:

- `reference/Scripts/README.md`
- `outputs/research-index.md`

### C. Writing Power

Standardize every post through `posts/_template.md`.

Minimum output for each post:

- Metadata.
- Post text.
- Hook options.
- CTA options.
- Safety notes.
- Visual notes.
- Repurpose path.
- Evidence/source notes.

Workflow:

```text
Idea -> Strategy Gate -> Draft -> Safety -> Voice -> Visual -> Evidence -> Dashboard
```

### D. Video Power

Add a video script layer that sits beside posts, not inside random notes.

Recommended output shape:

```text
outputs/video-scripts/YYYY-MM-DD-slug.md
```

Each video script should include:

- Duration: 15/30/45/60/90s.
- Hook.
- Spoken script.
- On-screen text.
- B-roll/visual notes.
- Caption.
- Safety notes.
- Source post/reference.

Use:

- `Gold-Smith-video.md` for structure.
- `1000_hook_short_form_tai_chinh.md` for hook inspiration.
- `Gold-Smith-fb.md` for core brand substance.

### E. Safety Power

Make safety a required local check before publish.

Commands:

```bash
python scripts/validate-content-safety.py posts
python scripts/build-dashboard.py
```

Needed improvement:

- Extend validator to scan `outputs/video-scripts/`.
- Add "unverified claim" markers for figures, dates, and market data.
- Add a report mode: `--format markdown`.

### F. Learning Power

The workspace needs a simple content ledger.

Recommended file:

```text
outputs/content-ledger.md
```

Fields:

- Date.
- Platform.
- Title.
- Persona.
- Pillar.
- Format.
- Status.
- Experiment tag.
- Safety status.
- Published URL.
- Metrics after 24h/7d.
- Lesson learned.

This can later power dashboard filters.

## 4. 30-Day Roadmap

### Week 1 - Clean Operating Base

1. Delete accidental `context/context.exe`.
2. Add `reference/Scripts/README.md`.
3. Add `outputs/video-scripts/README.md`.
4. Add `outputs/content-ledger.md`.
5. Update `README.md` and `CLAUDE.md` to mention video script storage and content ledger.

Done when:

- No accidental executable in `context/`.
- Every large reference folder has a README.
- New output locations are documented.

### Week 2 - Build Research Index

1. Review 10 transcript files from `reference/Scripts/`.
2. Review top rows from `outputs/finance_influencer_videos/videos.csv`.
3. Create `outputs/research-index.md` with 30 reusable angles.
4. Tag each angle by persona, pillar, safety risk, and output format.

Done when:

- At least 30 scored ideas exist.
- At least 10 are video-first.
- At least 10 are Facebook/Threads-first.

### Week 3 - Upgrade Production Flow

1. Create 5 posts using `posts/_template.md`.
2. Convert 3 posts into short-form scripts.
3. Run safety validator.
4. Rebuild dashboard.
5. Log every asset in `outputs/content-ledger.md`.

Done when:

- 5 post files exist.
- 3 video script files exist.
- Dashboard builds.
- Ledger has all items.

### Week 4 - Learning Loop

1. Add real metrics if available.
2. Run `/weekly-content-review-v2`.
3. Identify top 3 hooks, top 3 weak points, and 3 repeatable formats.
4. Update `context/metrics.md`.
5. Decide next month pillar ratio.

Done when:

- At least one weekly review exists.
- Metrics are no longer all `TBD`.
- Next month content priorities are explicit.

## 5. Priority Backlog

### P0 - Immediate

- Remove `context/context.exe`. Done 2026-05-14.
- Add README for `reference/Scripts/`. Done 2026-05-14.
- Add video script output folder and README. Done 2026-05-14.
- Add `outputs/content-ledger.md`. Done 2026-05-14.

### P1 - High

- Extend `scripts/validate-content-safety.py` to scan video scripts.
- Add dashboard filters for persona/platform/status.
- Create `outputs/research-index.md`. Done 2026-05-14.
- Create a `/create-video-script-v2` command.
- Create `/research-viral-videos-v2` and `scripts/research_viral_videos.py` for viral video metadata/link/transcript research. Done 2026-05-14.

### P2 - Medium

- Add transcript scoring helper script.
- Add CSV-to-idea mining workflow for influencer videos.
- Add monthly content calendar.
- Add experiment summary charts.

### P3 - Later

- Canva/visual workflow integration.
- Automated content package export.
- Publish checklist per platform.
- Analytics import from real social platforms.

## 6. Implementation Log

### P0 - Completed 2026-05-14

1. Deleted `context/context.exe`.
2. Added `reference/Scripts/README.md`.
3. Added `outputs/video-scripts/README.md`.
4. Added `outputs/content-ledger.md`.
5. Updated docs to point to these files.

### Recommended Next Implementation

Start P1:

1. Create `/create-video-script-v2`.
2. Use `/research-viral-videos-v2` to seed `outputs/research-index.md`.
3. Extend `scripts/validate-content-safety.py` to scan `outputs/video-scripts/`.
4. Add dashboard filters for persona/platform/status.

This gives the workspace a cleaner structure before adding more automation.
