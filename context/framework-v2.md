# Gold Smith Content OS v2

_Cap nhat lan dau: 2026-05-13_
_Muc dich: Chuan hoa workspace thanh he dieu hanh noi dung co the mo rong, co review, co research va co safety gate ro rang._

## v2.1 Operating Layer

Tu 2026-05-13, v2 co them lop van hanh v2.1 tai:

```text
context/operating-model-v2-1.md
```

v2.1 them NEXUS-lite cho content: handoff, quality gate, evidence gate, weekly market intelligence, experiment tracking va analytics loop.

Command bo sung:

- `/market-intelligence-v2`
- `/weekly-content-review-v2`

## Ly Do Co Ban v2

Workspace v1 da co nen tang tot: style guide, persona, rules, scripts va dashboard. Van de chinh la cac lop dang nam rai rac va chua co mot pipeline ro rang tu research -> y tuong -> ban nhap -> review -> xuat ban -> repurpose.

v2 giu nguyen nguon su that cu, nhung them lop dieu phoi de moi tac vu noi dung co du:

1. Chien luoc.
2. Du lieu.
3. Giong viet.
4. An toan tai chinh.
5. Visual/repurpose.
6. Luu tru va dashboard.

## Thu Tu Nguon Su That

Khi co mau thuan, uu tien theo thu tu:

1. `Gold-Smith-fb.md` - bo nao van phong master.
2. `.claude/rules/safety.md` - an toan tai chinh bat buoc.
3. `context/profile.md`, `context/business.md`, `context/strategy.md`, `context/icp.md`, `context/voice-analysis.md`.
4. `.claude/rules/` - persona, workflow, templates, tone, vocabulary, design.
5. `posts/` - bai da tao va bai mau.
6. `reference/` - tham chieu phu, khong duoc lan at Gold Smith voice.

## Kien Truc Van Hanh

```text
Brief / Request
  -> Intake Layer
  -> Strategy Layer
  -> Research Layer
  -> Draft Layer
  -> Safety Review
  -> Voice Edit
  -> Visual / Repurpose
  -> Storage
  -> Dashboard / Metrics
```

### 1. Intake Layer

Muc tieu: hieu dung viec can lam truoc khi viet.

Can xac dinh:

- Chu de.
- Persona.
- Kenh dang.
- Muc tieu.
- Goc nhin chinh.
- Du kien bat buoc.
- Du lieu can xac minh.
- CTA mong muon.

Neu brief thieu:

- Dau tu/giao dich -> mac dinh persona F0.
- Chi tieu/luong/tiet kiem -> mac dinh Gen Z/Millennials.
- Bao hiem/con cai/gia dinh -> mac dinh phu nu/gia dinh tre.
- Startup/von/fintech -> mac dinh doanh nhan/startup/fintech.

### 2. Strategy Layer

Muc tieu: dat bai viet vao dung cot noi dung.

Cot noi dung v2:

1. F0 tra hoc phi.
2. Mot phut doc thi truong.
3. Tien cua nguoi tre.
4. Mai nha tai chinh.
5. Triet hoc dau tu.
6. Founder doc dong tien.
7. Fintech hieu con nguoi.

Output cua layer nay:

- Persona chinh.
- Pain point.
- Muc tieu hanh dong.
- Template phu hop.
- Goc canh tranh cua bai.

### 3. Research Layer

Muc tieu: khong viet dua tren cam giac khi bai can du lieu.

Dung khi:

- Bai co tin nong, vi mo, ty gia, vang, lai suat, forex, chung khoan, crypto.
- Bai co so lieu, thanh tich, follower, offer, workshop, gia ban.
- Bai can lay y tuong tu influencer/video/research.

Nguyen tac:

- Du lieu chua xac minh ghi `TBD`.
- Khong tu tao so lieu.
- Neu can tin moi, phai xac minh truoc khi dua vao bai.
- Research output nen luu vao `outputs/` neu co gia tri tai su dung.

### 4. Draft Layer

Muc tieu: tao ban nhap dung Gold Smith voice.

Moi bai hoan chinh can co:

- Metadata.
- Post Text copy-paste ready.
- 3 hook thay the.
- 3 CTA thay the.
- Image/Repurpose Notes.
- Safety check ngan.
- 5 y tuong bai tiep theo neu dang lam ideation.

### 5. Safety Review

Muc tieu: chan rui ro truoc khi giao bai.

Bat buoc kiem:

- Khong cam ket loi nhuan.
- Khong phiem lenh mua/ban neu thieu boi canh.
- Khong kich thich all-in, full margin, vay tien.
- Khong tao FOMO bang ngon ngu "co hoi cuoi", "chac thang", "bao loi".
- Co rui ro, diem sai, ty trong, khau vi rui ro hoac nguyen tac bao toan von khi bai co dau tu.
- Neu noi ve san pham/offer ma du lieu chua xac minh, phai de `TBD` hoac hoi user.

### 6. Voice Edit

Muc tieu: bien bai dung y thanh bai dung chat Gold Smith.

Kiem:

- Cau ngan, co luc.
- Doan 1-3 cau.
- Hook danh vao su that kho nghe hoac pain point.
- Triet hoc la gia vi, khong thanh bai thuyet phap.
- Ket bai co CTA mem.
- Giong chuyen gia thuc chien, khong phai nguoi ban tin hieu.

### 7. Visual / Repurpose

Muc tieu: moi bai co huong dung lai.

Loai output:

- Text-only Facebook/Threads.
- Quote visual.
- Infographic.
- Carousel.
- Video script 45-60 giay.
- Personal photo overlay.

Cong cu:

- `scripts/build-dashboard.py`
- `scripts/generate-carousel.py`
- `scripts/generate-infographic.py`
- `scripts/add-photo-overlay.py`

### 8. Storage

Bai text-only:

```text
posts/YYYY-MM-DD-slug.md
```

Bai co visual:

```text
posts/NNN-slug/
  post.md
  image.png
  carousel.pdf
  carousel-slides/
  content.json
  source-notes.md
```

Research/draft/batch:

```text
outputs/YYYY-MM-DD-description.md
```

Ke hoach thay doi workspace:

```text
plans/YYYY-MM-DD-description.md
```

## Bo Agent v2

v2 dung cac agent chuyen biet theo tung cong doan:

| Agent                       | Muc dich                                                          |
| --------------------------- | ----------------------------------------------------------------- |
| `content-strategist`        | Chon persona, cot noi dung, angle, format va CTA                  |
| `financial-safety-reviewer` | Kiem tra rui ro compliance va ngon ngu tai chinh nguy hiem        |
| `voice-editor`              | Chinh giong Gold Smith: sac, gon, thuc chien, co chieu sau        |
| `visual-director`           | De xuat visual, carousel, infographic, photo overlay va repurpose |
| `researcher`                | Thu thap/xac minh du lieu khi bai can tin moi hoac research       |

## Tieu Chuan Done

Mot output duoc xem la dat khi:

1. Dung persona va pain point.
2. Dung Gold Smith voice.
3. Co safety layer ro.
4. Khong bia du lieu.
5. Co CTA mem.
6. Co huong visual/repurpose.
7. Duoc luu dung noi neu user yeu cau ghi file.
8. Dashboard duoc rebuild neu co thay doi trong `posts/`.

## Backlog Cai Thien Sau v2 Nen Tang

1. Tach `Gold-Smith-fb.md` thanh module nho hon de de bao tri.
2. Nang `outputs/dashboard.html` thanh content command center co filter persona/platform/status.
3. Tao `outputs/content-calendar.md` hoac dashboard lich dang bai.
4. Chuyen `outputs/finance_influencer_videos/` thanh research pipeline co scoring va cach bien video thanh y tuong bai.
5. Them mau `post.md` chuan trong `posts/_template.md`.
6. Them script validate safety tu khoa cam truoc khi xuat ban.

## Cleanup Da Hoan Tat

- Da them operating model v2.1.
- Da them bo agent content/safety/voice/visual/evidence/analytics.
- Da chuan hoa cac skill content ideation, viral replication va carousel ve Gold Smith.
- Da go cac file rong/deprecated trong `.claude`.
