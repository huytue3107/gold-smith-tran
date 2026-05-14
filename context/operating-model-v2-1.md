# Gold Smith Operating Model v2.1

_Cap nhat: 2026-05-13_
_Nguon tham chieu: Agency/NEXUS patterns, da rut gon cho content OS tai chinh._

## Muc Dich

v2.1 them lop van hanh len tren `context/framework-v2.md`.

`framework-v2.md` tra loi: pipeline noi dung gom nhung buoc nao.

`operating-model-v2-1.md` tra loi: moi buoc ban giao cho ai, pass/fail bang tieu chi nao, bang chung can co la gi, va he thong hoc lai nhu the nao.

## Nguyen Tac

1. **Evidence over claims**: Khong chap nhan danh gia "hay", "dung", "an toan", "dep" neu khong co ly do cu the.
2. **Safety before sharpness**: Bai tai chinh co rui ro thi an toan dung truoc do sac.
3. **No auto-publish**: Agent co the tao, review, de xuat lich; khong tu dong dang noi dung tai chinh.
4. **Context continuity**: Moi lan handoff phai mang theo persona, angle, safety constraints va file lien quan.
5. **Small gates, fast loops**: Review tung buoc nho thay vi doi den cuoi moi sua.

## Pipeline v2.1

```text
1. Intake
2. Strategy Gate
3. Research Gate
4. Draft Gate
5. Safety Gate
6. Voice Gate
7. Visual Gate
8. Evidence Gate
9. Storage / Dashboard
10. Analytics / Learning Loop
```

## Gate Definitions

### 1. Intake

**Owner:** primary assistant

**Pass criteria:**

- Chu de ro.
- Persona duoc xac dinh hoac mac dinh hop ly.
- Platform/muc tieu duoc xac dinh.
- Du lieu thieu quan trong duoc danh dau `TBD` hoac hoi user.

### 2. Strategy Gate

**Owner:** `content-strategist`

**Pass criteria:**

- Persona dung.
- Pain point dung.
- Content pillar dung.
- Template va CTA phu hop.
- Repurpose path co ly do.

**Evidence:** Strategy Brief.

### 3. Research Gate

**Owner:** `trend-researcher` hoac `researcher`

**Pass criteria:**

- Tin moi/so lieu da co nguon.
- Nguon co ngay thang.
- Muc do tin cay duoc ghi.
- Du lieu khong chac duoc ghi `TBD`.

**Evidence:** Market Intelligence Brief hoac source notes.

### 4. Draft Gate

**Owner:** writer/content creator

**Pass criteria:**

- Co metadata.
- Co Post Text.
- Co 3 hook.
- Co 3 CTA.
- Co image/repurpose notes.
- Co safety check ngan.

### 5. Safety Gate

**Owner:** `financial-safety-reviewer`

**Pass criteria:**

- Khong cam ket loi nhuan.
- Khong phiem lenh.
- Khong all-in/full margin/vay tien.
- Khong FOMO qua da.
- Co rui ro/diem sai/quan tri von neu noi ve dau tu.

**Evidence:** Safety Review.

### 6. Voice Gate

**Owner:** `voice-editor`

**Pass criteria:**

- Hook co luc.
- Cau ngan va ro.
- Doan 1-3 cau.
- Dung tu vung Gold Smith.
- Triet hoc vua du.
- CTA mem.

### 7. Visual Gate

**Owner:** `visual-director`

**Pass criteria:**

- Visual dung brand.
- Chu tren anh ngan va doc duoc tren mobile.
- Khong neon, khong khoe tien/lai.
- Co file path hoac prompt ro neu can tao asset.

### 8. Evidence Gate

**Owner:** `content-evidence-reviewer`

**Pass criteria:**

- File output co du thanh phan.
- Claim co nguon hoac `TBD`.
- Dashboard render du neu bai duoc luu vao `posts/`.
- Visual duoc kiem tra ve readability neu co.
- Khong co contradiction voi source of truth.

**Verification commands (bat buoc chay va paste output truoc khi claim done):**

```bash
python scripts/validate-content-safety.py <path-to-post>
# Expect: exit code 0, "Safety validation passed"
```

Neu bai duoc luu vao `posts/`:

```bash
python scripts/build-dashboard.py
# Expect: dashboard.html rebuild khong loi
```

**Evidence before assertions:** Khong duoc noi "bai an toan" / "bai dat chuan" neu chua paste output cua 2 command tren. "Toi nghi" / "co le" / "chac la" khong tinh.

### 9. Storage / Dashboard

**Owner:** primary assistant

**Pass criteria:**

- Bai text-only luu dung `posts/YYYY-MM-DD-slug.md`.
- Bai co visual luu dung `posts/NNN-slug/post.md`.
- Research/draft/batch luu dung `outputs/`.
- Rebuild dashboard khi co thay doi trong `posts/`.

### 10. Analytics / Learning Loop

**Owner:** `analytics-reporter` + `experiment-tracker`

**Pass criteria:**

- Bai co tag experiment neu dang test hook/CTA/format.
- Performance sau khi dang duoc ghi vao experiment log neu co du lieu.
- Weekly brief rut ra bai hoc va next action.

## Handoff Rules

Moi handoff can co:

- From / To.
- Task.
- Persona.
- Platform.
- Goal.
- Current file/path.
- Constraints.
- Acceptance criteria.
- Evidence required.

Dung template: `reference/templates/content-handoff-v2-1.md`.

## Cadence De Xuat

### Daily khi san xuat noi dung

- Tao 1-3 y tuong.
- Chon 1 bai uu tien.
- Draft -> safety -> voice -> visual notes.

### Weekly

- Chay `/market-intelligence-v2` de tao brief tin hieu thi truong.
- Chay `/weekly-content-review-v2` de review bai da tao, backlog, va experiment.

### Monthly

- Cap nhat `context/metrics.md` neu co analytics that.
- Tong hop top performing content.
- Dieu chinh content pillar ratio.

## Agent Map v2.1

| Stage       | Primary agent               | Support                                       |
| ----------- | --------------------------- | --------------------------------------------- |
| Strategy    | `content-strategist`        | `brand-guardian`                              |
| Research    | `trend-researcher`          | `researcher`, `financial-safety-reviewer`     |
| Draft       | primary assistant           | `voice-editor`                                |
| Safety      | `financial-safety-reviewer` | `content-evidence-reviewer`                   |
| Voice       | `voice-editor`              | `brand-guardian`                              |
| Visual      | `visual-director`           | `brand-guardian`, `content-evidence-reviewer` |
| Measurement | `analytics-reporter`        | `experiment-tracker`                          |

## What Not To Import From Agency/NEXUS

- Khong dung full 7-phase NEXUS cho moi bai viet.
- Khong auto-publish.
- Khong dung investment ratings nhu Buy/Hold/Sell.
- Khong dat metric growth tuy tien khi chua co analytics that.
- Khong them compliance doanh nghiep qua nang neu chua co san pham/data nguoi dung.
