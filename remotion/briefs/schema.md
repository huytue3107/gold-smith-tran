# Brief Schema — Remotion Video Input

Mọi video Remotion của Gold Smith nhận brief dạng JSON tại `briefs/YYYY-MM-DD-slug.json`.

## Required fields

| Field      | Type   | Constraint                                             | Mô tả                                                              |
| ---------- | ------ | ------------------------------------------------------ | ------------------------------------------------------------------ |
| `slug`     | string | kebab-case                                             | ID asset, match với `outputs/content-ledger.md`                    |
| `date`     | string | YYYY-MM-DD                                             | Ngày sản xuất                                                      |
| `persona`  | enum   | F0 / GenZ-Millennial / PhuNu-GiaDinh / Founder-Fintech | Target ICP                                                         |
| `pillar`   | string | match strategy.md                                      | Trụ cột nội dung                                                   |
| `hook`     | string | 8-120 char                                             | Câu hook 3s đầu — lấy/chỉnh từ `1000_hook_short_form_tai_chinh.md` |
| `context`  | string | ≤ 220 char                                             | Bối cảnh 5-25s                                                     |
| `takeaway` | string | ≤ 180 char                                             | Câu chốt 25-50s — phải đáng lưu                                    |
| `cta`      | string | ≤ 80 char                                              | CTA mềm 50-60s                                                     |

## Optional fields (có default)

| Field              | Default                                                          |
| ------------------ | ---------------------------------------------------------------- |
| `brandMark`        | `"GOLD SMITH TRAN — NHA GIA KIM TAI CHINH"`                      |
| `safetyDisclaimer` | `"Khong phai khuyen nghi dau tu. Quan tri von la viec cua ban."` |

## Tổng độ dài

Composition `MarketReading`: **60s** (1800 frames @ 30fps).

Cấu trúc đã hardcode trong `src/compositions/market-reading/MarketReading.tsx`:

- 0-5s: Hook
- 5-25s: Context
- 25-50s: Takeaway
- 50-60s: CTA + Safety disclaimer

## Cách tạo brief từ bài Facebook

1. Đọc bài Facebook trong `posts/`.
2. Xác định câu đáng nhớ nhất → `takeaway`.
3. Tìm hook từ bài hoặc lấy từ `1000_hook_short_form_tai_chinh.md`.
4. Rút gọn bối cảnh xuống ≤220 ký tự → `context`.
5. Lấy CTA mềm từ bài (hoặc 1 trong 3 CTA alternatives).
6. Lưu brief vào `remotion/briefs/<slug>.json`.
7. Update `outputs/content-ledger.md`: Format = `Video 60s`, Status = `Draft`.
