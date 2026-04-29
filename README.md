# Gold Smith Tran Content OS

Workspace này là hệ thống viết bài cho **Gold Smith Tran - Nhà Gia Kim Forex**.

Mục tiêu: tạo nội dung tài chính sắc bén, thực chiến, có chiều sâu nhưng an toàn; ưu tiên Facebook và Threads, sau đó repurpose sang video ngắn, carousel hoặc tài nguyên cộng đồng.

## Nguồn Sự Thật

Đọc theo thứ tự:

1. `CLAUDE.md` - operating manual của workspace.
2. `Gold-Smith-fb.md` - style guide chính, bộ não văn phong.
3. `context/` - hồ sơ thương hiệu, ICP, chiến lược, metrics, voice analysis.
4. `.claude/rules/` - luật persona, tone, safety, workflow, template.
5. `posts/` - bài đã tạo hoặc sẵn sàng xuất bản.

Nếu có mâu thuẫn, ưu tiên `Gold-Smith-fb.md` và nguyên tắc an toàn tài chính.

## Workspace Structure

```text
.
├── CLAUDE.md              # Operating manual chính
├── Gold-Smith-fb.md       # Style guide master
├── .claude/
│   ├── Claude.md          # Tham chiếu phụ cho Claude Code
│   ├── commands/          # /prime, /create-10-posts, /create-plan, /implement
│   └── rules/             # Persona, tone, safety, workflow, templates
├── context/               # Brand brain
│   ├── profile.md
│   ├── business.md
│   ├── strategy.md
│   ├── icp.md
│   ├── metrics.md
│   ├── voice-analysis.md
│   └── data/
├── posts/                 # Bài hoàn chỉnh
├── outputs/               # Dashboard, draft, batch plan
├── plans/                 # Kế hoạch triển khai thay đổi
├── reference/             # Visual refs, writing refs
└── scripts/               # Dashboard, carousel, infographic, photo overlay
```

## Workflow Viết Bài

### 1. Prime context

Khi bắt đầu session:

```text
/prime
```

Lệnh này yêu cầu Claude đọc `CLAUDE.md`, `Gold-Smith-fb.md`, `context/` và `.claude/rules/`.

### 2. Viết bài đơn

Brief nên có:

```text
Chủ đề:
Persona:
Kênh đăng:
Mục tiêu:
Góc nhìn chính:
Dữ kiện bắt buộc:
CTA mong muốn:
```

Nếu thiếu persona, mặc định:

- Giao dịch/đầu tư: F0.
- Chi tiêu/lương/tiết kiệm: Gen Z/Millennials.
- Bảo hiểm/con cái/gia đình: Phụ nữ & gia đình trẻ.
- Startup/vốn/fintech: Doanh nhân/Startup/Fintech.

### 3. Tạo batch 10 bài

```text
/create-10-posts
```

Output nên gồm bài viết, hook/CTA test, visual concept và thư mục trong `posts/`.

### 4. Dựng dashboard

```bash
python scripts/build-dashboard.py
```

Dashboard được tạo tại:

```text
outputs/dashboard.html
```

## Chuẩn Bài Viết

Mỗi bài nên lưu trong `posts/` hoặc một thư mục `posts/NNN-slug/` nếu có visual.

Một bài hoàn chỉnh phải có:

- Metadata: ngày, platform, persona, mục tiêu, phương pháp, visual.
- Post text copy-paste ready.
- 3 hook thay thế.
- 3 CTA thay thế.
- Gợi ý visual hoặc prompt tạo visual.
- 5 ý tưởng bài tiếp theo nếu đang dùng workflow sáng tạo nội dung.

## Nguyên Tắc An Toàn Tài Chính

Không bao giờ:

- Cam kết lợi nhuận.
- Phím lệnh mua/bán khi thiếu bối cảnh.
- Kích thích all-in, full margin, vay tiền đầu tư.
- Tạo FOMO bằng ngôn ngữ "cơ hội cuối", "chắc thắng", "bao lời".

Luôn ưu tiên:

- Quản trị vốn.
- Điểm sai.
- Khẩu vị rủi ro.
- Kỷ luật và xác suất.
- Sự thật có thể kiểm chứng.

## Dữ Liệu Chưa Xác Minh

Các thông tin như website, email, số followers, offer, lịch workshop, thành tích đầu tư hiện được ghi `TBD` trong `context/`. Không tự bịa các dữ liệu này trong bài viết hoặc CTA.

## Visual

- Ảnh cá nhân: dùng `scripts/add-photo-overlay.py`.
- Carousel: dùng `scripts/generate-carousel.py`.
- Infographic AI: dùng `scripts/generate-infographic.py` nếu có API key.
- Style visual cần giữ cảm giác tài chính, tối giản, sắc, không neon, không khoe lãi.
