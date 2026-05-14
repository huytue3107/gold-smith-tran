# Ke Hoach: Gold Smith Content OS v2.1 Agency Upgrade

**Tao luc:** 2026-05-13
**Trang thai:** Implemented
**Yeu cau:** Lay bai hoc tu `E:\CLAUDE\agency-agents` de bo sung vao Gold Smith Content OS.

---

## Tong Quan

### Ke Hoach Nay Dat Duoc Dieu Gi

Ke hoach nay chuyen cac pattern huu ich tu Agency/NEXUS thanh mot ban NEXUS-lite phu hop voi content OS tai chinh. Muc tieu la them quality gate, handoff, evidence, analytics va cadence van hanh ma khong lam workspace phinh ra nhu mot he multi-agent day du.

### Vi Sao Dieu Nay Quan Trong

Gold Smith v2 da co pipeline noi dung. v2.1 bo sung lop van hanh: ai nhan viec, ban giao nhu the nao, pass/fail dua tren bang chung gi, va moi tuan he thong hoc duoc gi tu noi dung da tao.

---

## Trang Thai Hien Tai

### Cau Truc Lien Quan Dang Co

- `context/framework-v2.md`: pipeline v2.
- `.claude/agents/`: da co content-strategist, financial-safety-reviewer, voice-editor, visual-director.
- `.claude/commands/create-content-v2.md`: tao content theo pipeline v2.
- `.claude/commands/review-content-v2.md`: review content theo v2.
- `outputs/finance_influencer_videos/`: research video influencer chua tich hop vao pipeline.

### Khoang Trong Can Giai Quyet

- Chua co operating model v2.1 cho handoff/quality gate/cadence.
- Chua co agent evidence/reality check danh rieng cho content.
- Chua co agent analytics/experiment de hoc tu hieu suat bai.
- Chua co template chuan cho handoff, market intelligence, experiment log, weekly brief.
- Chua co command rieng cho market intelligence va weekly review.

---

## Thay Doi Da Trien Khai

### File Moi

| File                                               | Muc dich                            |
| -------------------------------------------------- | ----------------------------------- |
| `context/operating-model-v2-1.md`                  | Mo ta NEXUS-lite cho Gold Smith     |
| `.claude/agents/brand-guardian.md`                 | Giu brand identity va consistency   |
| `.claude/agents/content-evidence-reviewer.md`      | Evidence gate cho content           |
| `.claude/agents/trend-researcher.md`               | Market/trend intelligence cho topic |
| `.claude/agents/analytics-reporter.md`             | Phan tich hieu suat noi dung        |
| `.claude/agents/experiment-tracker.md`             | Theo doi test hook/CTA/format       |
| `reference/templates/content-handoff-v2-1.md`      | Mau handoff giua agent              |
| `reference/templates/market-intelligence-brief.md` | Mau research thi truong             |
| `reference/templates/content-experiment-log.md`    | Mau ghi nhan experiment             |
| `reference/templates/weekly-executive-brief.md`    | Mau brief tuan                      |
| `.claude/commands/market-intelligence-v2.md`       | Tao market intelligence brief       |
| `.claude/commands/weekly-content-review-v2.md`     | Review tuan va de xuat hanh dong    |

### File Da Cap Nhat

| File                      | Noi dung                          |
| ------------------------- | --------------------------------- |
| `context/framework-v2.md` | Them ghi chu v2.1 va cac gate moi |
| `README.md`               | Them command/agent v2.1           |
| `CLAUDE.md`               | Them che do v2.1                  |
| `.claude/Claude.md`       | Them tham chieu v2.1              |

---

## Nguyen Tac Thiet Ke

1. **Lay co che, khong be nguyen agent**: NEXUS day du qua nang cho content OS.
2. **Evidence over claims**: Bai hay, visual dep, safety pass deu can ly do ro.
3. **No auto-publish**: Noi dung tai chinh phai co nguoi duyet truoc khi dang.
4. **No investment recommendation leakage**: Khong ke thua Buy/Hold/Sell, price target, hay khuyen nghi mua/ban.
5. **Cadence nhe**: Daily/weekly/monthly review vua du cho mot content OS ca nhan.

---

## Implementation Notes

**Implemented:** 2026-05-13

### Summary

Da tao operating model v2.1, agent bo sung, template handoff/research/experiment/weekly brief, va command market intelligence/weekly review.

### Deviations from Plan

None.

### Issues Encountered

None.
