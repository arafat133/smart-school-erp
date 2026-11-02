import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'stu\secure_school_system\assets\js\core.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(9850, 9950):
    print(f"{i+1}: {lines[i]}", end="")
