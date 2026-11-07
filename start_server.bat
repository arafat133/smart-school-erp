@echo off
setlocal
chcp 65001 > nul
title Smart School Cloud ERP - High Concurrency Server
color 0A
cd /d "%~dp0"

if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" run_server.py
) else (
    python run_server.py
)

if %errorlevel% neq 0 (
    echo.
    echo Server stopped. Press any key to exit...
    pause > nul
)
