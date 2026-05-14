---
name: content-debugging
description: Use khi mot bai Gold Smith underperform (reach, engagement, saves, comments thap, audience phan ung tieu cuc). Debug systematic theo nguyen nhan goc thay vi doi angle ngau nhien.
---

# Content Debugging — Khi bai khong chay

Cam hung tu Superpowers `systematic-debugging`: bug = root-cause analysis, khong "thu random fix".

## Nguyen tac cot loi

1. **Mot bien moi lan test.** Doi 2 thu cung luc = khong biet thu nao tao ket qua.
2. **Du lieu truoc cam giac.** "Bai nay khong hay" khong tinh. Reach? Engagement rate? Saves? Comments? CTR?
3. **Log vao experiment tracker.** `reference/templates/content-experiment-log.md`.
4. **Khong viet lai bai goc.** Tao variant moi, giu original lam control.

## Debug checklist — kiem theo thu tu

### Buoc 1: Hook hong

**Symptom:** Reach thap, dwell time duoi 2s.

- So 3 hook alternatives ban da xuat — chon hook nao?
- Hook co dung dang theo `Gold-Smith-fb.md` / `Gold-Smith-video.md`?
- Hook co thuoc nhom da chay tot truoc do?
- Co bi giat tit, FOMO hoac qua chung chung?
- Tham khao `1000_hook_short_form_tai_chinh.md` cho variant.

**Fix:** Re-test voi hook alternative #2 hoac #3, giu nguyen body.

### Buoc 2: Persona sai

**Symptom:** Reach co nhung engagement thap, comment lac de.

- Audience reach thuc te co match ICP target?
- Pain point co dung khau vi cua persona?
- Vocabulary co qua chuyen sau (F0) hoac qua so cap (Founder)?
- Doc lai `context/icp.md` → "Doi tuong nay co thuc su can bai nay?"

**Fix:** Re-frame voi persona khac, giu nguyen insight.

### Buoc 3: Timing/competition

**Symptom:** Bai chat luong nhung reach thap bat thuong.

- Dang trung tin nong khac (vang, ty gia, su kien chinh tri)?
- Dang trung gio thap (sau 22h, truoc 7h)?
- Co thuat toan platform thay doi?
- Bai cung pillar dang truoc do co an reach?

**Fix:** Reschedule, khong viet lai noi dung.

### Buoc 4: CTA cung hoac nham muc tieu

**Symptom:** Saves cao nhung comments thap (hoac nguoc lai).

- CTA dang muc tieu gi: comment, save, follow, inbox, share?
- CTA co match muc tieu khong? "Luu bai" thi dung doi comment.
- CTA co mem qua khong (nguoi doc khong biet phai lam gi)?
- CTA co cung qua khong (nghe nhu quang cao)?

**Fix:** Doi mot CTA tu 3 CTA alternatives da xuat.

### Buoc 5: Safety overreach

**Symptom:** Bai an toan nhung nhat. Khong saves, khong share.

- Co qua nhieu disclaimer lam loang luan diem?
- Co dung qua nhieu "co the", "neu", "tuy thuoc" lam mat decision?
- Sac va an toan co bi danh doi sai huong?

**Fix:** Giu safety, tang sac bang cau chot. Doc lai `.claude/rules/tone-voice.md` truc 1-3.

### Buoc 6: Visual mismatch

**Symptom:** Format text-only nhung audience can visual hoac nguoc lai.

- Bai dai > 600 tu khong co break visual?
- Bai phan tich thi truong khong co chart/data point?
- Bai persona Gen Z khong co visual cho Threads/Reels?

**Fix:** Repurpose sang carousel hoac video ngan theo `Gold-Smith-video.md`.

### Buoc 7: Pillar saturation

**Symptom:** Audience met pillar nay.

- Da dang lien tiep nhieu bai cung pillar?
- Ti le pillar co lech khoi 25/20/20/15/10/5/5?
- Audience comment "lai bai nay nua a"?

**Fix:** Switch pillar, khong viet lai bai cu.

## Anti-patterns can tranh

- **"Doi angle thu xem"** — khong biet bien nao broken, chi tao noise.
- **"Viet lai theo voice khac"** — voice Gold Smith la constant, khong phai bien.
- **"Tang volume bai"** — bai khong chay khong duoc fix bang nhieu bai khong chay hon.
- **"Boost post"** — paid khong fix organic problem.
- **"Doi luc dang"** — chi fix Buoc 3, khong fix Buoc 1-2.

## Output

Sau khi debug, ghi vao `reference/templates/content-experiment-log.md`:

```markdown
## <YYYY-MM-DD> Debug: <slug bai>

**Symptom:** ...
**Hypothesis:** Buoc <N> — <ten nhom>
**Variable changed:** <chi mot bien>
**Variant:** <link bai moi>
**Control:** <link bai goc>
**Expected metric:** <metric + target>
**Result:** <fill sau khi do>
```

## Khi nao goi skill nay

- Bai dang > 24h nhung reach < expected.
- Engagement rate thap hon trung binh 7 ngay.
- Comment tieu cuc hoac lac chu de.
- Saves cao nhung khong ra inbox/community.
- User report "bai nay khong giong Gold Smith".

## Khi KHONG goi skill nay

- Bai moi dang < 6h (chua du data).
- Khong co metric cu the (chi "cam giac khong hay").
- Test < 3 bai cung pillar (du lieu khong du de ket luan pillar saturation).
