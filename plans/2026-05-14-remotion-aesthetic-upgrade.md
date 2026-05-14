# 0001 Remotion Aesthetic Upgrade + ElevenLabs Voice-Over

**Date:** 2026-05-14
**Status:** Proposed → Approved (Option A — full sprint)
**Owner:** Gold Smith Tran workspace
**Inspiration:** ADR template from `harness-experimental` repo

---

## Context

`remotion/` v0 (commit `9cd3092`) chạy đúng nhưng thẩm mỹ ở cấp 2-3/10:

- Nền phẳng `#F5F3EE`, không texture/atmosphere.
- Text fade-up đơn giản, không kinetic typography.
- Không transition giữa sequences (jump cut).
- Không có visual element ngoài chữ (không shape, không chart, không icon).
- Không có audio (music + voice-over).
- 1 composition duy nhất (`MarketReading` 60s), không variety theo độ dài.

Gold Smith là thương hiệu tài chính "thực chiến, sắc bén, có chiều sâu" — output video hiện tại trông như default PowerPoint, không khớp positioning.

Đồng thời, user cung cấp **ElevenLabs API key** để bổ sung voice-over tự động, giảm phụ thuộc vào ghi giọng người.

---

## Decision

Adopt **Option A — Full sprint upgrade** (~8-10h work) thay vì MVP polish, vì user đã commit đầu tư bằng cách cấp ElevenLabs API. Mục tiêu output level 7-8/10, đủ chuyên nghiệp cho TikTok/Reels/Shorts của thương hiệu tài chính.

---

## Alternatives Considered

1. **Option B — MVP polish (3-4h):** Chỉ làm Phase 1+2 + 3 component. Đẹp hơn 70% mà không over-engineering. **Loại** vì user chọn full sprint.
2. **Option C — Wait for data:** Render 5-10 video với template hiện tại, đo engagement trước. **Loại** vì có sẵn budget upgrade.
3. **Adobe After Effects / CapCut Pro manual:** **Loại** vì mất khả năng programmatic, không scale, không version control.
4. **Manim (Python):** **Loại** — math-focused, không phù hợp finance/lifestyle.

---

## Phase Plan

### Phase 1 — Foundation packages (1-2h)

Install ecosystem packages vào `remotion/`:

```bash
cd remotion
npm install \
  @remotion/transitions \
  @remotion/shapes \
  @remotion/paths \
  @remotion/google-fonts \
  @remotion/zod-types \
  @remotion/noise \
  @remotion/media-utils \
  @remotion/elevenlabs
```

Plus Tailwind v4 (optional, decide during impl):

```bash
npm install @remotion/tailwind-v4 tailwindcss@4
```

**Deliverable:** Updated `package.json` + lock file. No code changes yet.

### Phase 2 — Background + Brand layer (2h)

Build foundational visual components:

| File                                      | Purpose                                                                                                                      |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `src/components/BackgroundAtmosphere.tsx` | Mesh gradient (3-4 spots, opacity 0.05-0.1) + Perlin noise (opacity 0.03, animated) + grid overlay (1px lines, opacity 0.04) |
| `src/components/BrandBar.tsx`             | Bottom-anchored: "GST" mark + "GOLD SMITH TRAN — NHA GIA KIM FOREX" + pillar tag với animated accent dot                     |
| `src/components/SafeZone.tsx`             | Padding wrapper tránh crop zone của TikTok/Reels (top 200px UI, bottom 280px UI)                                             |

**Deliverable:** 3 components + isolated test in studio.

### Phase 3 — Component library (2-3h)

Reusable building blocks cho mọi composition:

| File                                    | Purpose                                                            |
| --------------------------------------- | ------------------------------------------------------------------ |
| `src/components/KineticText.tsx`        | Word-by-word reveal với spring, stagger 4 frames                   |
| `src/components/AnimatedNumber.tsx`     | Counter cho %, $, VND với spring physics                           |
| `src/components/SparklineChart.tsx`     | Mini SVG path chart từ array data (cho phân tích thị trường)       |
| `src/components/AccentBar.tsx`          | Left border vàng có animation vẽ (path-draw)                       |
| `src/components/PillarTag.tsx`          | Top-center pillar label, uppercase, accent vàng                    |
| `src/components/Disclaimer.tsx`         | Chuẩn hoá safety footer text với fade-in                           |
| `src/components/SequenceTransition.tsx` | Wrapper áp dụng `@remotion/transitions` (fade + slide) giữa scenes |

**Deliverable:** 7 components, mỗi cái có default props demo trong studio.

### Phase 4 — Composition variety (2-3h)

5 compositions cho 5 độ dài theo `Gold-Smith-video.md`:

| ID                | Duration | Frames @30fps | Use case                                 |
| ----------------- | -------- | ------------- | ---------------------------------------- |
| `MarketReading15` | 15s      | 450           | Hook + 1 dữ kiện + CTA mềm (teaser)      |
| `MarketReading30` | 30s      | 900           | + 1 framework nhỏ (cảnh báo nhanh)       |
| `MarketReading45` | 45s      | 1350          | + ví dụ + nguyên tắc (default, phổ biến) |
| `MarketReading60` | 60s      | 1800          | + góc chuyên gia + dữ kiện vĩ mô         |
| `MarketReading90` | 90s      | 2700          | + tình huống case study + bài học series |

Mỗi composition reuse component library. Zod schema riêng nhưng share base schema fields (hook, takeaway, cta, persona, pillar).

Update `Root.tsx` để register cả 5 compositions.

**Deliverable:** 5 composition files + updated brief schema docs.

### Phase 5 — ElevenLabs voice-over integration (1-2h)

Brief mở rộng để optional add VO:

```typescript
{
  ...existingFields,
  voiceOver: {
    enabled: boolean,
    voiceId: string,       // ElevenLabs voice ID, default Vietnamese voice
    stability: 0.5,
    similarityBoost: 0.75,
    style: 0.4,            // 0-1, 0.4 cho tone "thực chiến tỉnh táo"
  }
}
```

Tạo `scripts/generate-voiceover.py`:

- Input: brief JSON path.
- Build script text từ hook + context + takeaway + cta.
- Call ElevenLabs API → MP3 → save to `remotion/public/audio/<slug>.mp3`.
- Brief tự động reference audio file path.

Tạo `src/components/VoiceOver.tsx` dùng `<Audio>` của Remotion để embed MP3 vào composition.

Audio ducking: background music opacity 0.6 → 0.2 khi VO chạy.

**Deliverable:**

- Python script + ElevenLabs API integration.
- VoiceOver component.
- Updated brief schema + docs.

### Phase 6 — Audio + music (1h, optional)

- Chọn 3 background music track license-free từ Pixabay/Uppbeat.
- Lưu vào `remotion/public/audio/bg/`.
- Brief field `backgroundMusic: 'minimal' | 'tense' | 'reflective' | 'none'`.
- Auto-duck volume khi VO present.

**Deliverable:** 3 MP3 + Music component wrapper.

---

## ElevenLabs Configuration

**API Key:** Stored in `.env` as `ELEVENLABS_API_KEY` (gitignored). Never commit.

**Recommended Vietnamese voices** (verify lúc impl):

- Multilingual v2 model hỗ trợ tiếng Việt tốt.
- Test 3 voices: 1 nam trầm (Gold Smith narrator chính), 1 nam trung (variety), 1 nữ trầm (cho persona Phụ nữ/gia đình).

**Pricing budget:**

- Free tier: 10k chars/month.
- Starter $5/month: 30k chars.
- Creator $22/month: 100k chars.
- 1 video 60s ≈ 200-250 chars VO → Free tier đủ cho 40 video/month.

**Caching strategy:** MP3 đã render lưu vào `remotion/public/audio/<slug>.mp3`, không re-generate trừ khi brief thay đổi hash.

---

## Style Decisions

### Typography hierarchy

| Element    | Font weight        | Size | Notes                   |
| ---------- | ------------------ | ---- | ----------------------- |
| Hook       | Be Vietnam Pro 800 | 96px | Leading 1.05            |
| Context    | Be Vietnam Pro 500 | 52px | Leading 1.4             |
| Takeaway   | Be Vietnam Pro 700 | 72px | Left border vàng accent |
| CTA        | Be Vietnam Pro 600 | 44px | Mềm, không lệnh         |
| Disclaimer | Be Vietnam Pro 400 | 22px | Muted, italic           |
| Brand bar  | Be Vietnam Pro 500 | 18px | Letter-spacing 4        |
| Pillar tag | Be Vietnam Pro 600 | 16px | Uppercase, accent vàng  |

### Motion language

- Hook: word-by-word reveal, stagger 4 frames, spring damping 12.
- Context: block fade + slide-up 60px, 600ms ease-out.
- Takeaway: border-left vàng vẽ trước (path-draw 15 frames), text reveal sau.
- Number/percentage: counter spring physics.
- Transitions: `fade` 15 frames giữa sequences chính, `slide` cho takeaway.
- Brand bar: always-on, accent dot pulse subtle.

### Color system

Giữ nguyên palette từ `design.md`:

- Background base: `#F5F3EE`
- Mesh gradient spots: `#C6A15B` opacity 0.06, `#D4AF37` opacity 0.04
- Ink: `#151515`
- Accent: `#C6A15B` (vàng chính), `#D4AF37` (vàng phụ)
- Muted: `#6F6F6F`, `#A7A7A7`

Tránh: neon, tím công nghệ, screenshot lợi nhuận.

---

## Trade-offs

| Trade-off                                    | Decision                                                              |
| -------------------------------------------- | --------------------------------------------------------------------- |
| node_modules tăng ~30MB → 530MB              | Accept (đã gitignored)                                                |
| Render time +50-100% với transitions + noise | Accept; vẫn <2 phút cho 60s                                           |
| Code complexity 1 file → ~12 files           | Accept; có TypeScript guard                                           |
| Maintenance burden tăng                      | Mitigate bằng component library + Zod schema                          |
| ElevenLabs cost $5-22/tháng nếu vượt free    | Accept; budget thấp so với content team                               |
| Voice AI có thể "máy" hơn giọng người        | Mitigate: chọn voice phù hợp + style 0.4 + test 5 sample trước commit |

---

## Risks

| Risk                               | Likelihood                  | Impact | Mitigation                                                |
| ---------------------------------- | --------------------------- | ------ | --------------------------------------------------------- |
| ElevenLabs Vietnamese quality thấp | Med                         | High   | Test 3 voice trước; fallback ghi giọng người nếu fail     |
| Render time blocker khi batch      | Low                         | Med    | Phase 6 evaluate `@remotion/lambda`                       |
| Component library over-engineer    | Med                         | Low    | Strict YAGNI: chỉ build component nào dùng ≥2 composition |
| API key leak                       | High (đã expose trong chat) | High   | **Rotate sau khi commit plan**, dùng cái mới              |
| Tailwind v4 instability            | Low                         | Med    | Có thể skip Phase 1's Tailwind, dùng inline style         |

---

## Acceptance Criteria

Sprint xem là Done khi:

- [ ] 5 compositions render thành công cho 5 độ dài.
- [ ] Mỗi composition pass Zod schema validation.
- [ ] Background atmosphere không flash/glitch trong 60s render.
- [ ] Be Vietnam Pro load đúng cho cả latin + vietnamese subset.
- [ ] ElevenLabs VO generate được tiếng Việt từ brief JSON.
- [ ] VO sync với caption (caption hiện song song hoặc trước VO 1 frame).
- [ ] Output MP4 60s file size < 15MB (h264, yuv420p).
- [ ] Render time 60s < 2 phút trên máy hiện tại.
- [ ] Validator content-safety pass cho cả script text (no profit promise / no signal / no FOMO).
- [ ] `outputs/content-ledger.md` có 1 row mẫu Video 60s với metrics columns.

---

## Implementation Order

```
1. Phase 1 install packages       (1-2h)
2. Phase 2 background + brand     (2h)
3. Phase 3 component library      (2-3h)
4. Phase 4 5 compositions         (2-3h)
5. Phase 5 ElevenLabs VO          (1-2h)
6. Phase 6 background music       (1h, optional)
```

Mỗi phase commit riêng để dễ rollback. Tổng commit ước tính: 6-8.

---

## Out of Scope

- 3D effects (`@remotion/three`).
- Skia rendering (`@remotion/skia`).
- Lottie/Rive animations (chưa có asset).
- Multi-language render (chỉ tiếng Việt).
- AWS Lambda render scaling (chờ volume tăng).
- Auto-thumbnail generation.
- Auto-upload to TikTok/Meta API.

---

## Follow-up after sprint

Sau khi sprint xong, evaluate:

1. Render 5 video real từ 5 post hiện có trong `posts/`.
2. Đo feedback từ audience trong 7 ngày.
3. So sánh engagement vs baseline (no video).
4. Quyết định: scale với `@remotion/lambda` hoặc giữ local.

---

## Decision Log

| Date       | Decision                                               |
| ---------- | ------------------------------------------------------ |
| 2026-05-14 | Approve full sprint Option A. User cấp ElevenLabs key. |
| TBD        | Voice ID selection sau khi test 3 candidates.          |
| TBD        | Tailwind v4 keep/drop sau Phase 1.                     |

---

## Security Note

⚠️ ElevenLabs API key đã được paste trong chat trước khi vào `.env`. **Strongly recommend rotate key** sau khi sprint done:

1. Đăng nhập https://elevenlabs.io
2. Settings → API Keys → Revoke current → Create new
3. Update `.env`

Key hiện tại stored an toàn trong `.env` (gitignored), nhưng có khả năng đã bị log trong transcript.
