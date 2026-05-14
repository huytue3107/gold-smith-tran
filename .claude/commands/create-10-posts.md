# Tạo Batch 10 Nội Dung

Tạo 10 nội dung sẵn sàng biên tập/xuất bản cho **Gold Smith Tran - Nhà Gia Kim Forex**.

Ưu tiên Facebook và Threads. Với mỗi bài, thêm hướng repurpose sang video ngắn hoặc visual nếu phù hợp.

## Nguồn Bắt Buộc

Trước khi viết, đọc:

- `CLAUDE.md`
- `Gold-Smith-fb.md`
- `Gold-Smith-video.md` (khi co bai repurpose video)
- `1000_hook_short_form_tai_chinh.md` (luot khi can hook)
- `context/strategy.md`
- `context/icp.md`
- `context/voice-analysis.md`
- `.claude/rules/safety.md`
- `.claude/rules/red-flags-content.md`
- `.claude/rules/templates.md`
- `.claude/rules/content-strategy.md`
- `outputs/content-ledger.md` (de tranh trung pillar/persona voi asset gan day)

## Cơ Cấu Nội Dung

### Theo Phương Pháp

| Phương pháp               | Số lượng | Mô tả                                                                                      |
| ------------------------- | -------- | ------------------------------------------------------------------------------------------ |
| Tin nóng / Market Reading | 3        | Bám tỷ giá, vàng, USD, lãi suất, dòng tiền, tin vĩ mô. Phải có dữ kiện và cảnh báo rủi ro. |
| Pain Point                | 3        | Đào sâu nỗi đau F0, người trẻ, gia đình, founder.                                          |
| Series / Education        | 2        | Bài thuộc series như "F0 trả học phí", "Tiền của người trẻ", "Mái nhà tài chính".          |
| Viral Replication         | 2        | Mượn cấu trúc bài đã hiệu quả, thay substance bằng góc Gold Smith.                         |

### Theo Persona

| Persona                         | Số lượng tối thiểu |
| ------------------------------- | ------------------ |
| Nhà đầu tư F0                   | 4                  |
| Gen Z/Millennials               | 2                  |
| Phụ nữ & gia đình trẻ           | 2                  |
| Doanh nhân/Startup/Fintech      | 1                  |
| Persona linh hoạt theo tin nóng | 1                  |

## Handoff Discipline

Khi gọi specialist agent cho từng bài (voice-editor, financial-safety-reviewer, visual-director...), prompt phải **self-contained** theo `reference/templates/content-handoff-v2-1.md`. Không gọi suông "review batch này" — mỗi bài gói riêng đủ context.

## Parallel Dispatch

Khi 10 bài có persona/pillar độc lập, dispatch song song theo nguyên tắc:

- Mỗi bài = 1 handoff packet độc lập.
- Không chia sẻ state giữa các bài (mỗi bài tự chứa brief, persona, source files cần đọc).
- Safety review chạy SAU mỗi bài draft xong, không gộp batch.

### Theo Định Dạng

| Định dạng                    | Số lượng khuyến nghị |
| ---------------------------- | -------------------- |
| Facebook post dài            | 5                    |
| Facebook/Threads post ngắn   | 2                    |
| Video script 45-60 giây      | 2                    |
| Carousel/Infographic concept | 1                    |

Không bắt buộc bài nào cũng phải có visual thật ngay, nhưng mỗi bài phải có **Image Notes** hoặc **Repurpose Notes**.

## Output Cho Mỗi Bài

Mỗi bài phải có:

1. Tiêu đề nội bộ.
2. Persona.
3. Mục tiêu.
4. Phương pháp.
5. Platform chính.
6. Bài chính copy-paste ready.
7. 3 hook thay thế.
8. 3 CTA thay thế.
9. Image/Video/Repurpose notes.
10. Safety check ngắn.

## Lưu File

Nếu được yêu cầu ghi file, lưu kế hoạch batch tại:

```text
outputs/YYYY-MM-DD-batch-content-plan.md
```

Nếu triển khai từng bài, lưu vào:

```text
posts/NNN-slug/post.md
```

hoặc với bài text-only:

```text
posts/YYYY-MM-DD-slug.md
```

## Checklist Trước Khi Giao

- Không có cam kết lợi nhuận.
- Không có phím lệnh mua/bán cụ thể nếu thiếu bối cảnh.
- Không kích thích all-in, full margin, vay tiền đầu tư.
- Mỗi bài có persona và nỗi đau rõ.
- Mỗi bài có CTA mềm, không bán hàng lộ liễu khi offer chưa xác minh.
- Giọng viết đúng: thực chiến, sắc bén, quyết đoán, có chiều sâu, gọn.
