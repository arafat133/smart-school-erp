"""
Comprehensive audit of ALL openForm() calls vs actual form definitions.
Find: which forms are missing modal definitions, which need more fields.
"""
import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Find ALL openForm calls across HTML and JS
html_calls = re.findall(r"openForm\(['\"]([^'\"]+)['\"]\)", html)
js_calls = re.findall(r"openForm\(['\"]([^'\"]+)['\"]\)", js)
all_calls = sorted(set(html_calls + js_calls))

print(f"Total unique openForm() types found: {len(all_calls)}")
print("=" * 60)

# 2. Find which ones have actual form definitions in the openForm function
# Look for case/if blocks inside openForm that handle each type
openform_start = js.find('function openForm(')
if openform_start == -1:
    openform_start = js.find('function openForm (')

if openform_start >= 0:
    # Get ~15000 chars of the openForm function
    openform_body = js[openform_start:openform_start+20000]
    
    defined_forms = []
    for call_type in all_calls:
        # Check if this type is handled in openForm
        patterns = [
            f"type === '{call_type}'",
            f'type === "{call_type}"',
            f"type == '{call_type}'",
            f'type == "{call_type}"',
            f"'{call_type}'",
        ]
        found_in_openform = any(p in openform_body for p in patterns)
        
        # Also check if there's a dedicated handler anywhere in JS
        found_anywhere = f"'{call_type}'" in js or f'"{call_type}"' in js
        
        # Check for fields innerHTML assignment
        has_fields = False
        if found_in_openform:
            # Look for innerHTML or fields content near the type reference
            idx = openform_body.find(f"'{call_type}'")
            if idx == -1:
                idx = openform_body.find(f'"{call_type}"')
            if idx >= 0:
                nearby = openform_body[idx:idx+2000]
                has_fields = 'innerHTML' in nearby or 'fields' in nearby or '<input' in nearby or '<select' in nearby
        
        status = "✅ DEFINED" if found_in_openform and has_fields else ("⚠️ PARTIAL" if found_in_openform else "❌ MISSING")
        print(f"  {status}: openForm('{call_type}')")
        
        if status != "✅ DEFINED":
            # Show where it's called from
            html_locs = [(m.start(), html[:m.start()].count('\n')+1) for m in re.finditer(f"openForm\\(['\"]" + re.escape(call_type) + "['\"]\\)", html)]
            js_locs = [(m.start(), js[:m.start()].count('\n')+1) for m in re.finditer(f"openForm\\(['\"]" + re.escape(call_type) + "['\"]\\)", js)]
            if html_locs:
                print(f"    Called in school.html at lines: {[l[1] for l in html_locs]}")
            if js_locs:
                print(f"    Called in app.js at lines: {[l[1] for l in js_locs]}")
else:
    print("ERROR: openForm function not found in app.js!")

# 3. Also check for other form-related buttons without openForm
print("\n" + "=" * 60)
print("BUTTONS WITH CUSTOM HANDLERS (not openForm):")
print("=" * 60)
# Find buttons that call functions other than openForm, goTo, render*, toggle*, switch*
btn_handlers = re.findall(r'onclick="([^"]+)"', html)
custom_handlers = set()
for h in btn_handlers:
    if not any(h.startswith(p) for p in ['openForm', 'goTo', 'render', 'toggle', 'switch', 'window.print', 'toast', 'exportCustom', 'generateCustom', 'exportBackup']):
        func_name = h.split('(')[0].strip()
        custom_handlers.add(func_name)

for h in sorted(custom_handlers):
    defined = f"function {h}" in js
    print(f"  {'✅' if defined else '❌'} {h}() -> {'defined' if defined else 'NOT DEFINED'}")

# 4. Check saveForm definitions
print("\n" + "=" * 60)
print("SAVE FORM HANDLER CHECK:")
print("=" * 60)
saveform_start = js.find('function saveForm(')
if saveform_start >= 0:
    saveform_body = js[saveform_start:saveform_start+15000]
    for call_type in all_calls:
        handled = f"'{call_type}'" in saveform_body or f'"{call_type}"' in saveform_body
        print(f"  {'✅' if handled else '❌'} saveForm('{call_type}')")
