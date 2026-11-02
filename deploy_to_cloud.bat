@echo off
cd /d "%~dp0"
python deploy_to_cloud.py
if %errorlevel% neq 0 (
    echo.
    echo An error occurred. Press any key to exit...
    pause > nul
)
