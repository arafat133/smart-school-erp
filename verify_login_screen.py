import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "http://127.0.0.1:8000/school"
req = urllib.request.Request(url, headers={'User-Agent': 'TestBot/1.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# 1. Check schools count in schoolId select
match_select = re.search(r'<select id="schoolId"[^>]*>(.*?)</select>', html, re.DOTALL)
if match_select:
    options = re.findall(r'<option[^>]*>.*?</option>', match_select.group(1))
    print(f"Schools in dropdown on /school: {len(options)} options found {'[PASS]' if len(options) == 30 else '[FAIL]'}")
    for opt in options[:3]:
        print("  - " + opt.strip())
    print("  ...")
    for opt in options[-2:]:
        print("  - " + opt.strip())
else:
    print("[FAIL] schoolId select not found in HTML!")

# 2. Check userType options
match_user_type = re.search(r'<select id="userType"[^>]*>(.*?)</select>', html, re.DOTALL)
if match_user_type:
    has_saas = 'saas_admin' in match_user_type.group(1)
    print(f"Contains saas_admin in userType: {has_saas} {'[FAIL]' if has_saas else '[PASS - CLEAN]'}")
    roles = re.findall(r'<option[^>]*>(.*?)</option>', match_user_type.group(1))
    print("Available roles in dropdown:")
    for r in roles:
        print(f"  - {r.strip()}")
else:
    print("[FAIL] userType select not found!")

# 3. Check demo badges
has_demo_badges = 'الحسابات التجريبية' in html or '👑 مدير مدرسة' in html
print(f"Contains demo test accounts badges: {has_demo_badges} {'[FAIL]' if has_demo_badges else '[PASS - COMPLETELY REMOVED]'}")
