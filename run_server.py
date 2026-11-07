import os
import sys
import time
import socket
import subprocess

# Ensure UTF-8 console output on Windows
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

def free_port(port=8000):
    """Cleanly terminates any process holding the specified port on Windows."""
    print(f"[*] فحص المنفذ {port} وتحرير أي عمليات سابقة...")
    try:
        cmd = f"Get-NetTCPConnection -LocalPort {port} -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess"
        res = subprocess.run(["powershell", "-NoProfile", "-Command", cmd], capture_output=True, text=True)
        pids = set(p.strip() for p in res.stdout.splitlines() if p.strip() and p.strip() != '0')
        if pids:
            for pid in pids:
                print(f"[*] تم رصد عملية سابقة (PID {pid}) تشغل المنفذ {port} - جاري إنهاؤها...")
                subprocess.run(["taskkill", "/F", "/PID", pid], capture_output=True)
            time.sleep(1)
            print(f"[✓] تم تحرير المنفذ {port} بنجاح!")
        else:
            print(f"[✓] المنفذ {port} متاح وجاهز للتشغيل.")
    except Exception as e:
        print(f"[!] تنبيه أثناء فحص المنفذ: {e}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

    print("=" * 72)
    print("      🏫 منظومة المدارس الذكية السحابية - السيرفر فائق السرعة")
    print("         Smart School Cloud ERP - High Concurrency Server")
    print("=" * 72)
    print()

    # Step 1: Free Port 8000
    free_port(8000)

    # Step 2: System info
    cpu_count = os.cpu_count() or 4
    workers = min(4, cpu_count)
    print(f"[*] مواصفات المعالج: {cpu_count} أنوية متزامنة.")
    print(f"[*] سعة الخادم: 10,000 اتصال متزامن (GZip Compressed).")
    print(f"[*] الرابط المحلي المباشر: http://127.0.0.1:8000")
    print()
    print("=" * 72)
    print(" خادم النظام قيد العمل الآن. اضغط CTRL+C لإيقاف السيرفر.")
    print("=" * 72)
    print()

    # Step 3: Run Uvicorn
    # Use the venv python if available, else current sys.executable
    venv_python = os.path.join(base_dir, ".venv", "Scripts", "python.exe")
    python_bin = venv_python if os.path.exists(venv_python) else sys.executable

    # Run with workers, fallback to standard mode if Windows multi-worker socket error occurs
    cmd_multi = [
        python_bin, "-m", "uvicorn", "app.main:app",
        "--host", "127.0.0.1",
        "--port", "8000",
        "--workers", str(workers),
        "--limit-concurrency", "10000",
        "--backlog", "4096"
    ]

    try:
        ret = subprocess.run(cmd_multi)
        if ret.returncode != 0:
            print("\n[!] إعادة التشغيل بالنمط الأحادي السريع...")
            cmd_single = [
                python_bin, "-m", "uvicorn", "app.main:app",
                "--host", "127.0.0.1",
                "--port", "8000"
            ]
            subprocess.run(cmd_single)
    except KeyboardInterrupt:
        print("\n[*] تم إيقاف السيرفر بأمان.")

if __name__ == "__main__":
    main()
