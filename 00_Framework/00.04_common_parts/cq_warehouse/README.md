# cq_warehouse Standard Parts Library

**Version:** 1.0.0  
**Catalog of Standard Mechanical Components**

This directory contains wrapper functions for standard mechanical components from the cq_warehouse library. All parts are automatically converted to build123d format for use in assemblies.

## Available Parts

### Fasteners

| Function | Part Number Format | Description | Dimensions | Standard |
|----------|-------------------|------------|------------|----------|
| `get_bolt_m4x12()` | `DCS-COMMON-FAST-M4X12-SS-A001` | M4×12mm socket head cap screw | M4-0.7 × 12mm | ISO 4762 |
| `get_bolt_m6x20()` | `DCS-COMMON-FAST-M6X20-SS-A001` | M6×20mm socket head cap screw | M6-1.0 × 20mm | ISO 4762 |
| `get_bolt_m8x25()` | `DCS-COMMON-FAST-M8X25-SS-A001` | M8×25mm socket head cap screw | M8-1.25 × 25mm | ISO 4762 |
| `get_bolt_m10x30()` | `DCS-COMMON-FAST-M10X30-SS-A001` | M10×30mm hex head bolt | M10-1.5 × 30mm | ISO 4014 |
| `get_bolt_m10x35()` | `DCS-COMMON-FAST-M10X35-SS-A001` | M10×35mm hex head bolt | M10-1.5 × 35mm | ISO 4014 |
| `get_bolt_m12x40()` | `DCS-COMMON-FAST-M12X40-SS-A001` | M12×40mm hex head bolt | M12-1.75 × 40mm | ISO 4014 |
| `get_bolt_m12x50()` | `DCS-COMMON-FAST-M12X50-SS-A001` | M12×50mm hex head bolt | M12-1.75 × 50mm | ISO 4014 |
| `get_bolt_m16x50()` | `DCS-COMMON-FAST-M16X50-SS-A001` | M16×50mm hex head bolt | M16-2.0 × 50mm | ISO 4014 |
| `get_hex_nut_m4()` | `DCS-COMMON-FAST-M4-NUT-SS-A001` | M4 hex nut | M4-0.7 | ISO 4032 |
| `get_hex_nut_m6()` | `DCS-COMMON-FAST-M6-NUT-SS-A001` | M6 hex nut | M6-1.0 | ISO 4032 |
| `get_hex_nut_m8()` | `DCS-COMMON-FAST-M8-NUT-SS-A001` | M8 hex nut | M8-1.25 | ISO 4032 |
| `get_hex_nut_m10()` | `DCS-COMMON-FAST-M10-NUT-SS-A001` | M10 hex nut | M10-1.5 | ISO 4032 |
| `get_hex_nut_m12()` | `DCS-COMMON-FAST-M12-NUT-SS-A001` | M12 hex nut | M12-1.75 | ISO 4032 |
| `get_hex_nut_m16()` | `DCS-COMMON-FAST-M16-NUT-SS-A001` | M16 hex nut | M16-2.0 | ISO 4032 |
| `get_washer_m4()` | `DCS-COMMON-FAST-M4-WASHER-SS-A001` | M4 flat washer | M4 | ISO 7089 |
| `get_washer_m6()` | `DCS-COMMON-FAST-M6-WASHER-SS-A001` | M6 flat washer | M6 | ISO 7089 |
| `get_washer_m8()` | `DCS-COMMON-FAST-M8-WASHER-SS-A001` | M8 flat washer | M8 | ISO 7089 |
| `get_washer_m10()` | `DCS-COMMON-FAST-M10-WASHER-SS-A001` | M10 flat washer | M10 | ISO 7089 |
| `get_washer_m12()` | `DCS-COMMON-FAST-M12-WASHER-SS-A001` | M12 flat washer | M12 | ISO 7089 |
| `get_washer_m16()` | `DCS-COMMON-FAST-M16-WASHER-SS-A001` | M16 flat washer | M16 | ISO 7089 |

### Bearings

| Function | Part Number Format | Description | Dimensions (ID×OD×W) | Type |
|----------|-------------------|------------|----------------------|------|
| `get_bearing_6205()` | `DCS-COMMON-BRG-6205-A001` | 6205 deep groove ball bearing | 25×52×15mm | Deep groove |
| `get_bearing_6206()` | `DCS-COMMON-BRG-6206-A001` | 6206 deep groove ball bearing | 30×62×16mm | Deep groove |
| `get_bearing_2inch()` | `DCS-COMMON-BRG-2IN-A001` | 2" ID deep groove ball bearing | 50.8×90×20mm* | Deep groove |

*Note: 2" bearing dimensions are approximate. Adjust for specific bearing selection.

## Usage Examples

### Fasteners

```python
from build123d import *
from common_parts.cq_warehouse.fasteners import (
    get_bolt_m6x20,
    get_hex_nut_m6,
    get_washer_m6
)

# Get fasteners
bolt = get_bolt_m6x20(part_number="DCS-COMMON-FAST-M6X20-A001")
nut = get_hex_nut_m6(part_number="DCS-COMMON-FAST-M6-NUT-A001")
washer = get_washer_m6(part_number="DCS-COMMON-FAST-M6-WASHER-A001")

# Position in assembly
bolt_positioned = Location((0, 0, 0)) * bolt
nut_positioned = Location((0, 0, 20)) * nut
washer_positioned = Location((0, 0, -1)) * washer

# Create assembly
fastener_assembly = Compound(children=[
    bolt_positioned,
    nut_positioned,
    washer_positioned
])
```

### Bearings

```python
from build123d import *
from common_parts.cq_warehouse.bearings import get_bearing_6205

# Get bearing
bearing = get_bearing_6205(part_number="DCS-COMMON-BRG-6205-A001")

# Position in assembly
bearing_positioned = Location((0, 0, 0)) * bearing

# Use in assembly
assembly = Compound(children=[bearing_positioned])
```

### In Assembly Files

```python
from build123d import *
from pathlib import Path
import sys

# Add common parts path
common_parts_dir = Path(__file__).parent.parent / "common_parts"
sys.path.insert(0, str(common_parts_dir))

# Import common parts
from cq_warehouse.fasteners.standard_fasteners import get_bolt_m12x40
from cq_warehouse.bearings.ball_bearings import get_bearing_2inch

# Load custom parts (build123d)
trailer_frame = load_step_file("trailer_frame_A001.step")

# Get standard parts
bolts = []
for i in range(24):
    bolt = get_bolt_m12x40(part_number=f"DCS-COMMON-FAST-M12X40-{i+1:02d}")
    # Position bolt...
    bolts.append(bolt)

# Create assembly
assembly_components = [trailer_frame] + bolts
ground_station_assembly = Compound(children=assembly_components)
```

## Adding New Parts

### Step 1: Check cq_warehouse Library

First, check if the part exists in cq_warehouse:
- [cq_warehouse Documentation](https://github.com/gumyr/cq_warehouse)
- Available modules: `fastener`, `bearing`, `gear`, `pulley`, etc.

### Step 2: Create Wrapper Function

Add wrapper function to appropriate module:

```python
# In fasteners/standard_fasteners.py
def get_bolt_m4x16(part_number: Optional[str] = None) -> Part:
    """Get M4×16mm socket head cap screw."""
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M4X16-SS-A001"
    
    return cq_warehouse_to_build123d(
        SocketHeadCapScrew,
        size="M4-0.7",
        length=16,
        fastener_type="iso4762",
        part_number=part_number
    )
```

### Step 3: Export in __init__.py

Add to `fasteners/__init__.py`:

```python
from .standard_fasteners import get_bolt_m4x16

__all__ = [
    # ... existing exports ...
    "get_bolt_m4x16",
]
```

### Step 4: Update Documentation

Add entry to this README.md table.

## Part Numbering Convention

**Format:** `[PROJECT]-COMMON-[CATEGORY]-[SPEC]-[REVISION]`

**Categories:**
- `FAST` - Fasteners
- `BRG` - Bearings
- `GEAR` - Gears
- `PULLEY` - Pulleys

**Examples:**
- `DCS-COMMON-FAST-M6X20-SS-A001` - M6×20mm stainless steel bolt
- `DCS-COMMON-BRG-6205-A001` - 6205 bearing
- `DCS-COMMON-GEAR-SPUR-20T-A001` - 20-tooth spur gear

## Standards Compliance

All parts in this library follow international standards:

- **Fasteners:** ISO standards (ISO 4762, ISO 4014, ISO 4032, ISO 7089)
- **Bearings:** ISO standards (ISO 15 - Rolling bearings)
- **Gears:** ISO standards (ISO 53, ISO 54, etc.)

## References

- [cq_warehouse GitHub](https://github.com/gumyr/cq_warehouse)
- [ISO Fastener Standards](https://www.iso.org/standard/iso-catalogue.html)
- [ISO Bearing Standards](https://www.iso.org/standard/iso-catalogue.html)

