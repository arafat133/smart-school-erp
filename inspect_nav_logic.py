import sys
sys.stdout.reconfigure(encoding='utf-8')
with open("assets/js/core.js", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

pos = text.find("Transition UI from login screen to App Layout")
print(text[pos:pos+1500])
