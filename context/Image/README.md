# Ảnh Cá Nhân

Thư mục này chứa ảnh cá nhân dùng trong posts. Ảnh cá nhân giúp tăng độ tin cậy và kết nối với audience.

## Khi Nào Dùng Ảnh Cá Nhân

- Bài học/kinh nghiệm cá nhân
- Hậu trường, sự kiện
- Cập nhật công ty/dự án
- Chia sẻ quan điểm, góc nhìn founder

## Cách Thêm Ảnh

1. Đặt ảnh vào thư mục này với tên mô tả rõ ràng
2. Dùng định dạng `.jpg` hoặc `.png`
3. Độ phân giải tối thiểu: 1080x1080px (vuông) hoặc 1080x1350px (portrait)

**Gợi ý đặt tên:**

```
at-desk-working.jpg
casual-outdoor.jpg
speaking-event.jpg
headshot-professional.jpg
```

## Quy Trình Thêm Text Overlay

Sau khi chọn ảnh phù hợp với bài post, chạy script overlay để thêm text hook:

```bash
python3 scripts/add-photo-overlay.py \
  --photo context/images/TEN-ANH.jpg \
  --text "Hook text ngắn gọn, tối đa ~12 từ" \
  --highlight "TỪ KHÓA" "CON SỐ" \
  --output posts/NNN-slug/image.png \
  --position bottom
```

- `--highlight`: những từ sẽ được tô màu accent vàng kim `#C6A15B`
- `--position`: `bottom` (mặc định) | `top` | `center`
- Không overlay lên mặt người — chọn position tránh vùng mặt
