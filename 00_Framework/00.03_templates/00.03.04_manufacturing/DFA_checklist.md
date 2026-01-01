# Design for Assembly (DFA) Checklist

**Purpose:** Ensure designs are optimized for assembly

**Owner:** @DesignEng  
**Version:** 1.0  
**Date:** 2024-12-22

---

## DFA Review Checklist

### Fastener Count
- [ ] Fastener count minimized
- [ ] Fasteners standardized (same size/type where possible)
- [ ] Fastener locations accessible
- [ ] Fastener installation tool access verified

### Self-Locating Features
- [ ] Self-locating features included (pins, guides, etc.)
- [ ] Parts cannot be assembled incorrectly
- [ ] Alignment features included
- [ ] No ambiguity in assembly orientation

### Assembly Sequence
- [ ] Assembly sequence logical
- [ ] Assembly sequence documented
- [ ] No interference during assembly
- [ ] Parts accessible during assembly
- [ ] Assembly can be done with standard tools

### Tool Access
- [ ] Tool access for fasteners verified
- [ ] Tool clearance adequate
- [ ] No blind fastening (if possible)
- [ ] Tool access documented

### Assembly Time
- [ ] Assembly time estimated
- [ ] Assembly time reasonable
- [ ] Time reduction opportunities identified

### Assembly Difficulty
- [ ] Assembly difficulty scored (1-5 scale)
- [ ] Average difficulty < 3.0
- [ ] High difficulty operations justified
- [ ] Difficulty reduction opportunities identified

### Serviceability
- [ ] Disassembly possible (if required)
- [ ] Service access adequate
- [ ] Service procedures documented
- [ ] Replacement parts accessible

### Error-Proofing
- [ ] Error-proofing features included
- [ ] Parts cannot be assembled incorrectly
- [ ] Visual indicators for correct orientation
- [ ] Asymmetric features prevent wrong orientation

---

## Assembly Time Estimation

**Standard Times:**
- Part placement: ~15 seconds
- Fastener installation: ~30 seconds per fastener
- Alignment: ~60 seconds
- Verification: ~30 seconds

**Estimation Method:**
1. List all assembly operations
2. Estimate time for each operation
3. Sum total assembly time
4. Add 20% buffer for complexity

**Documentation:** `02_Design/manufacturing/assembly_time_estimation.md`

---

## Assembly Difficulty Scoring

**Scale:** 1 (Easy) to 5 (Very Difficult)

**Scoring Criteria:**
- **1 - Easy:** Simple placement, no alignment needed
- **2 - Simple:** Basic alignment, standard tools
- **3 - Moderate:** Some alignment, multiple steps
- **4 - Difficult:** Complex alignment, special tools
- **5 - Very Difficult:** Multiple complex steps, special skills

**Target:** Average difficulty < 3.0

---

## DFA Review Results

**Assembly:** [Assembly Name]  
**Review Date:** [Date]  
**Reviewed By:** @DesignEng

**Assembly Time:** [Time] minutes  
**Assembly Difficulty:** [Average Score] / 5.0

**Issues Identified:**
1. [Issue 1]
2. [Issue 2]

**Recommendations:**
1. [Recommendation 1]
2. [Recommendation 2]

**Status:** [ ] Pass | [ ] Pass with Recommendations | [ ] Fail - Redesign Required

---

## Related Documents

- DFA Review Process: `02_Design/manufacturing/DFA_review_process.md`
- Assembly Time Estimation: `02_Design/manufacturing/assembly_time_estimation.md`

