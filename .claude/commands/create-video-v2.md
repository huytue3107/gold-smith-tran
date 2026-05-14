# Create Video v2

Bien mot bai Gold Smith da pass Evidence Gate thanh video 60s Remotion.

## Input

`$ARGUMENTS` la duong dan toi bai trong `posts/`, hoac slug.

Vi du:

```text
/create-video-v2 posts/2026-04-28-ty-gia-usd.md
```

## Nguon Bat Buoc

1. `Gold-Smith-video.md` — voice video master.
2. `1000_hook_short_form_tai_chinh.md` — kho hook tham khao.
3. `.claude/rules/safety.md` — quy tac 1%.
4. `.claude/rules/red-flags-content.md`.
5. `remotion/briefs/schema.md` — brief format.
6. `remotion/src/compositions/market-reading/schema.ts` — Zod schema.
7. Bai goc trong `posts/<slug>.md`.

## Precondition Check (Evidence Gate)

Truoc khi tao video, bai goc PHAI:

- Da pass `python scripts/validate-content-safety.py <post-path>` (exit code 0).
- Da co entry trong `outputs/content-ledger.md` voi Status >= Reviewed.
- Da co metadata day du.

Neu chua, dung lai va goi `/review-content-v2` truoc.

## Pipeline

### 1. Generate draft brief

```bash
python scripts/brief-to-video.py posts/<slug>.md --persona <P> --pillar "<pillar>"
```

Output: `remotion/briefs/<slug>.json` (DRAFT).

### 2. Review brief

Doc lai brief va kiem:

- Hook ≤ 120 char, sac, khong giat tit.
- Context ≤ 220 char, fit 20s voice-over.
- Takeaway ≤ 180 char, dang nho.
- CTA ≤ 80 char, mem, mot muc tieu.
- Safety: khong cam ket loi, khong phiem lenh, khong FOMO.

Neu thay chua dat, chinh JSON va doc lai.

### 3. Preview trong studio (optional)

```bash
cd remotion && npm start
```

Mo studio o http://localhost:3000, chon composition `MarketReading`, doi props sang `briefs/<slug>.json`.

### 4. Render

```bash
cd remotion
npx remotion render src/index.ts MarketReading out/<slug>.mp4 --props=briefs/<slug>.json
```

### 5. Move + ledger update

```bash
mkdir -p outputs/video-scripts/<slug>
mv remotion/out/<slug>.mp4 outputs/video-scripts/<slug>/final.mp4
cp remotion/briefs/<slug>.json outputs/video-scripts/<slug>/brief.json
```

Then update `outputs/content-ledger.md`:

- Add row hoac update row hien co.
- Format: `Video 60s`.
- Status: `Published` (neu da dang) hoac `Ready` (neu cho dang).
- Asset path: `outputs/video-scripts/<slug>/final.mp4`.

## Output Format

```markdown
# Video Production Report

**Source post:** posts/<slug>.md
**Brief:** remotion/briefs/<slug>.json
**Output:** outputs/video-scripts/<slug>/final.mp4
**Duration:** 60s
**Composition:** MarketReading

## Brief Summary

- Hook: ...
- Context: ...
- Takeaway: ...
- CTA: ...

## Safety Check

- Validator: PASS (exit 0)
- Profit promise: none
- Blind signal: none
- FOMO: none
- Capital management note: present

## Next Steps

- Voice-over: <ghi am tu nguoi that hoac TTS — tuy chon>
- Upload: TikTok / Reels / Shorts
- Update content-ledger.md
```

## Khi nao KHONG dung

- Bai chua pass Evidence Gate.
- Bai khong phu hop format video (qua dai, qua nhieu nuance, can visual phuc tap).
- Cot noi dung khong phai "Mot phut doc thi truong", "F0 tra hoc phi", hoac "Triet hoc dau tu" — composition `MarketReading` toi uu cho 3 pillar nay.

Voi pillar khac, tao composition moi truoc trong `remotion/src/compositions/`.
