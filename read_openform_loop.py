import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('stu/secure_school_system/assets/js/core.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Line 9880 to 9945 in core.js:")
for i in range(9880, 9945):
    print(f"{i+1}: {lines[i]}", end="")
