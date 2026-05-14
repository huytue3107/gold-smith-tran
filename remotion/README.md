# Gold Smith Remotion Video Pipeline

Render video tài chính cho Gold Smith Tran bằng React + Remotion.

## Cài đặt lần đầu

```bash
cd remotion
npm install
```

Cần Node ≥18. Lần đầu npm install có thể tải ~500MB (Remotion compositor native + Chromium).

## Lệnh chính

```bash
# Studio (preview real-time)
npm start

# Render composition mặc định ra out/market-reading.mp4
npm run build

# Render với brief tuỳ chỉnh
npx remotion render src/index.ts MarketReading out/<slug>.mp4 \
  --props=briefs/<slug>.json
```

## Compositions có sẵn

| ID              | Duration | Aspect             | Mục đích                                          |
| --------------- | -------- | ------------------ | ------------------------------------------------- |
| `MarketReading` | 60s      | 1080x1920 vertical | "Một phút đọc thị trường" cho TikTok/Reels/Shorts |

## License

**Free License** — Gold Smith Tran ở quy mô cá nhân / ≤3 nhân viên đủ điều kiện dùng miễn phí.
Nếu quy mô tăng ≥4 nhân viên (for-profit), phải mua Company License: https://remotion.dev/license

## Cấu trúc

```
remotion/
├── package.json
├── tsconfig.json
├── remotion.config.ts
├── src/
│   ├── index.ts            # Register root
│   ├── Root.tsx            # Composition registry
│   └── compositions/
│       └── market-reading/
│           ├── MarketReading.tsx   # Component video
│           └── schema.ts            # Zod brief schema
├── briefs/                  # JSON briefs per asset
│   ├── schema.md            # Hướng dẫn viết brief
│   └── *.json
└── out/                     # Rendered MP4 (gitignored)
```

## Pipeline tích hợp

```
posts/<slug>.md (bài Facebook đã pass Evidence Gate)
        ↓
brief từ bài (manual hoặc qua /create-video command)
        ↓
remotion/briefs/<slug>.json
        ↓
npx remotion render → remotion/out/<slug>.mp4
        ↓
copy/move → outputs/video-scripts/<slug>/final.mp4
        ↓
update outputs/content-ledger.md với Format=Video 60s, Status=Published
```

Chi tiết brief format: xem `briefs/schema.md`.
