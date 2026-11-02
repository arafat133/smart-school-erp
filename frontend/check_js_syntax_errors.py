import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Check for orphan '} else'
lines = js.splitlines()
errors = []

for idx, line in enumerate(lines, 1):
    stripped = line.strip()
    if stripped.startswith("} else") or stripped.startswith("else if") or stripped.startswith("else"):
        # Check preceding non-empty line
        prev_idx = idx - 2
        while prev_idx >= 0 and not lines[prev_idx].strip():
            prev_idx -= 1
        if prev_idx >= 0:
            prev_line = lines[prev_idx].strip()
            if prev_line.endswith(";") or prev_line.startswith("function") or prev_line == "{":
                errors.append((idx, line, prev_line))

print(f"Found {len(errors)} potential orphan else issues:")
for line_num, l, p in errors:
    print(f"  Line {line_num}: '{l}' (after '{p}')")
