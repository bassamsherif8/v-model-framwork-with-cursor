# Activate CAD virtual environment
# Run this script to activate the Python 3.11 environment for CAD work

Write-Host "Activating CAD virtual environment (Python 3.11)..." -ForegroundColor Green
& ".\cad_env\Scripts\Activate.ps1"

Write-Host ""
Write-Host "Python version:" -ForegroundColor Cyan
python --version

Write-Host ""
Write-Host "To install packages:" -ForegroundColor Yellow
Write-Host "  pip install build123d OCP" -ForegroundColor White

Write-Host ""
Write-Host "To deactivate when done:" -ForegroundColor Yellow
Write-Host "  deactivate" -ForegroundColor White

