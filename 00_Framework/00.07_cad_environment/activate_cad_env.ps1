# Activate Python 3.11 CAD environment
# This script activates the virtual environment with all CAD libraries
# Standard V-Model Framework Pattern

if (-not (Test-Path "cad_env\Scripts\Activate.ps1")) {
    Write-Host "======================================================================" -ForegroundColor Red
    Write-Host "ERROR: CAD environment not found" -ForegroundColor Red
    Write-Host "======================================================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "The cad_env directory does not exist." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "To create the CAD environment, run:" -ForegroundColor Cyan
    Write-Host "  python setup_cad_env.py" -ForegroundColor White
    Write-Host ""
    Write-Host "Or manually:" -ForegroundColor Cyan
    Write-Host "  python -m venv cad_env --python=python3.11" -ForegroundColor White
    Write-Host "  .\cad_env\Scripts\pip.exe install build123d cadquery-ocp" -ForegroundColor White
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "Activating CAD Environment (Python 3.11)" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""

& ".\cad_env\Scripts\Activate.ps1"

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to activate CAD environment" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "CAD Environment activated!" -ForegroundColor Green
Write-Host ""
Write-Host "Python version:" -ForegroundColor Cyan
python --version
Write-Host ""

Write-Host "Checking CAD libraries..." -ForegroundColor Yellow
python -c "import build123d; print('  [OK] build123d available')" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "  [WARNING] build123d not available" -ForegroundColor Yellow
    Write-Host "  Install: .\cad_env\Scripts\pip.exe install build123d cadquery-ocp" -ForegroundColor White
}

python -c "import OCP; print('  [OK] OCP available')" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "  [WARNING] OCP not available" -ForegroundColor Yellow
    Write-Host "  Install: .\cad_env\Scripts\pip.exe install cadquery-ocp" -ForegroundColor White
}

python -c "import cadquery as cq; print('  [OK] CadQuery:', cq.__version__)" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "  [WARNING] CadQuery not available" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "Ready to use CAD libraries!" -ForegroundColor Green
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "To run scripts with CAD environment:" -ForegroundColor Cyan
Write-Host "  .\run_with_cad_env.ps1 `"your_script.py`"" -ForegroundColor White
Write-Host ""
Write-Host "To deactivate when done:" -ForegroundColor Cyan
Write-Host "  deactivate" -ForegroundColor White
Write-Host ""

