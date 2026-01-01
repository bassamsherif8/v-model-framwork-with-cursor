@echo off
REM Start local web server for PROJECT_DASHBOARD.html
REM This is required because browsers block loading local JSON files directly

echo ========================================
echo Starting Dashboard Web Server
echo ========================================
echo.
echo Server will start on: http://localhost:8000
echo.
echo To view the dashboard:
echo   1. Open your web browser
echo   2. Navigate to: http://localhost:8000/PROJECT_DASHBOARD.html
echo.
echo Press Ctrl+C to stop the server
echo.
echo ========================================
echo.

REM Check if dashboard_data.json exists
if not exist "dashboard_data.json" (
    echo WARNING: dashboard_data.json not found!
    echo Generating it now...
    python generate_dashboard_data.py
    echo.
)

REM Start the web server
python -m http.server 8000

