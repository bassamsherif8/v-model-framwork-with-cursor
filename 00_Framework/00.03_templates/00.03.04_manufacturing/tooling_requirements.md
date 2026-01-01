# Tooling Requirements

**Purpose:** Identify and document tooling requirements for manufacturing

**Owner:** @DesignEng  
**Version:** 1.0  
**Date:** 2024-12-22

---

## Tooling Types

### CNC Machining Tooling
- **Cutting Tools:** End mills, drills, taps, reamers
- **Fixtures:** Workholding fixtures, vise jaws
- **Jigs:** Drilling jigs, inspection jigs
- **Gauges:** Inspection gauges, go/no-go gauges

### 3D Printing Tooling
- **Build Plates:** Standard or custom
- **Support Structures:** Generated automatically
- **Post-Processing Tools:** Sanding, finishing

### Sheet Metal Tooling
- **Dies:** Bending dies, punching dies
- **Fixtures:** Bending fixtures, welding fixtures
- **Templates:** Layout templates

### Casting Tooling
- **Molds:** Sand molds, investment molds, die molds
- **Patterns:** Master patterns
- **Cores:** Core boxes

---

## Tooling Requirements Template

```markdown
# Tooling Requirements: [Part Number] - [Part Name]

**Date:** [Date]  
**Manufacturing Process:** [Process]

## Tooling List

| Tooling Item | Type | Quantity | Cost Estimate | Lead Time | Notes |
|--------------|------|----------|---------------|-----------|-------|
| [Item 1] | [Type] | [Qty] | [Cost] | [Time] | [Notes] |

## Tooling Cost Summary
- Total Tooling Cost: [Cost]
- Tooling Cost per Unit (at MOQ): [Cost]

## Tooling Lead Time
- Total Lead Time: [Time]
- Critical Path: [Item]

## Tooling Design Requirements
- [Requirement 1]
- [Requirement 2]

## Tooling Maintenance
- Maintenance Requirements: [Description]
- Replacement Schedule: [Schedule]

## Notes
[Any additional notes]
```

---

## Tooling Cost Estimation

### CNC Machining
- **Cutting Tools:** $50-500 per tool
- **Fixtures:** $500-5000 per fixture
- **Jigs:** $200-2000 per jig
- **Gauges:** $100-1000 per gauge

### Sheet Metal
- **Dies:** $1000-10000 per die set
- **Fixtures:** $500-3000 per fixture

### Casting
- **Molds:** $5000-50000 per mold
- **Patterns:** $1000-10000 per pattern

---

## Related Documents

- Process Selection Matrix: `02_Design/manufacturing/process_selection_matrix.md`
- Lead Time Estimation: `02_Design/manufacturing/lead_time_estimation.md`

