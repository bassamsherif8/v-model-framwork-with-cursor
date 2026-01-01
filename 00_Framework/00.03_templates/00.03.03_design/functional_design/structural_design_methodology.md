# Structural Design Methodology

**Purpose:** Methodology for structural design of mechanical parts

**Owner:** @DesignEng  
**Version:** 1.0  
**Date:** 2025-12-30

---

## Overview

Structural design ensures parts can withstand expected loads with appropriate safety factors. This methodology covers load path design, stress analysis, reinforcement design, and material selection.

---

## Load Path Design

### Principles

**Direct Load Paths:**
- Shortest path from load to support
- Minimizes material usage
- Reduces stress
- Most efficient

**Example:**
```
Load → Direct connection → Support
```

**Distributed Load Paths:**
- Spread load over larger area
- Reduces stress concentration
- Improves strength
- Better for high loads

**Example:**
```
Load → Gussets → Base → Support
```

### Load Path Optimization

**Minimize Path Length:**
- Shorter paths = less material
- Shorter paths = less deflection
- Direct connections preferred

**Avoid Sharp Turns:**
- Sharp turns = stress concentration
- Use fillets at corners
- Smooth transitions

**Distribute Loads:**
- Multiple load paths
- Reduces stress in any one path
- Improves reliability

---

## Stress Analysis Basics

### Stress Types

**Normal Stress (σ):**
- Tensile: σ = F/A (positive)
- Compressive: σ = -F/A (negative)
- Units: Pa (N/m²), psi (lbf/in²)

**Shear Stress (τ):**
- τ = F/A
- Units: Pa, psi

**Bending Stress (σ):**
- σ = Mc/I
- M = moment (N·m, lbf·in)
- c = distance from neutral axis (m, in)
- I = moment of inertia (m⁴, in⁴)

**Torsional Stress (τ):**
- τ = Tr/J
- T = torque (N·m, lbf·in)
- r = radius (m, in)
- J = polar moment of inertia (m⁴, in⁴)

### Stress Concentration

**Stress Concentration Factor (Kt):**
- Kt = σ_max / σ_nominal
- Sharp corners: Kt = 2-3
- Fillets: Kt = 1.1-1.5
- Holes: Kt = 2-3

**Minimizing Stress Concentration:**
- Use fillets (minimum R2mm)
- Use chamfers
- Avoid sharp corners
- Avoid sudden changes in cross-section

---

## Reinforcement Design

### Gussets

**Purpose:** Reinforce joints and load points

**Design:**
- Triangular shape
- Size: 0.5-1× material thickness
- Height: Based on load (typically 20-50mm)
- Angle: 30-45° typical

**Placement:**
- At joints (corners, T-joints)
- At load points
- At stress concentration areas

**Example:**
- Base plate: 10mm thick
- Gusset: 8mm thick, 30mm height, 45° angle

### Ribs

**Purpose:** Increase stiffness, reduce deflection

**Design:**
- Longitudinal reinforcements
- Height: 2-3× material thickness
- Thickness: 0.5-1× material thickness
- Spacing: 3-5× rib height

**Placement:**
- Along length for bending stiffness
- Perpendicular to load direction
- Evenly spaced

**Example:**
- Base plate: 10mm thick
- Rib: 5mm thick, 25mm height
- Spacing: 75mm (3× height)

### Fillets

**Purpose:** Reduce stress concentration

**Design:**
- Minimum radius: 2mm (0.08")
- Larger for high stress areas
- Typical: R2mm-R5mm

**Placement:**
- All internal corners
- At stress concentration points
- At load path transitions

**Example:**
- Internal corner: R3mm fillet
- Reduces stress concentration from Kt=3 to Kt=1.2

### Chamfers

**Purpose:** Assembly ease, stress relief

**Design:**
- 45° typical angle
- Size: 1-2mm typical
- Can be larger for assembly

**Placement:**
- External corners
- Edges for assembly
- Stress relief at transitions

---

## Material Selection

### Material Properties

**Strength:**
- Yield strength (σ_y): Stress at which material yields
- Ultimate strength (σ_u): Maximum stress before failure
- Units: MPa, ksi

**Stiffness:**
- Young's modulus (E): Stiffness in tension/compression
- Shear modulus (G): Stiffness in shear
- Units: GPa, Msi

**Density:**
- Mass per unit volume
- Units: kg/m³, lb/in³

### Common Materials

**Aluminum 6061-T6:**
- Yield: 276 MPa (40 ksi)
- Ultimate: 310 MPa (45 ksi)
- E: 68.9 GPa (10 Msi)
- Density: 2.70 g/cm³
- Good: Lightweight, machinable
- Bad: Lower strength than steel

**Steel A36:**
- Yield: 250 MPa (36 ksi)
- Ultimate: 400 MPa (58 ksi)
- E: 200 GPa (29 Msi)
- Density: 7.85 g/cm³
- Good: Strong, weldable
- Bad: Heavy, rusts

**Stainless Steel 304:**
- Yield: 205 MPa (30 ksi)
- Ultimate: 515 MPa (75 ksi)
- E: 193 GPa (28 Msi)
- Density: 8.00 g/cm³
- Good: Corrosion resistant
- Bad: Expensive, lower strength

**Titanium Grade 5:**
- Yield: 880 MPa (128 ksi)
- Ultimate: 950 MPa (138 ksi)
- E: 110 GPa (16 Msi)
- Density: 4.43 g/cm³
- Good: High strength/weight
- Bad: Expensive, difficult to machine

### Material Selection Process

1. **Identify Requirements:**
   - Strength requirements
   - Stiffness requirements
   - Weight requirements
   - Environmental requirements
   - Cost constraints

2. **Evaluate Options:**
   - Compare material properties
   - Consider manufacturing process
   - Consider availability
   - Consider cost

3. **Select Material:**
   - Best fit for requirements
   - Verify availability
   - Verify cost

---

## Safety Factor Guidelines

### Safety Factor Selection

**Static Loads:**
- Well-known loads: SF = 2.0
- Uncertain loads: SF = 3.0-4.0
- Critical applications: SF = 4.0-6.0

**Dynamic Loads:**
- Fatigue: SF = 2.0-3.0
- Impact: SF = 3.0-5.0
- Vibration: SF = 2.0-4.0

**Material Uncertainty:**
- Known material: SF = 1.5-2.0
- Unknown material: SF = 2.0-3.0

**Manufacturing Uncertainty:**
- High quality: SF = 1.5-2.0
- Standard quality: SF = 2.0-3.0

### Safety Factor Calculation

**Allowable Stress:**
- σ_allowable = σ_yield / SF
- Or: σ_allowable = σ_ultimate / SF

**Design Stress:**
- σ_design ≤ σ_allowable
- Verify: σ_design = Load / Area ≤ σ_allowable

---

## Deflection Limits

### Typical Deflection Limits

**General Structures:**
- L/250 to L/500 (L = span length)
- Example: 1000mm span → 2-4mm max deflection

**Precision Structures:**
- L/1000 to L/2000
- Example: 1000mm span → 0.5-1mm max deflection

**Machine Components:**
- Based on function
- Bearings: 0.01-0.1mm
- Gears: 0.05-0.2mm

### Deflection Calculations

**Cantilever Beam:**
- δ = FL³/(3EI)
- F = force (N, lbf)
- L = length (m, in)
- E = Young's modulus (Pa, psi)
- I = moment of inertia (m⁴, in⁴)

**Simply Supported Beam:**
- δ = 5FL³/(384EI) (uniform load)
- δ = FL³/(48EI) (point load at center)

**Fixed Beam:**
- δ = FL³/(192EI) (point load at center)

---

## Design Optimization

### Strength/Weight Optimization

**Topology Optimization:**
- Remove material where loads are low
- Add material where loads are high
- Optimize for strength/weight ratio

**Geometry Optimization:**
- Optimize cross-section shape
- Optimize reinforcement placement
- Optimize material distribution

### Cost Optimization

**Material Selection:**
- Choose cost-effective materials
- Consider manufacturing cost
- Consider total cost (material + manufacturing)

**Design Simplification:**
- Simplify geometry when possible
- Reduce number of features
- Reduce manufacturing complexity

---

## References

- Functional Design Methodology: `02_Design/functional_design/functional_design_methodology.md`
- Process-Specific Design Guidelines: `02_Design/manufacturing/process_specific_design_guidelines.md`
- Machinery's Handbook
- Roark's Formulas for Stress and Strain

