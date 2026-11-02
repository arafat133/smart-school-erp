with open('c:/Users/LENOVO/Desktop/stu/secure_school_system/frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()
s = []
ok = True
for i, char in enumerate(js):
    if char == '{': s.append(i)
    elif char == '}':
        if not s:
            print("Unmatched closing brace at pos", i)
            ok = False
        else: s.pop()
if s:
    print("Unmatched opening brace at pos", s)
    ok = False
if ok: print("Brace check OK.")
