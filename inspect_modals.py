with open(r'stu\secure_school_system\templates\partials\_modals.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Length of _modals.html:", len(text))
print("First 300 chars of _modals.html:\n", text[:300])
print("\nLast 300 chars of _modals.html:\n", text[-300:])
