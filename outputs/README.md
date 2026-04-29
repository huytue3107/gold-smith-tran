# Outputs

Thư mục này chứa file làm việc được tạo ra trong quá trình vận hành hệ thống nội dung Gold Smith.

## Nội Dung Thường Gặp

| File/Folder | Được tạo bởi | Mô tả |
| --- | --- | --- |
| `dashboard.html` | `scripts/build-dashboard.py` | Dashboard tổng hợp bài trong `posts/` |
| `YYYY-MM-DD-batch-content-plan.md` | `/create-10-posts` | Kế hoạch batch nhiều bài |
| `YYYY-MM-DD-content-ideas.md` | Content ideation | Ý tưởng bài theo persona/trụ cột |
| `classified.json` | `scripts/classify-emails.py` | Kết quả phân loại email nếu dùng Gmail workflow |

## Xem Dashboard

```bash
python scripts/build-dashboard.py
start outputs/dashboard.html
```

## Quy Ước

- `outputs/` là nơi chứa file làm việc, không phải nguồn sự thật.
- Bài cuối cùng hoặc bài sẵn sàng đăng phải nằm trong `posts/`.
- Có thể xóa output cũ nếu không còn cần.
