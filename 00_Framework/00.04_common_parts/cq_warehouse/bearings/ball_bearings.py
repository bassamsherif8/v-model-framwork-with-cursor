"""
Standard Bearings Library
Wrapper functions for standard ball bearings using cq_warehouse

This module provides easy-to-use functions for generating standard bearings
that are compatible with build123d assemblies. All functions return build123d
Part objects ready for use in assemblies.

Part Number Format: [PROJECT]-COMMON-BRG-[SIZE]-[REVISION]
Example: DCS-COMMON-BRG-6205-A001

Usage:
    from common_parts.cq_warehouse.bearings import get_bearing_6205
    
    bearing = get_bearing_6205(part_number="DCS-COMMON-BRG-6205-A001")
    # Use in build123d assembly...
"""

from typing import Optional
from build123d import Part

# Import converter
import sys
from pathlib import Path

# Add parent directories to path for imports
_common_parts_dir = Path(__file__).parent.parent.parent
sys.path.insert(0, str(_common_parts_dir))

from cq_warehouse.converters.cq_to_build123d import cq_warehouse_to_build123d

# Import cq_warehouse bearing modules
try:
    from cq_warehouse.bearing import BallBearing
    CQ_WAREHOUSE_AVAILABLE = True
except ImportError:
    CQ_WAREHOUSE_AVAILABLE = False
    print("WARNING: cq_warehouse not installed. Install with: pip install cq-warehouse")


# ============================================================================
# BALL BEARINGS - Deep Groove Ball Bearings
# ============================================================================

def get_bearing_6205(part_number: Optional[str] = None) -> Part:
    """
    Get 6205 deep groove ball bearing (25×52×15mm).
    
    Standard dimensions:
    - Inner diameter: 25mm
    - Outer diameter: 52mm
    - Width: 15mm
    
    Args:
        part_number: Part number (default: "DCS-COMMON-BRG-6205-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-BRG-6205-A001"
    
    return cq_warehouse_to_build123d(
        BallBearing,
        inner_diameter=25,
        outer_diameter=52,
        width=15,
        part_number=part_number
    )


def get_bearing_6206(part_number: Optional[str] = None) -> Part:
    """
    Get 6206 deep groove ball bearing (30×62×16mm).
    
    Standard dimensions:
    - Inner diameter: 30mm
    - Outer diameter: 62mm
    - Width: 16mm
    
    Args:
        part_number: Part number (default: "DCS-COMMON-BRG-6206-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-BRG-6206-A001"
    
    return cq_warehouse_to_build123d(
        BallBearing,
        inner_diameter=30,
        outer_diameter=62,
        width=16,
        part_number=part_number
    )


def get_bearing_2inch(part_number: Optional[str] = None) -> Part:
    """
    Get 2" ID deep groove ball bearing (50.8mm ID).
    
    This is a common size for trailer axles and hose reels.
    Standard dimensions:
    - Inner diameter: 50.8mm (2 inches)
    - Outer diameter: 90mm (approximate)
    - Width: 20mm (approximate)
    
    Note: Exact dimensions may vary by manufacturer. Adjust outer_diameter
    and width as needed for specific bearing selection.
    
    Args:
        part_number: Part number (default: "DCS-COMMON-BRG-2IN-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-BRG-2IN-A001"
    
    # 2" = 50.8mm
    # Common 2" ID bearing dimensions (may need adjustment for specific bearing)
    return cq_warehouse_to_build123d(
        BallBearing,
        inner_diameter=50.8,  # 2 inches
        outer_diameter=90,     # Approximate - adjust for specific bearing
        width=20,              # Approximate - adjust for specific bearing
        part_number=part_number
    )

