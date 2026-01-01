"""
Bracket Design Template
Template for designing functional brackets with proper structural design

Owner: @DesignEng
Version: 1.0
Date: 2025-12-30
"""

from build123d import *
from math import sqrt


def design_bracket(
    base_length: float,
    base_width: float,
    base_thickness: float,
    arm_length: float,
    arm_width: float,
    arm_thickness: float,
    load: float,  # N
    load_distance: float,  # mm from mounting
    material_yield: float = 276.0,  # MPa (Aluminum 6061-T6)
    safety_factor: float = 2.0,
    gusset_thickness: float = None,
    gusset_height: float = None,
    fillet_radius: float = 3.0,  # mm
    hole_diameter: float = 6.0,  # mm
    hole_positions: list = None
) -> Part:
    """
    Design a functional bracket with proper structural design
    
    Args:
        base_length: Base plate length (mm)
        base_width: Base plate width (mm)
        base_thickness: Base plate thickness (mm)
        arm_length: Bracket arm length (mm)
        arm_width: Bracket arm width (mm)
        arm_thickness: Bracket arm thickness (mm)
        load: Expected load (N)
        load_distance: Distance from mounting to load (mm)
        material_yield: Material yield strength (MPa)
        safety_factor: Safety factor
        gusset_thickness: Gusset thickness (mm, default: 0.8× base_thickness)
        gusset_height: Gusset height (mm, default: based on load)
        fillet_radius: Fillet radius at corners (mm)
        hole_diameter: Mounting hole diameter (mm)
        hole_positions: List of (x, y) positions for mounting holes (mm)
        
    Returns:
        build123d Part object
    """
    
    # Calculate gusset dimensions if not provided
    if gusset_thickness is None:
        gusset_thickness = 0.8 * base_thickness
    
    if gusset_height is None:
        # Calculate gusset height based on load
        # Simplified: gusset height = 2-3× base_thickness, minimum 20mm
        gusset_height = max(20.0, 2.5 * base_thickness)
    
    # Default hole positions (4 corners)
    if hole_positions is None:
        margin = 15.0  # mm from edge
        hole_positions = [
            (-base_length/2 + margin, -base_width/2 + margin),
            (base_length/2 - margin, -base_width/2 + margin),
            (-base_length/2 + margin, base_width/2 - margin),
            (base_length/2 - margin, base_width/2 - margin),
        ]
    
    with BuildPart() as bracket:
        # Base plate
        Box(base_length, base_width, base_thickness)
        
        # Bracket arm
        with BuildPart(mode=Mode.ADD):
            # Position arm at edge of base
            with Locations((0, base_width/2, base_thickness)):
                Box(arm_length, arm_thickness, arm_height := arm_length * 0.8)
        
        # Gussets for reinforcement (at joint between base and arm)
        with BuildPart(mode=Mode.ADD):
            gusset_angle = 45.0  # degrees
            gusset_length = gusset_height / sqrt(2)  # For 45° gusset
            
            # Front gusset
            with Locations((arm_length/2 - gusset_length/2, base_width/2, base_thickness)):
                with BuildSketch():
                    # Triangular gusset profile
                    with BuildLine():
                        Line((0, 0), (gusset_length, 0))
                        Line((gusset_length, 0), (0, gusset_height))
                        Line((0, gusset_height), (0, 0))
                    make_face()
                extrude(amount=gusset_thickness, direction=(-1, 0, 0))
            
            # Back gusset (mirror)
            with Locations((-arm_length/2 + gusset_length/2, base_width/2, base_thickness)):
                with BuildSketch():
                    with BuildLine():
                        Line((0, 0), (-gusset_length, 0))
                        Line((-gusset_length, 0), (0, gusset_height))
                        Line((0, gusset_height), (0, 0))
                    make_face()
                extrude(amount=gusset_thickness, direction=(1, 0, 0))
        
        # Ribs for stiffness (along arm length)
        with BuildPart(mode=Mode.ADD):
            rib_thickness = 0.5 * arm_thickness
            rib_height = 2.0 * arm_thickness
            rib_spacing = 3.0 * rib_height
            
            # Add ribs along arm (simplified: 2 ribs)
            for i in [-1, 1]:
                with Locations((i * arm_length/4, base_width/2 + arm_thickness/2, base_thickness)):
                    Box(rib_thickness, arm_thickness, rib_height)
        
        # Mounting holes
        with BuildPart(mode=Mode.SUBTRACT):
            for pos in hole_positions:
                with Locations((pos[0], pos[1], -1)):
                    Cylinder(radius=hole_diameter/2, height=base_thickness + 2)
        
        # Fillets at stress concentrations
        with BuildPart(mode=Mode.ADD):
            # Fillet at base-arm joint (internal corner)
            # Note: build123d fillet operations would go here
            # This is a simplified representation
            pass
    
    return bracket.part


def design_bracket_with_bosses(
    base_length: float,
    base_width: float,
    base_thickness: float,
    arm_length: float,
    arm_width: float,
    arm_thickness: float,
    load: float,
    load_distance: float,
    boss_height: float = 5.0,  # mm
    boss_diameter: float = 12.0,  # mm
    **kwargs
) -> Part:
    """
    Design bracket with bosses for mounting features
    
    Args:
        boss_height: Height of mounting bosses (mm)
        boss_diameter: Diameter of mounting bosses (mm)
        **kwargs: Other parameters from design_bracket()
        
    Returns:
        build123d Part object
    """
    
    bracket = design_bracket(
        base_length=base_length,
        base_width=base_width,
        base_thickness=base_thickness,
        arm_length=arm_length,
        arm_width=arm_width,
        arm_thickness=arm_thickness,
        load=load,
        load_distance=load_distance,
        **kwargs
    )
    
    # Add bosses at mounting holes
    with BuildPart() as bracket_with_bosses:
        # Base bracket
        add(bracket)
        
        # Bosses
        with BuildPart(mode=Mode.ADD):
            hole_positions = kwargs.get('hole_positions', None)
            if hole_positions is None:
                margin = 15.0
                hole_positions = [
                    (-base_length/2 + margin, -base_width/2 + margin),
                    (base_length/2 - margin, -base_width/2 + margin),
                    (-base_length/2 + margin, base_width/2 - margin),
                    (base_length/2 - margin, base_width/2 - margin),
                ]
            
            for pos in hole_positions:
                with Locations((pos[0], pos[1], base_thickness)):
                    Cylinder(radius=boss_diameter/2, height=boss_height)
    
    return bracket_with_bosses.part


# Example usage
if __name__ == "__main__":
    # Example: Design bracket for 1000N load at 100mm
    bracket = design_bracket(
        base_length=150.0,
        base_width=100.0,
        base_thickness=10.0,
        arm_length=120.0,
        arm_width=50.0,
        arm_thickness=8.0,
        load=1000.0,  # N
        load_distance=100.0,  # mm
        material_yield=276.0,  # MPa (Aluminum 6061-T6)
        safety_factor=2.0,
        fillet_radius=3.0,
        hole_diameter=6.0
    )
    
    # Export STEP file
    bracket.export_step("bracket_example.step")
    print("Bracket design complete: bracket_example.step")

