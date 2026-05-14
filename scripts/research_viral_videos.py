#!/usr/bin/env python3
"""
Research viral/high-view finance videos, collect links, fetch transcripts, and
optionally download video files.

Default behavior is metadata + transcript only. Use --download-video only for
content you have rights to download or reuse.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "outputs" / "viral_video_research"
DEFAULT_SCRIPT_DIR = ROOT / "reference" / "Scripts"
DEFAULT_INDEX = ROOT / "outputs" / "research-index.md"
LOCAL_WHISPER_WRAPPER = ROOT / "scripts" / "transcribe_with_faster_whisper_xxl.py"


DEFAULT_SOURCES = [
    "https://www.youtube.com/@TheRamseyShow/videos",
    "https://www.youtube.com/@TheRichDadChannel/videos",
    "https://www.youtube.com/@warikoo/videos",
    "https://www.youtube.com/@PranjalKamra/videos",
    "https://www.youtube.com/@CARachanaRanade/videos",
    "https://www.youtube.com/@GrahamStephan/videos",
    "https://www.youtube.com/@thaiphamofficialvn/videos",
    "https://www.youtube.com/@hieu-tv/videos",
    "https://www.youtube.com/@Erika2/videos",
    "https://www.youtube.com/@MarkTilbury/videos",
    "https://www.youtube.com/@humphrey/videos",
]


def slugify(value: str, max_len: int = 120) -> str:
    value = re.sub(r"[^\w\s.-]", "", value, flags=re.UNICODE).strip().lower()
    value = re.sub(r"[\s_]+", "-", value)
    return (value or "unknown")[:max_len].strip("-")


def run(cmd: list[str], cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        errors="replace",
    )


def resolve_workspace_path(value: str) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return ROOT / path


def ensure_yt_dlp() -> None:
    proc = run([sys.executable, "-m", "yt_dlp", "--version"])
    if proc.returncode != 0:
        raise SystemExit(
            "yt-dlp is required. Install it with: python -m pip install yt-dlp"
        )


def collect_metadata(source_url: str, limit: int | None) -> list[dict]:
    cmd = [
        sys.executable,
        "-m",
        "yt_dlp",
        "--ignore-errors",
        "--skip-download",
        "--dump-json",
    ]
    if limit:
        cmd += ["--playlist-end", str(limit)]
    cmd.append(source_url)

    proc = run(cmd)
    rows: list[dict] = []
    for line in proc.stdout.splitlines():
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            continue
        if item.get("_type") == "playlist":
            continue
        rows.append(
            {
                "title": item.get("title") or "",
                "id": item.get("id") or "",
                "url": item.get("webpage_url") or item.get("original_url") or source_url,
                "channel": item.get("channel") or item.get("uploader") or "",
                "view_count": item.get("view_count"),
                "like_count": item.get("like_count"),
                "comment_count": item.get("comment_count"),
                "upload_date": item.get("upload_date") or "",
                "duration": item.get("duration"),
                "source_url": source_url,
            }
        )
    return rows


def parse_upload_date(value: str) -> datetime | None:
    if not value or len(value) != 8:
        return None
    try:
        return datetime.strptime(value, "%Y%m%d").replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def virality_score(video: dict, now: datetime) -> float:
    views = video.get("view_count") or 0
    likes = video.get("like_count") or 0
    comments = video.get("comment_count") or 0
    uploaded = parse_upload_date(video.get("upload_date") or "")
    age_days = 30.0
    if uploaded:
        age_days = max((now - uploaded).days, 1)
    view_velocity = views / age_days
    engagement = likes + (comments * 3)
    return round(view_velocity + (engagement * 0.5), 2)


def select_top_videos(rows: list[dict], top: int, min_views: int) -> list[dict]:
    now = datetime.now(timezone.utc)
    filtered = [r for r in rows if isinstance(r.get("view_count"), int) and r["view_count"] >= min_views]
    for row in filtered:
        row["virality_score"] = virality_score(row, now)
    filtered.sort(key=lambda r: (r["virality_score"], r.get("view_count") or 0), reverse=True)
    return filtered[:top]


def write_shortcut(path: Path, url: str) -> None:
    path.write_text(f"[InternetShortcut]\nURL={url}\n", encoding="utf-8")


def clean_subtitle_text(path: Path) -> str:
    lines: list[str] = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.upper().startswith("WEBVTT"):
            continue
        if re.match(r"^\d+$", line):
            continue
        if "-->" in line:
            continue
        if line.startswith(("NOTE", "Kind:", "Language:")):
            continue
        line = re.sub(r"<[^>]+>", "", line)
        line = re.sub(r"\s+", " ", line).strip()
        if line:
            lines.append(line)

    deduped: list[str] = []
    for line in lines:
        if not deduped or deduped[-1] != line:
            deduped.append(line)
    return "\n".join(deduped).strip()


def fetch_transcript(video: dict, work_dir: Path, script_dir: Path) -> Path | None:
    slug = slugify(video["title"])
    base = work_dir / slug
    cmd = [
        sys.executable,
        "-m",
        "yt_dlp",
        "--skip-download",
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs",
        "vi,en.*",
        "--sub-format",
        "vtt/srt/best",
        "-o",
        str(base) + ".%(ext)s",
        video["url"],
    ]
    proc = run(cmd)
    subtitle_files = sorted(work_dir.glob(f"{slug}*.vtt")) + sorted(work_dir.glob(f"{slug}*.srt"))
    if not subtitle_files:
        video["transcript_status"] = "not_found"
        video["transcript_error"] = proc.stderr.strip()[-500:]
        return None

    transcript_text = clean_subtitle_text(subtitle_files[0])
    if not transcript_text:
        video["transcript_status"] = "empty"
        return None

    script_dir.mkdir(parents=True, exist_ok=True)
    out_path = script_dir / f"{video.get('channel') or 'unknown'} - {video['title']}.txt"
    safe_out = script_dir / f"{slugify(out_path.stem, 180)}.txt"
    safe_out.write_text(transcript_text + "\n", encoding="utf-8")
    video["transcript_status"] = "saved"
    video["transcript_path"] = str(safe_out.relative_to(ROOT))
    return safe_out


def download_video(video: dict, media_dir: Path) -> list[Path]:
    media_dir.mkdir(parents=True, exist_ok=True)
    before = {p.resolve() for p in media_dir.glob("*") if p.is_file()}
    output = str(media_dir / "%(title).180B [%(id)s].%(ext)s")
    cmd = [
        sys.executable,
        "-m",
        "yt_dlp",
        "-f",
        "bv*+ba/b",
        "--merge-output-format",
        "mp4",
        "-o",
        output,
        video["url"],
    ]
    proc = run(cmd)
    video["download_status"] = "downloaded" if proc.returncode == 0 else "failed"
    if proc.returncode != 0:
        video["download_error"] = proc.stderr.strip()[-500:]
        return []

    after = {p.resolve() for p in media_dir.glob("*") if p.is_file()}
    downloaded = sorted(after - before)
    video["downloaded_files"] = [str(p.relative_to(ROOT)) for p in downloaded if p.is_relative_to(ROOT)]
    return downloaded


def write_csv(path: Path, rows: list[dict]) -> None:
    fields = [
        "rank",
        "id",
        "title",
        "channel",
        "url",
        "view_count",
        "like_count",
        "comment_count",
        "upload_date",
        "duration",
        "virality_score",
        "transcript_status",
        "transcript_path",
        "local_transcript_status",
        "local_transcript_path",
        "download_status",
        "downloaded_files",
        "source_url",
    ]
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def infer_pillar(title: str) -> str:
    text = title.lower()
    if any(k in text for k in ["stock", "market", "vn-index", "fed", "dollar", "usd", "gold", "vàng", "bitcoin"]):
        return "Dong tien vi mo / F0 tra hoc phi"
    if any(k in text for k in ["debt", "emi", "loan", "credit", "bankruptcy", "saving", "retirement"]):
        return "Tien cua nguoi tre / Mai nha tai chinh"
    if any(k in text for k in ["ai", "business", "income", "side hustle", "marketing"]):
        return "Founder doc dong tien / Fintech hieu con nguoi"
    return "F0 tra hoc phi"


def append_research_index(index_path: Path, rows: list[dict]) -> None:
    index_path.parent.mkdir(parents=True, exist_ok=True)
    if not index_path.exists():
        index_path.write_text(
            "# Gold Smith Research Index\n\n"
            "| Date | Source | Title | Views | Score | Pillar | Reusable Angle | Transcript | URL |\n"
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n",
            encoding="utf-8",
        )

    today = datetime.now().strftime("%Y-%m-%d")
    lines = []
    for row in rows:
        title = (row.get("title") or "").replace("|", "-")
        channel = (row.get("channel") or "Unknown").replace("|", "-")
        pillar = infer_pillar(title).replace("|", "-")
        angle = f"Adapt hook/structure into Gold Smith safety-first angle for {pillar}".replace("|", "-")
        transcript = row.get("transcript_path") or "TBD"
        url = row.get("url") or ""
        lines.append(
            f"| {today} | {channel} | {title} | {row.get('view_count') or ''} | "
            f"{row.get('virality_score') or ''} | {pillar} | {angle} | {transcript} | {url} |\n"
        )

    with index_path.open("a", encoding="utf-8") as f:
        f.writelines(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Research viral finance videos and transcripts.")
    parser.add_argument("sources", nargs="*", help="YouTube channel/video/playlist URLs. Defaults to built-in finance creator list.")
    parser.add_argument("--limit", type=int, default=20, help="Videos to scan per channel/playlist.")
    parser.add_argument("--top", type=int, default=10, help="Top videos to keep after scoring.")
    parser.add_argument("--min-views", type=int, default=0, help="Minimum view count.")
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT), help="Output directory.")
    parser.add_argument("--script-dir", default=str(DEFAULT_SCRIPT_DIR), help="Transcript text output directory.")
    parser.add_argument("--download-video", action="store_true", help="Download video files too. Use only with rights/permission.")
    parser.add_argument("--local-transcribe", action="store_true", help="After --download-video, transcribe downloaded media with Faster-Whisper-XXL.")
    parser.add_argument("--local-language", default="", help="Language for local transcription, e.g. vi/en. Empty means auto detect.")
    parser.add_argument("--local-device", default="", help="Device for local transcription, e.g. cuda/cpu. Empty uses app default.")
    parser.add_argument("--no-transcript", action="store_true", help="Skip transcript download.")
    parser.add_argument("--update-index", action="store_true", help="Append selected videos to outputs/research-index.md.")
    args = parser.parse_args()

    ensure_yt_dlp()

    out_dir = resolve_workspace_path(args.out_dir)
    script_dir = resolve_workspace_path(args.script_dir)
    media_dir = out_dir / "media"
    links_dir = out_dir / "links"
    transcript_work_dir = out_dir / "transcript_raw"
    for path in [out_dir, links_dir, transcript_work_dir]:
        path.mkdir(parents=True, exist_ok=True)

    sources = args.sources or DEFAULT_SOURCES
    all_rows: list[dict] = []
    for source in sources:
        all_rows.extend(collect_metadata(source, args.limit))

    selected = select_top_videos(all_rows, args.top, args.min_views)
    for idx, video in enumerate(selected, start=1):
        video["rank"] = idx
        write_shortcut(links_dir / f"{idx:02d}-{slugify(video['title'])}.url", video["url"])
        if not args.no_transcript:
            fetch_transcript(video, transcript_work_dir, script_dir)
        if args.download_video:
            download_video(video, media_dir)
        else:
            video["download_status"] = "skipped"

    payload = {
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "source_count": len(sources),
        "scanned_count": len(all_rows),
        "selected_count": len(selected),
        "download_video": args.download_video,
        "selected": selected,
    }
    (out_dir / "manifest.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    write_csv(out_dir / "manifest.csv", selected)

    if args.local_transcribe:
        if not args.download_video:
            print("Local transcription skipped: --local-transcribe requires --download-video.")
            return 2
        elif not LOCAL_WHISPER_WRAPPER.exists():
            print(f"Local transcription skipped: wrapper not found at {LOCAL_WHISPER_WRAPPER}")
            return 2
        else:
            media_to_transcribe: list[Path] = []
            for row in selected:
                for item in row.get("downloaded_files") or []:
                    path = resolve_workspace_path(item)
                    if path.exists():
                        media_to_transcribe.append(path)
            media_to_transcribe = sorted(set(media_to_transcribe))
            if not media_to_transcribe:
                print("Local transcription skipped: no newly downloaded media files found.")
                return 2

            before_transcripts = {p.resolve() for p in script_dir.glob("*.txt")}
            local_cmd = [
                sys.executable,
                str(LOCAL_WHISPER_WRAPPER),
                *[str(p) for p in media_to_transcribe],
                "--output-dir",
                str(script_dir),
                "--vad",
                "--word-timestamps",
            ]
            if args.local_language:
                local_cmd += ["--language", args.local_language]
            if args.local_device:
                local_cmd += ["--device", args.local_device]
            local_proc = run(local_cmd)
            print(local_proc.stdout)
            if local_proc.returncode != 0:
                print(local_proc.stderr)
                return local_proc.returncode

            after_transcripts = {p.resolve() for p in script_dir.glob("*.txt")}
            new_transcripts = sorted(after_transcripts - before_transcripts)
            for row in selected:
                video_id = row.get("id") or ""
                matched = None
                if video_id:
                    matched = next((p for p in new_transcripts if video_id in p.name), None)
                if not matched:
                    title_slug = slugify(row.get("title") or "", 60)
                    matched = next((p for p in new_transcripts if title_slug and title_slug[:30] in slugify(p.stem, 180)), None)
                if matched:
                    row["local_transcript_status"] = "saved"
                    row["local_transcript_path"] = str(matched.relative_to(ROOT))
                    if not row.get("transcript_path"):
                        row["transcript_path"] = row["local_transcript_path"]
                        row["transcript_status"] = "saved_local"
                else:
                    row["local_transcript_status"] = "not_matched"

            payload["selected"] = selected
            (out_dir / "manifest.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
            write_csv(out_dir / "manifest.csv", selected)

    if args.update_index:
        append_research_index(DEFAULT_INDEX, selected)

    print(f"Scanned videos: {len(all_rows)}")
    print(f"Selected videos: {len(selected)}")
    print(f"Manifest: {out_dir / 'manifest.csv'}")
    print(f"Links: {links_dir}")
    if not args.no_transcript:
        saved = sum(1 for row in selected if row.get("transcript_status") == "saved")
        print(f"Transcripts saved: {saved}")
    if args.download_video:
        print(f"Media: {media_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
