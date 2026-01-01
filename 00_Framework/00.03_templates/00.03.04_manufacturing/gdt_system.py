"""
GD&T (Geometric Dimensioning & Tolerancing) System
ASME Y14.5-2018 Standard

This module provides GD&T annotation functionality for technical drawings,
including feature control frames, datum references, and geometric tolerances.

Usage:
    from gdt_system import create_feature_control_frame, create_datum_reference
    fcf = create_feature_control_frame("flatness", 0.05, ["A"])
"""

from freecad_setup import initialize_freecad

# GD&T Symbols (ASME Y14.5-2018)
GDT_SYMBOLS = {
    "flatness": "⏊",
    "straightness": "—",
    "circularity": "○",
    "cylindricity": "⌭",
    "profile_of_line": "⌓",
    "profile_of_surface": "⌓",
    "angularity": "∠",
    "perpendicularity": "⟂",
    "parallelism": "∥",
    "position": "⌖",
    "concentricity": "◎",
    "symmetry": "⌯",
    "circular_runout": "↗",
    "total_runout": "↗↗",
}

# Datum reference letters (A-Z)
DATUM_LETTERS = [chr(ord('A') + i) for i in range(26)]

class FeatureControlFrame:
    """
    Feature Control Frame for GD&T callouts
    
    Format: [Geometric Characteristic Symbol] [Tolerance Value] [Datum References]
    Example: ⏊ 0.05 A (Flatness 0.05mm relative to Datum A)
    """
    
    def __init__(self, geometric_characteristic, tolerance_value, datum_references=None, 
                 material_condition=None, modifier=None):
        """
        Initialize Feature Control Frame
        
        Args:
            geometric_characteristic (str): GD&T symbol name (e.g., "flatness", "position")
            tolerance_value (float): Tolerance value in mm
            datum_references (list): List of datum references (e.g., ["A", "B", "C"])
            material_condition (str): Material condition modifier ("M", "L", "S") - optional
            modifier (str): Additional modifier (e.g., "CZ" for combined zone) - optional
        """
        self.geometric_characteristic = geometric_characteristic
        self.tolerance_value = tolerance_value
        self.datum_references = datum_references or []
        self.material_condition = material_condition
        self.modifier = modifier
        
        # Get symbol
        self.symbol = GDT_SYMBOLS.get(geometric_characteristic.lower(), "?")
    
    def __str__(self):
        """String representation of feature control frame"""
        parts = [self.symbol, f"{self.tolerance_value:.3f}"]
        
        # Add material condition modifier if present
        if self.material_condition:
            parts.append(self.material_condition)
        
        # Add datum references
        if self.datum_references:
            parts.extend(self.datum_references)
        
        # Add modifier if present
        if self.modifier:
            parts.append(self.modifier)
        
        return " ".join(parts)
    
    def to_dict(self):
        """Convert to dictionary for serialization"""
        return {
            "geometric_characteristic": self.geometric_characteristic,
            "symbol": self.symbol,
            "tolerance_value": self.tolerance_value,
            "datum_references": self.datum_references,
            "material_condition": self.material_condition,
            "modifier": self.modifier,
            "string": str(self)
        }

class DatumReference:
    """
    Datum Reference for GD&T
    
    Datums establish reference frames for geometric tolerances.
    """
    
    def __init__(self, letter, description, feature_type="plane"):
        """
        Initialize Datum Reference
        
        Args:
            letter (str): Datum letter (A-Z)
            description (str): Description of datum feature
            feature_type (str): Type of feature ("plane", "axis", "point")
        """
        if letter not in DATUM_LETTERS:
            raise ValueError(f"Invalid datum letter: {letter}. Must be A-Z.")
        
        self.letter = letter.upper()
        self.description = description
        self.feature_type = feature_type
    
    def __str__(self):
        """String representation of datum reference"""
        return f"Datum {self.letter}: {self.description} ({self.feature_type})"
    
    def to_dict(self):
        """Convert to dictionary for serialization"""
        return {
            "letter": self.letter,
            "description": self.description,
            "feature_type": self.feature_type
        }

# Standard Datum Reference Framework for Delta CNC
STANDARD_DATUMS = {
    "A": DatumReference("A", "Base platform top surface", "plane"),
    "B": DatumReference("B", "Base platform center axis", "axis"),
    "C": DatumReference("C", "Base platform angular reference (0° position)", "plane")
}

def create_feature_control_frame(geometric_characteristic, tolerance_value, 
                                 datum_references=None, material_condition=None, modifier=None):
    """
    Create a Feature Control Frame
    
    Args:
        geometric_characteristic (str): GD&T symbol name
        tolerance_value (float): Tolerance value in mm
        datum_references (list): List of datum letters
        material_condition (str): Material condition modifier
        modifier (str): Additional modifier
    
    Returns:
        FeatureControlFrame: Feature control frame object
    
    Examples:
        # Flatness
        fcf = create_feature_control_frame("flatness", 0.05, ["A"])
        
        # Position
        fcf = create_feature_control_frame("position", 0.02, ["A", "B", "C"])
        
        # Perpendicularity
        fcf = create_feature_control_frame("perpendicularity", 0.05, ["A"])
    """
    return FeatureControlFrame(
        geometric_characteristic=geometric_characteristic,
        tolerance_value=tolerance_value,
        datum_references=datum_references,
        material_condition=material_condition,
        modifier=modifier
    )

def create_datum_reference(letter, description, feature_type="plane"):
    """
    Create a Datum Reference
    
    Args:
        letter (str): Datum letter (A-Z)
        description (str): Description of datum feature
        feature_type (str): Type of feature
    
    Returns:
        DatumReference: Datum reference object
    """
    return DatumReference(letter, description, feature_type)

def get_gdt_specifications_for_part(part_type):
    """
    Get GD&T specifications for a specific part type
    
    Args:
        part_type (str): Part type ("base_platform", "actuator_mount", "upper_arm", 
                                   "lower_arm", "end_effector", "ball_joint")
    
    Returns:
        list: List of FeatureControlFrame objects
    """
    specifications = {
        "base_platform": [
            create_feature_control_frame("flatness", 0.05, ["A"]),
            create_feature_control_frame("circularity", 0.1),
            create_feature_control_frame("perpendicularity", 0.05, ["A"]),
            create_feature_control_frame("position", 0.02, ["A", "B", "C"]),  # Actuator mount holes
        ],
        "actuator_mount": [
            create_feature_control_frame("position", 0.02, ["A", "B", "C"]),  # Relative to base
            create_feature_control_frame("concentricity", 0.02, ["A"]),  # Actuator hole
            create_feature_control_frame("perpendicularity", 0.02, ["A"]),  # Mounting surface
        ],
        "upper_arm": [
            create_feature_control_frame("straightness", 0.02),  # Per 100mm
            create_feature_control_frame("roundness", 0.01),
            create_feature_control_frame("parallelism", 0.02),  # Between arms
        ],
        "lower_arm": [
            create_feature_control_frame("straightness", 0.02),  # Per 100mm
            create_feature_control_frame("roundness", 0.01),
            create_feature_control_frame("parallelism", 0.02),  # Between arms
        ],
        "end_effector": [
            create_feature_control_frame("flatness", 0.02, ["A"]),
            create_feature_control_frame("position", 0.02, ["A", "B", "C"]),  # Arm mount positions
            create_feature_control_frame("concentricity", 0.05, ["A"]),  # Spindle hole
        ],
        "ball_joint": [
            create_feature_control_frame("roundness", 0.005),  # Ball
            create_feature_control_frame("concentricity", 0.01),
        ],
    }
    
    return specifications.get(part_type.lower(), [])

def apply_gdt_to_drawing(drawing_template, part_type, feature_positions):
    """
    Apply GD&T callouts to a drawing template
    
    Args:
        drawing_template (dict): Drawing template
        part_type (str): Part type
        feature_positions (dict): Dictionary mapping features to positions
            Example: {"top_surface": (100, 200), "mount_hole_1": (150, 180)}
    
    Returns:
        dict: Updated drawing template with GD&T callouts
    """
    gdt_specs = get_gdt_specifications_for_part(part_type)
    
    gdt_callouts = []
    for fcf in gdt_specs:
        # Find feature position (simplified - actual implementation would match features)
        position = feature_positions.get("default", (0, 0))
        
        callout = {
            "feature_control_frame": fcf.to_dict(),
            "position": position,
            "feature": "default"  # Would be matched to actual feature
        }
        gdt_callouts.append(callout)
    
    drawing_template["gdt_callouts"] = gdt_callouts
    return drawing_template

def create_dimension_with_tolerance(dimension_value, tolerance, is_critical=False):
    """
    Create a dimension with tolerance specification
    
    Args:
        dimension_value (float): Nominal dimension value
        tolerance (float or tuple): Tolerance value(s)
            If float: ±tolerance (bilateral)
            If tuple: (lower, upper) (unilateral)
        is_critical (bool): Whether this is a critical dimension
    
    Returns:
        dict: Dimension specification
    
    Examples:
        # Bilateral tolerance
        dim = create_dimension_with_tolerance(450.0, 0.1)
        # Result: "450 ±0.1"
        
        # Unilateral tolerance
        dim = create_dimension_with_tolerance(50.0, (0.0, 0.02))
        # Result: "50 +0.02/-0.00"
    """
    if isinstance(tolerance, tuple):
        lower, upper = tolerance
        tolerance_str = f"+{upper:.3f}/-{lower:.3f}"
    else:
        tolerance_str = f"±{tolerance:.3f}"
    
    dimension = {
        "nominal": dimension_value,
        "tolerance": tolerance,
        "tolerance_string": tolerance_str,
        "is_critical": is_critical,
        "string": f"{dimension_value:.3f} {tolerance_str}"
    }
    
    if is_critical:
        dimension["string"] = f"{dimension['string']} (CRITICAL)"
    
    return dimension

if __name__ == "__main__":
    # Test GD&T system
    print("Testing GD&T system...")
    
    # Test Feature Control Frame
    fcf1 = create_feature_control_frame("flatness", 0.05, ["A"])
    print(f"✓ Feature Control Frame: {fcf1}")
    
    fcf2 = create_feature_control_frame("position", 0.02, ["A", "B", "C"])
    print(f"✓ Feature Control Frame: {fcf2}")
    
    # Test Datum Reference
    datum_a = STANDARD_DATUMS["A"]
    print(f"✓ Datum Reference: {datum_a}")
    
    # Test GD&T specifications
    base_specs = get_gdt_specifications_for_part("base_platform")
    print(f"\n✓ Base Platform GD&T Specifications ({len(base_specs)} callouts):")
    for spec in base_specs:
        print(f"  - {spec}")
    
    # Test dimension with tolerance
    dim = create_dimension_with_tolerance(450.0, 0.1, is_critical=False)
    print(f"\n✓ Dimension: {dim['string']}")
    
    dim_critical = create_dimension_with_tolerance(200.0, 0.02, is_critical=True)
    print(f"✓ Critical Dimension: {dim_critical['string']}")

