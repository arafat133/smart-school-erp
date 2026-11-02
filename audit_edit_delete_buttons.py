"""
Audit and verify edit and delete buttons in all table rendering functions in app.js
"""
import re, time

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Find all function renderXxx() blocks
render_func_names = re.findall(r'function\s+(render[A-Za-z0-9_]+)\s*\(', js)
render_func_names = list(set(render_func_names))

print(f"Total render functions found: {len(render_func_names)}")

missing_edit_delete = []

for fn in sorted(render_func_names):
    # Extract function body
    match = re.search(rf'function\s+{fn}\s*\([^)]*\)\s*\{{(.*?)\n\}}', js, re.DOTALL)
    if match:
        body = match.group(1)
        # Check if it renders a table row with innerHTML or appendChild
        if 'innerHTML' in body and ('<tr' in body or '`' in body):
            has_edit = 'btn-edit' in body or 'fa-pen' in body or 'fa-edit' in body or 'openForm' in body or 'editItem' in body
            has_delete = 'btn-delete' in body or 'fa-trash' in body or 'delItem' in body or 'deleteRecord' in body
            
            status = []
            if not has_edit: status.append("MISSING EDIT")
            if not has_delete: status.append("MISSING DELETE")
            
            if status:
                print(f"  {fn}(): " + ", ".join(status))
                missing_edit_delete.append((fn, has_edit, has_delete))
            else:
                print(f"  {fn}(): ✅ Edit & Delete present")

print(f"\nTotal render functions needing Edit/Delete buttons: {len(missing_edit_delete)}")
