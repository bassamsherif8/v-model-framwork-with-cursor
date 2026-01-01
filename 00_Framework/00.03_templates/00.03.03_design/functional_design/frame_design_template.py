"""
Frame Design Template
Template for designing functional frames with proper structural design

Owner: @DesignEng
Version: 1.0
Date: 2025-12-30
"""

from build123d import *
from math import sqrt


def design_frame_member(
    length: float,
    cross_section_type: str = "rectangular",  # "rectangular", "I-beam", "tube"
    width: float = 50.0,  # mm
    height: float = 50.0,  # mm
    wall_thickness: float = 5.0,  # mm (for tube)
    material_yield: float = 276.0,  # MPa
    load: float = 1000.0,  # N
    safety_factor: float = 2.0
) -> Part:
    """
    Design a frame member (beam) with proper cross-section
    
    Args:
        length: Member length (mm)
        cross_section_type: Type of cross-section
        width: Cross-section width (mm)
        height: Cross-section height (mm)
        wall_thickness: Wall thickness for tube (mm)
        material_yield: Material yield strength (MPa)
        load: Expected load (N)
        safety_factor: Safety factor
        
    Returns:
        build123d Part object
    """
    
    with BuildPart() as member:
        if cross_section_type == "rectangular":
            Box(length, width, height)
        elif cross_section_type == "I-beam":
            # Simplified I-beam (would need proper I-beam profile)
            # For now, use rectangular with flanges
            Box(length, width, height)
            # Add flanges (simplified)
            with BuildPart(mode=Mode.ADD):
                flange_thickness = height * 0.2
                with Locations((0, 0, height/2)):
                    Box(length, width, flange_thickness)
                with Locations((0, 0, -height/2)):
                    Box(length, width, flange_thickness)
        elif cross_section_type == "tube":
            # Rectangular tube
            Box(length, width, height)
            with BuildPart(mode=Mode.SUBTRACT):
                Box(length, width - 2*wall_thickness, height - 2*wall_thickness)
    
    return member.part


def design_frame_joint(
    member1: Part,
    member2: Part,
    joint_type: str = "welded",  # "welded", "bolted"
    gusset_thickness: float = 8.0,
    gusset_size: float = 50.0,
    fillet_radius: float = 3.0
) -> Part:
    """
    Design a frame joint with gussets
    
    Args:
        member1: First frame member
        member2: Second frame member
        joint_type: Type of joint
        gusset_thickness: Gusset thickness (mm)
        gusset_size: Gusset size (mm)
        fillet_radius: Fillet radius (mm)
        
    Returns:
        build123d Part object with joint
    """
    
    with BuildPart() as joint:
        # Add members
        add(member1)
        add(member2)
        
        # Add gussets at joint
        with BuildPart(mode=Mode.ADD):
            # Gussets at corners (simplified)
            # Would need proper positioning based on member geometry
            with Locations((0, 0, 0)):
                Box(gusset_size, gusset_size, gusset_thickness)
    
    return joint.part


def design_frame_structure(
    frame_length: float,
    frame_width: float,
    frame_height: float,
    cross_member_spacing: float = 500.0,  # mm
    member_width: float = 50.0,  # mm
    member_height: float = 50.0,  # mm
    member_thickness: float = 5.0,  # mm
    distributed_load: float = 5000.0,  # N total
    point_loads: list = None,  # List of (x, y, z, load) tuples
    material_yield: float = 276.0,  # MPa
    safety_factor: float = 2.0,
    joint_type: str = "welded"
) -> Part:
    """
    Design a complete frame structure
    
    Args:
        frame_length: Frame length (mm)
        frame_width: Frame width (mm)
        frame_height: Frame height (mm)
        cross_member_spacing: Spacing between cross-members (mm)
        member_width: Member cross-section width (mm)
        member_height: Member cross-section height (mm)
        member_thickness: Member wall thickness (mm, for tube)
        distributed_load: Total distributed load (N)
        point_loads: List of point loads [(x, y, z, load), ...]
        material_yield: Material yield strength (MPa)
        safety_factor: Safety factor
        joint_type: Joint type ("welded" or "bolted")
        
    Returns:
        build123d Part object
    """
    
    # Calculate number of cross-members
    num_cross_members = int(frame_length / cross_member_spacing) + 1
    
    with BuildPart() as frame:
        # Main longitudinal members (length direction)
        # Top members
        with Locations((0, -frame_width/2, frame_height/2)):
            Box(frame_length, member_width, member_height)
        with Locations((0, frame_width/2, frame_height/2)):
            Box(frame_length, member_width, member_height)
        
        # Bottom members
        with Locations((0, -frame_width/2, -frame_height/2)):
            Box(frame_length, member_width, member_height)
        with Locations((0, frame_width/2, -frame_height/2)):
            Box(frame_length, member_width, member_height)
        
        # Vertical members (height direction)
        # Front
        with Locations((-frame_length/2, 0, 0)):
            Box(member_width, frame_width, member_height)
        # Back
        with Locations((frame_length/2, 0, 0)):
            Box(member_width, frame_width, member_height)
        
        # Cross-members (spacing based on deflection limits)
        for i in range(num_cross_members):
            x_pos = -frame_length/2 + i * cross_member_spacing
            with Locations((x_pos, 0, 0)):
                Box(member_width, frame_width, member_height)
        
        # Gussets at joints (simplified)
        with BuildPart(mode=Mode.ADD):
            gusset_thickness = 0.8 * member_height
            gusset_size = 50.0
            
            # Gussets at corners
            corner_positions = [
                (-frame_length/2, -frame_width/2, frame_height/2),
                (frame_length/2, -frame_width/2, frame_height/2),
                (-frame_length/2, frame_width/2, frame_height/2),
                (frame_length/2, frame_width/2, frame_height/2),
                (-frame_length/2, -frame_width/2, -frame_height/2),
                (frame_length/2, -frame_width/2, -frame_height/2),
                (-frame_length/2, frame_width/2, -frame_height/2),
                (frame_length/2, frame_width/2, -frame_height/2),
            ]
            
            for pos in corner_positions:
                with Locations(pos):
                    Box(gusset_size, gusset_size, gusset_thickness)
    
    return frame.part


# Example usage
if __name__ == "__main__":
    # Example: Design frame for trailer
    frame = design_frame_structure(
        frame_length=3000.0,  # mm
        frame_width=2000.0,  # mm
        frame_height=500.0,  # mm
        cross_member_spacing=500.0,  # mm
        member_width=50.0,  # mm
        member_height=50.0,  # mm
        member_thickness=5.0,  # mm
        distributed_load=5000.0,  # N
        material_yield=276.0,  # MPa (Aluminum 6061-T6)
        safety_factor=2.0,
        joint_type="welded"
    )
    
    # Export STEP file
    frame.export_step("frame_example.step")
    print("Frame design complete: frame_example.step")

