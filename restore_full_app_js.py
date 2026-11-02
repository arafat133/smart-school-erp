"""
Restore full app.js by running builder scripts sequence
"""
import os, subprocess, time

scripts_sequence = [
    'fix_all_missing_buttons.py',
    'update_requested_pages_js.py',
    'update_financial_js.py',
    'update_hr_staff_js.py',
    'update_control_exam_js.py',
    'update_warehouse_js.py',
    'update_activities_transport_js.py',
    'update_sms_reports_js.py',
    'update_admin_tools_js.py',
    'update_issue_orders_and_reported_js.py',
    'update_master_goto_all_final.py',
    'upgrade_security_and_login.py',
    'update_js_audit_and_diff.py'
]

print("Executing restoration sequence for app.js...")
for script in scripts_sequence:
    if os.path.exists(script):
        try:
            res = subprocess.run(['python', script], capture_output=True, text=True, encoding='utf-8')
            print(f"  ✓ Ran {script} (exit code {res.returncode})")
        except Exception as e:
            print(f"  ❌ Error running {script}:", e)

sz = os.path.getsize('frontend/app.js')
print(f"Restored app.js size: {sz} bytes")
