import csv
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs" / "finance_influencer_videos"
RAW_DIR = OUT_DIR / "raw"


PEOPLE = [
    {
        "name": "Dave Ramsey",
        "platform": "YouTube",
        "profile_url": "https://www.youtube.com/@TheRamseyShow/videos",
        "note": "Official Ramsey Show channel; Facebook has high reach but video view extraction is not reliable without account/API access.",
    },
    {
        "name": "Robert Kiyosaki",
        "platform": "YouTube",
        "profile_url": "https://www.youtube.com/@TheRichDadChannel/videos",
        "note": "Official Rich Dad channel.",
    },
    {
        "name": "Ankur Warikoo",
        "platform": "YouTube",
        "profile_url": "https://www.youtube.com/@warikoo/videos",
        "note": "Large finance/career creator in India.",
    },
    {
        "name": "Pranjal Kamra",
        "platform": "YouTube",
        "profile_url": "https://www.youtube.com/@PranjalKamra/videos",
        "note": "Investing education channel.",
    },
    {
        "name": "CA Rachana Ranade",
        "platform": "YouTube",
        "profile_url": "https://www.youtube.com/@CARachanaRanade/videos",
        "note": "Chartered accountant and stock-market education creator.",
    },
    {
        "name": "Graham Stephan",
        "platform": "YouTube",
        "profile_url": "https://www.youtube.com/@GrahamStephan/videos",
        "note": "Personal finance and real-estate creator.",
    },
    {
        "name": "Thai Pham",
        "platform": "YouTube",
        "profile_url": "https://www.youtube.com/@thaiphamofficialvn/videos",
        "note": "Vietnamese finance/investing creator.",
    },
    {
        "name": "Hieu TV",
        "platform": "YouTube",
        "profile_url": "https://www.youtube.com/@hieu-tv/videos",
        "note": "Vietnamese personal-finance podcast/channel.",
    },
    {
        "name": "Erika Kullberg",
        "platform": "YouTube",
        "profile_url": "https://www.youtube.com/@Erika2/videos",
        "note": "Also very large on TikTok/Instagram; YouTube metadata is used where accessible.",
    },
    {
        "name": "Mark Tilbury",
        "platform": "YouTube",
        "profile_url": "https://www.youtube.com/@MarkTilbury/videos",
        "note": "Also large on TikTok; YouTube metadata is used where accessible.",
    },
    {
        "name": "Humphrey Yang",
        "platform": "YouTube",
        "profile_url": "https://www.youtube.com/@humphrey/videos",
        "note": "Also large on TikTok; YouTube metadata is used where accessible.",
    },
    {
        "name": "Tatiana London",
        "platform": "TikTok",
        "profile_url": "https://www.tiktok.com/@tatlondono",
        "note": "TikTok profile. Public top-by-view extraction often requires browser/session access.",
    },
    {
        "name": "Vivian Tu / Your Rich BFF",
        "platform": "TikTok",
        "profile_url": "https://www.tiktok.com/@yourrichbff",
        "note": "TikTok profile. Public top-by-view extraction often requires browser/session access.",
    },
    {
        "name": "Bàn Luận Tài Chính",
        "platform": "TikTok",
        "profile_url": "https://www.tiktok.com/@banluantaichinh",
        "note": "Vietnamese TikTok finance/current-affairs account. Requires manual verification if TikTok blocks scraping.",
    },
]


def slugify(value: str) -> str:
    value = re.sub(r"[^\w\s.-]", "", value, flags=re.UNICODE).strip().lower()
    value = re.sub(r"[\s_]+", "-", value)
    return value or "unknown"


def run_yt_dlp(url: str, limit: int | None) -> list[dict]:
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
    cmd.append(url)

    proc = subprocess.run(
        cmd,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        errors="replace",
    )

    videos = []
    for line in proc.stdout.splitlines():
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            continue
        if item.get("_type") == "playlist":
            continue
        videos.append(
            {
                "title": item.get("title") or "",
                "url": item.get("webpage_url") or item.get("original_url") or "",
                "view_count": item.get("view_count"),
                "like_count": item.get("like_count"),
                "upload_date": item.get("upload_date") or "",
                "duration": item.get("duration"),
            }
        )

    return videos


def write_csv(path: Path, rows: list[dict]) -> None:
    fields = [
        "person",
        "platform",
        "rank",
        "title",
        "url",
        "view_count",
        "like_count",
        "upload_date",
        "duration",
        "profile_url",
        "status",
        "scope",
        "note",
    ]
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    # Full-channel extraction can be slow for multi-thousand-video channels.
    # Default to all videos; pass an integer argument to cap per channel.
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else None
    scope = f"top_by_view_within_latest_{limit}_youtube_videos" if limit else "top_by_view_full_channel_metadata"
    collected_at = datetime.now(timezone.utc).isoformat()
    manifest = []
    summary = []

    for person in PEOPLE:
        person_dir = OUT_DIR / slugify(person["name"])
        person_dir.mkdir(exist_ok=True)

        if person["platform"] == "YouTube":
            videos = run_yt_dlp(person["profile_url"], limit)
            raw_path = RAW_DIR / f"{slugify(person['name'])}.json"
            raw_path.write_text(
                json.dumps(
                    {
                        "person": person,
                        "collected_at": collected_at,
                        "limit": limit,
                        "videos": videos,
                    },
                    ensure_ascii=False,
                    indent=2,
                ),
                encoding="utf-8",
            )
            videos = [v for v in videos if isinstance(v.get("view_count"), int)]
            videos.sort(key=lambda v: v["view_count"], reverse=True)
            top = videos[:3]
            if top:
                for idx, video in enumerate(top, start=1):
                    row = {
                        "person": person["name"],
                        "platform": person["platform"],
                        "rank": idx,
                        "title": video["title"],
                        "url": video["url"],
                        "view_count": video["view_count"],
                        "like_count": video["like_count"],
                        "upload_date": video["upload_date"],
                        "duration": video["duration"],
                        "profile_url": person["profile_url"],
                        "status": "metadata_collected",
                        "scope": scope,
                        "note": person["note"],
                    }
                    manifest.append(row)
                    (person_dir / f"{idx:02d}_{slugify(video['title'])}.url").write_text(
                        f"[InternetShortcut]\nURL={video['url']}\n",
                        encoding="utf-8",
                    )
            else:
                manifest.append(
                    {
                        "person": person["name"],
                        "platform": person["platform"],
                        "rank": "",
                        "title": "",
                        "url": person["profile_url"],
                        "view_count": "",
                        "like_count": "",
                        "upload_date": "",
                        "duration": "",
                        "profile_url": person["profile_url"],
                        "status": "no_public_video_metadata_returned",
                        "scope": scope,
                        "note": person["note"],
                    }
                )
            summary.append({"person": person["name"], "videos_found": len(videos)})
        else:
            manifest.append(
                {
                    "person": person["name"],
                    "platform": person["platform"],
                    "rank": "",
                    "title": "",
                    "url": person["profile_url"],
                    "view_count": "",
                    "like_count": "",
                    "upload_date": "",
                    "duration": "",
                    "profile_url": person["profile_url"],
                    "status": "manual_verification_required",
                    "scope": "profile_link_only_no_reliable_public_top_by_view_extraction",
                    "note": person["note"],
                }
            )
            (person_dir / "profile.url").write_text(
                f"[InternetShortcut]\nURL={person['profile_url']}\n",
                encoding="utf-8",
            )
            summary.append({"person": person["name"], "videos_found": 0})

    write_csv(OUT_DIR / "videos.csv", manifest)
    (OUT_DIR / "videos.json").write_text(
        json.dumps(
            {
                "collected_at": collected_at,
                "downloaded_video_files": False,
                "reason": "Only link and public metadata were collected to avoid unauthorized copying of copyrighted platform videos.",
                "limit": limit,
                "summary": summary,
                "items": manifest,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    (OUT_DIR / "README.md").write_text(
        "# Finance influencer video manifest\n\n"
        f"Collected at: `{collected_at}`\n\n"
        "This folder contains public links and metadata only. It does not contain downloaded video files.\n\n"
        f"Collection scope: `{scope}` for YouTube rows.\n\n"
        "- `videos.csv`: spreadsheet-friendly manifest.\n"
        "- `videos.json`: structured manifest.\n"
        "- `raw/`: raw metadata collected from YouTube via yt-dlp.\n"
        "- Each person folder contains `.url` shortcuts for available top videos or profile pages.\n\n"
        "Rows marked `manual_verification_required` need browser/API access because TikTok, Instagram, or Facebook did not expose reliable top-by-view data through public unauthenticated extraction.\n",
        encoding="utf-8",
    )

    print(f"Wrote {OUT_DIR}")
    print(f"Rows: {len(manifest)}")


if __name__ == "__main__":
    main()
