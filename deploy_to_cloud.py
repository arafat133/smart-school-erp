import os
import sys
import json
import urllib.request
import urllib.error
import subprocess
import webbrowser
import threading
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent

def run_git(cmd):
    result = subprocess.run(cmd, cwd=str(BASE_DIR), capture_output=True, text=True, encoding="utf-8", errors="replace")
    return result.returncode == 0, result.stdout, result.stderr

def deploy_with_token(token, log_callback=print, finished_callback=None):
    token = token.strip()
    if not token:
        log_callback("❌ يرجى إدخال رمز الوصول (Personal Access Token) الخاص بك على GitHub!")
        if finished_callback: finished_callback(False)
        return

    try:
        log_callback("🔍 [1/5] جاري التحقق من صحة التوكن والاتصال بـ GitHub...")
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "SmartSchoolERP-Deployer"
        }

        # 1. Get authenticated user
        user_req = urllib.request.Request("https://api.github.com/user", headers=headers)
        with urllib.request.urlopen(user_req, timeout=15) as resp:
            user_data = json.loads(resp.read().decode())
        
        username = user_data.get("login")
        log_callback(f"✅ تم الاتصال بنجاح بالحساب: @{username}")

        # 2. Create Repository on GitHub
        repo_name = "smart-school-erp"
        log_callback(f"📦 [2/5] جاري إنشاء المستودع السحابي ({repo_name}) على GitHub...")
        
        create_payload = json.dumps({
            "name": repo_name,
            "description": "Smart School Cloud ERP System - Production Release",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        }).encode("utf-8")

        create_req = urllib.request.Request(
            "https://api.github.com/user/repos", 
            data=create_payload, 
            headers=headers
        )

        repo_url = f"https://github.com/{username}/{repo_name}"
        try:
            with urllib.request.urlopen(create_req, timeout=15) as resp:
                created_repo = json.loads(resp.read().decode())
                repo_url = created_repo.get("html_url", repo_url)
                log_callback(f"🎉 تم إنشاء المستودع السحابي: {repo_url}")
        except urllib.error.HTTPError as e:
            if e.code == 422:
                log_callback(f"ℹ️ المستودع ({repo_name}) موجود مسبقاً في حسابك، سيتم تحديث الكود عليه.")
            else:
                log_callback(f"⚠️ تنبيه أثناء إنشاء المستودع: {e}")

        # 3. Configure Git Remote & Push
        log_callback("🚀 [3/5] جاري رفع ملفات النظام بالكامل (Git Push)...")
        authenticated_remote = f"https://{username}:{token}@github.com/{username}/{repo_name}.git"
        clean_remote = f"https://github.com/{username}/{repo_name}.git"

        run_git(["git", "remote", "remove", "origin"])
        ok, out, err = run_git(["git", "remote", "add", "origin", authenticated_remote])
        run_git(["git", "branch", "-M", "main"])
        
        push_ok, push_out, push_err = run_git(["git", "push", "-u", "origin", "main", "--force"])
        
        # Reset to clean remote URL so credentials are not kept in git config
        run_git(["git", "remote", "set-url", "origin", clean_remote])

        if not push_ok:
            log_callback(f"❌ خطأ أثناء الرفع: {push_err or push_out}")
            if finished_callback: finished_callback(False)
            return

        log_callback("🌟 تم رفع النظام بنجاح إلى GitHub!")
        log_callback(f"🔗 رابط المستودع: {clean_remote}")

        # 4. Open Vercel & Render
        log_callback("🌐 [4/5] جاري فتح منصة Vercel للاستضافة السحابية للواجهة...")
        vercel_url = f"https://vercel.com/new/import?s={clean_remote}"
        webbrowser.open(vercel_url)

        log_callback("🌐 [5/5] جاري فتح منصة Render لاستضافة الباك إند...")
        render_url = f"https://dashboard.render.com/blueprints/new"
        webbrowser.open(render_url)

        log_callback("\n" + "="*50)
        log_callback("🏆 مبروك! اكتملت عملية النشر والرفع بنجاح تام!")
        log_callback(f"1. مستودع GitHub: {clean_remote}")
        log_callback(f"2. صفحة Vercel المفتوحة في متصفحك: اضغط Deploy مباشرة")
        log_callback(f"3. صفحة Render المفتوحة في متصفحك: اختر المستودع واضغط Apply")
        log_callback("="*50)

        if finished_callback: finished_callback(True)

    except Exception as ex:
        log_callback(f"❌ حدث خطأ غير متوقع: {ex}")
        if finished_callback: finished_callback(False)

def launch_gui():
    import tkinter as tk
    from tkinter import ttk, messagebox

    root = tk.Tk()
    root.title("🏫 أداة الاستضافة السحابية لنظام المدارس الذكية | Cloud ERP Deployer")
    root.geometry("720x560")
    root.resizable(False, False)
    root.configure(bg="#0F172A")

    # Header
    header_frame = tk.Frame(root, bg="#1E293B", pady=15)
    header_frame.pack(fill="x")

    lbl_title = tk.Label(
        header_frame, 
        text="🏫 نظام المدارس السحابي الآمن — أداة النشر والاستضافة التلقائية", 
        font=("Segoe UI", 13, "bold"), 
        fg="#38BDF8", 
        bg="#1E293B"
    )
    lbl_title.pack()

    lbl_sub = tk.Label(
        header_frame, 
        text="الربط الآلي بين GitHub و Vercel و Render بضغطة زر واحدة", 
        font=("Segoe UI", 9), 
        fg="#94A3B8", 
        bg="#1E293B"
    )
    lbl_sub.pack(pady=4)

    # Main Container
    container = tk.Frame(root, bg="#0F172A", padx=25, pady=15)
    container.pack(fill="both", expand=True)

    # Step 1: Token Button
    step1_frame = tk.Frame(container, bg="#0F172A")
    step1_frame.pack(fill="x", pady=6)

    def open_token_url():
        webbrowser.open("https://github.com/settings/tokens/new?scopes=repo,read:org&description=SmartSchoolERP-Deployer")

    btn_token = tk.Button(
        step1_frame, 
        text="1️⃣ اضغط هنا لفتح صفحة إنشاء التوكن في GitHub (تجهيز تلقائي)", 
        command=open_token_url,
        font=("Segoe UI", 10, "bold"),
        bg="#2563EB", 
        fg="white", 
        activebackground="#1D4ED8",
        activeforeground="white",
        cursor="hand2",
        relief="flat",
        pady=8
    )
    btn_token.pack(fill="x")

    # Step 2: Input Box
    lbl_prompt = tk.Label(
        container, 
        text="2️⃣ الصق الرمز (Personal Access Token) الذي نسخته من GitHub هنا:", 
        font=("Segoe UI", 10), 
        fg="#E2E8F0", 
        bg="#0F172A", 
        anchor="e"
    )
    lbl_prompt.pack(fill="x", pady=(12, 4))

    entry_token = tk.Entry(
        container, 
        font=("Consolas", 11), 
        bg="#1E293B", 
        fg="#38BDF8", 
        insertbackground="white",
        relief="flat",
        bd=6
    )
    entry_token.pack(fill="x", ipady=4)

    # Step 3: Deploy Button
    btn_deploy = tk.Button(
        container, 
        text="🚀 3️⃣ ابدأ الرفع والاستضافة السحابية الشاملة الآن", 
        font=("Segoe UI", 11, "bold"),
        bg="#10B981", 
        fg="white", 
        activebackground="#059669",
        activeforeground="white",
        cursor="hand2",
        relief="flat",
        pady=10
    )
    btn_deploy.pack(fill="x", pady=14)

    # Log Display
    lbl_log = tk.Label(container, text="سجل العمليات المباشر:", font=("Segoe UI", 9), fg="#94A3B8", bg="#0F172A", anchor="e")
    lbl_log.pack(fill="x")

    txt_log = tk.Text(
        container, 
        height=10, 
        font=("Segoe UI", 9), 
        bg="#1E293B", 
        fg="#F1F5F9", 
        relief="flat", 
        padx=10, 
        pady=8
    )
    txt_log.pack(fill="both", expand=True)

    def log_to_gui(msg):
        def _do():
            txt_log.insert(tk.END, msg + "\n")
            txt_log.see(tk.END)
        root.after(0, _do)

    def on_deploy():
        token = entry_token.get().strip()
        if not token:
            messagebox.showwarning("تنبيه", "يرجى لصق رمز التوكن (GitHub Token) أولاً!")
            return
        btn_deploy.config(state="disabled", text="⏳ جاري النشر والرفع...")
        
        def _worker():
            def _done(success):
                def _reset():
                    btn_deploy.config(state="normal", text="🚀 3️⃣ ابدأ الرفع والاستضافة السحابية الشاملة الآن")
                    if success:
                        messagebox.showinfo("نجاح تام", "🎉 تم رفع النظام إلى GitHub وفتح صفحات Vercel و Render بنجاح!")
                root.after(0, _reset)

            deploy_with_token(token, log_callback=log_to_gui, finished_callback=_done)

        threading.Thread(target=_worker, daemon=True).start()

    btn_deploy.config(command=on_deploy)
    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        token = sys.argv[1]
        deploy_with_token(token)
    else:
        try:
            launch_gui()
        except Exception:
            token = input("أدخل رمز GitHub Token الخاص بك: ").strip()
            deploy_with_token(token)
