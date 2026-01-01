# CAD Environment Setup Guide

**Purpose:** Standardized CAD environment setup for V-Model projects  
**Version:** 1.0  
**Date:** 2025-12-30

---

## Overview

All V-Model projects requiring CAD libraries (build123d, FreeCAD) use a standardized Python 3.11 virtual environment named `cad_env`. This ensures consistent, isolated dependencies across projects.

---

## Quick Start

### Automatic Setup (Recommended)

1. **Run setup script:**
   ```powershell
   python setup_cad_env.py
   ```

2. **Activate environment:**
   ```powershell
   .\activate_cad_env.ps1
   ```
   Or double-click: `activate_cad_env.bat`

3. **Verify installation:**
   ```powershell
   python -c "import build123d; import OCP; print('OK')"
   ```

---

## Manual Setup

If automatic setup fails:

1. **Create virtual environment:**
   ```powershell
   python -m venv cad_env --python=python3.11
   ```
   Or if Python 3.11 is not default:
   ```powershell
   py -3.11 -m venv cad_env
   ```

2. **Activate environment:**
   ```powershell
   .\cad_env\Scripts\Activate.ps1
   ```

3. **Install dependencies:**
   ```powershell
   pip install build123d cadquery-ocp cadquery cq-warehouse
   ```

---

## Using CAD Environment

### Method 1: Generic Wrapper (Recommended)

Use the generic wrapper to run any script with CAD environment:

```powershell
.\run_with_cad_env.bat "02_Design/parts/generate_step_files.py"
```

Or PowerShell:
```powershell
.\run_with_cad_env.ps1 "02_Design/parts/generate_step_files.py"
```

**Benefits:**
- Automatically activates CAD environment
- Verifies dependencies before running
- Keeps window open to show results
- Works with any Python script

### Method 2: Manual Activation

1. **Activate environment:**
   ```powershell
   .\activate_cad_env.ps1
   ```

2. **Run your script:**
   ```powershell
   python 02_Design/parts/generate_step_files.py
   ```

### Method 3: Project-Specific Wrappers

For frequently used scripts, create project-specific wrappers:

**Example:** `02_Design/parts/generate_step_files_with_cad_env.bat`

```batch
@echo off
call ..\..\run_with_cad_env.bat "generate_step_files.py"
```

---

## Standard Files

Every V-Model project with CAD should include:

| File | Purpose |
|------|---------|
| `cad_env/` | Virtual environment directory (Python 3.11) |
| `activate_cad_env.bat` | Windows batch activation script |
| `activate_cad_env.ps1` | PowerShell activation script |
| `run_with_cad_env.bat` | Generic wrapper for any script |
| `run_with_cad_env.ps1` | PowerShell generic wrapper |
| `setup_cad_env.py` | Automatic environment setup script |
| `CAD_ENV_SETUP.md` | This documentation file |

---

## Dependencies

### Required Packages

- **build123d** - Python-based CAD library
- **cadquery-ocp** - OpenCASCADE Community Edition (OCP) bindings
- **cadquery** - Parametric CAD library
- **cq-warehouse** - Standard parts library

### Installation

```powershell
.\activate_cad_env.ps1
pip install build123d cadquery-ocp cadquery cq-warehouse
```

---

## Troubleshooting

### "Python 3.11 not found"

**Solution:** Install Python 3.11 or use py launcher:
```powershell
py -3.11 -m venv cad_env
```

### "build123d not available"

**Solution:** Install in activated environment:
```powershell
.\activate_cad_env.ps1
pip install build123d cadquery-ocp
```

### "OCP not available"

**Solution:** OCP is included with cadquery-ocp:
```powershell
.\activate_cad_env.ps1
pip install cadquery-ocp
```

**Note:** Python 3.14+ may not have pre-built wheels. Use Python 3.11 in `cad_env`.

### "Virtual environment activation fails"

**Solution:** Check PowerShell execution policy:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### "Script window closes immediately"

**Solution:** Use wrapper scripts (`run_with_cad_env.bat` or `.ps1`) - they keep the window open.

---

## Best Practices

1. **Always use wrapper scripts** for scripts requiring CAD libraries
2. **Never assume environment is activated** - always activate in wrapper
3. **Keep windows open** - Use `pause` in batch files
4. **Verify dependencies** - Check build123d/OCP before running
5. **Document in project README** - Include CAD env activation instructions

---

## Integration with V-Model Framework

This pattern is automatically included when using the V-Model Framework Copier:

1. Framework copier copies all CAD environment files
2. New projects have `cad_env` setup ready
3. Standard activation scripts included
4. Generic wrappers available for any script

---

## Version Compatibility

| Python Version | OCP Support | Recommended |
|----------------|--------------|-------------|
| Python 3.11   | ✅ Pre-built wheels | ✅ **Recommended** |
| Python 3.12   | ⚠️ May need conda | ⚠️ Possible |
| Python 3.13   | ⚠️ May need conda | ⚠️ Possible |
| Python 3.14+  | ❌ No pre-built wheels | ❌ Not recommended |

**Best Practice:** Always use Python 3.11 in `cad_env` for maximum compatibility.

---

## Future Projects

When starting a new V-Model project:

1. **Copy framework** using V-Model Framework Copier
2. **Run setup:** `python setup_cad_env.py`
3. **Verify:** `.\activate_cad_env.ps1` then `python -c "import build123d; print('OK')"`
4. **Use wrappers:** `.\run_with_cad_env.bat "your_script.py"`

---

**Status:** Standard Pattern - Use in All CAD Projects  
**Last Updated:** 2025-12-30

