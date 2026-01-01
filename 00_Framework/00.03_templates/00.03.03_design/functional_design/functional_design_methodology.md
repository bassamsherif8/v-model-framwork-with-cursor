# Functional Design Methodology

**Purpose:** Comprehensive methodology for functional design of mechanical parts

**Owner:** @DesignEng  
**Version:** 1.0  
**Date:** 2025-12-30

---

## Overview

Functional design is the process of designing parts based on their intended function, loads, and interfaces. This methodology ensures parts are designed for their purpose, not just manufacturability.

**CRITICAL:** Functional design MUST be completed before detailed geometry design.

---

## Functional Design Process

### Step 1: Functional Requirements Analysis

**Purpose:** Understand what the part needs to do

**Activities:**
1. **Identify Function:**
   - What is the part's primary function?
   - What role does it play in the system?
   - What problem does it solve?

2. **Identify Loads:**
   - Static loads (weight, preload)
   - Dynamic loads (vibration, impact, fatigue)
   - Thermal loads (expansion, contraction)
   - Environmental loads (wind, water, chemicals)

3. **Identify Constraints:**
   - Geometric constraints (size, shape, space)
   - Material constraints (availability, cost, properties)
   - Manufacturing constraints (process, capability)
   - Assembly constraints (access, sequence)

4. **Review Against Project Plan:**
   - Verify compliance with all relevant REQ-XXX requirements
   - Check consistency with overall project plan
   - Verify interface requirements

**Output:** Functional requirements document

---

### Step 2: Load Analysis

**Purpose:** Quantify loads and design load paths

**Activities:**
1. **Create Force Diagrams:**
   - Free Body Diagrams (FBD) for part
   - Identify all forces and moments
   - Identify support reactions
   - Identify internal forces

2. **Calculate Expected Loads:**
   - Forces (N, lbf)
   - Moments (N·m, lbf·in)
   - Torques (N·m, lbf·in)
   - Pressures (Pa, psi)

3. **Identify Load Paths:**
   - Direct load paths (most efficient)
   - Indirect load paths (less efficient)
   - Load concentration points
   - Stress concentration areas

4. **Calculate Stress:**
   - Normal stress (σ = F/A)
   - Shear stress (τ = F/A)
   - Bending stress (σ = Mc/I)
   - Torsional stress (τ = Tr/J)

**Output:** Load analysis document with FBDs and calculations

---

### Step 3: Interface Design

**Purpose:** Design how parts connect and interact

**Activities:**
1. **Design Connection Interfaces:**
   - Mounting points (holes, threads, slots)
   - Mating surfaces (flat, curved, angled)
   - Alignment features (pins, keys, slots)
   - Sealing surfaces (O-rings, gaskets)

2. **Verify Mounting Features:**
   - Hole sizes and tolerances
   - Thread specifications
   - Clearances and fits
   - Fastener selection

3. **Check Alignment Requirements:**
   - Positional tolerances
   - Angular tolerances
   - Parallelism/perpendicularity
   - Concentricity

4. **Design for Assembly (DFA):**
   - Assembly sequence
   - Tool access
   - Part orientation
   - Fastener accessibility

5. **Review Against Assembly Requirements:**
   - Verify compatibility with mating parts
   - Check clearance/interference
   - Verify interface specifications

**Output:** Interface design document

---

### Step 4: Structural Design

**Purpose:** Design part to withstand loads efficiently

**Activities:**
1. **Design Load Paths:**
   - Direct paths from load to support
   - Minimize path length
   - Avoid sharp turns
   - Distribute loads evenly

2. **Add Reinforcements:**
   - **Gussets:** Triangular reinforcements at joints
     - Size based on load (typically 0.5-1× material thickness)
     - Place at stress concentration points
   - **Ribs:** Longitudinal reinforcements for stiffness
     - Height: 2-3× material thickness
     - Spacing: 3-5× rib height
   - **Fillets:** Rounded corners to reduce stress concentration
     - Minimum radius: 2mm (0.08")
     - Larger for high stress areas
   - **Chamfers:** Angled edges for assembly and stress relief
     - Typical: 45° angle, 1-2mm size

3. **Optimize Geometry:**
   - Remove material where loads are low
   - Add material where loads are high
   - Optimize for strength/weight ratio
   - Consider topology optimization

4. **Verify Structural Adequacy:**
   - Hand calculations (simplified models)
   - Finite Element Analysis (FEA) for complex parts
   - Safety factors (typically 2-4 for static, higher for dynamic)
   - Deflection limits

5. **Material Selection:**
   - Based on loads and requirements
   - Consider strength, stiffness, weight, cost
   - Consider manufacturing process
   - Consider environmental factors

**Output:** Structural design document with calculations

---

### Step 5: Project Plan Compliance Review

**Purpose:** Verify design meets all project requirements

**Activities:**
1. **Review Against Requirements:**
   - All functional requirements (REQ-XXX)
   - All performance requirements
   - All interface requirements
   - All safety requirements

2. **Check Consistency:**
   - With other parts in project
   - With assembly requirements
   - With overall project plan

3. **Document Deviations:**
   - Identify any deviations
   - Justify deviations
   - Assess impact
   - Obtain approval if needed

4. **Use Automated Reviewer:**
   - Run `02_Design/compliance/project_plan_reviewer.py`
   - Generate compliance report
   - Address any issues

**Output:** Compliance report

---

## Design Principles

### Load Path Design

**Direct Load Paths:**
- Shortest path from load to support
- Minimizes material usage
- Reduces stress
- Example: Direct connection from load point to mounting point

**Distributed Load Paths:**
- Spread load over larger area
- Reduces stress concentration
- Improves strength
- Example: Load spread through gussets

### Stress Concentration Minimization

**Fillets:**
- Minimum radius: 2mm (0.08")
- Larger for high stress areas
- Reduces stress concentration factor (Kt)

**Chamfers:**
- 45° typical
- Size: 1-2mm typical
- Reduces sharp edges

**Hole Design:**
- Avoid sharp corners
- Use fillets at hole edges
- Consider stress concentration around holes

### Reinforcement Design

**Gussets:**
- Triangular reinforcements
- Size: 0.5-1× material thickness
- Place at joints and load points
- Angle: 30-45° typical

**Ribs:**
- Longitudinal reinforcements
- Height: 2-3× material thickness
- Spacing: 3-5× rib height
- Improves stiffness

**Bosses:**
- Raised features for mounting
- Height: Based on fastener length
- Diameter: Based on fastener size
- Adds strength at mounting points

---

## Examples

### Bracket Design

**Function:** Support load at distance from mounting point

**Load Analysis:**
- Load: 1000N at 100mm from mounting
- Moment: 100N·m
- Support: 4 bolts at corners

**Load Path:**
- Direct path from load point to mounting bolts
- Gussets at corners to distribute load
- Ribs along length for stiffness

**Structural Design:**
- Base plate: 10mm thick (based on bending stress)
- Gussets: 8mm thick, 30mm height
- Ribs: 5mm thick, 20mm height
- Fillets: R3mm at all corners

### Mount Design

**Function:** Mount component with vibration isolation

**Load Analysis:**
- Weight: 50kg (500N)
- Vibration: 10g acceleration
- Dynamic load: 5000N

**Load Path:**
- Distributed through mounting points
- Vibration isolation pads
- Reinforced mounting structure

**Structural Design:**
- Mounting plate: 12mm thick
- Gussets at mounting points
- Ribs for stiffness
- Vibration isolation features

### Frame Design

**Function:** Support structure for system

**Load Analysis:**
- Distributed load: 5000N total
- Point loads: 1000N at specific points
- Bending and torsion

**Load Path:**
- Through structural members
- Through joints (welded/bolted)
- Through cross-members

**Structural Design:**
- Member sizing based on loads
- Joint design (welded/bolted)
- Cross-member spacing (based on deflection)
- Gussets at joints

---

## Tools and Resources

### Analysis Tools

**Hand Calculations:**
- Stress calculations (σ = F/A, σ = Mc/I)
- Deflection calculations (δ = FL³/(3EI))
- Safety factor calculations

**FEA Software:**
- FreeCAD (built-in FEA)
- OpenFOAM
- CalculiX
- Commercial: ANSYS, SolidWorks Simulation

### Design Tools

**CAD Software:**
- build123d (Python-based)
- FreeCAD
- OpenSCAD
- Commercial: SolidWorks, Inventor, CATIA

### Reference Materials

**Standards:**
- ASME Y14.5: Geometric Dimensioning and Tolerancing
- ISO 2768: General Tolerances
- AWS D1.1: Structural Steel Welding
- Machinery's Handbook

**Textbooks:**
- Shigley's Mechanical Engineering Design
- Roark's Formulas for Stress and Strain
- Design of Machine Elements

---

## Documentation Requirements

Each part MUST have a functional design document: `[part_number]_functional_design.md`

**Required Sections:**
1. Functional Requirements
2. Load Analysis (with FBDs)
3. Interface Design
4. Structural Design (with calculations)
5. Project Plan Compliance Review
6. Design Rationale

**Template:** See `02_Design/functional_design/templates/functional_design_template.md`

---

## References

- Project Plan Reviewer: `02_Design/compliance/project_plan_reviewer.py`
- Process-Specific Design Guidelines: `02_Design/manufacturing/process_specific_design_guidelines.md`
- Functional Design Checklist: `02_Design/functional_design/functional_design_checklist.md`

