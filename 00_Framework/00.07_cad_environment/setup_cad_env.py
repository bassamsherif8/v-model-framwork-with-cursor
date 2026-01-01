"""
Project CAD Environment Setup
Creates and configures CAD environment for V-Model projects

Usage:
    python setup_cad_env.py

This script:
1. Creates a Python 3.11 virtual environment named 'cad_env'
2. Installs CAD dependencies (build123d, cadquery-ocp, etc.)
3. Verifies installation
"""

import subprocess
import sys
import os
from pathlib import Path

def check_python_version():
    """Check if Python 3.11 is available"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 11:
        return True, f"{version.major}.{version.minor}.{version.micro}"
    return False, f"{version.major}.{version.minor}.{version.micro}"

def find_python311():
    """Try to find Python 3.11 executable"""
    import shutil
    
    # Try common names
    for name in ['python3.11', 'py -3.11', 'python311']:
        if shutil.which(name):
            return name
    
    # Try py launcher with version
    try:
        result = subprocess.run(['py', '-3.11', '--version'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return 'py -3.11'
    except:
        pass
    
    return None

def create_venv(venv_path: Path, python_exe=None):
    """Create virtual environment"""
    if python_exe:
        print(f"Creating virtual environment with: {python_exe}")
        if 'py -3.11' in python_exe:
            # Use py launcher
            cmd = ['py', '-3.11', '-m', 'venv', str(venv_path)]
        else:
            cmd = [python_exe, '-m', 'venv', str(venv_path)]
    else:
        print("Creating virtual environment with current Python...")
        cmd = [sys.executable, '-m', 'venv', str(venv_path)]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"ERROR: Failed to create virtual environment")
        print(f"Command: {' '.join(cmd)}")
        print(f"Error: {result.stderr}")
        return False
    
    return True

def install_packages(venv_path: Path):
    """Install CAD packages in virtual environment"""
    if sys.platform == 'win32':
        pip = venv_path / "Scripts" / "pip.exe"
        python = venv_path / "Scripts" / "python.exe"
    else:
        pip = venv_path / "bin" / "pip"
        python = venv_path / "bin" / "python"
    
    if not pip.exists():
        print(f"ERROR: pip not found at {pip}")
        return False
    
    packages = [
        "build123d",
        "cadquery-ocp",
        "cadquery",
        "cq-warehouse"
    ]
    
    print("\nInstalling CAD dependencies...")
    print("This may take several minutes...")
    
    for package in packages:
        print(f"\nInstalling {package}...")
        result = subprocess.run([str(pip), "install", package], 
                              capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"WARNING: Failed to install {package}")
            print(f"Error: {result.stderr}")
            # Continue with other packages
        else:
            print(f"  ✓ {package} installed")
    
    return True

def verify_installation(venv_path: Path):
    """Verify CAD packages are installed"""
    if sys.platform == 'win32':
        python = venv_path / "Scripts" / "python.exe"
    else:
        python = venv_path / "bin" / "python"
    
    print("\nVerifying installation...")
    
    checks = [
        ("build123d", "import build123d"),
        ("OCP", "import OCP"),
        ("cadquery", "import cadquery as cq"),
    ]
    
    all_ok = True
    for name, import_cmd in checks:
        result = subprocess.run([str(python), "-c", import_cmd],
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  ✓ {name} available")
        else:
            print(f"  ✗ {name} NOT available")
            all_ok = False
    
    return all_ok

def main():
    """Main setup function"""
    print("="*70)
    print("CAD Environment Setup")
    print("="*70)
    print()
    
    project_root = Path.cwd()
    venv_path = project_root / "cad_env"
    
    # Check if already exists
    if venv_path.exists():
        response = input(f"CAD environment already exists at {venv_path}\n"
                        f"Recreate? (y/N): ").strip().lower()
        if response == 'y':
            import shutil
            print("Removing existing environment...")
            shutil.rmtree(venv_path)
        else:
            print("Keeping existing environment.")
            print("\nVerifying existing installation...")
            if verify_installation(venv_path):
                print("\n✓ CAD environment is ready!")
            else:
                print("\n⚠ CAD environment exists but some packages are missing.")
                print("Run: cad_env\\Scripts\\pip.exe install build123d cadquery-ocp")
            return
    
    # Check Python version
    is_ok, version = check_python_version()
    print(f"Current Python version: {version}")
    
    python_exe = None
    if not is_ok:
        print(f"WARNING: Python 3.11+ recommended (current: {version})")
        print("Attempting to find Python 3.11...")
        python_exe = find_python311()
        if python_exe:
            print(f"Found: {python_exe}")
        else:
            print("Python 3.11 not found. Using current Python.")
            response = input("Continue anyway? (y/N): ").strip().lower()
            if response != 'y':
                print("Setup cancelled.")
                return
    
    # Create virtual environment
    print(f"\nCreating virtual environment at: {venv_path}")
    if not create_venv(venv_path, python_exe):
        print("\nERROR: Failed to create virtual environment")
        return
    
    print("✓ Virtual environment created")
    
    # Install packages
    if not install_packages(venv_path):
        print("\nWARNING: Some packages failed to install")
        print("You may need to install them manually:")
        print("  cad_env\\Scripts\\pip.exe install build123d cadquery-ocp")
    
    # Verify installation
    if verify_installation(venv_path):
        print("\n" + "="*70)
        print("✓ CAD Environment Setup Complete!")
        print("="*70)
        print("\nTo activate the environment:")
        print("  Windows: activate_cad_env.bat")
        print("  PowerShell: .\\activate_cad_env.ps1")
        print("\nTo run scripts with CAD environment:")
        print("  run_with_cad_env.bat \"script.py\"")
    else:
        print("\n" + "="*70)
        print("⚠ Setup completed with warnings")
        print("="*70)
        print("\nSome packages may need manual installation.")
        print("See CAD_ENV_SETUP.md for troubleshooting.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user.")
    except Exception as e:
        print(f"\n\nERROR: {e}")
        import traceback
        traceback.print_exc()

