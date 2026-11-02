import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'stu\secure_school_system\assets\js\core.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'function saveForm(' in l:
        print(f"saveForm found at line {i+1}")
        for j in range(i, min(len(lines), i + 70)):
            print(f"{j+1}: {lines[j]}", end="")
        break
