# Assembly Instructions
## Delta CNC Mechanism

**Assembly:** DCNC-DELTA-ASSY-A001  
**Date:** 2024-12-22  
**Version:** 1.0  
**Status:** Active

---

## Assembly Overview

This document provides step-by-step assembly instructions for the Delta CNC mechanism. Follow these instructions carefully to ensure proper assembly and alignment.

**Required Tools:**
- Torque wrench (8-10 N⋅m range)
- Precision square
- Dial indicator or CMM (for alignment verification)
- Thread locking compound (Loctite 243 or equivalent)
- Clean room or clean work area
- Precision measurement tools (calipers, micrometers)

**Required Parts:**
- 1x Base Platform (DCNC-BASE-PLATFORM-A001)
- 3x Actuator Mounts (DCNC-ACTUATOR-ACT-MOUNT-A001)
- 3x Upper Arms (DCNC-ARM-UPPER-ARM-A001)
- 3x Lower Arms (DCNC-ARM-LOWER-ARM-A001)
- 1x End-Effector (DCNC-END-EFFECTOR-A001)
- 6x Ball Joints (DCNC-JOINT-BALL-JOINT-A001)
- 12x M6x1.0 bolts (for mounting)
- Thread locking compound

---

## Pre-Assembly Inspection

**Before beginning assembly, verify:**

1. **Base Platform:**
   - [ ] Flatness of top surface verified (Datum A): ≤0.05mm
   - [ ] Actuator mount holes positioned at 120° ±0.02° spacing
   - [ ] All dimensions within tolerance

2. **Actuator Mounts (3x):**
   - [ ] All three mounts identical
   - [ ] Actuator hole concentricity: ≤0.02mm
   - [ ] Mounting surface perpendicularity: ≤0.02mm

3. **Arms:**
   - [ ] Upper arms: All three lengths match within ±0.02mm
   - [ ] Lower arms: All three lengths match within ±0.02mm
   - [ ] Straightness verified: ≤0.02mm per 100mm
   - [ ] Roundness verified: ≤0.01mm

4. **End-Effector:**
   - [ ] Flatness verified: ≤0.02mm
   - [ ] Arm mount positions at 120° ±0.02° spacing
   - [ ] Spindle hole concentricity: ≤0.05mm

5. **Ball Joints (6x):**
   - [ ] All six joints identical
   - [ ] Ball diameter: 16mm ±0.005mm
   - [ ] Socket clearance: 0.01-0.02mm

---

## Assembly Sequence

### Step 1: Base Platform Preparation

**Objective:** Verify base platform flatness and prepare for actuator mount installation.

1. Place base platform on flat surface (granite surface plate or equivalent)
2. Verify flatness of top surface using dial indicator or CMM
   - **Requirement:** Flatness ≤0.05mm (Datum A)
   - **Acceptance:** If flatness exceeds 0.05mm, part must be reworked or rejected
3. Mark Datum A (top surface) for reference
4. Mark center of base platform (Datum B - center axis)
5. Mark 0° reference position (Datum C - angular reference)

**Inspection Checkpoint:** Base platform flatness verified and datums marked.

---

### Step 2: Actuator Mount Installation

**Objective:** Install three actuator mounts at 120° spacing with precise alignment.

1. **Position First Actuator Mount:**
   - Position at 0° (reference position)
   - Align mounting holes with base platform holes
   - Verify perpendicularity of mounting surface to Datum A

2. **Install First Actuator Mount:**
   - Apply thread locking compound to M6 bolts
   - Install bolts hand-tight
   - Torque to 8-10 N⋅m
   - Verify mounting surface perpendicularity: ≤0.02mm

3. **Position Second Actuator Mount:**
   - Position at 120° from first mount
   - Verify angular spacing: 120° ±0.02°
   - Align mounting holes

4. **Install Second Actuator Mount:**
   - Apply thread locking compound
   - Install bolts hand-tight
   - Torque to 8-10 N⋅m
   - Verify perpendicularity and angular spacing

5. **Position Third Actuator Mount:**
   - Position at 240° (120° from second mount)
   - Verify angular spacing: 120° ±0.02°
   - Align mounting holes

6. **Install Third Actuator Mount:**
   - Apply thread locking compound
   - Install bolts hand-tight
   - Torque to 8-10 N⋅m
   - Verify perpendicularity and angular spacing

7. **Verify Actuator Mount Alignment:**
   - Measure angular spacing between all three mounts
   - **Requirement:** 120° ±0.02° between each pair
   - Verify concentricity of actuator holes: ≤0.02mm relative to Datum A

**Inspection Checkpoint:** All three actuator mounts installed and aligned.

---

### Step 3: Actuator Installation

**Objective:** Install actuators into actuator mounts (if actuators are part of assembly).

**Note:** This step assumes actuators are separate components. If actuators are integrated, skip this step.

1. **Prepare Actuators:**
   - Verify actuator specifications match requirements
   - Clean actuator mounting surfaces

2. **Install Actuators:**
   - Insert actuator into each actuator mount hole
   - Verify fit: Actuator hole diameter 50mm ±0.02mm
   - Secure actuators per actuator manufacturer specifications

3. **Verify Actuator Alignment:**
   - Verify actuators are parallel to each other
   - Verify actuators are perpendicular to base platform (Datum A)

**Inspection Checkpoint:** Actuators installed and aligned.

---

### Step 4: Upper Arm Installation

**Objective:** Install three upper arms with length consistency verification.

1. **Prepare Upper Arms:**
   - Verify all three arms have identical length: 200mm ±0.02mm
   - Verify straightness: ≤0.02mm per 100mm
   - Verify roundness: ≤0.01mm

2. **Install Upper Arms:**
   - Attach upper arm to actuator mount (via ball joint)
   - Verify ball joint clearance: 0.01-0.02mm
   - Secure connection per joint specifications

3. **Verify Upper Arm Installation:**
   - Verify all three arms are parallel: ≤0.02mm
   - Verify arm lengths match: ±0.02mm
   - Verify joint operation (smooth movement)

**Inspection Checkpoint:** Upper arms installed and verified.

---

### Step 5: Lower Arm Installation

**Objective:** Install three lower arms with length consistency verification.

1. **Prepare Lower Arms:**
   - Verify all three arms have identical length: 250mm ±0.02mm
   - Verify straightness: ≤0.02mm per 100mm
   - Verify roundness: ≤0.01mm

2. **Install Lower Arms:**
   - Attach lower arm to upper arm (via ball joint)
   - Attach lower arm to end-effector (via ball joint)
   - Verify ball joint clearance: 0.01-0.02mm
   - Secure connections per joint specifications

3. **Verify Lower Arm Installation:**
   - Verify all three arms are parallel: ≤0.02mm
   - Verify arm lengths match: ±0.02mm
   - Verify joint operation (smooth movement)

**Inspection Checkpoint:** Lower arms installed and verified.

---

### Step 6: End-Effector Installation

**Objective:** Install end-effector with precise arm mount alignment.

1. **Prepare End-Effector:**
   - Verify flatness: ≤0.02mm
   - Verify arm mount positions: 120° ±0.02° spacing
   - Verify spindle hole concentricity: ≤0.05mm

2. **Install End-Effector:**
   - Attach end-effector to lower arms (via ball joints)
   - Verify all three arm connections are secure
   - Verify arm mount angular spacing: 120° ±0.02°

3. **Verify End-Effector Installation:**
   - Verify end-effector flatness maintained: ≤0.02mm
   - Verify arm mount positions: 120° ±0.02°
   - Verify end-effector can move freely through workspace

**Inspection Checkpoint:** End-effector installed and verified.

---

### Step 7: Final Alignment and Calibration

**Objective:** Verify complete assembly alignment and prepare for calibration.

1. **Verify Assembly Alignment:**
   - Verify actuator mount angular spacing: 120° ±0.02°
   - Verify arm lengths: Upper arms ±0.02mm, Lower arms ±0.02mm
   - Verify end-effector arm mount spacing: 120° ±0.02°
   - Verify all joints operate smoothly

2. **Verify Workspace:**
   - Command end-effector to all corners of 300mm × 300mm × 300mm workspace
   - Verify no mechanical interference
   - Verify smooth motion throughout workspace

3. **Calibration:**
   - Perform kinematic calibration (forward and inverse kinematics)
   - Verify positioning accuracy: ±0.05mm (REQ-005)
   - Verify repeatability: ±0.02mm (REQ-006)

**Inspection Checkpoint:** Assembly complete and calibrated.

---

## Torque Specifications

| Fastener | Torque | Notes |
|----------|--------|-------|
| M6 mounting bolts (base to actuator mounts) | 8-10 N⋅m | Apply thread locking compound |
| M6 mounting bolts (actuator mounts) | 8-10 N⋅m | Apply thread locking compound |
| Critical fasteners | Per specification | See assembly notes |

**Thread Locking Compound:**
- Use Loctite 243 or equivalent for all M6 mounting bolts
- Apply to threads before installation
- Allow curing time per manufacturer specifications

---

## Alignment Procedures

### Actuator Mount Angular Alignment

**Procedure:**
1. Mark center of base platform (Datum B)
2. Mark 0° reference position (Datum C)
3. Measure angular position of each actuator mount
4. Verify spacing: 120° ±0.02° between each pair
5. Adjust if necessary (may require re-machining if out of tolerance)

**Measurement Method:**
- Use precision angle measurement tool or CMM
- Measure from center of base platform to center of each actuator mount
- Calculate angular spacing

### Arm Length Verification

**Procedure:**
1. Measure length of each upper arm
2. Verify all three match within ±0.02mm
3. Measure length of each lower arm
4. Verify all three match within ±0.02mm

**Measurement Method:**
- Use precision calipers or CMM
- Measure from joint center to joint center
- Record measurements and compare

### End-Effector Arm Mount Alignment

**Procedure:**
1. Mark center of end-effector
2. Measure angular position of each arm mount
3. Verify spacing: 120° ±0.02° between each pair
4. Adjust if necessary

**Measurement Method:**
- Use precision angle measurement tool or CMM
- Measure from center of end-effector to center of each arm mount
- Calculate angular spacing

---

## Troubleshooting

### Problem: Actuator Mount Angular Spacing Out of Tolerance

**Symptoms:** Angular spacing not 120° ±0.02°

**Possible Causes:**
- Base platform holes not positioned correctly
- Actuator mount installation error

**Solutions:**
1. Verify base platform hole positions
2. Re-install actuator mounts with careful alignment
3. If base platform is out of tolerance, part must be reworked or rejected

### Problem: Arm Lengths Don't Match

**Symptoms:** Arms have different lengths outside ±0.02mm tolerance

**Possible Causes:**
- Manufacturing error in arm lengths
- Measurement error

**Solutions:**
1. Re-measure all arms using precision tools
2. If arms are out of tolerance, parts must be reworked or rejected
3. Verify measurement method and tools

### Problem: End-Effector Not Moving Smoothly

**Symptoms:** Jerky motion or binding

**Possible Causes:**
- Ball joint clearance incorrect
- Arm alignment issues
- Joint contamination

**Solutions:**
1. Verify ball joint clearance: 0.01-0.02mm
2. Check arm alignment and parallelism
3. Clean joints and re-lubricate if necessary
4. Verify joint installation

---

## Safety Notes

1. **Personal Protective Equipment:**
   - Safety glasses required during assembly
   - Gloves recommended when handling parts

2. **Work Area:**
   - Clean, well-lit work area
   - Adequate space for assembly
   - Secure work surface

3. **Tool Safety:**
   - Use tools only for intended purposes
   - Verify torque wrench calibration
   - Use proper tool sizes

4. **Part Handling:**
   - Handle precision parts carefully
   - Avoid dropping or damaging parts
   - Clean parts before assembly

---

**Document Control:**
- **Owner:** @DesignEng
- **Reviewer:** @SeniorEng, @Skeptic
- **Last Updated:** 2024-12-22
- **Next Review:** After first assembly

