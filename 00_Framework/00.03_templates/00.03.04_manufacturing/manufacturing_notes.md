# Manufacturing Notes - Drone Cleaning System (DCS) Trailer

**Project:** Drone Cleaning System (DCS) - Facade Cleaning Trailer  
**Date:** 2025-12-30  
**Status:** Manufacturing-Ready  
**Version:** A001

---

## General Manufacturing Notes

### Material Specifications

**Steel A36 (ASTM A36):**
- Used for: Frame components, mount bases
- Standard: ASTM A36
- Properties: Yield strength 250 MPa, Ultimate strength 400 MPa
- Surface finish: Ra 3.2μm (as-welded typical)

**Aluminum 6061-T6:**
- Used for: Guide arm components, drone mount adapter
- Standard: ASTM B211
- Properties: Yield strength 276 MPa, Ultimate strength 310 MPa
- Surface finish: Ra 1.6μm (machined)

**Carbon Fiber (for bracket):**
- Used for: Drone nozzle bracket base
- Standard: Custom composite
- Properties: High strength-to-weight ratio
- Surface finish: As-molded

**HDPE (for tank):**
- Used for: Water tank body (purchased component)
- Standard: ASTM D1998
- Properties: Food-grade, UV resistant
- Surface finish: As-molded

---

## Welding Requirements (AWS D1.1)

### Weld Joint Types

**Fillet Welds:**
- Most common for frame connections
- Leg length: 6-8mm (based on material thickness)
- Standard: AWS D1.1

**Butt Welds:**
- For edge-to-edge connections
- Full penetration for critical joints
- Standard: AWS D1.1

### Weld Accessibility

- **Minimum Clearance:** 150mm for TIG/MIG torch
- **Weld Positions:** All weld positions accessible
- **Distortion Control:** Tack welding sequence required

### Weld Inspection

- **Visual Inspection:** Required for all welds
- **NDT:** Required for critical welds (tank mount, axle mount)
- **Quality Standard:** AWS D1.1

---

## Tolerances (REQ-002)

### Frame Dimensions
- **Overall Length:** ±2mm
- **Overall Width:** ±2mm
- **Mounting Hole Positions:** ±0.5mm

### Machined Parts
- **Typical Tolerance:** ±0.1mm
- **Precision Surfaces:** ±0.05mm
- **Thread Tolerances:** Per ISO standards

---

## Surface Finish Specifications

### Default Surface Finish
- **As-Welded (Steel):** Ra 3.2μm
- **Machined (Aluminum):** Ra 1.6μm
- **Precision Surfaces:** Ra 0.8μm (bearing surfaces, joints)
- **Very Precision Surfaces:** Ra 0.4μm (precision joints)

### Surface Treatment
- **Steel Parts:** Primer + paint or galvanizing (rust protection)
- **Aluminum Parts:** Anodizing (optional, for corrosion protection)

---

## Thread Specifications

### Standard Threads
- **M12 Bolts:** M12x1.75-6H (frame connections)
- **M10 Bolts:** M10x1.5-6H (mounting connections)
- **M8 Bolts:** M8x1.25-6H (smaller connections)
- **M6 Bolts:** M6x1.0-6H (light-duty connections)
- **M4 Bolts:** M4x0.7-6H (drone bracket)

### Thread Depth
- **Through Holes:** THRU
- **Blind Holes:** Minimum 1.5× bolt diameter engagement
- **Tap Drill Sizes:** Per ISO standards

---

## Hole Specifications

### Standard Holes
- **Clearance Holes:** Bolt diameter + 1mm (e.g., M12 = 13mm hole)
- **Precision Holes:** Reamed to size with position tolerance
- **Position Tolerance:** ±0.5mm typical, ±0.02mm for precision

### Hole Callouts
- Format: ⌀[Drill Size] DRILL → [Tap Size] [Position Tolerance]
- Example: ⌀5.0 DRILL → M6x1.0-6H THRU, Position: ±0.02mm

---

## Manufacturing Process Notes

### Welding (11 parts)
- **Process:** MIG/TIG welding per AWS D1.1
- **Weld Size:** 6-8mm leg length (fillet welds)
- **Distortion Control:** Tack welding sequence, proper fixturing
- **Post-Weld:** Visual inspection, NDT for critical welds

### CNC Machining (2-4 parts)
- **Tool Access:** Minimum 2× tool diameter clearance
- **Internal Radii:** Minimum 0.5-3mm (tool radius)
- **Thread Milling:** M12+ threads
- **Thread Tapping:** M6- threads
- **Surface Finish:** Ra 1.6μm typical

### Purchased Components (3 parts)
- **Water Tank:** Ready-built 1000L tank (HDPE or stainless steel)
- **Guide Arm Tubes:** Standard extruded aluminum tubes (80mm OD, 5mm wall)
- **Reel Drum:** Can be purchased or custom welded

---

## Assembly Notes

### Frame Assembly
1. **Main Rails:** Position and align main rails
2. **Cross Members:** Weld cross members to main rails (fillet welds, 6mm leg)
3. **Axle Mounts:** Weld axle mounts to main rails (fillet welds, 8mm leg)
4. **Tank Mount:** Weld tank mount base to frame (fillet welds, 6-8mm leg)
5. **Mount Bases:** Weld pump, generator, reel mount bases to frame

### Component Mounting
- **Tank:** Bolted to tank mount base (M10 bolts, 4 locations)
- **Pump:** Bolted to pump mount base (M8 bolts)
- **Generator:** Bolted to generator mount base (M8 bolts)
- **Reel:** Bolted to reel mount base (M10 bolts)

### Guide Arm Assembly
1. **Base:** Mount guide arm base to frame
2. **Lower Tube:** Weld or bolt lower tube to base
3. **Joint:** Weld or bolt joint to lower tube
4. **Upper Tube:** Weld or bolt upper tube to joint
5. **Nozzle Bracket:** Mount nozzle bracket to upper tube

---

## Quality Control

### Incoming Inspection
- **Material Certificates:** Required for all materials
- **Dimensional Check:** Verify critical dimensions
- **Surface Finish:** Verify surface finish meets specifications

### In-Process Inspection
- **Weld Quality:** Visual inspection, NDT for critical welds
- **Dimensional Check:** Verify dimensions during manufacturing
- **Thread Quality:** Verify thread quality and engagement

### Final Inspection
- **Dimensional Inspection:** Verify all dimensions per drawing
- **Surface Finish:** Verify surface finish meets specifications
- **Assembly Fit:** Verify parts fit together correctly
- **Weight Verification:** Required for drone components (REQ-006)

---

## Special Requirements

### Weight Constraints (REQ-006)
- **Drone Nozzle Bracket:** ≤0.8 kg total
- **Drone Nozzle Assembly:** ≤0.5 kg
- **Total Payload:** ≤2.7 kg (including hose)
- **Verification:** Actual weight measurement mandatory before production

### Environmental Protection
- **Steel Parts:** Rust protection (primer + paint or galvanizing)
- **Aluminum Parts:** Anodizing optional
- **Tank:** UV-resistant material (HDPE or stainless steel)

---

## Documentation Requirements

### Technical Drawings
- **Format:** DXF, DWG, PDF (all three required)
- **Views:** Front, top, side, isometric, section views as required
- **Dimensions:** All dimensions with tolerances
- **GD&T:** Per ASME Y14.5-2018
- **Location:** `02_Design/manufacturing/drawings/`

### STEP Files
- **Format:** STEP with PMI (Product Manufacturing Information)
- **Location:** `02_Design/parts/`
- **Naming:** `[part_number]-A001.step`

### Manufacturing Notes
- **General Notes:** This document
- **Part-Specific Notes:** `02_Design/manufacturing/part_notes/`

---

## Standards Reference

- **AWS D1.1** - Structural Welding Code - Steel
- **ASTM A36** - Standard Specification for Carbon Structural Steel
- **ASTM B211** - Standard Specification for Aluminum and Aluminum-Alloy Bars, Rods, and Wire
- **ASME Y14.5-2018** - Geometric Dimensioning and Tolerancing
- **ISO 2768** - General Tolerances
- **ISO 965** - ISO General Purpose Metric Screw Threads

---

**Status:** Manufacturing-Ready  
**Version:** A001  
**Date:** 2025-12-30
