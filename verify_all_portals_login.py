import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for portal, url in [("School", "http://127.0.0.1:8000/school"), ("Admin", "http://127.0.0.1:8000/admin"), ("Parent", "http://127.0.0.1:8000/parent")]:
    req = urllib.request.Request(url, headers={'User-Agent': 'TestBot/1.0'})
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    
    has_demo = 'الحسابات التجريبية' in html or '👑 مدير مدرسة' in html
    match_select = re.search(r'<select id="schoolId"[^>]*>(.*?)</select>', html, re.DOTALL)
    sch_count = len(re.findall(r'<option[^>]*>.*?</option>', match_select.group(1))) if match_select else 0

    print(f"[{portal} Portal]:")
    print(f" - Schools in dropdown: {sch_count}/30")
    print(f" - Demo accounts box present: {has_demo} {'[FAIL]' if has_demo else '[CLEAN - REMOVED]'}")
