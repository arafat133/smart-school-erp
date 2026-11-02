import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update saveForm to trigger saveFormData if type is present
old_saveform = "function saveForm() {\n        const type = formType || (typeof currentFormType !== 'undefined' ? currentFormType : formType);"
new_saveform = "function saveForm() {\n        const type = formType || (typeof currentFormType !== 'undefined' ? currentFormType : formType);\n        if (type && typeof saveFormData === 'function') { try { saveFormData(type); } catch(e){} }"

if old_saveform in content:
    content = content.replace(old_saveform, new_saveform)
    print("Updated saveForm()")

# 2. Remove top save buttons inside fields.innerHTML in openForm handlers
pattern_button = r"\s*<button class=['\"]btn-save['\"][^>]*>.*?</button>"

matches = re.findall(pattern_button, content, flags=re.DOTALL)
print(f"Found {len(matches)} top save buttons inside form fields. Removing them...")

content = re.sub(pattern_button, "", content, flags=re.DOTALL)

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved app.js successfully!")
