import sys
sys.stdout.reconfigure(encoding='utf-8')
with open("assets/js/core.js", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

pos = text.find("window.currentSchoolCode =")
print(text[pos-100:pos+500])
