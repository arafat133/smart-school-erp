import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('stu/secure_school_system/templates/partials/_sidebar_school.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f'Total lines in _sidebar_school.html: {len(lines)}')
for i, line in enumerate(lines):
    if 'goTo(' in line:
        print(f'{i+1}: {line.strip()}')
