"""
Comprehensive audit of all buttons in the system:
1. Find all openForm('type') calls and check which are handled
2. Find all delete/edit button handlers
3. Find all search/filter handlers
4. Report missing handlers
"""
import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("=" * 80)
print("AUDIT 1: All openForm('type') calls in HTML and JS")
print("=" * 80)

# Find all openForm calls in HTML
html_form_calls = set(re.findall(r"openForm\('([^']+)'", html))
# Find all openForm calls in JS
js_form_calls = set(re.findall(r"openForm\('([^']+)'", js))

all_form_types = sorted(html_form_calls | js_form_calls)
print(f"\nTotal unique openForm types found: {len(all_form_types)}")

# Check which form types are actually handled in openForm
# Look for patterns like: formType === 'xxx' or type === 'xxx' or === 'xxx'
handled_types = set()
for ft in all_form_types:
    # Check if there's a handler for this form type
    patterns = [
        f"=== '{ft}'",
        f"== '{ft}'",
        f'=== "{ft}"',
        f'== "{ft}"',
    ]
    found = any(p in js for p in patterns)
    status = "✅ HANDLED" if found else "❌ NOT HANDLED"
    if not found:
        handled_types.add(ft)
    print(f"  openForm('{ft}'): {status}")

print(f"\n{'=' * 80}")
print("AUDIT 2: All onclick handlers in HTML buttons")
print("=" * 80)

# Find all onclick handlers in HTML
onclick_calls = re.findall(r'onclick="([^"]+)"', html)
# Check for function calls that might not exist
func_calls_in_html = set()
for oc in onclick_calls:
    funcs = re.findall(r'(\w+)\s*\(', oc)
    for fn in funcs:
        if fn not in ('toast', 'goTo', 'openForm', 'window', 'document', 'parseInt', 'String', 'JSON', 'Object', 'Array', 'Date', 'Math', 'console', 'alert', 'confirm', 'prompt', 'setTimeout', 'setInterval', 'clearTimeout', 'clearInterval', 'if', 'const', 'let', 'var', 'return', 'this', 'classList', 'getElementById', 'querySelector', 'remove', 'add', 'toggle', 'print'):
            func_calls_in_html.add(fn)

print(f"\nTotal unique function calls in HTML onclick: {len(func_calls_in_html)}")
for fn in sorted(func_calls_in_html):
    # Check if function is defined in JS
    patterns = [
        f"function {fn}",
        f"window.{fn} =",
        f"window.{fn}=",
        f"const {fn} =",
        f"let {fn} =",
        f"var {fn} =",
    ]
    found = any(p in js for p in patterns)
    status = "✅ DEFINED" if found else "❌ MISSING"
    print(f"  {fn}(): {status}")

print(f"\n{'=' * 80}")
print("AUDIT 3: Delete button patterns")
print("=" * 80)

# Find delete patterns
delete_patterns_html = re.findall(r'onclick="([^"]*(?:delet|remov|حذف)[^"]*)"', html, re.IGNORECASE)
print(f"\nDelete onclick handlers in HTML: {len(delete_patterns_html)}")
for dp in delete_patterns_html[:20]:
    print(f"  {dp[:100]}")

# Find delete functions in JS
delete_funcs = re.findall(r'function\s+(delete\w+|remove\w+)', js, re.IGNORECASE)
print(f"\nDelete functions defined in JS: {len(delete_funcs)}")
for df in delete_funcs:
    print(f"  {df}()")

print(f"\n{'=' * 80}")
print("AUDIT 4: Search/filter patterns")
print("=" * 80)

# Find search inputs and their handlers
search_inputs = re.findall(r'oninput="([^"]+)"', html)
search_onchange = re.findall(r'onchange="([^"]+)"', html)
print(f"\nSearch oninput handlers: {len(search_inputs)}")
for si in search_inputs[:10]:
    print(f"  {si[:100]}")
print(f"\nFilter onchange handlers: {len(search_onchange)}")
for sc in search_onchange[:10]:
    print(f"  {sc[:100]}")

print(f"\n{'=' * 80}")
print("AUDIT 5: Table body IDs in HTML vs render functions in JS")
print("=" * 80)

# Find all tbody IDs
tbody_ids = re.findall(r'id="(tbl-[^"]+)"', html)
print(f"\nTotal tbody IDs in HTML: {len(tbody_ids)}")
for tid in sorted(tbody_ids):
    # Check if this tbody ID is referenced in JS
    found = tid in js
    status = "✅ USED IN JS" if found else "❌ NOT USED IN JS"
    print(f"  #{tid}: {status}")

print(f"\n{'=' * 80}")
print("AUDIT 6: openForm wrapper chain analysis")
print("=" * 80)

# Count how many times openForm is redefined/wrapped
openform_wraps = js.count('window.openForm =')
print(f"\nwindow.openForm reassignment count: {openform_wraps}")

# Find each reassignment location
for m in re.finditer(r'window\.openForm\s*=\s*function', js):
    line_num = js[:m.start()].count('\n') + 1
    context = js[max(0,m.start()-50):m.start()+100].replace('\n', ' ')
    print(f"  Line {line_num}: ...{context[:120]}...")
