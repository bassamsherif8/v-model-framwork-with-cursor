# Start local web server for PROJECT_DASHBOARD.html
# This is required because browsers block loading local JSON files directly

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting Dashboard Web Server" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Server will start on: http://localhost:8000" -ForegroundColor Green
Write-Host ""
Write-Host "To view the dashboard:" -ForegroundColor Yellow
Write-Host "  1. Open your web browser" -ForegroundColor Yellow
Write-Host "  2. Navigate to: http://localhost:8000/PROJECT_DASHBOARD.html" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if dashboard_data.json exists
if (-not (Test-Path "dashboard_data.json")) {
    Write-Host "WARNING: dashboard_data.json not found!" -ForegroundColor Red
    Write-Host "Generating it now..." -ForegroundColor Yellow
    python generate_dashboard_data.py
    Write-Host ""
}

# Start the web server
python -m http.server 8000

