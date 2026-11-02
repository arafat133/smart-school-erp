with open('frontend/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

depth = 0
for idx in range(2351, 4197):
    line = lines[idx]
    clean = line.split('//')[0]
    opens = clean.count('{')
    closes = clean.count('}')
    depth += opens - closes
    if depth < 1:
        print(f"Brace depth dropped to {depth} at line {idx+1}: {line.strip()}")

print(f"Final depth at line 4196: {depth}")
