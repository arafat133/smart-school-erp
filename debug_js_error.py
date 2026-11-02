"""
Inspect app.js lines around 4042 for selectedOptions error
"""
with open('frontend/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
start = max(0, 4035 - 1)
end = min(len(lines), 4055)

for i in range(start, end):
    print(f"Line {i+1}: {lines[i]}", end='')
