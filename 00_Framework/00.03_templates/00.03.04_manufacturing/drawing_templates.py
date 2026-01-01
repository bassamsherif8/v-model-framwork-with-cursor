"""
Drawing Template System
For Manufacturing Technical Drawings

This module provides drawing templates with title blocks for technical drawings
following ASME Y14.5 and ISO standards.

Usage:
    from drawing_templates import create_drawing_template
    template = create_drawing_template(part_number, part_name, revision, material)
"""

from freecad_setup import initialize_freecad, create_freecad_document

# Standard drawing sheet sizes (ISO A series)
SHEET_SIZES = {
    "A4": (210, 297),  # mm
    "A3": (297, 420),  # mm
    "A2": (420, 594),  # mm
    "A1": (594, 841),  # mm
    "A0": (841, 1189),  # mm
}

# Title block dimensions (standard ISO format)
TITLE_BLOCK_WIDTH = 180  # mm
TITLE_BLOCK_HEIGHT = 55  # mm

def create_title_block(doc, sheet_width, sheet_height, part_info):
    """
    Create title block for technical drawing
    
    Args:
        doc: FreeCAD document
        sheet_width (float): Sheet width in mm
        sheet_height (float): Sheet height in mm
        part_info (dict): Part information dictionary
            - part_number (str): Part number (e.g., "DCNC-BASE-PLATFORM-A001")
            - part_name (str): Part name (e.g., "Base Platform")
            - revision (str): Revision (e.g., "A001")
            - material (str): Material specification (e.g., "6061-T6 Aluminum per ASTM B211")
            - scale (str): Drawing scale (e.g., "1:1")
            - drawn_by (str): Drawn by (optional)
            - checked_by (str): Checked by (optional)
            - date (str): Date (optional, defaults to current date)
    
    Returns:
        FreeCAD object: Title block object
    """
    try:
        import FreeCAD
        from datetime import datetime
        
        # Default values
        part_number = part_info.get("part_number", "")
        part_name = part_info.get("part_name", "")
        revision = part_info.get("revision", "A001")
        material = part_info.get("material", "6061-T6 Aluminum per ASTM B211")
        scale = part_info.get("scale", "1:1")
        drawn_by = part_info.get("drawn_by", "")
        checked_by = part_info.get("checked_by", "")
        date = part_info.get("date", datetime.now().strftime("%Y-%m-%d"))
        
        # Title block position (bottom right corner)
        title_block_x = sheet_width - TITLE_BLOCK_WIDTH
        title_block_y = 0
        
        # Create title block as a group of lines and text
        # Note: This is a conceptual implementation
        # Actual FreeCAD implementation would use TechDraw workbench
        
        # Title block structure:
        # ┌─────────────────────────────────────────┐
        # │ Part Number: DCNC-BASE-PLATFORM-A001   │
        # │ Part Name: Base Platform               │
        # │ Revision: A001                         │
        # │ Material: 6061-T6 Aluminum per ASTM   │
        # │ Scale: 1:1                             │
        # │ Date: 2024-12-22                       │
        # │ Drawn By: [Name]                       │
        # │ Checked By: [Name]                     │
        # └─────────────────────────────────────────┘
        
        # For now, return a placeholder object
        # Actual implementation will create FreeCAD objects
        title_block = {
            "part_number": part_number,
            "part_name": part_name,
            "revision": revision,
            "material": material,
            "scale": scale,
            "drawn_by": drawn_by,
            "checked_by": checked_by,
            "date": date,
            "x": title_block_x,
            "y": title_block_y,
            "width": TITLE_BLOCK_WIDTH,
            "height": TITLE_BLOCK_HEIGHT
        }
        
        return title_block
        
    except Exception as e:
        print(f"Error creating title block: {e}")
        return None

def create_drawing_template(part_number, part_name, revision="A001", 
                           material="6061-T6 Aluminum per ASTM B211",
                           sheet_size="A3", scale="1:1"):
    """
    Create a complete drawing template with title block
    
    Args:
        part_number (str): Part number (e.g., "DCNC-BASE-PLATFORM-A001")
        part_name (str): Part name (e.g., "Base Platform")
        revision (str): Revision (e.g., "A001")
        material (str): Material specification
        sheet_size (str): Sheet size ("A4", "A3", "A2", "A1", "A0")
        scale (str): Drawing scale (e.g., "1:1", "1:2")
    
    Returns:
        dict: Drawing template information
    """
    if not initialize_freecad():
        print("FreeCAD not available. Creating template structure only.")
        return None
    
    try:
        import FreeCAD
        
        # Get sheet dimensions
        if sheet_size not in SHEET_SIZES:
            sheet_size = "A3"  # Default to A3
        
        sheet_width, sheet_height = SHEET_SIZES[sheet_size]
        
        # Create new document
        doc = create_freecad_document(f"{part_number}_Drawing")
        
        # Part information
        part_info = {
            "part_number": part_number,
            "part_name": part_name,
            "revision": revision,
            "material": material,
            "scale": scale,
            "date": None,  # Will be set by title block function
        }
        
        # Create title block
        title_block = create_title_block(doc, sheet_width, sheet_height, part_info)
        
        # Drawing template structure
        template = {
            "document": doc,
            "sheet_size": sheet_size,
            "sheet_width": sheet_width,
            "sheet_height": sheet_height,
            "title_block": title_block,
            "part_info": part_info,
            "views": [],  # Will contain drawing views
            "dimensions": [],  # Will contain dimensions
            "gdt_callouts": [],  # Will contain GD&T callouts
            "notes": []  # Will contain manufacturing notes
        }
        
        return template
        
    except Exception as e:
        print(f"Error creating drawing template: {e}")
        return None

def add_drawing_view(template, view_type, position, scale=1.0):
    """
    Add a drawing view to the template
    
    Args:
        template (dict): Drawing template
        view_type (str): View type ("front", "top", "side", "isometric", "section")
        position (tuple): View position (x, y) in mm
        scale (float): View scale (default 1.0)
    
    Returns:
        dict: View information
    """
    view = {
        "type": view_type,
        "position": position,
        "scale": scale,
        "dimensions": [],
        "gdt_callouts": []
    }
    
    template["views"].append(view)
    return view

def get_title_block_template():
    """
    Get title block template structure
    
    Returns:
        dict: Title block template structure
    """
    return {
        "fields": [
            {"name": "part_number", "label": "Part Number", "position": (10, 45), "size": (80, 5)},
            {"name": "part_name", "label": "Part Name", "position": (10, 40), "size": (80, 5)},
            {"name": "revision", "label": "Revision", "position": (10, 35), "size": (30, 5)},
            {"name": "material", "label": "Material", "position": (10, 30), "size": (80, 5)},
            {"name": "scale", "label": "Scale", "position": (10, 25), "size": (30, 5)},
            {"name": "date", "label": "Date", "position": (10, 20), "size": (30, 5)},
            {"name": "drawn_by", "label": "Drawn By", "position": (10, 15), "size": (40, 5)},
            {"name": "checked_by", "label": "Checked By", "position": (50, 15), "size": (40, 5)},
        ],
        "width": TITLE_BLOCK_WIDTH,
        "height": TITLE_BLOCK_HEIGHT
    }

if __name__ == "__main__":
    # Test drawing template creation
    print("Testing drawing template creation...")
    
    template = create_drawing_template(
        part_number="DCNC-BASE-PLATFORM-A001",
        part_name="Base Platform",
        revision="A001",
        material="6061-T6 Aluminum per ASTM B211",
        sheet_size="A3",
        scale="1:1"
    )
    
    if template:
        print("✓ Drawing template created successfully")
        print(f"  Part Number: {template['part_info']['part_number']}")
        print(f"  Sheet Size: {template['sheet_size']}")
        print(f"  Sheet Dimensions: {template['sheet_width']} x {template['sheet_height']} mm")
    else:
        print("✗ Drawing template creation failed")

