@echo off
REM Generic wrapper to run any script with CAD environment
REM Usage: run_with_cad_env.bat "script.py" [arguments]
REM Example: run_with_cad_env.bat "02_Design/parts/generate_step_files.py"

setlocal

if "%~1"=="" (
    echo ======================================================================
    echo ERROR: No script specified
    echo ======================================================================
    echo.
    echo Usage: run_with_cad_env.bat "script.py" [arguments]
    echo.
    echo Examples:
    echo   run_with_cad_env.bat "02_Design/parts/generate_step_files.py"
    echo   run_with_cad_env.bat "02_Design/manufacturing/run_drawings_freecad.py"
    echo.
    pause
    exit /b 1
)

echo ======================================================================
echo Running with CAD Environment
echo ======================================================================
echo.

echo Activating CAD Environment (Python 3.11)...
if not exist "cad_env\Scripts\activate.bat" (
    echo ERROR: CAD environment not found at: cad_env\Scripts\activate.bat
    echo.
    echo Please run setup_cad_env.py first to create the CAD environment.
    echo.
    pause
    exit /b 1
)

call cad_env\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate CAD environment
    pause
    exit /b 1
)

echo.
echo CAD Environment activated!
python --version
echo.

echo ======================================================================
echo Running: %~1
echo ======================================================================
echo.

REM Run the script with any additional arguments
python %*

set EXIT_CODE=%ERRORLEVEL%

echo.
echo ======================================================================
echo Execution Complete
echo ======================================================================
if %EXIT_CODE% EQU 0 (
    echo Status: SUCCESS
) else (
    echo Status: FAILED (Exit code: %EXIT_CODE%)
)
echo ======================================================================
pause

exit /b %EXIT_CODE%

