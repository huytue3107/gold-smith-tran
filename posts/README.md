# Posts

Thư mục này chứa bài viết hoàn chỉnh hoặc gần hoàn chỉnh cho Gold Smith Tran.

## Cấu Trúc Khuyến Nghị

Bài text-only có thể lưu trực tiếp:

```text
posts/YYYY-MM-DD-slug.md
```

Dung `posts/_template.md` lam mau khi tao bai moi.

Bài có visual nên lưu trong thư mục riêng:

```text
posts/001-ten-bai/
├── post.md
├── image.png
├── carousel.pdf
├── carousel-slides/
├── content.json
└── source-notes.md
```

## Format `post.md`

```markdown
# Bài NNN: Tiêu Đề

**Ngày đăng:** DD/MM/YYYY - slot TBD
**Platform:** Facebook, Threads, Video ngắn
**Persona:** F0 / Gen Z-Millennials / Gia đình trẻ / Founder-Fintech
**Mục tiêu:** Trust / Save / Comment / Inbox / Community
**Phương pháp:** Tin nóng / Pain Point / Viral Replication / Series / Q&A
**Visual:** Text-only / Ảnh cá nhân / Infographic / Carousel / Quote

---

## Post Text

[Nội dung copy-paste ready]

---

## Hook Options

1. ...
2. ...
3. ...

---

## CTA Options

1. ...
2. ...
3. ...

---

## Image Notes

[Ý tưởng visual hoặc prompt]
```

## Tiêu Chuẩn

- Không dùng markdown heading trong phần copy-paste nếu nền tảng đăng không hỗ trợ.
- Mỗi đoạn 1-3 câu.
- Câu quan trọng có thể đứng riêng một dòng.
- Bài đầu tư phải có rủi ro, điểm sai hoặc quản trị vốn.
- Không cam kết lợi nhuận, không phím lệnh, không tạo FOMO mù quáng.

## Dashboard

Sau khi thêm bài mới:

```bash
python scripts/build-dashboard.py
```

Dashboard sẽ được tạo tại `outputs/dashboard.html`.

Truoc khi publish, co the chay:

```bash
python scripts/validate-content-safety.py posts
```
