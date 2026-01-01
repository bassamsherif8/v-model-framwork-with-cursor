# Engineering Change Order (ECO) Process

**Purpose:** Manage and control changes to designs after production release

**Owner:** @SeniorEng  
**Version:** 1.0  
**Date:** 2024-12-22

---

## Overview

Once a design is released for production (PROD-v1.0), all changes must go through the Engineering Change Order (ECO) process. This ensures:
- Changes are properly evaluated
- Impact is assessed (technical, cost, schedule)
- Changes are approved before implementation
- Change history is tracked

---

## Change Classification

### Minor Changes (A001 → A002)
**Definition:** Changes that do not affect form, fit, or function

**Examples:**
- Documentation corrections (typos, clarifications)
- Non-functional cosmetic changes
- Drawing updates (better clarity, no dimension changes)
- Material notes updates (no material change)

**Process:**
- ECO required
- Impact analysis required
- @SeniorEng approval required
- Revision: Increment number (A001 → A002)

### Major Changes (A001 → B001)
**Definition:** Changes that affect form, fit, or function

**Examples:**
- Dimension changes
- Material changes
- Design modifications
- Tolerance changes
- GD&T changes

**Process:**
- ECO required
- Comprehensive impact analysis required
- @SeniorEng approval required
- May require Pre-Production Review
- Revision: Increment letter (A001 → B001)

---

## ECO Process Steps

### 1. Change Request
- **Who:** Anyone (DesignEng, Builder, Skeptic, Supplier, etc.)
- **What:** Document change request
- **Where:** `02_Design/production/ECO_requests/ECO-[Number].md`
- **Format:** Use ECO template

### 2. Impact Analysis
- **Who:** @SeniorEng (with input from @DesignEng, @Skeptic)
- **What:** Analyze impact of proposed change
- **Consider:**
  - **Technical Impact:**
    - Design changes required
    - Manufacturing changes required
    - Assembly changes required
    - Tooling changes required
  - **Cost Impact:**
    - Material cost changes
    - Tooling cost changes
    - Rework cost (if parts already produced)
    - Scrap cost (if parts must be scrapped)
  - **Schedule Impact:**
    - Lead time changes
    - Delivery impact
    - Production delay
  - **Risk Assessment:**
    - Quality risks
    - Reliability risks
    - Performance risks

### 3. ECO Review
- **Who:** @SeniorEng
- **What:** Review impact analysis and make decision
- **Decision:** Approve, Reject, or Request More Information

### 4. Implementation
- **Who:** @DesignEng (design changes), @Builder (if code changes)
- **What:** Implement approved changes
- **Update:** All affected documentation

### 5. Verification
- **Who:** @Skeptic
- **What:** Verify changes meet requirements
- **Update:** Test documentation

### 6. ECO Closure
- **Who:** @SeniorEng
- **What:** Close ECO and update revision
- **Update:** ECO log and release new version

---

## ECO Template

```markdown
# ECO-[Number]: [Change Description]

**Date:** [Date]  
**Requested By:** [Name/Role]  
**Status:** [Pending | Under Review | Approved | Rejected | Implemented | Closed]

## Change Description

[Detailed description of requested change]

## Reason for Change

[Why is this change needed?]

## Impact Analysis

### Technical Impact
- [ ] Design changes required
- [ ] Manufacturing changes required
- [ ] Assembly changes required
- [ ] Tooling changes required
- [Details]

### Cost Impact
- Material cost: [Change]
- Tooling cost: [Change]
- Rework cost: [If applicable]
- Scrap cost: [If applicable]
- Total cost impact: [Total]

### Schedule Impact
- Lead time change: [Days]
- Delivery impact: [Description]
- Production delay: [Days]

### Risk Assessment
- Quality risks: [Description]
- Reliability risks: [Description]
- Performance risks: [Description]

## Affected Parts

| Part Number | Part Name | Current Revision | Proposed Revision |
|-------------|-----------|------------------|-------------------|
| [PART-001] | [Name] | A001 | A002 |

## Approval

**@SeniorEng Review:**
- [ ] Impact analysis complete
- [ ] Change approved / rejected
- [ ] Revision level assigned

**Signature:** _________________  
**Date:** _________________

## Implementation

- [ ] Changes implemented
- [ ] Documentation updated
- [ ] Verification complete
- [ ] ECO closed

**Implemented By:** [Name]  
**Date:** [Date]  
**New Revision:** [Revision]
```

---

## ECO Log

Track all ECOs in: `02_Design/production/ECO_log.md`

**Format:**
| ECO Number | Date | Description | Status | Revision Change |
|------------|------|-------------|--------|-----------------|
| ECO-001 | [Date] | [Description] | [Status] | A001 → A002 |

---

## Revision Control Rules

### Revision Format
- Format: `[Letter][Number][Number][Number]`
- Example: A001, A002, B001, B002

### Revision Increment Rules
- **Minor Change:** Increment number (A001 → A002)
- **Major Change:** Increment letter (A001 → B001)

### When to Increment
- **A001 → A002:** Documentation, non-functional changes
- **A001 → B001:** Functional changes, design modifications

---

## Change Tracking

All changes must be tracked in:
- ECO log: `02_Design/production/ECO_log.md`
- Part revision history: In part documentation
- Release notes: In release documentation

---

## Approval Authority

**@SeniorEng** has final approval authority for all ECOs.

**Approval Criteria:**
- Impact analysis complete
- Risks assessed
- Cost justified
- Schedule acceptable
- Change necessary

---

## Emergency Changes

For emergency changes (safety, critical defects):
- ECO still required
- Expedited review process
- May implement before full approval (with justification)
- Full documentation required after implementation

---

## Related Documents

- Change Management Workflow: `02_Design/production/change_management_workflow.md`
- Release Gate Checklist: `02_Design/production/release_gate_checklist.md`
- Release Documentation: `02_Design/production/release_documentation_template.md`

