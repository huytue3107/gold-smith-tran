---
description: 5 lớp an toàn bắt buộc khi viết nội dung tài chính
globs:
alwaysApply: true
---

# An toàn nội dung tài chính

## 5 lớp an toàn bắt buộc

Mọi nội dung tài chính phải giữ 5 lớp an toàn:

1. **Không cam kết lợi nhuận.**
2. **Không khuyến nghị mua/bán cụ thể nếu thiếu bối cảnh.**
3. **Không kích thích all in, vay mượn, full margin.**
4. **Luôn nhắc đến rủi ro, điểm sai, quản trị vốn nếu bài có yếu tố đầu tư.**
5. **Nếu nói về sản phẩm tài chính, giải thích phù hợp khẩu vị rủi ro từng nhóm.**

## Từ ngữ TUYỆT ĐỐI TRÁNH

Không bao giờ dùng các cụm từ sau:

- Chắc chắn thắng
- Cam kết lợi nhuận
- Tín hiệu 100%
- All in / Full margin
- Cơ hội cuối đời
- Lệnh bao thắng
- Làm giàu nhanh
- Bí mật không ai biết
- Kèo thơm
- X100 tài khoản
- Không vào là tiếc cả đời

## Checklist trước khi xuất nội dung

Trước khi giao bài, tự kiểm tra:

- [ ] Hook đã đủ mạnh chưa?
- [ ] Bài có đánh đúng nỗi đau persona không?
- [ ] Có câu nào đáng lưu lại không?
- [ ] Có đoạn nào quá dài không?
- [ ] Có chỗ nào hô hào quá đà không?
- [ ] Có nhắc đến rủi ro hoặc kỷ luật không?
- [ ] CTA đã mềm nhưng đủ rõ chưa?
- [ ] Bài tạo cảm giác chuyên gia hay chỉ giống người bán nhóm?
- [ ] Giọng viết có đúng 5 trục không?
- [ ] Có vi phạm 5 lớp an toàn không?

## Nguyên tắc lõi

- Khi có nghi ngờ, luôn ưu tiên **an toàn** hơn **ấn tượng**.
- Triết học là **gia vị**, không phải **món chính**.
- Viết để người đọc **tỉnh ra**, không phải để họ **mơ mộng**.

## Quy tắc 1%

Nếu có 1% khả năng nội dung chạm safety risk → **bắt buộc** chạy full safety review. Không rationalize "bài này nhẹ thôi, chắc không sao".

**Trigger bắt buộc:** Khi nội dung chứa bất kỳ từ trong danh sách finance terms:

```
đầu tư, giao dịch, forex, vàng, USD, thị trường, lãi suất, tỷ giá,
chứng khoán, crypto, lệnh, vị thế, danh mục, lợi nhuận, vốn
```

Không được tuyên bố output là "done" trước khi:

1. Chạy `python scripts/validate-content-safety.py <path>` và paste exit code 0.
2. Đối chiếu xong với 5 lớp an toàn + danh sách từ tuyệt đối tránh ở trên.
3. Đọc lại `.claude/rules/red-flags-content.md` nếu có suy nghĩ muốn skip gate.

**Không có exception** vì user đang vội, vì bài "chỉ nói chung chung", hoặc vì "đã quen tay".
