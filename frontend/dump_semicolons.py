import re
with open(r"c:\Users\LENOVO\Desktop\stu\secure_school_system\frontend\app.js", "r", encoding="utf-8") as f:
    js = f.read()

pattern = r'\}\s*;[\s\r\n]*\s*title\.innerHTML'
matches = list(re.finditer(pattern, js))
for m in matches:
    start = max(0, m.start() - 50)
    end = min(len(js), m.end() + 50)
    print(f"--- MATCH AT LINE {js[:m.start()].count('\n')+1} ---")
    print(js[start:end])
    print("--------------------------------")
