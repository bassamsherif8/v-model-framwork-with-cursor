# Functional Design Checklist

**Purpose:** Mandatory checklist for functional design of mechanical parts

**Owner:** @DesignEng  
**Version:** 1.0  
**Date:** 2025-12-30

---

## Usage

This checklist MUST be completed for each part before proceeding to manufacturing-ready design. Functional design MUST be completed before detailed geometry design.

---

## Checklist Items

### Functional Requirements

- [ ] Functional requirements identified and documented
- [ ] Part function clearly defined
- [ ] Role in system understood
- [ ] Loads identified (static, dynamic, thermal, environmental)
- [ ] Constraints identified (geometric, material, manufacturing, assembly)
- [ ] Review against project plan completed
- [ ] All relevant REQ-XXX requirements verified
- [ ] Functional requirements documented in `[part_number]_functional_design.md`

### Load Analysis

- [ ] Loads analyzed (forces, moments, constraints)
- [ ] Free Body Diagrams (FBD) created
- [ ] Expected loads calculated
- [ ] Load paths identified
- [ ] Stress concentrations identified
- [ ] Load analysis documented with calculations

### Interface Design

- [ ] Interfaces properly designed
- [ ] Connection interfaces designed (mounting points, mating surfaces)
- [ ] Mounting features verified (holes, threads, clearances)
- [ ] Alignment requirements checked
- [ ] Design for Assembly (DFA) considered
- [ ] Review against assembly requirements completed
- [ ] Interface compatibility verified with mating parts
- [ ] Interface design documented

### Structural Design

- [ ] Load paths designed and verified
- [ ] Structural adequacy verified (hand calc or FEA)
- [ ] Stress concentrations minimized (fillets, chamfers)
- [ ] Geometry optimized for function (not just manufacturability)
- [ ] Reinforcements added (gussets, ribs, fillets)
  - [ ] Gussets at joints and load points
  - [ ] Ribs for stiffness (if needed)
  - [ ] Fillets at stress concentrations (minimum R2mm)
  - [ ] Chamfers for assembly and stress relief
- [ ] Material selection justified based on loads
- [ ] Safety factors appropriate for application
- [ ] Deflection limits satisfied (if applicable)
- [ ] Weight optimization considered (if applicable)
- [ ] Structural design documented with calculations

### Project Plan Compliance

- [ ] Project plan compliance verified
- [ ] All requirements (REQ-XXX) met
- [ ] Consistency with other parts verified
- [ ] Interface compatibility verified
- [ ] Automated reviewer used: `02_Design/compliance/project_plan_reviewer.py`
- [ ] Compliance report generated
- [ ] Any deviations documented and justified

### Documentation

- [ ] Functional design document created: `[part_number]_functional_design.md`
- [ ] All required sections included:
  - [ ] Functional Requirements
  - [ ] Load Analysis (with FBDs)
  - [ ] Interface Design
  - [ ] Structural Design (with calculations)
  - [ ] Project Plan Compliance Review
  - [ ] Design Rationale
- [ ] Calculations documented
- [ ] FBDs included
- [ ] Design rationale explained

---

## Review Process

1. **Complete Functional Requirements:**
   - Identify function, loads, constraints
   - Review against project plan
   - Document in functional design document

2. **Complete Load Analysis:**
   - Create FBDs
   - Calculate loads
   - Identify load paths
   - Document calculations

3. **Complete Interface Design:**
   - Design connection interfaces
   - Verify mounting features
   - Check alignment requirements
   - Document interface design

4. **Complete Structural Design:**
   - Design load paths
   - Add reinforcements
   - Verify structural adequacy
   - Document structural design

5. **Complete Project Plan Compliance:**
   - Review against all requirements
   - Check consistency
   - Run automated reviewer
   - Document compliance status

6. **Complete Documentation:**
   - Create functional design document
   - Include all required sections
   - Document calculations and rationale

7. **Review and Approval:**
   - Review completed checklist
   - Verify all items completed
   - Obtain approval if needed
   - Proceed to manufacturing-ready design

---

## Blocking Criteria

**BLOCKING (Cannot proceed to manufacturing-ready design):**
- Functional requirements not identified
- Loads not analyzed
- Structural adequacy not verified
- Major project plan non-compliance
- Critical interface incompatibility

**NON-BLOCKING (Can proceed with documentation):**
- Minor documentation incomplete (can be completed later)
- Non-critical interface clarification
- Minor deviation with justification

---

## References

- Functional Design Methodology: `02_Design/functional_design/functional_design_methodology.md`
- Structural Design Methodology: `02_Design/functional_design/structural_design_methodology.md`
- Project Plan Reviewer: `02_Design/compliance/project_plan_reviewer.py`
- Process-Specific Design Guidelines: `02_Design/manufacturing/process_specific_design_guidelines.md`

