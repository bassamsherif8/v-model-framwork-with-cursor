# Generic wrapper to run any script with CAD environment
# Usage: .\run_with_cad_env.ps1 "script.py" [arguments]
# Example: .\run_with_cad_env.ps1 "02_Design/parts/generate_step_files.py"

param(
    [Parameter(Mandatory=$true)]
    [string]$Script,
    
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$Arguments
)

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "Running with CAD Environment" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""

if (-not (Test-Path "cad_env\Scripts\Activate.ps1")) {
    Write-Host "ERROR: CAD environment not found at: cad_env\Scripts\Activate.ps1" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please run setup_cad_env.py first to create the CAD environment." -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "Activating CAD Environment (Python 3.11)..." -ForegroundColor Green
& ".\cad_env\Scripts\Activate.ps1"

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to activate CAD environment" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "CAD Environment activated!" -ForegroundColor Green
python --version
Write-Host ""

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "Running: $Script" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""

# Run the script with any additional arguments
if ($Arguments.Count -gt 0) {
    & python $Script $Arguments
} else {
    & python $Script
}

$EXIT_CODE = $LASTEXITCODE

Write-Host ""
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "Execution Complete" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan

if ($EXIT_CODE -eq 0) {
    Write-Host "Status: SUCCESS" -ForegroundColor Green
} else {
    Write-Host "Status: FAILED (Exit code: $EXIT_CODE)" -ForegroundColor Red
}

Write-Host "======================================================================" -ForegroundColor Cyan
Read-Host "Press Enter to exit"

exit $EXIT_CODE

