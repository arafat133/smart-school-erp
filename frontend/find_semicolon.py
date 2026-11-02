import re

file_path = r"c:\Users\LENOVO\Desktop\stu\secure_school_system\frontend\app.js"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find "} ;"
matches = re.finditer(r"\}\s*;\s*[\r\n]+\s*title\.innerHTML", content)
for m in matches:
    start = max(0, m.start() - 50)
    end = min(len(content), m.end() + 100)
    print("MATCH:\n", content[start:end])

