with open('frontend/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

depth = 0
for idx in range(4196, len(lines)):
    line = lines[idx]
    clean = line.split('//')[0]
    opens = clean.count('{')
    closes = clean.count('}')
    old_depth = depth
    depth += opens - closes
    if depth != old_depth:
        print(f"L{idx+1}: opens={opens}, closes={closes} -> new depth={depth}")

print(f"Final depth at end of file: {depth}")
