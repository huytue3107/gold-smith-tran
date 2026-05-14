# Review Content v2

Review mot bai Gold Smith theo framework v2.

## Input

target: $ARGUMENTS

Co the la duong dan file trong `posts/`/`outputs/` hoac noi dung user dan truc tiep.

## Nguon Bat Buoc

1. `context/framework-v2.md`
2. `Gold-Smith-fb.md`
3. `Gold-Smith-video.md` (neu review script video)
4. `.claude/rules/safety.md`
5. `.claude/rules/red-flags-content.md` (chan reviewer chinh minh rationalize)
6. `.claude/rules/tone-voice.md`
7. `.claude/rules/vocabulary.md`
8. `context/voice-analysis.md`

## Checklist Review

### Strategy Fit

- Persona co ro khong?
- Pain point co dung khong?
- Cot noi dung co khop chien luoc khong?
- CTA co phu hop muc tieu khong?

### Financial Safety

- Co cam ket loi nhuan khong?
- Co phiem lenh khong?
- Co kich thich all-in, margin, vay tien khong?
- Co FOMO qua da khong?
- Co du lieu chua xac minh khong?
- Co lop quan tri rui ro khong?

### Voice Fit

- Hook co du sac khong?
- Cau co gon khong?
- Doan co thoang khong?
- Tu vung co dung Gold Smith khong?
- Triet hoc co vua du khong?
- Bai co cau dang luu lai khong?

### Output Completeness

- Co 3 hook thay the khong?
- Co 3 CTA thay the khong?
- Co visual/repurpose notes khong?
- Co metadata khong?

### Local Safety Validator

Neu bai da nam trong `posts/`, chay:

```bash
python scripts/validate-content-safety.py posts
```

Dung ket qua nay nhu canh bao nhanh; van phai doc lai bang mat nguoi.

## Output Format

```markdown
## Content Review v2

**Status:** Pass / Needs revision / Blocked

### Highest-priority issues

- ...

### Safety issues

- ...

### Voice issues

- ...

### Strategy issues

- ...

### Suggested rewrite

<Chi viet lai nhung doan can sua, khong viet lai toan bai neu khong can>

### Final recommendation

...
```
