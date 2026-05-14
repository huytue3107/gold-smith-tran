# Research Viral Videos v2

Tu dong research video viral/high-view, lay link, lay transcript/script, va cap nhat research index cho Gold Smith.

## Input

`$ARGUMENTS` co the la:

- De trong: dung danh sach finance creators mac dinh trong `scripts/research_viral_videos.py`.
- Mot hoac nhieu YouTube channel/video/playlist URL.
- Them tham so: `--limit`, `--top`, `--min-views`, `--download-video`, `--local-transcribe`, `--local-language`, `--local-device`, `--no-transcript`, `--update-index`.

## Safety / Rights

Mac dinh chi lay metadata, link va transcript/subtitle cong khai.

Chi dung `--download-video` khi user co quyen tai, luu tru hoac tai su dung video. Neu khong ro quyen, khong tai video.

## Command

```bash
python scripts/research_viral_videos.py $ARGUMENTS --update-index
```

Vi du:

```bash
python scripts/research_viral_videos.py --limit 20 --top 10 --min-views 50000 --update-index
```

Tai video neu co quyen:

```bash
python scripts/research_viral_videos.py "https://www.youtube.com/@hieu-tv/videos" --limit 20 --top 5 --download-video --update-index
```

Tai video va transcribe bang Faster-Whisper-XXL local:

```bash
python scripts/research_viral_videos.py "https://www.youtube.com/@hieu-tv/videos" --limit 20 --top 5 --download-video --local-transcribe --local-language vi --local-device cuda --update-index
```

## Outputs

- `outputs/viral_video_research/manifest.csv`
- `outputs/viral_video_research/manifest.json`
- `outputs/viral_video_research/links/*.url`
- `reference/Scripts/*.txt` neu transcript co san
- `outputs/research-index.md` neu dung `--update-index`
- `outputs/viral_video_research/media/` neu dung `--download-video`

## Review Step

Sau khi chay:

1. Mo `outputs/viral_video_research/manifest.csv`.
2. Kiem tra video nao co transcript.
3. Chon angle phu hop voi Gold Smith pillar.
4. Khong copy voice/claim cua creator khac.
5. Neu co so lieu/du bao/thi truong, phai xac minh lai truoc khi viet bai.
