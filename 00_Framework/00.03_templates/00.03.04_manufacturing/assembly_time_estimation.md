# Assembly Time Estimation

**Purpose:** Estimate assembly time for designs

**Owner:** @DesignEng  
**Version:** 1.0  
**Date:** 2024-12-22

---

## Standard Assembly Times

### Part Operations
- **Part placement:** ~15 seconds
- **Part orientation:** ~10 seconds
- **Part alignment:** ~30-60 seconds (depending on complexity)

### Fastener Operations
- **Fastener installation (hand):** ~30 seconds per fastener
- **Fastener installation (power tool):** ~15 seconds per fastener
- **Fastener tightening:** ~10 seconds per fastener
- **Torque verification:** ~15 seconds per fastener

### Other Operations
- **Alignment verification:** ~30 seconds
- **Visual inspection:** ~30 seconds
- **Functional test:** ~60-120 seconds (depending on complexity)
- **Documentation:** ~30 seconds

---

## Estimation Method

### Step 1: List Operations
List all assembly operations in sequence.

### Step 2: Estimate Time
Estimate time for each operation using standard times.

### Step 3: Apply Complexity Factors
- **Simple:** Standard time × 1.0
- **Moderate:** Standard time × 1.2
- **Complex:** Standard time × 1.5
- **Very Complex:** Standard time × 2.0

### Step 4: Add Buffer
Add 20% buffer for unexpected issues.

### Step 5: Calculate Total
Sum all operation times.

---

## Assembly Time Estimation Template

```markdown
# Assembly Time Estimation: [Assembly Name]

**Date:** [Date]  
**Estimated By:** @DesignEng

## Assembly Operations

| Step | Operation | Standard Time | Complexity Factor | Estimated Time |
|------|-----------|---------------|-------------------|----------------|
| 1 | [Operation] | [Time] | [Factor] | [Time] |
| 2 | [Operation] | [Time] | [Factor] | [Time] |

## Total Time
- Sum of Operations: [Time] minutes
- Buffer (20%): [Time] minutes
- **Total Estimated Time:** [Time] minutes

## Notes
[Any special considerations]
```

---

## Related Documents

- DFA Checklist: `02_Design/manufacturing/DFA_checklist.md`
- DFA Review Process: `02_Design/manufacturing/DFA_review_process.md`

