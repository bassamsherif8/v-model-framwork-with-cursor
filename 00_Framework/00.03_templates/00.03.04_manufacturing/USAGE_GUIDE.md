# Manufacturing Documentation Usage Guide
## How to Use the Manufacturing Framework

**Date:** 2024-12-22  
**Version:** 1.0

---

## Overview

This guide explains how to use the manufacturing documentation framework to generate manufacturing-ready technical drawings and documentation for the Delta CNC mechanism parts.

---

## Prerequisites

### Required Software

1. **FreeCAD** (for drawing generation)
   - Download: https://www.freecad.org/downloads.php
   - Version: 0.20 or later recommended
   - Verify Python API access after installation

2. **Python 3.8+**
   - Required for running Python scripts
   - Verify: `python --version`

3. **CAD Software** (optional, for viewing)
   - Any CAD software that can open DXF, DWG, or STEP files
   - Examples: AutoCAD, SolidWorks, Fusion 360, FreeCAD

### Required Files

- Part geometry files (STEP format) in `02_Design/parts/`
- Manufacturing specifications database (`manufacturing_data.py`)
- GD&T system (`gdt_system.py`)
- Drawing generator (`technical_drawing_generator.py`)

---

## Step-by-Step Usage

### Step 1: Verify FreeCAD Installation

On Windows, use the FreeCAD console executable (`FreeCADCmd.exe`) to run the setup script **inside FreeCAD's Python environment**.

```powershell
cd "D:\Ideas and Businesses\brainstorming sessions\Project AI Engineer Mechatronics Cursor v1\3rd test - build123d and composer 1 adding V MODEL R&D\02_Design\manufacturing"
& "C:\Program Files\FreeCAD 1.0\bin\FreeCADCmd.exe" "freecad_setup.py"
```

**Expected Output (example):**
```
Checking FreeCAD availability...
[OK] FreeCAD 0.20.x available
  Path: C:\Program Files\FreeCAD 1.0\bin\
  Modules: Part, PartDesign, TechDraw, Drawing

Testing FreeCAD initialization...
[OK] FreeCAD environment setup successful
  Document: DeltaCNC_Manufacturing_Drawings
```

**If FreeCAD is not found:**
- Install FreeCAD from https://www.freecad.org/downloads.php
- Update the `FREECAD_CMD` path in `freecad_setup.py` to match your installation
- Re-run the command above

---

### Step 2: Verify Part Geometry Files

Ensure STEP files exist for all parts:

```bash
# Check for part files
ls 02_Design/parts/*.step
```

**Required Files:**
- `DCNC-BASE-PLATFORM-A001.step`
- `DCNC-ACTUATOR-ACT-MOUNT-A001.step` (or base part number)
- `DCNC-ARM-UPPER-ARM-A001.step`
- `DCNC-ARM-LOWER-ARM-A001.step`
- `DCNC-END-EFFECTOR-A001.step`
- `DCNC-JOINT-BALL-JOINT-A001.step`

---

### Step 3: Generate Technical Drawings

#### Option A: Generate All Drawings at Once (Recommended)

Run the drawing generator **inside FreeCAD** using `FreeCADCmd.exe`:

```powershell
cd "D:\Ideas and Businesses\brainstorming sessions\Project AI Engineer Mechatronics Cursor v1\3rd test - build123d and composer 1 adding V MODEL R&D"
& "C:\Program Files\FreeCAD 1.0\bin\FreeCADCmd.exe" "02_Design\manufacturing\technical_drawing_generator.py"
```

This will:
1. Load manufacturing specifications for each part
2. Create drawing templates with title blocks
3. Generate multi-view drawings (front, top, side, isometric, section)
4. Apply dimensions with tolerances
5. Apply GD&T callouts
6. Add manufacturing notes
7. Export to DXF, DWG, and PDF formats

#### Option B: Generate Drawing for Single Part (Interactive in FreeCAD)

You can also open FreeCAD's Python console or a custom macro and call the generator manually:

```python
import sys
import os

sys.path.append(r"D:\Ideas and Businesses\brainstorming sessions\Project AI Engineer Mechatronics Cursor v1\3rd test - build123d and composer 1 adding V MODEL R&D\02_Design\manufacturing")

from technical_drawing_generator import generate_technical_drawing

# Generate drawing for base platform
drawing = generate_technical_drawing(
    part_number="DCNC-BASE-PLATFORM-A001",
    output_dir="02_Design/manufacturing/drawings"
)
print(\"Drawing generated for:\", drawing and drawing.get('part_number', 'unknown'))
```

---

### Step 4: Verify Generated Drawings

Check that drawings were generated:

```bash
# List generated drawings
ls 02_Design/manufacturing/drawings/
```

**Expected Files (per part):**
- `DCNC-BASE-PLATFORM-A001_drawing.dxf`
- `DCNC-BASE-PLATFORM-A001_drawing.dwg`
- `DCNC-BASE-PLATFORM-A001_drawing.pdf`

**Verify Drawing Content:**
- Open PDF files to verify:
  - [ ] All views present (front, top, side, isometric, section)
  - [ ] All dimensions shown with tolerances
  - [ ] GD&T callouts present
  - [ ] Manufacturing notes included
  - [ ] Title block complete

---

### Step 5: Generate STEP Files with PMI

```python
from technical_drawing_generator import generate_pmi_step

# Generate STEP file with PMI for base platform
generate_pmi_step(
    part_number="DCNC-BASE-PLATFORM-A001",
    output_dir="02_Design/manufacturing/parts"
)
```

**Expected Output:**
- `DCNC-BASE-PLATFORM-A001_pmi.step`

**Verify PMI Content:**
- Open STEP file in CAD software
- Verify PMI includes:
  - [ ] Dimensions with tolerances
  - [ ] GD&T callouts
  - [ ] Manufacturing notes
  - [ ] Material specifications

---

## Customization

### Adding New Parts

1. **Add to Manufacturing Database:**

```python
# Edit manufacturing_data.py
MANUFACTURING_SPECS["DCNC-NEW-PART-A001"] = {
    "part_name": "New Part",
    "material": "6061-T6 Aluminum per ASTM B211",
    "surface_finish": {...},
    "threads": {...},
    "holes": {...},
    "dimensions": {...},
    "gdt": {...},
    "manufacturing_notes": [...]
}
```

2. **Add Manufacturing Notes:**

Edit `manufacturing_notes.md` to add part-specific notes.

3. **Generate Drawing:**

```python
generate_technical_drawing("DCNC-NEW-PART-A001")
```

### Modifying Drawing Templates

Edit `drawing_templates.py` to customize:
- Title block format
- Sheet sizes
- Drawing scale
- View layouts

### Modifying GD&T Specifications

Edit `gdt_system.py` to:
- Add new GD&T callouts
- Modify datum references
- Update tolerance values

---

## Troubleshooting

### Issue: FreeCAD Not Found

**Symptoms:**
```
FreeCAD not found. Please install FreeCAD...
```

**Solutions:**
1. Install FreeCAD from https://www.freecad.org/downloads.php
2. Add FreeCAD to system PATH
3. Update `freecad_setup.py` with correct FreeCAD path

### Issue: Part Geometry Not Found

**Symptoms:**
```
STEP file not found: 02_Design/parts/DCNC-BASE-PLATFORM-A001.step
```

**Solutions:**
1. Verify STEP files exist in `02_Design/parts/`
2. Check part number matches exactly
3. Generate STEP files from CAD design if missing

### Issue: Drawing Generation Fails

**Symptoms:**
```
Error generating technical drawing: ...
```

**Solutions:**
1. Check FreeCAD Python API access
2. Verify part geometry is valid STEP file
3. Check manufacturing specifications exist for part
4. Review error message for specific issue

### Issue: GD&T Callouts Missing

**Symptoms:**
- Drawings generated but GD&T callouts not present

**Solutions:**
1. Verify GD&T specifications exist in `manufacturing_data.py`
2. Check `gdt_system.py` for correct part type mapping
3. Verify FreeCAD TechDraw module supports GD&T

---

## Best Practices

### Drawing Generation

1. **Always Verify Drawings:**
   - Check all views are present
   - Verify dimensions and tolerances
   - Confirm GD&T callouts
   - Review manufacturing notes

2. **Maintain Consistency:**
   - Use same drawing template for all parts
   - Follow same dimensioning style
   - Apply GD&T consistently

3. **Document Changes:**
   - Update manufacturing specifications when design changes
   - Update drawings when specifications change
   - Maintain revision history

### Manufacturing Specifications

1. **Keep Specifications Updated:**
   - Update `manufacturing_data.py` when design changes
   - Update `manufacturing_notes.md` when requirements change
   - Sync with tolerance analysis

2. **Verify Completeness:**
   - All dimensions have tolerances
   - All surfaces have finish specifications
   - All threads have complete callouts
   - All holes have complete specifications

### Quality Control

1. **Review Before Release:**
   - Complete manufacturing readiness checklist
   - Verify all 12 issues addressed
   - Review drawings for completeness
   - Verify specifications match requirements

2. **Maintain Traceability:**
   - Link drawings to requirements
   - Link specifications to tolerance analysis
   - Document changes and revisions

---

## Advanced Usage

### Batch Processing

Generate drawings for all parts:

```python
from technical_drawing_generator import generate_all_part_drawings
from manufacturing_data import get_all_part_numbers

# Get all part numbers
part_numbers = get_all_part_numbers()

# Generate drawings for all parts
for part_number in part_numbers:
    print(f"Generating drawing for: {part_number}")
    drawing = generate_technical_drawing(part_number)
    if drawing:
        print(f"✓ Drawing generated: {part_number}")
    else:
        print(f"✗ Drawing generation failed: {part_number}")
```

### Custom Drawing Views

Modify `technical_drawing_generator.py` to add custom views:

```python
def generate_views(part_geometry, template, part_number):
    views = []
    
    # Add standard views
    views.append(create_view("front", ...))
    views.append(create_view("top", ...))
    
    # Add custom detail view
    views.append(create_detail_view("critical_feature", ...))
    
    return views
```

### Export to Additional Formats

Add export functionality for additional formats:

```python
def export_to_additional_formats(template, part_number):
    # Export to SVG
    export_svg(template, f"{part_number}_drawing.svg")
    
    # Export to PNG (for documentation)
    export_png(template, f"{part_number}_drawing.png")
```

---

## Integration with Other Tools

### CAD Software Integration

**Importing Drawings:**
- DXF/DWG files can be imported into most CAD software
- STEP files with PMI can be opened in CAD software
- Verify PMI compatibility with target CAD software

**Exporting from CAD:**
- Export part geometry to STEP format
- Place STEP files in `02_Design/parts/`
- Use manufacturing framework to generate drawings

### Manufacturing Software Integration

**CNC Programming:**
- Use DXF files for CNC programming
- Use STEP files for CAM software
- Reference manufacturing notes for setup instructions

**Quality Control:**
- Use inspection procedures for part verification
- Use inspection checklist for documentation
- Reference technical drawings for measurements

---

## Support and Resources

### Documentation

- **Manufacturing Standards:** `02_Design/manufacturing_standards.md`
- **Manufacturing Notes:** `02_Design/manufacturing/manufacturing_notes.md`
- **Assembly Instructions:** `02_Design/manufacturing/assembly_instructions.md`
- **Inspection Procedures:** `04_Verification/manufacturing/inspection_procedures.md`

### Code Reference

- **Manufacturing Data:** `02_Design/manufacturing/manufacturing_data.py`
- **GD&T System:** `02_Design/manufacturing/gdt_system.py`
- **Drawing Generator:** `02_Design/manufacturing/technical_drawing_generator.py`
- **Drawing Templates:** `02_Design/manufacturing/drawing_templates.py`

### Standards

- **ASME Y14.5-2018:** Dimensioning and Tolerancing
- **ISO 2768:** General Tolerances
- **ISO 1302:** Surface Texture
- **ASTM B211:** Aluminum Specifications

---

**Last Updated:** 2024-12-22

