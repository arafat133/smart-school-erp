"""
Fix missing closing brace for saveForm in app.js
"""
with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

target = "toast(formEditId ? 'تم التعديل بنجاح ✅' : 'تمت الإضافة بنجاح ✅');"
replacement = "toast(formEditId ? 'تم التعديل بنجاح ✅' : 'تمت الإضافة بنجاح ✅');\n    closeModal('formModal');\n}"

if target in js:
    js = js.replace(target, replacement, 1)
    print("  ✓ Added missing closing brace for saveForm!")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js!")
