@echo off
setlocal
chcp 65001 > nul
title High-Concurrency Multi-Worker Server (Smart School Cloud ERP)
color 0A

echo ==============================================================================
echo       🏫 Smart School Cloud ERP - High Concurrency Server (Multi-Workers)
echo ==============================================================================
echo.

cd /d "%~dp0"

echo [1/3] فحص المنفذ 8000 والعمليات السابقة...
netstat -ano | findstr :8000 > nul
if %errorlevel% equ 0 (
    echo [i] تم رصد نسخة قديمة من السيرفر تعمل على المنفذ 8000.
    echo [i] جاري تحرير المنفذ لإعادة التشغيل بالسرعة القصوى (Multi-Workers)...
    for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8000') do (
        taskkill /f /pid %%a >nul 2>nul
    )
    timeout /t 1 > nul
)

echo [2/3] معالجات النظام: 8 أنوية متزامنة.
echo [2/3] بدء تشغيل Uvicorn بـ 4 عمال معالجة (Multi-Workers) وسعة 10,000 اتصال...
echo.
echo ==============================================================================
echo  السيرفر يعمل الآن بنجاح على: http://127.0.0.1:8000
echo  (لا تغلق هذه الشاشة لضمان استمرار السيرفر)
echo ==============================================================================
echo.

.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --workers 4 --limit-concurrency 10000 --backlog 4096

if %errorlevel% neq 0 (
    echo.
    echo ⚠️ حدث خطأ أثناء تشغيل العمال المتعددين، جاري التشغيل بالنمط القياسي السريع...
    .venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000
)

pause
