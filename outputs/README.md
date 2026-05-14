# Outputs

Thư mục này chứa file làm việc được tạo ra trong quá trình vận hành hệ thống nội dung Gold Smith.

## Nội Dung Thường Gặp

| File/Folder                        | Được tạo bởi                       | Mô tả                                           |
| ---------------------------------- | ---------------------------------- | ----------------------------------------------- |
| `dashboard.html`                   | `scripts/build-dashboard.py`       | Dashboard tổng hợp bài trong `posts/`           |
| `YYYY-MM-DD-batch-content-plan.md` | `/create-10-posts`                 | Kế hoạch batch nhiều bài                        |
| `YYYY-MM-DD-content-ideas.md`      | Content ideation                   | Ý tưởng bài theo persona/trụ cột                |
| `video-scripts/`                   | Video workflow                     | Script TikTok/Reels/Shorts theo Gold Smith      |
| `viral_video_research/`            | `scripts/research_viral_videos.py` | Metadata, links, transcript raw, optional media |
| `content-ledger.md`                | Weekly review                      | Theo dõi asset, status, experiment và metrics   |
| `research-index.md`                | Research workflow                  | Idea đã score từ transcript/influencer videos   |
| `classified.json`                  | `scripts/classify-emails.py`       | Kết quả phân loại email nếu dùng Gmail workflow |

## Xem Dashboard

```bash
python scripts/build-dashboard.py
start outputs/dashboard.html
```

## Quy Ước

- `outputs/` là nơi chứa file làm việc, không phải nguồn sự thật.
- Bài cuối cùng hoặc bài sẵn sàng đăng phải nằm trong `posts/`.
- Script video ngắn nằm trong `outputs/video-scripts/` cho tới khi có workflow publish riêng.
- Viral/high-view video research nam trong `outputs/viral_video_research/`.
- Downloaded media, neu co, chi la working file tam thoi va khong nen commit.
- Mọi asset quan trọng nên được ghi vào `outputs/content-ledger.md`.
- Có thể xóa output cũ nếu không còn cần.
