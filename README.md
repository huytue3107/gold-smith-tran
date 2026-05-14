# Gold Smith Tran Content OS

Workspace nay la he thong san xuat noi dung cho **Gold Smith Tran - Nha Gia Kim Forex**.

Muc tieu: tao noi dung tai chinh sac, thuc chien, co chieu sau va an toan. Kenh uu tien la Facebook va Threads; video ngan, carousel va infographic la huong repurpose.

## Operating Layer

Gold Smith hien dung Content OS v2.1:

```text
Brief -> Strategy -> Research -> Draft -> Safety Review -> Voice Edit -> Visual/Repurpose -> Evidence Gate -> Storage -> Dashboard -> Learning Loop
```

Doc theo thu tu:

1. `CLAUDE.md` - operating manual chinh.
2. `Gold-Smith-fb.md` - style guide va voice master cho Facebook/Threads.
   2b. `Gold-Smith-video.md` - style guide va voice master cho TikTok/Reels/Shorts.
3. `context/operating-model-v2-1.md` - NEXUS-lite, gate, handoff, cadence.
4. `context/framework-v2.md` - framework noi dung v2.
5. `context/` - profile, ICP, strategy, metrics, voice analysis.
6. `.claude/rules/` - rule chi tiet cho persona, safety, tone, template, workflow.
7. `posts/` - bai da tao hoac san sang bien tap.
8. `outputs/content-ledger.md` - so theo doi asset, status, experiment va metrics.
9. `reference/` - visual/writing/transcript references phu, khong lan at Gold Smith voice.

Neu co mau thuan, uu tien `Gold-Smith-fb.md`, `.claude/rules/safety.md`, roi den `context/`.

## Commands

- `/prime` - nap context Gold Smith.
- `/create-content-v2` - tao noi dung theo pipeline v2.
- `/review-content-v2` - review bai theo strategy, safety, voice va completeness.
- `/market-intelligence-v2` - tao market/content intelligence brief.
- `/research-viral-videos-v2` - research video viral/high-view, lay link va transcript/script.
- `/transcribe-local-video-v2` - dung Faster-Whisper-XXL local de transcribe media thanh script.
- `/create-video-v2` - bien bai da pass Evidence Gate thanh video 60s qua Remotion.
- `/weekly-content-review-v2` - review tuan, risk, experiment va next actions.
- `/create-10-posts` - tao batch 10 bai.

## Specialist Agents

- `content-strategist` - persona, pain point, pillar, format, CTA.
- `trend-researcher` - tin hieu thi truong va trend noi dung.
- `financial-safety-reviewer` - chan cam ket loi nhuan, phiem lenh, FOMO, all-in.
- `voice-editor` - dua bai ve dung giong Gold Smith.
- `visual-director` - quote, infographic, carousel, short video, photo overlay.
- `brand-guardian` - giu dinh vi, visual identity va messaging.
- `content-evidence-reviewer` - evidence gate truoc khi xem output la xong.
- `analytics-reporter` - doc hieu suat noi dung thanh insight.
- `experiment-tracker` - theo doi hook, CTA, format, persona, visual test.
- `researcher`, `code-reviewer`, `qa-tester` - dung khi can research/code/tooling.

## Workspace Structure

```text
.
|-- CLAUDE.md                 # Operating manual chinh
|-- Gold-Smith-fb.md          # Style guide master
|-- .claude/
|   |-- agents/               # Specialist agent definitions
|   |-- commands/             # Slash command playbooks
|   |-- rules/                # Content rules
|   `-- skills/.skills/       # Local skills
|-- context/                  # Brand brain va operating model
|-- posts/                    # Bai viet
|-- outputs/                  # Dashboard, draft, video scripts, content ledger, research output
|-- plans/                    # Change plans
|-- reference/                # Visual refs, templates, transcripts, optional writing refs
|-- remotion/                 # React + Remotion video pipeline (compositions, briefs, fonts)
`-- scripts/                  # Dashboard, carousel, infographic, overlay, research, brief-to-video tools
```

## Video Production (Remotion)

Bai Facebook da pass Evidence Gate co the duoc bien thanh video 60s qua Remotion:

```bash
python scripts/brief-to-video.py posts/<slug>.md --persona F0 --pillar "Mot phut doc thi truong"
cd remotion && npm install                              # lan dau, ~500MB
npx remotion render src/index.ts MarketReading out/<slug>.mp4 --props=briefs/<slug>.json
```

Composition hien co: `MarketReading` (60s, 1080x1920 vertical). Font: Be Vietnam Pro (woff2 da copy vao `remotion/public/fonts/`). License Remotion Free OK cho ca nhan/≤3 nhan vien. Chi tiet: `remotion/README.md` + `.claude/commands/create-video-v2.md`.

## Standard Content Output

Moi bai nen co:

- Metadata: date, platform, persona, objective, content pillar, format.
- Post text copy-paste ready.
- 3 hook options.
- 3 CTA options.
- Safety notes: risk, invalidation/diem sai, no profit promise.
- Visual or repurpose direction.
- Storage path hoac dashboard note neu da luu.

## Safety Rules

Khong bao gio:

- Cam ket loi nhuan.
- Phiem lenh mua/ban khi thieu boi canh.
- Kich thich all-in, full margin, vay tien dau tu.
- Tao FOMO bang ngon ngu nhu "co hoi cuoi", "chac thang", "bao loi".
- Bia website, followers, doanh thu, lich workshop, thanh tich dau tu.

Luon uu tien:

- Quan tri von.
- Diem sai.
- Khau vi rui ro.
- Ky luat va xac suat.
- Su that co the kiem chung.

## Scripts

```bash
python scripts/build-dashboard.py
python scripts/generate-carousel.py --json content.json --output posts/slug/carousel.pdf
python scripts/generate-infographic.py --prompt "..." --reference reference/infographic-ref-1.jpeg
python scripts/add-photo-overlay.py --image input.jpg --text "..."
python scripts/collect_finance_influencer_videos.py
python scripts/research_viral_videos.py --limit 20 --top 10 --update-index
python scripts/research_viral_videos.py "https://www.youtube.com/@hieu-tv/videos" --download-video --local-transcribe --local-language vi --local-device cuda --update-index
python scripts/transcribe_with_faster_whisper_xxl.py "outputs/viral_video_research/media" --language vi --device cuda --vad --word-timestamps
python scripts/brief-to-video.py posts/<slug>.md --persona F0 --pillar "Mot phut doc thi truong"
python scripts/validate-content-safety.py posts
```

Dashboard output:

```text
outputs/dashboard.html
```

## Video And Learning Loop

Short-form scripts live in:

```text
outputs/video-scripts/
```

Use `Gold-Smith-video.md` for script structure and `1000_hook_short_form_tai_chinh.md` for hook inspiration.

Track every meaningful asset in:

```text
outputs/content-ledger.md
```

Transcript references live in:

```text
reference/Scripts/
```

Transcript ideas should be scored into `outputs/research-index.md` before being turned into Gold Smith content.

Viral video research output:

```text
outputs/viral_video_research/
```

Local transcription uses the workspace clone at `tools/Faster-Whisper-XXL`, configured in `context/tools.md`.

## Cleanup Notes

- File rong/deprecated va command reset context cu da duoc loai bo.
- Cac skill da duoc chuan hoa ve Gold Smith thay vi mac dinh LinkedIn/Adam/YOUR BRAND.
- Da them `posts/_template.md` va `scripts/validate-content-safety.py`.
- Da them `outputs/video-scripts/`, `outputs/content-ledger.md` va `reference/Scripts/README.md`.
- Reference Adam Robinson duoc xem la tai lieu hoc packaging phu, khong phai voice chinh.
