@echo off
setlocal
chcp 65001 > nul
title High-Concurrency Multi-Worker Server (Smart School Cloud ERP)
color 0A

echo ==============================================================================
echo       🏫 Smart School Cloud ERP - High Concurrency Server (Multi-Workers)
echo ==============================================================================
echo.
echo  [*] Active CPU Cores detected on machine: 8 Logical Processors
echo  [*] Starting Uvicorn with 4 Concurrent Worker Processes...
echo  [*] Concurrency Limit: 10,000 active streams | Backlog: 4,096
echo.

cd /d "%~dp0"
.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --workers 4 --limit-concurrency 10000 --backlog 4096

pause
