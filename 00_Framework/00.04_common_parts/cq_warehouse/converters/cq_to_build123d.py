"""
Common Parts Bridge: CadQuery → build123d
Converts cq_warehouse parts to build123d-compatible format

This module provides conversion utilities to bridge CadQuery/cq_warehouse
parts with build123d assemblies. The conversion is done via STEP file
export/import to ensure compatibility.

Usage:
    from common_parts.cq_warehouse.converters import cq_part_to_build123d
    
    # Convert a CadQuery object
    build123d_part = cq_part_to_build123d(cq_object, part_number="DCS-COMMON-FAST-M6X20-A001")
"""

import cadquery as cq
from build123d import Part, import_step
from pathlib import Path
import tempfile
import os
from typing import Optional, Union


def cq_part_to_build123d(
    cq_object: Union[cq.Workplane, cq.Solid],
    part_number: Optional[str] = None,
    label: Optional[str] = None
) -> Part:
    """
    Convert a CadQuery object to build123d Part.
    
    Strategy: Export to STEP, then import into build123d.
    This ensures proper BREP geometry transfer between libraries.
    
    Args:
        cq_object: CadQuery Workplane or Solid object
        part_number: Part number for metadata (e.g., "DCS-COMMON-FAST-M6X20-A001")
        label: Label for the part (defaults to part_number if provided)
        
    Returns:
        build123d Part object ready for assembly
        
    Raises:
        RuntimeError: If conversion fails
        FileNotFoundError: If temporary file cannot be created
        
    Example:
        >>> import cadquery as cq
        >>> from common_parts.cq_warehouse.converters import cq_part_to_build123d
        >>> 
        >>> # Create a simple CadQuery part
        >>> cq_part = cq.Workplane("XY").box(10, 10, 10)
        >>> 
        >>> # Convert to build123d
        >>> build123d_part = cq_part_to_build123d(
        ...     cq_part,
        ...     part_number="TEST-PART-001"
        ... )
    """
    # Export CadQuery object to temporary STEP file
    tmp_file = None
    try:
        # Create temporary file
        tmp_fd, tmp_path = tempfile.mkstemp(suffix='.step', prefix='cq_convert_')
        tmp_file = tmp_path
        os.close(tmp_fd)  # Close file descriptor, we'll use the path
        
        # Export CadQuery object to STEP
        # Handle both Workplane and Solid objects
        if isinstance(cq_object, cq.Workplane):
            # Extract solid from workplane
            solid = cq_object.val()
            if solid is None:
                raise ValueError("Workplane does not contain a solid")
            cq.exporters.export(solid, tmp_path)
        elif isinstance(cq_object, cq.Solid):
            cq.exporters.export(cq_object, tmp_path)
        else:
            raise TypeError(f"Unsupported CadQuery object type: {type(cq_object)}")
        
        # Verify STEP file was created
        if not Path(tmp_path).exists():
            raise FileNotFoundError(f"STEP file was not created: {tmp_path}")
        
        # Import STEP into build123d
        build123d_part = import_step(tmp_path)
        
        # Add metadata
        if part_number:
            build123d_part.label = part_number
        elif label:
            build123d_part.label = label
        
        # Add metadata dictionary if supported
        if hasattr(build123d_part, 'metadata'):
            build123d_part.metadata = {
                "source": "cq_warehouse",
                "part_number": part_number or label or "UNKNOWN",
                "converted_from": "CadQuery"
            }
        
        return build123d_part
        
    except Exception as e:
        raise RuntimeError(f"Failed to convert CadQuery object to build123d: {e}") from e
        
    finally:
        # Clean up temporary file
        if tmp_file and Path(tmp_file).exists():
            try:
                Path(tmp_file).unlink()
            except Exception:
                # Ignore cleanup errors
                pass


def cq_warehouse_to_build123d(
    warehouse_part_func,
    *args,
    part_number: Optional[str] = None,
    label: Optional[str] = None,
    **kwargs
) -> Part:
    """
    Wrapper to convert cq_warehouse part directly to build123d.
    
    This function calls a cq_warehouse part generation function and
    immediately converts the result to build123d format.
    
    Args:
        warehouse_part_func: Function that generates a cq_warehouse part
        *args: Positional arguments to pass to warehouse_part_func
        part_number: Part number for metadata
        label: Label for the part
        **kwargs: Keyword arguments to pass to warehouse_part_func
        
    Returns:
        build123d Part object ready for assembly
        
    Example:
        >>> from cq_warehouse.fastener import SocketHeadCapScrew
        >>> from common_parts.cq_warehouse.converters import cq_warehouse_to_build123d
        >>> 
        >>> # Generate and convert in one step
        >>> bolt = cq_warehouse_to_build123d(
        ...     SocketHeadCapScrew,
        ...     size="M6-1.0",
        ...     length=20,
        ...     fastener_type="iso4762",
        ...     part_number="DCS-COMMON-FAST-M6X20-A001"
        ... )
    """
    # Call warehouse function to generate CadQuery part
    cq_part = warehouse_part_func(*args, **kwargs)
    
    # Convert to build123d
    return cq_part_to_build123d(cq_part, part_number=part_number, label=label)

