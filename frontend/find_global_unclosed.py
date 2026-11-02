with open('frontend/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

depth = 0
in_template = False

for idx, line in enumerate(lines, 1):
    clean = line.split('//')[0]
    # count backticks
    b_count = clean.count('`')
    if b_count % 2 != 0:
        in_template = not in_template
    
    if not in_template:
        opens = clean.count('{')
        closes = clean.count('}')
        depth += opens - closes
        if depth < 0:
            print(f"Brace depth dropped below 0 at line {idx}: {line.strip()}")
            depth = 0

print(f"Final global brace depth at end of app.js (line {len(lines)}): {depth}")
