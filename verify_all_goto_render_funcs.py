import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Extract functions called in master goTo dispatcher
master_goto_match = re.search(r'// Master Central Dispatcher for Page Renders.*?\};', js, re.DOTALL)
if master_goto_match:
    dispatcher_code = master_goto_match.group(0)
    calls = re.findall(r'(\w+)\(\)', dispatcher_code)
    print("Checking functions called in Master Central Dispatcher:")
    for fn in calls:
        if fn == '_origMasterGoTo':
            continue
        # Check standard function definition: function fnName(
        defined = re.search(rf'function\s+{fn}\s*\(', js) or (f'window.{fn}' in js) or (f'const {fn}' in js) or (f'let {fn}' in js)
        status = "✅ DEFINED" if defined else "❌ MISSING!"
        print(f"  {fn}: {status}")
else:
    print("Master Central Dispatcher not found!")
