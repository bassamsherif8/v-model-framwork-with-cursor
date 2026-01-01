# Design for Manufacturing (DFM) Checklist

**Purpose:** Ensure designs are optimized for manufacturing

**Owner:** @DesignEng  
**Version:** 1.0  
**Date:** 2024-12-22

---

## DFM Review Checklist

### Tool Access
- [ ] All features accessible by manufacturing tools
- [ ] No deep internal features requiring special tools
- [ ] Tool clearance verified (minimum clearance: tool diameter + 2mm)
- [ ] Tool path feasible (no collisions)
- [ ] Tool change minimized

### Undercuts
- [ ] No undercuts (or justified if necessary)
- [ ] Undercuts accessible if required
- [ ] Undercut manufacturing method defined

### Setup Minimization
- [ ] Number of setups minimized
- [ ] Features grouped by setup
- [ ] Setup sequence logical
- [ ] Fixturing points identified

### Standard Features
- [ ] Standard hole sizes used (preferred: M3, M4, M5, M6, M8)
- [ ] Standard thread sizes used
- [ ] Standard chamfer sizes (0.5mm x 45° typical)
- [ ] Standard fillet radii (R1, R2, R3 typical)
- [ ] Standard material sizes considered

### Material Selection
- [ ] Material optimized for manufacturing method
- [ ] Material readily available
- [ ] Material cost considered
- [ ] Material lead time acceptable

### Tolerances
- [ ] Tolerances achievable with selected manufacturing method
- [ ] Tolerances not tighter than necessary
- [ ] Critical tolerances identified
- [ ] Tolerance stack-up considered

### Surface Finish
- [ ] Surface finish achievable with selected method
- [ ] Surface finish not finer than necessary
- [ ] Critical surfaces identified
- [ ] Surface finish cost considered

### Machinability
- [ ] Tool paths feasible
- [ ] Cutting forces acceptable
- [ ] Chip evacuation considered
- [ ] Heat generation considered
- [ ] Material removal minimized

### Design Simplification
- [ ] Complex features simplified where possible
- [ ] Unnecessary features removed
- [ ] Design optimized for manufacturing
- [ ] Cost reduction opportunities identified

---

## Manufacturing Method Specific Checks

### CNC Machining
- [ ] 3-axis machining sufficient (or 4/5-axis justified)
- [ ] Tool access from top/bottom verified
- [ ] Internal corners have appropriate radii (≥ tool radius)
- [ ] Thin walls avoided (minimum 2mm typical)
- [ ] Deep pockets avoided (depth ≤ 5x width typical)

### 3D Printing
- [ ] Support structures minimized
- [ ] Overhangs < 45° (or supports acceptable)
- [ ] Layer orientation optimized
- [ ] Post-processing requirements considered
- [ ] Material anisotropy considered

### Sheet Metal
- [ ] Bend radii appropriate (≥ material thickness)
- [ ] Bend reliefs included
- [ ] K-factor considered
- [ ] Flat pattern feasible
- [ ] Minimum hole size (≥ material thickness)

### Casting
- [ ] Draft angles included (1-3° typical)
- [ ] Parting line defined
- [ ] Undercuts avoided (or cores justified)
- [ ] Uniform wall thickness (variation < 20%)
- [ ] Shrinkage allowance considered

---

## DFM Review Results

**Part Number:** [Part Number]  
**Part Name:** [Part Name]  
**Review Date:** [Date]  
**Reviewed By:** @DesignEng

**Overall DFM Score:** [Score] / 10

**Issues Identified:**
1. [Issue 1]
2. [Issue 2]

**Recommendations:**
1. [Recommendation 1]
2. [Recommendation 2]

**Status:** [ ] Pass | [ ] Pass with Recommendations | [ ] Fail - Redesign Required

---

## Related Documents

- DFM Review Process: `02_Design/manufacturing/DFM_review_process.md`
- Manufacturing Feedback Loop: `02_Design/manufacturing/manufacturing_feedback_loop.md`

