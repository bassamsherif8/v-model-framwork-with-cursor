# Common Parts Library - Usage Examples

This document provides practical examples of using common parts in build123d assemblies.

## Example 1: Basic Fastener Usage

```python
"""
Example: Using standard fasteners in an assembly
"""
from build123d import *
from pathlib import Path
import sys

# Add common parts to path
common_parts_dir = Path(__file__).parent
sys.path.insert(0, str(common_parts_dir))

from cq_warehouse.fasteners.standard_fasteners import (
    get_bolt_m6x20,
    get_hex_nut_m6,
    get_washer_m6
)

# Get fasteners
bolt = get_bolt_m6x20(part_number="DCS-COMMON-FAST-M6X20-A001")
nut = get_hex_nut_m6(part_number="DCS-COMMON-FAST-M6-NUT-A001")
washer = get_washer_m6(part_number="DCS-COMMON-FAST-M6-WASHER-A001")

# Position fasteners (example: mounting a bracket)
# Bolt goes through hole at (100, 100, 0)
bolt_positioned = Location((100, 100, 0)) * bolt
washer_positioned = Location((100, 100, -1)) * washer  # Under head
nut_positioned = Location((100, 100, 20)) * nut  # At end of bolt

# Create fastener assembly
fastener_assembly = Compound(children=[
    bolt_positioned,
    washer_positioned,
    nut_positioned
])

# Export
export_step(fastener_assembly, "fastener_example.step")
```

## Example 2: Multiple Fasteners in Assembly

```python
"""
Example: Using multiple fasteners to mount components
"""
from build123d import *
from pathlib import Path
import sys

# Add common parts to path
common_parts_dir = Path(__file__).parent
sys.path.insert(0, str(common_parts_dir))

from cq_warehouse.fasteners.standard_fasteners import get_bolt_m12x40, get_hex_nut_m12

# Mounting pattern: 4 bolts in corners
mounting_positions = [
    (200, 200, 0),   # Front-left
    (2200, 200, 0),  # Front-right
    (200, 1600, 0),  # Rear-left
    (2200, 1600, 0), # Rear-right
]

# Generate fasteners
fasteners = []
for i, pos in enumerate(mounting_positions):
    bolt = get_bolt_m12x40(part_number=f"DCS-COMMON-FAST-M12X40-{i+1:02d}")
    nut = get_hex_nut_m12(part_number=f"DCS-COMMON-FAST-M12-NUT-{i+1:02d}")
    
    # Position bolt
    bolt_pos = Location((pos[0], pos[1], pos[2])) * bolt
    # Position nut at end of bolt
    nut_pos = Location((pos[0], pos[1], pos[2] + 40)) * nut
    
    fasteners.extend([bolt_pos, nut_pos])

# Create assembly
mounting_assembly = Compound(children=fasteners)
```

## Example 3: Bearings in Assembly

```python
"""
Example: Using bearings in a rotating assembly
"""
from build123d import *
from pathlib import Path
import sys

# Add common parts to path
common_parts_dir = Path(__file__).parent
sys.path.insert(0, str(common_parts_dir))

from cq_warehouse.bearings.ball_bearings import get_bearing_6205

# Get bearings for both ends of a shaft
bearing1 = get_bearing_6205(part_number="DCS-COMMON-BRG-6205-1-A001")
bearing2 = get_bearing_6205(part_number="DCS-COMMON-BRG-6205-2-A001")

# Position bearings
# Bearing 1 at X=0, bearing 2 at X=500mm
bearing1_pos = Location((0, 0, 0)) * bearing1
bearing2_pos = Location((500, 0, 0)) * bearing2

# Create bearing assembly
bearing_assembly = Compound(children=[bearing1_pos, bearing2_pos])
```

## Example 4: Combining Custom and Standard Parts

```python
"""
Example: Combining custom build123d parts with standard cq_warehouse parts
"""
from build123d import *
from pathlib import Path
import sys

# Add paths
parts_dir = Path(__file__).parent.parent / "parts"
common_parts_dir = Path(__file__).parent
sys.path.insert(0, str(parts_dir))
sys.path.insert(0, str(common_parts_dir))

# Import standard parts
from cq_warehouse.fasteners.standard_fasteners import get_bolt_m12x40, get_hex_nut_m12
from cq_warehouse.bearings.ball_bearings import get_bearing_2inch

# Load custom part (build123d)
def load_step_file(filename):
    """Load a STEP file and return the Part object."""
    step_path = parts_dir / filename
    if not step_path.exists():
        raise FileNotFoundError(f"STEP file not found: {step_path}")
    return import_step(str(step_path))

# Load custom parts
hose_reel = load_step_file("hose_reel_A001.step")
hose_reel.label = "DCS-TRLR-HOSE-REEL-A001"

# Get standard parts
# Bearings for hose reel axle
bearing1 = get_bearing_2inch(part_number="DCS-COMMON-BRG-2IN-1-A001")
bearing2 = get_bearing_2inch(part_number="DCS-COMMON-BRG-2IN-2-A001")

# Mounting bolts
bolts = []
for i in range(4):
    bolt = get_bolt_m12x40(part_number=f"DCS-COMMON-FAST-M12X40-{i+1:02d}")
    # Position bolt at mounting holes...
    bolts.append(bolt)

# Position all components
hose_reel_pos = Location((1600, 900, 300)) * hose_reel
bearing1_pos = Location((1400, 900, 300)) * bearing1
bearing2_pos = Location((1800, 900, 300)) * bearing2

# Create complete assembly
assembly_components = [hose_reel_pos, bearing1_pos, bearing2_pos] + bolts
complete_assembly = Compound(children=assembly_components)
complete_assembly.label = "DCS-ASSY-HOSE-REEL-COMPLETE-A001"

# Export
export_step(complete_assembly, "hose_reel_complete_assembly.step")
```

## Example 5: Full Assembly with Standard Parts

```python
"""
Example: Complete assembly using both custom and standard parts
This example shows how to update ground_station_assembly_A001.py
to include standard fasteners and bearings.
"""
from build123d import *
from pathlib import Path
import sys

# Add paths
parts_dir = Path(__file__).parent.parent / "parts"
common_parts_dir = Path(__file__).parent.parent / "common_parts"
sys.path.insert(0, str(parts_dir))
sys.path.insert(0, str(common_parts_dir))

# Import standard parts
from cq_warehouse.fasteners.standard_fasteners import (
    get_bolt_m12x40,
    get_hex_nut_m12,
    get_washer_m12
)
from cq_warehouse.bearings.ball_bearings import get_bearing_2inch

# Load custom parts (existing code)
def load_step_file(filename):
    step_path = parts_dir / filename
    if not step_path.exists():
        raise FileNotFoundError(f"STEP file not found: {step_path}")
    return import_step(str(step_path))

trailer_frame = load_step_file("trailer_frame_A001.step")
tank_support = load_step_file("tank_support_A001.step")
# ... load other custom parts ...

# Position custom parts (existing positioning code)
trailer_frame_positioned = Location((200.0, 0.0, -50.0)) * trailer_frame
tank_support_positioned = Location((1300.0, 350.0, 100.0)) * tank_support
# ... position other parts ...

# NEW: Add standard fasteners for mounting
mounting_fasteners = []

# Mounting positions (example - adjust to actual hole positions)
mounting_holes = [
    (200, 200, 150),   # Example positions
    (2200, 200, 150),
    (200, 1600, 150),
    (2200, 1600, 150),
]

# Generate fasteners for each mounting hole
for i, hole_pos in enumerate(mounting_holes):
    bolt = get_bolt_m12x40(part_number=f"DCS-COMMON-FAST-M12X40-{i+1:02d}")
    nut = get_hex_nut_m12(part_number=f"DCS-COMMON-FAST-M12-NUT-{i+1:02d}")
    washer1 = get_washer_m12(part_number=f"DCS-COMMON-FAST-M12-WASHER-{i+1:02d}-1")
    washer2 = get_washer_m12(part_number=f"DCS-COMMON-FAST-M12-WASHER-{i+1:02d}-2")
    
    # Position fasteners
    bolt_pos = Location(hole_pos) * bolt
    washer1_pos = Location((hole_pos[0], hole_pos[1], hole_pos[2] - 1)) * washer1
    nut_pos = Location((hole_pos[0], hole_pos[1], hole_pos[2] + 40)) * nut
    washer2_pos = Location((hole_pos[0], hole_pos[1], hole_pos[2] + 40 + 1)) * washer2
    
    mounting_fasteners.extend([bolt_pos, washer1_pos, nut_pos, washer2_pos])

# NEW: Add bearings for hose reel
bearing1 = get_bearing_2inch(part_number="DCS-COMMON-BRG-2IN-1-A001")
bearing2 = get_bearing_2inch(part_number="DCS-COMMON-BRG-2IN-2-A001")

bearing1_pos = Location((1400, 900, 300)) * bearing1
bearing2_pos = Location((1800, 900, 300)) * bearing2

# Combine all components
assembly_components = [
    trailer_frame_positioned,
    tank_support_positioned,
    # ... other custom parts ...
] + mounting_fasteners + [bearing1_pos, bearing2_pos]

# Create assembly
ground_station_assembly = Compound(children=assembly_components)
ground_station_assembly.label = "DCS-ASSY-GROUND-STATION-A001"

# Export
export_step(ground_station_assembly, "ground_station_assembly_complete.step")
```

## Example 6: BOM Generation with Standard Parts

```python
"""
Example: Generate BOM including standard parts
"""
from pathlib import Path

def generate_assembly_bom_with_standard_parts():
    """Generate BOM including both custom and standard parts."""
    
    bom_data = [
        # Custom parts
        {
            "part_number": "DCS-TRLR-TRAILER-FRAME-A001",
            "part_name": "Trailer Frame",
            "quantity": 1,
            "material": "Steel A36 per ASTM A36",
            "supplier_part": "Custom",
            "notes": "Welded channel construction",
            "revision": "A001"
        },
        # ... other custom parts ...
        
        # Standard parts from common_parts
        {
            "part_number": "DCS-COMMON-FAST-M12X40-SS-A001",
            "part_name": "M12 × 40mm Hex Head Bolt",
            "quantity": 24,
            "material": "Stainless Steel 316",
            "supplier_part": "Standard (ISO 4014)",
            "notes": "For mounting components to frame",
            "revision": "A001"
        },
        {
            "part_number": "DCS-COMMON-FAST-M12-NUT-SS-A001",
            "part_name": "M12 Hex Nut",
            "quantity": 24,
            "material": "Stainless Steel 316",
            "supplier_part": "Standard (ISO 4032)",
            "notes": "For mounting components to frame",
            "revision": "A001"
        },
        {
            "part_number": "DCS-COMMON-BRG-2IN-A001",
            "part_name": "2\" ID Deep Groove Ball Bearing",
            "quantity": 2,
            "material": "Bearing Steel",
            "supplier_part": "Standard (e.g., SKF 6205 or equivalent)",
            "notes": "For hose reel axle",
            "revision": "A001"
        },
    ]
    
    return bom_data

# Save BOM
bom = generate_assembly_bom_with_standard_parts()
bom_path = Path(__file__).parent.parent / "assemblies" / "ground_station_assembly_BOM_complete.csv"

with open(bom_path, 'w', encoding='utf-8') as f:
    f.write("Part Number,Part Name,Quantity,Material,Supplier Part #,Notes,Revision\n")
    for item in bom:
        f.write(f"{item['part_number']},{item['part_name']},{item['quantity']},")
        f.write(f"{item['material']},{item['supplier_part']},{item['notes']},{item['revision']}\n")
```

## Best Practices

1. **Always specify part numbers** - Use consistent part numbering format
2. **Import from common_parts** - Never import cq_warehouse directly in project files
3. **Use wrapper functions** - Always use wrapper functions, not cq_warehouse directly
4. **Position carefully** - Standard parts need proper positioning in assemblies
5. **Update BOM** - Always include standard parts in BOM with correct quantities
6. **Document usage** - Comment where standard parts are used in assemblies

## Troubleshooting

### Import Errors

If you get import errors, ensure:
- CadQuery is installed: `pip install cadquery`
- cq_warehouse is installed: `pip install cq-warehouse`
- Common parts path is added to sys.path

### Conversion Errors

If conversion fails:
- Check that OCP is installed (required by build123d)
- Verify STEP export/import is working
- Check temporary file permissions

### Part Positioning

Standard parts are generated at origin (0,0,0). Always position them:
```python
part_positioned = Location((x, y, z)) * part
```

