with open('frontend/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx in range(2351, 4196):
    line = lines[idx]
    clean = line.split('//')[0]
    opens = clean.count('{')
    closes = clean.count('}')
    if opens != closes:
        print(f"L{idx+1} [opens={opens}, closes={closes}]: {line.strip()[:80]}")
