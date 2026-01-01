# Manufacturing Process Selection Matrix

**Purpose:** Guide selection of appropriate manufacturing process

**Owner:** @DesignEng  
**Version:** 1.0  
**Date:** 2024-12-22

---

## Process Comparison Matrix

| Criteria | CNC Machining | 3D Printing (FDM) | 3D Printing (SLA) | 3D Printing (SLS) | Sheet Metal | Casting |
|----------|---------------|-------------------|-------------------|-------------------|-------------|---------|
| **Tolerance** | ±0.001" | ±0.005" | ±0.002" | ±0.003" | ±0.005" | ±0.010" |
| **Surface Finish** | Ra 0.8-1.6μm | Ra 3-10μm | Ra 0.5-2μm | Ra 2-5μm | Ra 1.6-3.2μm | Ra 3-6μm |
| **Material Options** | Wide | Limited | Limited | Limited | Metals | Wide |
| **Setup Cost** | High | Low | Low | Medium | Medium | Very High |
| **Unit Cost (Low Qty)** | High | Low | Medium | Medium | Medium | Very High |
| **Unit Cost (High Qty)** | Low | High | High | High | Low | Very Low |
| **Lead Time** | 1-2 weeks | 1-3 days | 1-3 days | 3-5 days | 1-2 weeks | 3-6 weeks |
| **MOQ** | 1-10 | 1 | 1 | 1 | 10-100 | 100+ |
| **Complexity** | Medium | High | High | High | Low | Medium |
| **Max Size** | Large | Medium | Medium | Medium | Large | Large |

---

## Selection Guidelines

### CNC Machining
**Best For:**
- High precision requirements (±0.001" or better)
- Good surface finish (Ra < 1.6μm)
- Medium to high quantities (10+)
- Wide material selection needed
- Metal parts

**Not Suitable For:**
- Very low quantities (1-5)
- Very complex internal geometries
- Rapid prototyping

---

### 3D Printing (FDM)
**Best For:**
- Rapid prototyping
- Low quantities (1-10)
- Complex geometries
- Non-functional prototypes
- Low cost requirements

**Not Suitable For:**
- High precision (±0.001")
- Good surface finish
- Production quantities
- High strength requirements

---

### 3D Printing (SLA)
**Best For:**
- Rapid prototyping
- Good surface finish needed
- Complex geometries
- Visual prototypes
- Low quantities

**Not Suitable For:**
- Production quantities
- High strength
- High temperature
- Long-term durability

---

### 3D Printing (SLS)
**Best For:**
- Functional prototypes
- Complex geometries
- No support structures needed
- Medium quantities (1-50)

**Not Suitable For:**
- High precision
- Production quantities
- Very large parts

---

### Sheet Metal
**Best For:**
- Thin-walled parts
- Enclosures, brackets
- Medium quantities (10-1000)
- Low cost
- Fast lead time

**Not Suitable For:**
- Thick parts (>10mm)
- Complex 3D geometries
- Very high precision

---

### Casting
**Best For:**
- High quantities (100+)
- Complex geometries
- Low unit cost (at volume)
- Wide material selection

**Not Suitable For:**
- Low quantities
- Fast lead time
- High precision
- Low setup cost

---

## Selection Process

### Step 1: Define Requirements
- Quantity
- Tolerance
- Surface finish
- Material
- Lead time
- Cost target

### Step 2: Evaluate Options
- Compare processes using matrix
- Eliminate unsuitable processes
- Score remaining options

### Step 3: Cost Analysis
- Calculate setup cost
- Calculate unit cost
- Calculate total cost
- Consider break-even point

### Step 4: Select Process
- Best fit for requirements
- Document selection
- Justify selection

---

## Process Selection Template

```markdown
# Process Selection: [Part Number] - [Part Name]

**Date:** [Date]  
**Selected By:** @DesignEng

## Requirements
- Quantity: [Number]
- Tolerance: [Tolerance]
- Surface Finish: [Ra value]
- Material: [Material]
- Lead Time: [Time]
- Cost Target: [Cost]

## Process Evaluation

| Process | Score | Notes |
|---------|-------|-------|
| CNC Machining | [Score] | [Notes] |
| 3D Printing | [Score] | [Notes] |
| Sheet Metal | [Score] | [Notes] |
| Casting | [Score] | [Notes] |

## Selected Process
- **Process:** [Process Name]
- **Justification:** [Why this process?]

## Cost Analysis
- Setup Cost: [Cost]
- Unit Cost: [Cost]
- Total Cost: [Cost]
- Break-Even: [Quantity]

## Next Steps
- [ ] Tooling requirements identified
- [ ] Lead time confirmed
- [ ] Cost verified
```

---

## Related Documents

- Tooling Requirements: `02_Design/manufacturing/tooling_requirements.md`
- Lead Time Estimation: `02_Design/manufacturing/lead_time_estimation.md`

