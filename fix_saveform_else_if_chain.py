"""
Fix saveForm else-if chain in app.js
"""
import re, time

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the broken transition between receipt and change-password
old_broken = """        render('receipts'); render('enrollment');

    }

    closeModal('formModal');

    
        else if (formType === 'change-password') {"""

new_fixed = """        render('receipts'); render('enrollment');

    } else if (formType === 'change-password') {"""

if old_broken in js:
    js = js.replace(old_broken, new_fixed)
    print("  ✓ Fixed broken saveForm else-if chain!")
else:
    print("  ❌ Old broken block not found exact match. Using regex...")
    pattern = r"render\('receipts'\);\s*render\('enrollment'\);\s*\}\s*closeModal\('formModal'\);\s*else\s*if\s*\(\s*formType\s*===\s*'change-password'\s*\)"
    js = re.sub(pattern, "render('receipts'); render('enrollment');\n    } else if (formType === 'change-password')", js)
    print("  ✓ Replaced via regex!")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js!")
