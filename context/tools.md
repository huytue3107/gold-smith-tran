# Local Tools

## Faster-Whisper-XXL

Purpose: transcribe local audio/video into script files for Gold Smith research.

Workspace-local path:

```text
D:\Gold Smith\tools\Faster-Whisper-XXL
```

Fallback external path:

```text
D:\Faster-Whisper-XXL_r245.4_windows\Faster-Whisper-XXL
```

Wrapper:

```text
scripts/transcribe_with_faster_whisper_xxl.py
```

Command:

```bash
python scripts/transcribe_with_faster_whisper_xxl.py "path/to/media.mp4" --language vi --device cuda --vad --word-timestamps
```

Default output:

```text
reference/Scripts/
```

Use this after:

1. Downloading an allowed video via `scripts/research_viral_videos.py --download-video`.
2. Adding local media files manually.
3. Needing transcript where YouTube/TikTok subtitle is missing.

Rules:

- Do not commit downloaded media.
- Do not commit the portable app or model files; `tools/Faster-Whisper-XXL/` is ignored by git.
- Only transcribe media the user has rights to store/analyze.
- Treat transcript as research input, not final Gold Smith voice.

## Remotion (Video Pipeline)

Purpose: render 60s vertical videos from Gold Smith posts using React + TypeScript.

Workspace path:

```text
D:\Gold Smith\remotion
```

Install (lan dau):

```bash
cd remotion
npm install
```

Cac lenh chinh:

```bash
# Studio preview real-time
npm start

# Render default brief
npx remotion render src/index.ts MarketReading out/<slug>.mp4 --props=briefs/<slug>.json

# Generate brief tu post Facebook
python scripts/brief-to-video.py posts/<slug>.md --persona F0 --pillar "Mot phut doc thi truong"
```

Compositions hien co:

- `MarketReading` — 60s, 1080x1920 vertical (Hook 0-5s / Context 5-25s / Takeaway 25-50s / CTA 50-60s).

Backlog: them composition 15s, 30s, 45s, 90s (theo `Gold-Smith-video.md`).

Fonts: Be Vietnam Pro (4 weights × 2 subsets) tai `remotion/public/fonts/be-vietnam-pro/`. Load qua `remotion/src/fonts.ts` voi `delayRender` de chan render khi font chua xong.

License:

- Remotion Free License OK cho ca nhan / for-profit ≤3 nhan vien / non-profit / evaluation.
- Be Vietnam Pro: SIL OFL v1.1 (free, kem ca commercial, attribution co trong `remotion/public/fonts/be-vietnam-pro/LICENSE.txt`).

Rules:

- Do not commit `remotion/node_modules/` (gitignored, ~500MB).
- Do not commit `remotion/out/` (rendered MP4, gitignored).
- Brief input phai pass Zod schema trong `remotion/src/compositions/market-reading/schema.ts`.
- Bai source phai pass Evidence Gate truoc khi tao video — chay `python scripts/validate-content-safety.py posts/<file>` truoc.
- Sau khi render, move output ve `outputs/video-scripts/<slug>/final.mp4` va cap nhat `outputs/content-ledger.md`.
