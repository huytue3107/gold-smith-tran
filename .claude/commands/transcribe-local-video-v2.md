# Transcribe Local Video v2

Dung Faster-Whisper-XXL local de transcribe video/audio thanh script cho Gold Smith.

## Input

`$ARGUMENTS` la file hoac folder media local.

Vi du:

```bash
python scripts/transcribe_with_faster_whisper_xxl.py "outputs/viral_video_research/media" --language vi --device cuda --vad --word-timestamps
```

Mac dinh output vao:

```text
reference/Scripts/
```

## Tool Path

Mac dinh wrapper uu tien ban da clone trong workspace:

```text
D:\Gold Smith\tools\Faster-Whisper-XXL\faster-whisper-xxl.exe
```

Neu khong co, fallback ve:

```text
D:\Faster-Whisper-XXL_r245.4_windows\Faster-Whisper-XXL\faster-whisper-xxl.exe
```

Neu app duoc doi vi tri, set env var:

```powershell
$env:FASTER_WHISPER_XXL_HOME="D:\path\to\Faster-Whisper-XXL"
```

Hoac truyen:

```bash
python scripts/transcribe_with_faster_whisper_xxl.py file.mp4 --exe "D:\path\faster-whisper-xxl.exe"
```

## Recommended Gold Smith Defaults

- Vietnamese: `--language vi`
- English: `--language en`
- Unknown language: omit `--language`
- Better subtitles: `--vad --word-timestamps`
- Output: `txt srt`

## Safety / Rights

Chi transcribe file ma user co quyen luu tru/phan tich.

Transcript la reference phu. Khong copy voice/claim cua creator khac vao Gold Smith content neu chua bien tap va xac minh.
