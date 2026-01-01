@echo off
REM Activate Python 3.11 CAD environment
REM This script activates the virtual environment with all CAD libraries
REM Standard V-Model Framework Pattern

if not exist "cad_env\Scripts\activate.bat" (
    echo ======================================================================
    echo ERROR: CAD environment not found
    echo ======================================================================
    echo.
    echo The cad_env directory does not exist.
    echo.
    echo To create the CAD environment, run:
    echo   python setup_cad_env.py
    echo.
    echo Or manually:
    echo   python -m venv cad_env --python=python3.11
    echo   cad_env\Scripts\pip.exe install build123d cadquery-ocp
    echo.
    pause
    exit /b 1
)

echo ======================================================================
echo Activating CAD Environment (Python 3.11)
echo ======================================================================
echo.

call cad_env\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate CAD environment
    pause
    exit /b 1
)

echo CAD Environment activated!
echo.
echo Python version:
python --version
echo.

echo Checking CAD libraries...
python -c "import build123d; print('  [OK] build123d available')" 2>nul
if errorlevel 1 (
    echo   [WARNING] build123d not available
    echo   Install: cad_env\Scripts\pip.exe install build123d cadquery-ocp
)

python -c "import OCP; print('  [OK] OCP available')" 2>nul
if errorlevel 1 (
    echo   [WARNING] OCP not available
    echo   Install: cad_env\Scripts\pip.exe install cadquery-ocp
)

python -c "import cadquery as cq; print('  [OK] CadQuery:', cq.__version__)" 2>nul
if errorlevel 1 (
    echo   [WARNING] CadQuery not available
)

echo.
echo ======================================================================
echo Ready to use CAD libraries!
echo ======================================================================
echo.
echo To run scripts with CAD environment:
echo   run_with_cad_env.bat "your_script.py"
echo.
echo To deactivate when done:
echo   deactivate
echo.

