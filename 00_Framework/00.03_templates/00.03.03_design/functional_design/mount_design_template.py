"""
Mount Design Template
Template for designing functional mounts with vibration isolation considerations

Owner: @DesignEng
Version: 1.0
Date: 2025-12-30
"""

from build123d import *


def design_mount(
    base_length: float,
    base_width: float,
    base_thickness: float,
    component_weight: float,  # kg
    vibration_acceleration: float = 10.0,  # g
    material_yield: float = 276.0,  # MPa
    safety_factor: float = 2.5,  # Higher for dynamic loads
    mounting_hole_count: int = 4,
    hole_diameter: float = 8.0,  # mm
    gusset_thickness: float = None,
    rib_thickness: float = None,
    fillet_radius: float = 3.0
) -> Part:
    """
    Design a functional mount with vibration isolation considerations
    
    Args:
        base_length: Base plate length (mm)
        base_width: Base plate width (mm)
        base_thickness: Base plate thickness (mm)
        component_weight: Weight of component to mount (kg)
        vibration_acceleration: Expected vibration acceleration (g)
        material_yield: Material yield strength (MPa)
        safety_factor: Safety factor (higher for dynamic loads)
        mounting_hole_count: Number of mounting holes
        hole_diameter: Mounting hole diameter (mm)
        gusset_thickness: Gusset thickness (mm)
        rib_thickness: Rib thickness (mm)
        fillet_radius: Fillet radius (mm)
        
    Returns:
        build123d Part object
    """
    
    # Calculate dynamic load
    component_force = component_weight * 9.81  # N (weight)
    dynamic_load = component_force * vibration_acceleration  # N (with vibration)
    
    # Calculate required base thickness based on load
    # Simplified: base thickness based on bending stress
    # σ = Mc/I, where M = F*L/4 (simplified), I = b*t³/12
    # Solving for t: t = sqrt(12*M/(b*σ_allowable))
    allowable_stress = material_yield / safety_factor  # MPa
    moment = dynamic_load * base_length / 4  # N·mm (simplified)
    required_thickness = sqrt(12 * moment / (base_width * allowable_stress))  # mm
    
    # Use maximum of specified and calculated
    base_thickness = max(base_thickness, required_thickness)
    
    # Calculate gusset dimensions
    if gusset_thickness is None:
        gusset_thickness = 0.8 * base_thickness
    
    gusset_height = max(20.0, 2.5 * base_thickness)
    
    # Calculate rib dimensions
    if rib_thickness is None:
        rib_thickness = 0.5 * base_thickness
    
    rib_height = 2.0 * base_thickness
    rib_spacing = 3.0 * rib_height
    
    # Calculate mounting hole positions
    margin = 20.0  # mm from edge
    if mounting_hole_count == 4:
        hole_positions = [
            (-base_length/2 + margin, -base_width/2 + margin),
            (base_length/2 - margin, -base_width/2 + margin),
            (-base_length/2 + margin, base_width/2 - margin),
            (base_length/2 - margin, base_width/2 - margin),
        ]
    elif mounting_hole_count == 6:
        hole_positions = [
            (-base_length/2 + margin, -base_width/2 + margin),
            (0, -base_width/2 + margin),
            (base_length/2 - margin, -base_width/2 + margin),
            (-base_length/2 + margin, base_width/2 - margin),
            (0, base_width/2 - margin),
            (base_length/2 - margin, base_width/2 - margin),
        ]
    else:
        # Default: 4 holes
        hole_positions = [
            (-base_length/2 + margin, -base_width/2 + margin),
            (base_length/2 - margin, -base_width/2 + margin),
            (-base_length/2 + margin, base_width/2 - margin),
            (base_length/2 - margin, base_width/2 - margin),
        ]
    
    with BuildPart() as mount:
        # Base plate
        Box(base_length, base_width, base_thickness)
        
        # Gussets at mounting points (reinforcement)
        with BuildPart(mode=Mode.ADD):
            gusset_angle = 45.0  # degrees
            gusset_length = gusset_height / sqrt(2)  # For 45° gusset
            
            for pos in hole_positions:
                # Gusset at each mounting point
                with Locations((pos[0], pos[1], base_thickness)):
                    # Create triangular gusset
                    with BuildSketch():
                        with BuildLine():
                            # Triangular profile
                            Line((0, 0), (gusset_length, 0))
                            Line((gusset_length, 0), (0, gusset_height))
                            Line((0, gusset_height), (0, 0))
                        make_face()
                    # Extrude in all 4 directions (simplified: one direction)
                    extrude(amount=gusset_thickness, direction=(1, 1, 0))
        
        # Ribs for stiffness (distribute load)
        with BuildPart(mode=Mode.ADD):
            # Ribs along length
            num_ribs_length = int(base_length / rib_spacing)
            for i in range(num_ribs_length):
                x_pos = -base_length/2 + (i + 1) * rib_spacing
                with Locations((x_pos, 0, base_thickness)):
                    Box(rib_thickness, base_width, rib_height)
            
            # Ribs along width
            num_ribs_width = int(base_width / rib_spacing)
            for i in range(num_ribs_width):
                y_pos = -base_width/2 + (i + 1) * rib_spacing
                with Locations((0, y_pos, base_thickness)):
                    Box(base_length, rib_thickness, rib_height)
        
        # Mounting holes
        with BuildPart(mode=Mode.SUBTRACT):
            for pos in hole_positions:
                with Locations((pos[0], pos[1], -1)):
                    Cylinder(radius=hole_diameter/2, height=base_thickness + 2)
        
        # Fillets at stress concentrations
        # Note: build123d fillet operations would go here
    
    return mount.part


def design_mount_with_vibration_isolation(
    base_length: float,
    base_width: float,
    base_thickness: float,
    component_weight: float,
    isolation_pad_thickness: float = 5.0,  # mm
    isolation_pad_material: str = "rubber",
    **kwargs
) -> Part:
    """
    Design mount with vibration isolation pads
    
    Args:
        isolation_pad_thickness: Thickness of isolation pads (mm)
        isolation_pad_material: Material of isolation pads
        **kwargs: Other parameters from design_mount()
        
    Returns:
        build123d Part object
    """
    
    mount = design_mount(
        base_length=base_length,
        base_width=base_width,
        base_thickness=base_thickness,
        component_weight=component_weight,
        **kwargs
    )
    
    # Add isolation pad features (recesses for pads)
    with BuildPart() as mount_with_isolation:
        # Base mount
        add(mount)
        
        # Isolation pad recesses (simplified representation)
        with BuildPart(mode=Mode.SUBTRACT):
            pad_size = 30.0  # mm
            pad_depth = isolation_pad_thickness
            
            # Recesses at mounting points
            hole_positions = kwargs.get('hole_positions', [
                (-base_length/2 + 20, -base_width/2 + 20),
                (base_length/2 - 20, -base_width/2 + 20),
                (-base_length/2 + 20, base_width/2 - 20),
                (base_length/2 - 20, base_width/2 - 20),
            ])
            
            for pos in hole_positions:
                with Locations((pos[0], pos[1], base_thickness - pad_depth)):
                    Box(pad_size, pad_size, pad_depth + 1)
    
    return mount_with_isolation.part


# Example usage
if __name__ == "__main__":
    # Example: Design mount for 50kg component with 10g vibration
    mount = design_mount(
        base_length=200.0,
        base_width=150.0,
        base_thickness=12.0,
        component_weight=50.0,  # kg
        vibration_acceleration=10.0,  # g
        material_yield=276.0,  # MPa (Aluminum 6061-T6)
        safety_factor=2.5,
        mounting_hole_count=4,
        hole_diameter=8.0
    )
    
    # Export STEP file
    mount.export_step("mount_example.step")
    print("Mount design complete: mount_example.step")

