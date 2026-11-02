import re

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

pages = re.findall(r'<div class="page" id="(pg-[^"]+)">', html_content)
print(f"Total Pages in HTML: {len(pages)}")

# 1. Check all goTo target render functions
goto_targets = set(re.findall(r"goTo\(['\"](pg-[^'\"]+)['\"]\)", html_content + js_content))
print(f"Total Navigation Targets: {len(goto_targets)}")

# 2. Check render functions in JS
render_funcs = set(re.findall(r"function (render[A-Za-z0-9_]+)\s*\(", js_content))
print(f"Total Render Functions in JS: {len(render_funcs)}")

# 3. Check openForm types in JS
open_form_types = set(re.findall(r"type === ['\"]([^'\"]+)['\"]", js_content))
print(f"openForm handled types: {open_form_types}")

# 4. Check saveForm types in JS
save_form_types = set(re.findall(r"(?:formType|type) === ['\"]([^'\"]+)['\"]", js_content))
print(f"saveForm handled types: {save_form_types}")

# 5. Check confirmDel types in JS
del_types = set(re.findall(r"delType === ['\"]([^'\"]+)['\"]", js_content))
print(f"confirmDel handled types: {del_types}")

# Find missing render functions in goTo()
missing_renders = []
goto_blocks = re.findall(r"if\s*\(\s*id\s*===\s*['\"](pg-[^'\"]+)['\"]\s*\)\s*([A-Za-z0-9_]+)\(\);", js_content)
for pg_id, func_name in goto_blocks:
    if func_name not in js_content or f"function {func_name}" not in js_content:
        missing_renders.append((pg_id, func_name))

print("\nMissing Render Functions in JS:")
for pg, func in missing_renders:
    print(f"  - {pg} -> {func}()")

# Find pages with add buttons and check openForm parameter
add_buttons = re.findall(r"openForm\(['\"]([^'\"]+)['\"]\)", html_content)
print(f"\nTotal Add Button Types in HTML: {len(set(add_buttons))}")
missing_form_handlers = set(add_buttons) - open_form_types
print(f"Missing in openForm: {missing_form_handlers}")
