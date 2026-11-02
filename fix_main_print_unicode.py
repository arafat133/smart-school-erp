"""
Fix unicode print in app/main.py
"""
with open('app/main.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('print("🟢 Database Protection Engine Enabled: WAL Mode, Foreign Keys & Integrity Check Passed!")', 'print("[SEC] Database Protection Engine Enabled: WAL Mode, Foreign Keys & Integrity Check Passed!")')
code = code.replace('print("⚠️ DB Protection Warning:", e)', 'print("[SEC Warning] DB Protection Error:", e)')

with open('app/main.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Fixed app/main.py print unicode safely!")
