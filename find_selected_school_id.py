import sys
sys.stdout.reconfigure(encoding='utf-8')
with open("assets/js/core.js", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r"selectedSchoolId", text)]
print(f"Total occurrences of selectedSchoolId in core.js: {len(matches)}")
for pos in matches:
    print("--- MATCH ---")
    print(text[pos-40:pos+160])
