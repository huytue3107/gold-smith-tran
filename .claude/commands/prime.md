# Prime

Nạp context Gold Smith Tran trước khi bắt đầu viết hoặc chỉnh hệ thống nội dung.

## Chạy Lệnh Khám Phá

```bash
Get-ChildItem -Force
Get-ChildItem -Recurse -File -Include *.md | Select-Object -First 30 FullName
```

Nếu đang ở shell Unix-compatible, có thể dùng:

```bash
ls -la
find . -type f -name "*.md" | head -30
```

## Cần Đọc

Đọc theo thứ tự:

1. `CLAUDE.md`
2. `Gold-Smith-fb.md`
3. `Gold-Smith-video.md`
4. `1000_hook_short_form_tai_chinh.md` (chi can luot muc luc, doc chi tiet khi can hook)
5. `context/operating-model-v2-1.md`
6. `context/tools.md` (local tool adapters: Faster-Whisper-XXL...)
7. `context/framework-v2.md`
8. `context/profile.md`
9. `context/business.md`
10. `context/strategy.md`
11. `context/icp.md`
12. `context/metrics.md`
13. `context/voice-analysis.md`
14. `.claude/rules/safety.md`
15. `.claude/rules/red-flags-content.md` (anti-rationalization patterns)
16. `.claude/rules/workflow.md`
17. `.claude/rules/templates.md`
18. `.claude/rules/tone-voice.md`
19. `.claude/rules/content-strategy.md`
20. `outputs/content-ledger.md` (luot xem status va experiment cua asset gan day)

## Sau Khi Đọc

Tóm tắt ngắn:

1. Gold Smith là ai và workspace dùng để làm gì.
2. Nguồn sự thật chính và thứ tự ưu tiên.
3. Persona, trụ cột nội dung và kênh ưu tiên.
4. Nguyên tắc an toàn tài chính bắt buộc + quy tắc 1% và red-flags rationalization.
5. Pipeline v2.1 va gate nao bat buoc cho tac vu hien tai.
6. Cách bạn sẽ xuất bài khi nhận brief.
7. Trang thai content-ledger gan day (asset nao Draft/Reviewed/Ready/Published).
8. Khi nao goi `/create-video-v2`: sau khi bai pass Evidence Gate, dung Remotion + composition `MarketReading` (60s) de repurpose. Brief input qua `scripts/brief-to-video.py`. Chi tiet: `remotion/README.md` + `context/tools.md`.
