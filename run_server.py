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

def get_local_ip():
    """Detects the primary local LAN IPv4 address (Wi-Fi or Ethernet)."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

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

    print("=" * 75)
    print("      🏫 منظومة المدارس الذكية السحابية - السيرفر فائق السرعة")
    print("         Smart School Cloud ERP - High Concurrency Server")
    print("=" * 75)
    print()

    # Step 1: Free Port 8000
    free_port(8000)

    # Step 2: System info & IP Detection
    local_ip = get_local_ip()
    cpu_count = os.cpu_count() or 4
    workers = min(4, cpu_count)
    
    print()
    print("=" * 75)
    print("  🌐 روابط الوصول للنظام عبر الشبكة:")
    print("=" * 75)
    print(f"  💻 من هذا الكمبيوتر (Localhost):")
    print(f"     👉 http://127.0.0.1:8000/school.html")
    print()
    if local_ip != "127.0.0.1":
        print(f"  📱 من الهاتف المحمول (عبر نفس شبكة الواي فاي Wi-Fi):")
        print(f"     👉 http://{local_ip}:8000/school.html")
        print(f"     👉 بوابة ولي الأمر: http://{local_ip}:8000/parent.html")
    print()
    print(f"  ⚡ سعة السيرفر: 10,000 اتصال متزامن | {cpu_count} أنوية معالجة | مضغوط بـ GZip")
    print("=" * 75)
    print("  خادم النظام يعمل الآن بنجاح. اضغط CTRL+C لإيقاف السيرفر.")
    print("=" * 75)
    print()

    # Step 3: Run Uvicorn binding to 0.0.0.0 (allows external LAN connections from phones)
    venv_python = os.path.join(base_dir, ".venv", "Scripts", "python.exe")
    python_bin = venv_python if os.path.exists(venv_python) else sys.executable

    # Listen on 0.0.0.0 so phones on the Wi-Fi can connect
    cmd_multi = [
        python_bin, "-m", "uvicorn", "app.main:app",
        "--host", "0.0.0.0",
        "--port", "8000",
        "--workers", str(workers),
        "--limit-concurrency", "10000",
        "--backlog", "4096"
    ]

    try:
        ret = subprocess.run(cmd_multi)
        if ret.returncode != 0:
            print("\n[!] جاري التشغيل بالنمط الأحادي السريع المتوافق مع ويندوز...")
            cmd_single = [
                python_bin, "-m", "uvicorn", "app.main:app",
                "--host", "0.0.0.0",
                "--port", "8000"
            ]
            subprocess.run(cmd_single)
    except KeyboardInterrupt:
        print("\n[*] تم إيقاف السيرفر بأمان.")

if __name__ == "__main__":
    main()
