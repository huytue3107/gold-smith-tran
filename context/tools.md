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
