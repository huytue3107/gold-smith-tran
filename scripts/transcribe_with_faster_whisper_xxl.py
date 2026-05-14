#!/usr/bin/env python3
"""
Run the local Faster-Whisper-XXL portable app for Gold Smith transcripts.

The app itself stays outside the repo. This wrapper makes the Gold Smith
workspace able to transcribe downloaded/local media into reference/Scripts.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_HOME = ROOT / "tools" / "Faster-Whisper-XXL"
EXTERNAL_HOME = Path(r"D:\Faster-Whisper-XXL_r245.4_windows\Faster-Whisper-XXL")
DEFAULT_HOME = Path(os.environ["FASTER_WHISPER_XXL_HOME"]) if os.environ.get("FASTER_WHISPER_XXL_HOME") else (
    WORKSPACE_HOME if WORKSPACE_HOME.exists() else EXTERNAL_HOME
)
DEFAULT_EXE = DEFAULT_HOME / "faster-whisper-xxl.exe"
DEFAULT_OUTPUT_DIR = ROOT / "reference" / "Scripts"


MEDIA_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".m4a",
    ".aac",
    ".flac",
    ".ogg",
    ".opus",
    ".mp4",
    ".mov",
    ".mkv",
    ".webm",
    ".avi",
}


def resolve_workspace_path(value: str) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return ROOT / path


def collect_media(paths: list[str]) -> list[Path]:
    media: list[Path] = []
    for raw in paths:
        path = resolve_workspace_path(raw)
        if path.is_file() and path.suffix.lower() in MEDIA_EXTENSIONS:
            media.append(path)
        elif path.is_dir():
            media.extend(
                p for p in sorted(path.rglob("*")) if p.is_file() and p.suffix.lower() in MEDIA_EXTENSIONS
            )
    return sorted(set(media))


def main() -> int:
    parser = argparse.ArgumentParser(description="Transcribe media with Faster-Whisper-XXL.")
    parser.add_argument("media", nargs="+", help="Media file(s) or folder(s). Relative paths resolve from workspace root.")
    parser.add_argument("--exe", default=str(DEFAULT_EXE), help="Path to faster-whisper-xxl.exe.")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help="Transcript output directory.")
    parser.add_argument("--model", default="large-v2", help="Whisper model name.")
    parser.add_argument("--language", default="", help="Language code, e.g. vi/en/zh. Empty means auto detect.")
    parser.add_argument("--task", choices=["transcribe", "translate"], default="transcribe")
    parser.add_argument("--device", default="", help="cuda/cpu/cuda:1. Empty uses app default.")
    parser.add_argument("--compute-type", default="auto", help="auto/int8/float16/float32/etc.")
    parser.add_argument("--format", nargs="+", default=["txt", "srt"], help="Output formats: txt srt vtt json all.")
    parser.add_argument("--vad", action="store_true", help="Enable Silero VAD defaults.")
    parser.add_argument("--word-timestamps", action="store_true", help="Enable word timestamps.")
    parser.add_argument("--batch-recursive", action="store_true", help="Let XXL batch process directories recursively.")
    args = parser.parse_args()

    exe = Path(args.exe)
    if not exe.exists():
        print(f"Faster-Whisper-XXL executable not found: {exe}", file=sys.stderr)
        print("Set FASTER_WHISPER_XXL_HOME or pass --exe.", file=sys.stderr)
        return 2

    media = collect_media(args.media)
    if not media:
        print("No supported media files found.", file=sys.stderr)
        return 2

    output_dir = resolve_workspace_path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    cmd = [str(exe), *[str(p) for p in media]]
    cmd += ["--model", args.model]
    cmd += ["--task", args.task]
    cmd += ["--compute_type", args.compute_type]
    cmd += ["--output_dir", str(output_dir)]
    cmd += ["-f", *args.format]
    cmd += ["--print_progress"]

    if args.language:
        cmd += ["--language", args.language]
    if args.device:
        cmd += ["--device", args.device]
    if args.vad:
        cmd += [
            "--vad_method",
            "silero_v4_fw",
            "--vad_min_silence_duration_ms",
            "250",
            "--vad_speech_pad_ms",
            "80",
        ]
    if args.word_timestamps:
        cmd += ["--word_timestamps", "True"]
    if args.batch_recursive:
        cmd += ["--batch_recursive"]

    print(f"Media files: {len(media)}")
    print(f"Output dir: {output_dir}")
    print("Running Faster-Whisper-XXL...")

    proc = subprocess.run(
        cmd,
        cwd=exe.parent,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
