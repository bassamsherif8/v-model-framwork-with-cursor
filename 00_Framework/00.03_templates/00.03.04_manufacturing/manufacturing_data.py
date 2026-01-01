"""
Manufacturing Data and Standards
Reference data for manufacturing-ready designs

Used by @DesignEng for consistent manufacturing specifications
"""

# ============================================================================
# TOLERANCE STANDARDS
# ============================================================================

# Standard tolerance grades (ISO/ANSI)
TOLERANCE_GRADES = {
    "coarse": 0.5,      # ±0.5mm - Rough fabrication
    "medium": 0.2,      # ±0.2mm - General machining
    "fine": 0.1,        # ±0.1mm - Precision machining
    "very_fine": 0.05,  # ±0.05mm - High precision
    "ultra_fine": 0.01  # ±0.01mm - Ultra precision
}

# Default tolerances by feature type
DEFAULT_TOLERANCES = {
    "frame_dimensions": 0.5,        # ±0.5mm for frame structural dimensions
    "mounting_holes": 0.1,          # ±0.1mm for mounting holes
    "precision_holes": 0.05,        # ±0.05mm for precision alignment holes
    "threaded_holes": 0.1,          # ±0.1mm for threaded hole positions
    "surface_dimensions": 0.2,      # ±0.2mm for general surface dimensions
    "welded_assemblies": 1.0,       # ±1.0mm for welded frame assemblies
}

# Position tolerances (ISO 1101)
POSITION_TOLERANCES = {
    "loose": 0.5,       # General positioning
    "standard": 0.2,    # Standard mounting
    "tight": 0.1,       # Precision alignment
    "very_tight": 0.05  # High precision alignment
}

# ============================================================================
# SURFACE FINISH (Ra values in micrometers)
# ============================================================================

SURFACE_FINISH = {
    "as_welded": 12.5,      # Ra 12.5μm - As welded, rough
    "general": 3.2,         # Ra 3.2μm - General machining
    "standard": 1.6,        # Ra 1.6μm - Standard machining (default)
    "fine": 0.8,            # Ra 0.8μm - Fine machining
    "precision": 0.4,       # Ra 0.4μm - Precision surfaces (bearing surfaces)
    "very_precision": 0.2   # Ra 0.2μm - Very precision (high precision joints)
}

# Default surface finish
DEFAULT_SURFACE_FINISH = SURFACE_FINISH["standard"]  # Ra 1.6μm

# ============================================================================
# THREAD SPECIFICATIONS
# ============================================================================

# Metric thread specifications (ISO 261)
THREAD_SPECS = {
    "M6": {
        "pitch": 1.0,
        "major_dia": 6.0,
        "minor_dia": 4.917,
        "tap_drill": 5.0,
        "class": "6H"  # Internal thread class
    },
    "M8": {
        "pitch": 1.25,
        "major_dia": 8.0,
        "minor_dia": 6.647,
        "tap_drill": 6.8,
        "class": "6H"
    },
    "M10": {
        "pitch": 1.5,
        "major_dia": 10.0,
        "minor_dia": 8.376,
        "tap_drill": 8.5,
        "class": "6H"
    },
    "M12": {
        "pitch": 1.75,
        "major_dia": 12.0,
        "minor_dia": 10.106,
        "tap_drill": 10.2,
        "class": "6H"
    },
    "M16": {
        "pitch": 2.0,
        "major_dia": 16.0,
        "minor_dia": 13.835,
        "tap_drill": 14.0,
        "class": "6H"
    }
}

# Thread callout format: M[size]x[pitch]-[class] [depth]
def thread_callout(size, depth="THRU"):
    """Generate standard thread callout."""
    spec = THREAD_SPECS[size]
    return f"M{size}x{spec['pitch']}-{spec['class']} {depth}"

# ============================================================================
# HOLE SPECIFICATIONS
# ============================================================================

# Standard hole sizes (drill sizes in mm)
STANDARD_HOLES = {
    "clearance_M6": 6.5,    # Clearance hole for M6 bolt
    "clearance_M8": 9.0,    # Clearance hole for M8 bolt
    "clearance_M10": 11.0,  # Clearance hole for M10 bolt
    "clearance_M12": 13.0,  # Clearance hole for M12 bolt
    "clearance_M16": 17.0,  # Clearance hole for M16 bolt
}

# ============================================================================
# MATERIAL SPECIFICATIONS
# ============================================================================

MATERIALS = {
    "steel_a36": {
        "name": "Steel A36",
        "standard": "ASTM A36",
        "density": 7850.0,  # kg/m³
        "yield_strength": 250.0,  # MPa
        "tensile_strength": 400.0,  # MPa
        "surface_finish_default": SURFACE_FINISH["as_welded"]
    },
    "aluminum_6061_t6": {
        "name": "Aluminum 6061-T6",
        "standard": "ASTM B211",
        "density": 2700.0,  # kg/m³
        "yield_strength": 276.0,  # MPa
        "tensile_strength": 310.0,  # MPa
        "surface_finish_default": SURFACE_FINISH["standard"]
    }
}

# ============================================================================
# WELD SPECIFICATIONS
# ============================================================================

WELD_SPECS = {
    "fillet_weld": {
        "size": 5.0,  # mm leg length
        "type": "Fillet weld",
        "standard": "AWS D1.1"
    },
    "butt_weld": {
        "type": "Butt weld",
        "standard": "AWS D1.1"
    }
}

# ============================================================================
# GD&T DATUM FRAMEWORK
# ============================================================================

# Standard datum references
DATUM_SYSTEM = {
    "A": "Primary datum (usually primary plane or axis)",
    "B": "Secondary datum (usually secondary plane or axis)",
    "C": "Tertiary datum (usually tertiary plane or axis)"
}

# ============================================================================
# MANUFACTURING NOTES (General)
# ============================================================================

GENERAL_MANUFACTURING_NOTES = [
    "All dimensions in millimeters unless otherwise specified",
    "All tolerances are ± unless otherwise specified",
    "All surfaces Ra 1.6μm unless otherwise specified",
    "Remove all sharp edges (0.5mm chamfer or fillet)",
    "Verify dimensions before welding",
    "Clean all surfaces before welding (remove oil, rust, paint)",
    "Follow AWS D1.1 welding standards for structural steel",
    "Post-weld inspection required for all structural welds"
]
