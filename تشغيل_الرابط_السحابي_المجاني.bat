@echo off
setlocal
chcp 65001 > nul
title Cloudflare Live Tunnel (Smart School Cloud ERP)
color 0B

echo =======================================================================
echo          Smart School Cloud ERP - Cloudflare Live Tunnel
echo =======================================================================
echo.
echo  Starting Instant Cloud Tunnel (HTTPS)...
echo.

scratch\cloudflared.exe tunnel --url http://127.0.0.1:8000

pause
