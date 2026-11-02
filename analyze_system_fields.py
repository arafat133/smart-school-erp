import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

forms_info = []

for root, dirs, files in os.walk(r'stu\secure_school_system\templates'):
    for f in files:
        if f.endswith('.html'):
            fp = os.path.join(root, f)
            with open(fp, 'r', encoding='utf-8') as fh:
                c = fh.read()
            
            # Find all inputs
            inputs = re.findall(r'<input\s+([^>]+)>', c)
            selects = re.findall(r'<select\s+([^>]+)>', c)
            textareas = re.findall(r'<textarea\s+([^>]+)>', c)
            
            if inputs or selects or textareas:
                forms_info.append({
                    "file": fp,
                    "inputs_count": len(inputs),
                    "selects_count": len(selects),
                    "textareas_count": len(textareas)
                })

print(f"Total template files containing input fields: {len(forms_info)}")
total_inputs = sum(x['inputs_count'] for x in forms_info)
total_selects = sum(x['selects_count'] for x in forms_info)
total_textareas = sum(x['textareas_count'] for x in forms_info)
print(f"Grand totals -> Inputs: {total_inputs}, Selects: {total_selects}, Textareas: {total_textareas}")

# Let's check partials/_modals.html specifically
modals_fp = r'stu\secure_school_system\templates\partials\_modals.html'
if os.path.exists(modals_fp):
    with open(modals_fp, 'r', encoding='utf-8') as fh:
        mc = fh.read()
    modal_forms = re.findall(r'id=["\'](modal-[^"\']+|modalForm-[^"\']+|form-[^"\']+)["\']', mc)
    print(f"\n_modals.html exists with size: {len(mc)} bytes and ~{len(modal_forms)} modal sections")
