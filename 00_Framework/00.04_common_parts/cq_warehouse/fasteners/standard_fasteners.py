"""
Standard Fasteners Library
Wrapper functions for standard bolts, nuts, washers, and screws using cq_warehouse

This module provides easy-to-use functions for generating standard fasteners
that are compatible with build123d assemblies. All functions return build123d
Part objects ready for use in assemblies.

Part Number Format: [PROJECT]-COMMON-FAST-[SIZE]-[TYPE]-[REVISION]
Example: DCS-COMMON-FAST-M6X20-SS-A001

Usage:
    from common_parts.cq_warehouse.fasteners import get_bolt_m6x20
    
    bolt = get_bolt_m6x20(part_number="DCS-COMMON-FAST-M6X20-A001")
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

from common_parts.cq_warehouse.converters.cq_to_build123d import cq_warehouse_to_build123d

# Import cq_warehouse fastener modules
try:
    from cq_warehouse.fastener import (
        SocketHeadCapScrew,
        HexHeadScrew,
        HexNut,
        Washer,
    )
    CQ_WAREHOUSE_AVAILABLE = True
except ImportError:
    CQ_WAREHOUSE_AVAILABLE = False
    print("WARNING: cq_warehouse not installed. Install with: pip install cq-warehouse")


# ============================================================================
# BOLTS - Socket Head Cap Screws (ISO 4762)
# ============================================================================

def get_bolt_m6x20(part_number: Optional[str] = None) -> Part:
    """
    Get M6×20mm socket head cap screw (ISO 4762).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M6X20-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M6X20-SS-A001"
    
    return cq_warehouse_to_build123d(
        SocketHeadCapScrew,
        size="M6-1",
        length=20,
        fastener_type="iso4762",
        part_number=part_number
    )


def get_bolt_m8x25(part_number: Optional[str] = None) -> Part:
    """
    Get M8×25mm socket head cap screw (ISO 4762).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M8X25-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M8X25-SS-A001"
    
    return cq_warehouse_to_build123d(
        SocketHeadCapScrew,
        size="M8-1.25",
        length=25,
        fastener_type="iso4762",
        part_number=part_number
    )


def get_bolt_m12x40(part_number: Optional[str] = None) -> Part:
    """
    Get M12×40mm hex head bolt (ISO 4014).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M12X40-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M12X40-SS-A001"
    
    return cq_warehouse_to_build123d(
        HexHeadScrew,
        size="M12-1.75",
        length=40,
        fastener_type="iso4014",
        part_number=part_number
    )


# ============================================================================
# NUTS - Hex Nuts (ISO 4032)
# ============================================================================

def get_hex_nut_m6(part_number: Optional[str] = None) -> Part:
    """
    Get M6 hex nut (ISO 4032).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M6-NUT-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M6-NUT-SS-A001"
    
    return cq_warehouse_to_build123d(
        HexNut,
        size="M6-1",
        fastener_type="iso4032",
        part_number=part_number
    )


def get_hex_nut_m8(part_number: Optional[str] = None) -> Part:
    """
    Get M8 hex nut (ISO 4032).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M8-NUT-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M8-NUT-SS-A001"
    
    return cq_warehouse_to_build123d(
        HexNut,
        size="M8-1.25",
        fastener_type="iso4032",
        part_number=part_number
    )


def get_hex_nut_m12(part_number: Optional[str] = None) -> Part:
    """
    Get M12 hex nut (ISO 4032).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M12-NUT-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M12-NUT-SS-A001"
    
    return cq_warehouse_to_build123d(
        HexNut,
        size="M12-1.75",
        fastener_type="iso4032",
        part_number=part_number
    )


# ============================================================================
# WASHERS - Flat Washers (ISO 7089)
# ============================================================================

def get_washer_m6(part_number: Optional[str] = None) -> Part:
    """
    Get M6 flat washer (ISO 7089).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M6-WASHER-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M6-WASHER-SS-A001"
    
    return cq_warehouse_to_build123d(
        Washer,
        size="M6",
        fastener_type="iso7089",
        part_number=part_number
    )


def get_washer_m8(part_number: Optional[str] = None) -> Part:
    """
    Get M8 flat washer (ISO 7089).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M8-WASHER-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M8-WASHER-SS-A001"
    
    return cq_warehouse_to_build123d(
        Washer,
        size="M8",
        fastener_type="iso7089",
        part_number=part_number
    )


def get_washer_m12(part_number: Optional[str] = None) -> Part:
    """
    Get M12 flat washer (ISO 7089).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M12-WASHER-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M12-WASHER-SS-A001"
    
    return cq_warehouse_to_build123d(
        Washer,
        size="M12",
        fastener_type="iso7089",
        part_number=part_number
    )


# ============================================================================
# ADDITIONAL BOLTS - Additional sizes required for project
# ============================================================================

def get_bolt_m4x12(part_number: Optional[str] = None) -> Part:
    """
    Get M4×12mm socket head cap screw (ISO 4762).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M4X12-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M4X12-SS-A001"
    
    return cq_warehouse_to_build123d(
        SocketHeadCapScrew,
        size="M4-0.7",
        length=12,
        fastener_type="iso4762",
        part_number=part_number
    )


def get_bolt_m10x30(part_number: Optional[str] = None) -> Part:
    """
    Get M10×30mm hex head bolt (ISO 4014).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M10X30-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M10X30-SS-A001"
    
    return cq_warehouse_to_build123d(
        HexHeadScrew,
        size="M10-1.5",
        length=30,
        fastener_type="iso4014",
        part_number=part_number
    )


def get_bolt_m10x35(part_number: Optional[str] = None) -> Part:
    """
    Get M10×35mm hex head bolt (ISO 4014).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M10X35-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M10X35-SS-A001"
    
    return cq_warehouse_to_build123d(
        HexHeadScrew,
        size="M10-1.5",
        length=35,
        fastener_type="iso4014",
        part_number=part_number
    )


def get_bolt_m12x50(part_number: Optional[str] = None) -> Part:
    """
    Get M12×50mm hex head bolt (ISO 4014).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M12X50-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M12X50-SS-A001"
    
    return cq_warehouse_to_build123d(
        HexHeadScrew,
        size="M12-1.75",
        length=50,
        fastener_type="iso4014",
        part_number=part_number
    )


def get_bolt_m16x50(part_number: Optional[str] = None) -> Part:
    """
    Get M16×50mm hex head bolt (ISO 4014).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M16X50-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M16X50-SS-A001"
    
    return cq_warehouse_to_build123d(
        HexHeadScrew,
        size="M16-2",
        length=50,
        fastener_type="iso4014",
        part_number=part_number
    )


# ============================================================================
# ADDITIONAL NUTS - Additional sizes required for project
# ============================================================================

def get_hex_nut_m4(part_number: Optional[str] = None) -> Part:
    """
    Get M4 hex nut (ISO 4032).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M4-NUT-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M4-NUT-SS-A001"
    
    return cq_warehouse_to_build123d(
        HexNut,
        size="M4-0.7",
        fastener_type="iso4032",
        part_number=part_number
    )


def get_hex_nut_m10(part_number: Optional[str] = None) -> Part:
    """
    Get M10 hex nut (ISO 4032).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M10-NUT-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M10-NUT-SS-A001"
    
    return cq_warehouse_to_build123d(
        HexNut,
        size="M10-1.5",
        fastener_type="iso4032",
        part_number=part_number
    )


def get_hex_nut_m16(part_number: Optional[str] = None) -> Part:
    """
    Get M16 hex nut (ISO 4032).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M16-NUT-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M16-NUT-SS-A001"
    
    return cq_warehouse_to_build123d(
        HexNut,
        size="M16-2",
        fastener_type="iso4032",
        part_number=part_number
    )


# ============================================================================
# ADDITIONAL WASHERS - Additional sizes required for project
# ============================================================================

def get_washer_m4(part_number: Optional[str] = None) -> Part:
    """
    Get M4 flat washer (ISO 7089).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M4-WASHER-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M4-WASHER-SS-A001"
    
    return cq_warehouse_to_build123d(
        Washer,
        size="M4",
        fastener_type="iso7089",
        part_number=part_number
    )


def get_washer_m10(part_number: Optional[str] = None) -> Part:
    """
    Get M10 flat washer (ISO 7089).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M10-WASHER-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M10-WASHER-SS-A001"
    
    return cq_warehouse_to_build123d(
        Washer,
        size="M10",
        fastener_type="iso7089",
        part_number=part_number
    )


def get_washer_m16(part_number: Optional[str] = None) -> Part:
    """
    Get M16 flat washer (ISO 7089).
    
    Args:
        part_number: Part number (default: "DCS-COMMON-FAST-M16-WASHER-SS-A001")
        
    Returns:
        build123d Part object ready for assembly
    """
    if not CQ_WAREHOUSE_AVAILABLE:
        raise ImportError("cq_warehouse is required. Install with: pip install cq-warehouse")
    
    if part_number is None:
        part_number = "DCS-COMMON-FAST-M16-WASHER-SS-A001"
    
    return cq_warehouse_to_build123d(
        Washer,
        size="M16",
        fastener_type="iso7089",
        part_number=part_number
    )
