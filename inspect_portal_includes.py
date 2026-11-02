import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

for name in ['portals/school.html', 'portals/admin.html', 'portals/parent.html']:
    fp = 'stu/secure_school_system/templates/' + name
    print(f'=== {name} ===')
    with open(fp, 'r', encoding='utf-8') as f:
        text = f.read()
    includes = re.findall(r'{%\s*include\s*[\'"]([^\'"]+)[\'"]\s*%}', text)
    print(f'Total includes: {len(includes)}')
    for inc in includes:
        if any(k in inc for k in ['admin', 'saas', 'school_info', 'users', 'soc', 'db']):
            print(f'  {inc}')
