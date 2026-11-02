import sys
sys.stdout.reconfigure(encoding='utf-8')
with open("assets/js/core.js", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

pos = text.find("function checkAuthAndInitPortal")
if pos == -1:
    pos = text.find("checkAuthAndInitPortal")

print(text[pos:pos+3000])
