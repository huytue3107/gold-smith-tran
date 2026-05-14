# Create Content v2

Tao noi dung Gold Smith theo pipeline v2.

## Input

request: $ARGUMENTS

Neu user khong dua day du brief, suy luan theo `context/framework-v2.md` va chi hoi lai khi thieu du lieu co the lam sai ban chat bai viet.

## Nguon Bat Buoc

Doc theo thu tu:

1. `context/framework-v2.md`
2. `Gold-Smith-fb.md`
3. `Gold-Smith-video.md` (nếu output co video script hoac repurpose)
4. `1000_hook_short_form_tai_chinh.md` (kho hook tham khao)
5. `context/strategy.md`
6. `context/icp.md`
7. `context/voice-analysis.md`
8. `.claude/rules/safety.md`
9. `.claude/rules/templates.md`
10. `.claude/rules/tone-voice.md`
11. `.claude/rules/design.md`

## Pipeline

## Handoff Discipline

Khi goi specialist agent (`content-strategist`, `voice-editor`, `financial-safety-reviewer`, `visual-director`, `content-evidence-reviewer`...), prompt phai **self-contained** theo `reference/templates/content-handoff-v2-1.md`:

- From / To / Task / Persona / Platform / Goal.
- Current file/path neu co.
- Constraints va safety notes.
- Acceptance criteria.
- Evidence required.

Khong goi suong kieu "review bai nay". Agent kia khong co conversation context — phai dong goi du.

## Pipeline

### 1. Strategy

Dung vai tro `content-strategist` de xac dinh:

- Persona.
- Pain point.
- Content pillar.
- Platform.
- Goal.
- Template.
- Angle.
- CTA.
- Repurpose path.

### 2. Research

Neu bai co tin moi, so lieu, gia, follower, offer, workshop, thanh tich, hay thong tin co the thay doi, phai xac minh truoc khi viet.

Neu khong xac minh duoc, ghi `TBD` hoac hoi user.

### 3. Draft

Viet ban chinh theo `Gold-Smith-fb.md`.

Bat buoc co:

- Metadata.
- Post Text copy-paste ready.
- 3 hook thay the.
- 3 CTA thay the.
- Image/Repurpose Notes.
- Safety check ngan.

### 4. Safety Review

Dung checklist trong `.claude/rules/safety.md`.

Chan:

- Cam ket loi nhuan.
- Phiem lenh.
- All-in/full margin/vay tien.
- FOMO qua da.
- Du lieu chua xac minh.

### 5. Voice Edit

Chinh lai:

- Cau ngan, co luc.
- Doan 1-3 cau.
- Hook sac.
- Triet hoc vua du.
- CTA mem.

### 6. Visual/Repurpose

De xuat it nhat mot huong:

- Threads.
- Video script 15/30/45/60/90 giay (default 45s) theo `Gold-Smith-video.md`.
- Quote visual.
- Infographic.
- Carousel.
- Photo overlay.

## Output Format

```markdown
# <Tieu de noi bo>

**Ngay:** <YYYY-MM-DD>
**Platform:** ...
**Persona:** ...
**Muc tieu:** ...
**Cot noi dung:** ...
**Template:** ...
**Visual:** ...

---

## Strategy Brief

...

---

## Post Text

...

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

## Image / Repurpose Notes

...

---

## Safety Check

...
```

## Luu File

Chi ghi file khi user yeu cau hoac tac vu ro rang la tao output.

- Bai text-only: `posts/YYYY-MM-DD-slug.md`
- Bai co visual: `posts/NNN-slug/post.md`
- Draft/batch/research: `outputs/YYYY-MM-DD-description.md`

Neu co ghi vao `posts/`, chay:

```bash
python scripts/build-dashboard.py
```
