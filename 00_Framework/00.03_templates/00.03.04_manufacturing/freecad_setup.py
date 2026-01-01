"""
FreeCAD Environment Setup and Utilities
For Manufacturing Drawing Generation

This module provides setup and utility functions for FreeCAD Python API
to generate manufacturing-ready technical drawings.

Usage:
    import freecad_setup
    freecad_setup.initialize_freecad()
"""

import sys
import os

# ---------------------------------------------------------------------------
# FreeCAD path and command configuration
# ---------------------------------------------------------------------------
#
# On Windows, FreeCAD typically ships with:
# - GUI executable:       C:\Program Files\FreeCAD X.Y\bin\FreeCAD.exe
# - Console executable:   C:\Program Files\FreeCAD X.Y\bin\FreeCADCmd.exe
#
# For manufacturing drawing generation we want to run our Python scripts
# inside FreeCAD's own Python environment, using FreeCADCmd.exe.
#
# >>> IMPORTANT <<<
# You told me your FreeCAD GUI is at:
#   "C:\Program Files\FreeCAD 1.0\bin\freecad.exe"
# I will assume the console executable is:
#   "C:\Program Files\FreeCAD 1.0\bin\FreeCADCmd.exe"
# If it differs on your system, update FREECAD_CMD below accordingly.
#

FREECAD_CMD = r"C:\Program Files\FreeCAD 1.0\bin\FreeCADCmd.exe"

# FreeCAD library search paths (used when running inside system Python)
# Windows typical paths:
FREECAD_PATHS = [
    os.path.dirname(FREECAD_CMD),            # Directory of FreeCADCmd.exe
    r"C:\Program Files\FreeCAD\bin",        # Windows default
    r"C:\Program Files (x86)\FreeCAD\bin",  # Windows 32-bit
    r"C:\Users\{}\AppData\Local\Programs\FreeCAD\bin".format(os.getenv('USERNAME', '')),  # User install
]

# Linux typical paths:
if sys.platform.startswith('linux'):
    FREECAD_PATHS = [
        "/usr/lib/freecad/lib",          # Linux default
        "/usr/lib/freecad-python3/lib",  # Alternative
    ]

# macOS typical paths:
if sys.platform == 'darwin':
    FREECAD_PATHS = [
        "/Applications/FreeCAD.app/Contents/lib",        # macOS default
        "/Applications/FreeCAD.app/Contents/Resources/lib",  # Alternative
    ]

def find_freecad():
    """Find FreeCAD installation and add to Python path"""
    for path in FREECAD_PATHS:
        if os.path.exists(path):
            sys.path.insert(0, path)
            return path
    return None

def initialize_freecad():
    """
    Initialize FreeCAD Python API
    
    Returns:
        bool: True if FreeCAD initialized successfully, False otherwise
    """
    try:
        # Try to import FreeCAD (may already be available)
        import FreeCAD
        print("FreeCAD module found")
        return True
    except ImportError:
        # Try to find FreeCAD installation
        freecad_path = find_freecad()
        if freecad_path:
            try:
                import FreeCAD
                print(f"FreeCAD initialized from: {freecad_path}")
                return True
            except ImportError:
                print(f"FreeCAD path found but import failed: {freecad_path}")
                return False
        else:
            print("FreeCAD not found. Please install FreeCAD:")
            print("  Windows: https://www.freecad.org/downloads.php")
            print("  Linux: sudo apt-get install freecad")
            print("  macOS: https://www.freecad.org/downloads.php")
            return False

def create_freecad_document(name="DeltaCNC_Drawing"):
    """
    Create a new FreeCAD document
    
    Args:
        name (str): Document name
        
    Returns:
        FreeCAD.Document: New FreeCAD document
    """
    try:
        import FreeCAD
        doc = FreeCAD.newDocument(name)
        return doc
    except Exception as e:
        print(f"Error creating FreeCAD document: {e}")
        return None

def setup_drawing_environment():
    """
    Set up FreeCAD environment for technical drawing generation
    
    Returns:
        tuple: (FreeCAD module, Document) or (None, None) if failed
    """
    if not initialize_freecad():
        return None, None
    
    try:
        import FreeCAD
        doc = create_freecad_document("DeltaCNC_Manufacturing_Drawings")
        
        # Set units to millimeters
        FreeCAD.Units.setSchema(8)  # ISO 2768 (mm, N, s)
        
        # Set precision for dimensions
        FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Units").SetInt("Decimals", 3)
        
        return FreeCAD, doc
    except Exception as e:
        print(f"Error setting up drawing environment: {e}")
        return None, None

def check_freecad_availability():
    """
    Check if FreeCAD is available and report status
    
    Returns:
        dict: Status information
    """
    status = {
        "available": False,
        "version": None,
        "path": None,
        "modules": []
    }
    
    try:
        import FreeCAD
        status["available"] = True
        status["version"] = FreeCAD.Version()
        status["path"] = FreeCAD.getHomePath()
        
        # Check for required modules
        required_modules = ["Part", "PartDesign", "TechDraw", "Drawing"]
        for module_name in required_modules:
            try:
                module = getattr(FreeCAD, module_name)
                status["modules"].append(module_name)
            except AttributeError:
                pass
        
        return status
    except ImportError:
        return status

if __name__ == "__main__":
    # Test FreeCAD availability
    print("Checking FreeCAD availability...")
    status = check_freecad_availability()
    
    if status["available"]:
        print(f"[OK] FreeCAD {status['version']} available")
        print(f"  Path: {status['path']}")
        print(f"  Modules: {', '.join(status['modules'])}")
        
        # Test initialization
        print("\nTesting FreeCAD initialization...")
        FreeCAD, doc = setup_drawing_environment()
        if FreeCAD and doc:
            print("[OK] FreeCAD environment setup successful")
            print(f"  Document: {doc.Name}")
        else:
            print("[FAIL] FreeCAD environment setup failed")
    else:
        print("[FAIL] FreeCAD not available")
        print("\nPlease install FreeCAD:")
        print("  https://www.freecad.org/downloads.php")

