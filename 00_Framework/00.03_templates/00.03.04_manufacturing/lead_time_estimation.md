# Lead Time Estimation

**Purpose:** Estimate manufacturing lead times

**Owner:** @DesignEng  
**Version:** 1.0  
**Date:** 2024-12-22

---

## Lead Time Components

### Setup Time
- Tooling preparation
- Program preparation
- Fixture setup
- First article inspection

### Production Time
- Material procurement
- Manufacturing time
- Quality control

### Post-Processing Time
- Finishing
- Heat treatment
- Assembly
- Final inspection

---

## Standard Lead Times

### CNC Machining
- **Setup:** 1-3 days
- **Production:** 1-5 days (depending on quantity)
- **Post-Processing:** 1-2 days
- **Total:** 1-2 weeks

### 3D Printing
- **Setup:** 0.5-1 day
- **Production:** 1-3 days
- **Post-Processing:** 0.5-1 day
- **Total:** 1-3 days

### Sheet Metal
- **Setup:** 1-2 days
- **Production:** 2-5 days
- **Post-Processing:** 1-2 days
- **Total:** 1-2 weeks

### Casting
- **Tooling:** 2-4 weeks
- **Production:** 1-2 weeks
- **Post-Processing:** 1 week
- **Total:** 3-6 weeks (first order), 1-2 weeks (subsequent)

---

## Lead Time Estimation Template

```markdown
# Lead Time Estimation: [Part Number] - [Part Name]

**Date:** [Date]  
**Manufacturing Process:** [Process]

## Lead Time Breakdown

| Phase | Duration | Notes |
|-------|----------|-------|
| Material Procurement | [Days] | [Notes] |
| Tooling Setup | [Days] | [Notes] |
| Production | [Days] | [Notes] |
| Quality Control | [Days] | [Notes] |
| Post-Processing | [Days] | [Notes] |

## Total Lead Time
- **Estimated Lead Time:** [Days] days / [Weeks] weeks
- **Buffer (20%):** [Days] days
- **Total with Buffer:** [Days] days / [Weeks] weeks

## Critical Path
[Identify critical path items]

## Notes
[Any special considerations]
```

---

## Factors Affecting Lead Time

- **Quantity:** Higher quantity = longer production time
- **Complexity:** More complex = longer setup and production
- **Material Availability:** Material lead time affects total
- **Tooling:** Custom tooling adds lead time
- **Supplier Capacity:** Supplier workload affects lead time

---

## Related Documents

- Process Selection Matrix: `02_Design/manufacturing/process_selection_matrix.md`
- Tooling Requirements: `02_Design/manufacturing/tooling_requirements.md`

