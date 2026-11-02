import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace action cells that only have btn-edit with both btn-edit and btn-delete
def fix_action_cell(match):
    full = match.group(0)
    if 'btn-delete' in full or 'btn-del' in full or 'fa-trash' in full:
        return full
    # Extract onclick if possible
    btn_match = re.search(r'onclick=["\']([^"\']+)["\']', full)
    onclick_str = "toast('تم حذف السجل 🗑️')"
    if btn_match:
        fn_call = btn_match.group(1)
        if 'editItem' in fn_call:
            onclick_str = fn_call.replace('editItem', 'delItem')
        elif 'openForm' in fn_call:
            m = re.search(r"openForm\(['\"]([^'\"]+)['\"]", fn_call)
            if m:
                item_type = m.group(1)
                onclick_str = f"delItem('{item_type}', c.id || Date.now())"
    
    del_btn = f'<button class="btn-delete" onclick="{onclick_str}"><i class="fa-solid fa-trash"></i></button>'
    
    if '<div class="act">' in full or '<div class=\'act\'>' in full:
        return full.replace('</div></td>', f'{del_btn}</div></td>')
    else:
        return full.replace('</td>', f'').replace('<button class="btn-edit"', '<div class="act"><button class="btn-edit"').replace('</button>', f'</button>{del_btn}</div></td>')

pattern = r'<td>(?:<div class=["\']act["\']>)?\s*<button class=["\']btn-edit["\'][^>]*>.*?</button>\s*(?:</div>)?\s*</td>'

count = len(re.findall(pattern, content))
print(f"Found {count} action cells with only edit button. Adding delete button...")

new_content = re.sub(pattern, fix_action_cell, content)

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated table action buttons in app.js successfully!")
