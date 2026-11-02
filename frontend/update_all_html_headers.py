import re
from master_fix_all import MODULES

html_path = 'frontend/school.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

count = 0
for mod_type, cfg in MODULES.items():
    pg_id = f"pg-{mod_type}"
    headers = "".join([f"<th>{h}</th>" for h in cfg['headers']])
    new_thead = f"<thead><tr>{headers}</tr></thead>"
    
    # Match the specific page container
    pattern = rf'(<div class="page" id="{pg_id}">.*?<div class="table-wrapper"><table>)<thead><tr>.*?</tr></thead>'
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, rf'\1{new_thead}', content, flags=re.DOTALL)
        count += 1

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully updated Arabic table headers for {count} pages in school.html!")
