"""
Technical Drawing Generator
Multi-View Support for Manufacturing Drawings

This module provides functionality to generate technical drawings with multiple views,
dimensions, tolerances, and GD&T callouts using FreeCAD Python API.

Usage:
    from technical_drawing_generator import generate_technical_drawing
    drawing = generate_technical_drawing(part_number, part_geometry, output_dir)
"""

import os
import sys
from freecad_setup import initialize_freecad, create_freecad_document
from drawing_templates import create_drawing_template, add_drawing_view
from gdt_system import get_gdt_specifications_for_part, create_feature_control_frame
from manufacturing_data import get_part_manufacturing_specs

def generate_technical_drawing(part_number, part_geometry=None, output_dir="02_Design/manufacturing/drawings"):
    """
    Generate complete technical drawing for a part
    
    Args:
        part_number (str): Part number (e.g., "DCNC-BASE-PLATFORM-A001")
        part_geometry: FreeCAD Part object (optional, can load from STEP file)
        output_dir (str): Output directory for drawings
    
    Returns:
        dict: Drawing information dictionary
    """
    # Initialize FreeCAD
    if not initialize_freecad():
        print("FreeCAD not available. Cannot generate technical drawings.")
        return None
    
    try:
        import FreeCAD
        
        # Get manufacturing specifications
        specs = get_part_manufacturing_specs(part_number)
        if not specs:
            print(f"Manufacturing specifications not found for: {part_number}")
            return None
        
        # Create drawing template
        template = create_drawing_template(
            part_number=part_number,
            part_name=specs["part_name"],
            revision="A001",
            material=specs["material"],
            sheet_size="A3",
            scale="1:1"
        )
        
        if not template:
            print("Failed to create drawing template")
            return None
        
        # Load part geometry if not provided
        if part_geometry is None:
            part_geometry = load_part_from_step(part_number)
        
        # Generate views
        views = generate_views(part_geometry, template, part_number)
        template["views"] = views
        
        # Add dimensions
        dimensions = generate_dimensions(part_number, specs, template)
        template["dimensions"] = dimensions
        
        # Add GD&T callouts
        gdt_callouts = generate_gdt_callouts(part_number, specs, template)
        template["gdt_callouts"] = gdt_callouts
        
        # Add manufacturing notes
        notes = generate_manufacturing_notes(part_number, specs)
        template["notes"] = notes
        
        # Export drawings
        export_drawings(template, part_number, output_dir)
        
        return template
        
    except Exception as e:
        print(f"Error generating technical drawing: {e}")
        import traceback
        traceback.print_exc()
        return None

def load_part_from_step(part_number):
    """
    Load part geometry from STEP file
    
    Args:
        part_number (str): Part number
    
    Returns:
        FreeCAD Part object or None
    """
    try:
        import FreeCAD
        
        # Try to find STEP file
        step_file = f"02_Design/parts/{part_number}.step"
        if not os.path.exists(step_file):
            # Try with instance number removed
            base_part = part_number.rsplit("-", 1)[0] if part_number.count("-") > 3 else part_number
            step_file = f"02_Design/parts/{base_part}.step"
        
        if os.path.exists(step_file):
            doc = FreeCAD.openDocument(step_file)
            if doc.Objects:
                return doc.Objects[0]  # Return first object
        else:
            print(f"STEP file not found: {step_file}")
            return None
            
    except Exception as e:
        print(f"Error loading STEP file: {e}")
        return None

def generate_views(part_geometry, template, part_number):
    """
    Generate multiple views for technical drawing
    
    Args:
        part_geometry: FreeCAD Part object
        template (dict): Drawing template
        part_number (str): Part number
    
    Returns:
        list: List of view dictionaries
    """
    views = []
    
    # View positions on sheet (A3 = 297x420mm)
    sheet_width = template["sheet_width"]
    sheet_height = template["sheet_height"]
    
    # Front view (primary view, top-left)
    front_view = {
        "type": "front",
        "position": (50, sheet_height - 150),
        "scale": 1.0,
        "dimensions": [],
        "gdt_callouts": []
    }
    views.append(front_view)
    
    # Top view (above front view)
    top_view = {
        "type": "top",
        "position": (50, sheet_height - 80),
        "scale": 1.0,
        "dimensions": [],
        "gdt_callouts": []
    }
    views.append(top_view)
    
    # Side view (right of front view)
    side_view = {
        "type": "side",
        "position": (250, sheet_height - 150),
        "scale": 1.0,
        "dimensions": [],
        "gdt_callouts": []
    }
    views.append(side_view)
    
    # Isometric view (bottom-right)
    isometric_view = {
        "type": "isometric",
        "position": (250, sheet_height - 300),
        "scale": 0.7,
        "dimensions": [],
        "gdt_callouts": []
    }
    views.append(isometric_view)
    
    # Section view (if needed, bottom-left)
    section_view = {
        "type": "section",
        "position": (50, sheet_height - 300),
        "scale": 1.0,
        "section_plane": "A-A",  # Section plane identifier
        "dimensions": [],
        "gdt_callouts": []
    }
    views.append(section_view)
    
    return views

def generate_dimensions(part_number, specs, template):
    """
    Generate dimensions with tolerances for technical drawing
    
    Args:
        part_number (str): Part number
        specs (dict): Manufacturing specifications
        template (dict): Drawing template
    
    Returns:
        list: List of dimension dictionaries
    """
    dimensions = []
    
    # Get dimension specifications
    dim_specs = specs.get("dimensions", {})
    
    for dim_name, dim_data in dim_specs.items():
        dimension = {
            "name": dim_name,
            "value": dim_data["value"],
            "tolerance": dim_data["tolerance"],
            "is_critical": dim_data.get("is_critical", False),
            "unit": dim_data.get("unit", "mm"),
            "view": "front",  # Default view, can be customized
            "position": (0, 0)  # Position on drawing, to be set
        }
        
        # Format tolerance string
        if isinstance(dimension["tolerance"], tuple):
            lower, upper = dimension["tolerance"]
            dimension["tolerance_string"] = f"+{upper:.3f}/-{lower:.3f}"
        else:
            dimension["tolerance_string"] = f"±{dimension['tolerance']:.3f}"
        
        dimensions.append(dimension)
    
    return dimensions

def generate_gdt_callouts(part_number, specs, template):
    """
    Generate GD&T callouts for technical drawing
    
    Args:
        part_number (str): Part number
        specs (dict): Manufacturing specifications
        template (dict): Drawing template
    
    Returns:
        list: List of GD&T callout dictionaries
    """
    gdt_callouts = []
    
    # Get GD&T specifications
    gdt_specs = specs.get("gdt", {})
    
    # Map part number to part type
    part_type_map = {
        "DCNC-BASE-PLATFORM-A001": "base_platform",
        "DCNC-ACTUATOR-ACT-MOUNT-A001": "actuator_mount",
        "DCNC-ARM-UPPER-ARM-A001": "upper_arm",
        "DCNC-ARM-LOWER-ARM-A001": "lower_arm",
        "DCNC-END-EFFECTOR-A001": "end_effector",
        "DCNC-JOINT-BALL-JOINT-A001": "ball_joint"
    }
    
    base_part = part_number.split("-")[:4]
    base_part_number = "-".join(base_part)
    part_type = part_type_map.get(base_part_number, "")
    
    if part_type:
        # Get GD&T specifications from gdt_system
        from gdt_system import get_gdt_specifications_for_part
        fcf_list = get_gdt_specifications_for_part(part_type)
        
        for fcf in fcf_list:
            callout = {
                "feature_control_frame": fcf.to_dict(),
                "feature": "default",  # Would be matched to actual feature
                "position": (0, 0),  # Position on drawing, to be set
                "view": "front"  # Default view, can be customized
            }
            gdt_callouts.append(callout)
    
    return gdt_callouts

def generate_manufacturing_notes(part_number, specs):
    """
    Generate manufacturing notes for technical drawing
    
    Args:
        part_number (str): Part number
        specs (dict): Manufacturing specifications
    
    Returns:
        list: List of manufacturing note strings
    """
    notes = []
    
    # General notes
    notes.append("GENERAL NOTES:")
    notes.append("1. Material: 6061-T6 Aluminum per ASTM B211 (unless otherwise specified)")
    notes.append("2. Surface finish: Ra 1.6μm unless otherwise specified")
    notes.append("3. Remove all burrs and sharp edges")
    notes.append("4. Chamfer all edges 0.5mm x 45° unless specified otherwise")
    notes.append("5. All dimensions in millimeters (mm)")
    notes.append("6. All tolerances per ISO 2768-mK unless otherwise specified")
    
    # Part-specific notes
    part_notes = specs.get("manufacturing_notes", [])
    if part_notes:
        notes.append("")
        notes.append("PART-SPECIFIC NOTES:")
        for i, note in enumerate(part_notes, start=1):
            notes.append(f"{i}. {note}")
    
    return notes

def export_drawings(template, part_number, output_dir):
    """
    Export technical drawings to DXF, DWG, and PDF formats
    
    Args:
        template (dict): Drawing template
        part_number (str): Part number
        output_dir (str): Output directory
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Note: Actual FreeCAD export implementation would go here
    # This is a placeholder structure
    
    output_files = {
        "dxf": f"{output_dir}/{part_number}_drawing.dxf",
        "dwg": f"{output_dir}/{part_number}_drawing.dwg",
        "pdf": f"{output_dir}/{part_number}_drawing.pdf"
    }
    
    print(f"Drawing export structure created for: {part_number}")
    print(f"  DXF: {output_files['dxf']}")
    print(f"  DWG: {output_files['dwg']}")
    print(f"  PDF: {output_files['pdf']}")
    
    # Actual FreeCAD export code would:
    # 1. Create TechDraw pages for each view
    # 2. Add dimensions and GD&T callouts
    # 3. Add title block
    # 4. Export to DXF/DWG/PDF formats
    
    return output_files

def generate_all_part_drawings():
    """
    Generate technical drawings for all parts
    
    Returns:
        dict: Dictionary mapping part numbers to drawing templates
    """
    from manufacturing_data import get_all_part_numbers
    
    part_numbers = get_all_part_numbers()
    drawings = {}
    
    for part_number in part_numbers:
        print(f"\nGenerating drawing for: {part_number}")
        drawing = generate_technical_drawing(part_number)
        if drawing:
            drawings[part_number] = drawing
    
    return drawings

if __name__ == "__main__":
    # Entry point when running inside FreeCADCmd
    print("=" * 60)
    print("Generating technical drawings for all Delta CNC parts")
    print("=" * 60)
    
    drawings = generate_all_part_drawings()
    
    print("\nSummary:")
    print(f"[OK] Generated drawings for {len(drawings)} parts")

