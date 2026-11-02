with open('frontend/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines, 1):
    if 'function saveForm' in line:
        print(f"saveForm starts at line {idx}")
    if 'function ' in line and idx > 2352 and idx < 4000:
        print(f"Next function after saveForm starts at line {idx}: {line.strip()}")
