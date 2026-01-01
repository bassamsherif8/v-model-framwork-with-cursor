# Common Parts Library

**Version:** 1.0.0  
**Status:** Active  
**Purpose:** Standardized, reusable components for V-Model projects

## Overview

The Common Parts Library provides a centralized repository of standard mechanical components that can be used across multiple projects. This library integrates CadQuery and cq_warehouse for automatic generation of standard parts (fasteners, bearings, gears) while maintaining build123d for custom project-specific parts.

## Structure

```
common_parts/
├── cq_warehouse/          # CadQuery-based standard parts
│   ├── fasteners/         # Bolts, nuts, washers, screws
│   ├── bearings/          # Ball bearings, roller bearings
│   ├── gears/             # Spur gears, helical gears, bevel gears
│   └── converters/        # CadQuery → build123d conversion utilities
│
└── custom/                # Custom standard parts (build123d)
    ├── wheels/            # Wheel assemblies
    ├── axles/             # Axle assemblies
    └── hitches/           # Hitch assemblies
```

## Installation

### Prerequisites

- Python 3.8 or higher
- build123d (already in use)
- OCP (OpenCascade Python - already in use)

### Install CadQuery and cq_warehouse

```bash
# Install CadQuery
pip install cadquery

# Install cq_warehouse (standard parts library)
pip install cq-warehouse
```

### Verify Installation

```bash
# Verify CadQuery
python -c "import cadquery as cq; print('CadQuery OK')"

# Verify cq_warehouse
python -c "import cq_warehouse; print('cq_warehouse OK')"

# Verify build123d (should already be installed)
python -c "import build123d; print('build123d OK')"
```

## Usage

### Quick Start

```python
from build123d import *
from common_parts.cq_warehouse.fasteners import get_bolt_m6x20, get_hex_nut_m6

# Get standard fasteners
bolt = get_bolt_m6x20(part_number="DCS-COMMON-FAST-M6X20-A001")
nut = get_hex_nut_m6(part_number="DCS-COMMON-FAST-M6-NUT-A001")

# Use in assembly
assembly = Compound(children=[bolt, nut])
```

### Import Patterns

**Standard parts from cq_warehouse:**
```python
from common_parts.cq_warehouse.fasteners import get_bolt_m6x20
from common_parts.cq_warehouse.bearings import get_bearing_6205
```

**Custom parts (build123d):**
```python
from build123d import *
```

**Custom standard parts (build123d-based):**
```python
from common_parts.custom.wheels.wheel_assembly import get_standard_wheel_15in
```

## CAD Library Selection

### When to Use Each Library

**Use build123d for:**
- Custom project-specific parts (frames, brackets, mounts, housings)
- Complex assemblies requiring precise positioning
- Parts with custom geometry not available in standard libraries
- Primary assembly coordination

**Use CadQuery + cq_warehouse for:**
- Standard fasteners (bolts, nuts, washers, screws)
- Standard bearings (ball bearings, roller bearings)
- Standard gears (spur, helical, bevel)
- Standard pulleys and belts
- Any part available in cq_warehouse library

**Decision Tree:**
1. Is this a standard mechanical component? → Check cq_warehouse first
2. Available in cq_warehouse? → Use cq_warehouse via common_parts wrappers
3. Not available? → Use build123d for custom design
4. For assemblies: Use build123d as primary, import cq_warehouse parts via converter

## Part Numbering

**Format:** `[PROJECT]-COMMON-[CATEGORY]-[SPEC]-[REVISION]`

**Examples:**
- `DCS-COMMON-FAST-M6X20-SS-A001` - M6×20mm bolt
- `DCS-COMMON-BRG-6205-A001` - 6205 bearing
- `DCS-COMMON-FAST-M6-NUT-SS-A001` - M6 hex nut

**Categories:**
- `FAST` - Fasteners (bolts, nuts, washers, screws)
- `BRG` - Bearings
- `GEAR` - Gears
- `WHEEL` - Wheels
- `AXLE` - Axles
- `HITCH` - Hitches

## Available Parts

See `cq_warehouse/README.md` for complete catalog of available parts.

### Fasteners
- M6, M8, M12 bolts (socket head cap screws, hex head)
- M6, M8, M12 hex nuts
- M6, M8, M12 flat washers

### Bearings
- 6205 deep groove ball bearing (25×52×15mm)
- 6206 deep groove ball bearing (30×62×16mm)
- 2" ID bearing (50.8mm ID)

## Adding New Standard Parts

### For cq_warehouse Parts

1. Check if part exists in cq_warehouse library
2. Create wrapper function in appropriate category (fasteners, bearings, etc.)
3. Use converter to convert to build123d format
4. Update `cq_warehouse/README.md` with new part
5. Export function in `__init__.py`

### For Custom Standard Parts

1. Create part using build123d in `custom/[category]/`
2. Create template function that returns build123d Part
3. Document in appropriate README
4. Add to library index

## Examples

See `USAGE_EXAMPLES.md` for detailed usage examples.

## Troubleshooting

### Import Errors

**Error:** `ModuleNotFoundError: No module named 'cq_warehouse'`
**Solution:** Install cq_warehouse: `pip install cq-warehouse`

**Error:** `ModuleNotFoundError: No module named 'cadquery'`
**Solution:** Install CadQuery: `pip install cadquery`

### Conversion Errors

**Error:** `Failed to convert CadQuery object to build123d`
**Solution:** 
- Verify STEP export is working
- Check that OCP is installed
- Verify build123d can import STEP files

## References

- [CadQuery Documentation](https://cadquery.readthedocs.io/)
- [cq_warehouse Documentation](https://github.com/gumyr/cq_warehouse)
- [build123d Documentation](https://build123d.readthedocs.io/)

## License

This library follows the project's license and standards.

