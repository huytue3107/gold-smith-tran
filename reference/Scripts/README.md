# Transcript Reference Bank

Thu muc nay chua transcript video tai chinh, kinh doanh, personal finance va creator references.

Day la **reference phu**, khong phai voice chinh cua Gold Smith. Khi dung transcript, chi lay:

- Hook mechanics.
- Cach mo van de.
- Cau truc giai thich.
- Vi du/case co the kiem chung.
- Y tuong format video.

Khong lay:

- Loi hua loi nhuan.
- Buy/sell signal.
- Claim chua co nguon.
- Persona/voice cua creator khac.
- CTA ban hang qua manh.

## Cach Dung

Moi transcript nen duoc bien thanh idea theo khung:

```markdown
## Source

- **File:**
- **Creator/source:**
- **Topic:**
- **Hook type:**
- **Persona fit:** F0 / Gen Z-Millennials / Family / Founder-Fintech
- **Gold Smith pillar:**
- **Reusable angle:**
- **Safety risk:**
- **Suggested format:** Facebook / Threads / 15s / 30s / 45s / 60s / Carousel
```

Ket qua research nen luu vao:

```text
outputs/research-index.md
```

Tu dong lay transcript/script bang:

```bash
python scripts/research_viral_videos.py --limit 20 --top 10 --update-index
```

Script se uu tien subtitle/transcript cong khai. Neu video khong co subtitle, file transcript se duoc danh dau `not_found` trong manifest.

Neu da co file audio/video local, dung Faster-Whisper-XXL:

```bash
python scripts/transcribe_with_faster_whisper_xxl.py "path/to/media.mp4" --language vi --device cuda --vad --word-timestamps
```

## Safety Rule

Neu transcript co so lieu, su kien, du bao, gia, loi nhuan, thanh tich hoac claim ve thi truong, phai xac minh lai truoc khi dua vao bai Gold Smith.
