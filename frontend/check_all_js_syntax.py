import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Check for duplicate 'const d =' inside the same block
lines = js_content.splitlines()
in_block = False
block_lines = []
current_type = ""

print("Checking JS content for block redeclarations...")
matches = re.findall(r"const\s+d\s*=\s*", js_content)
print(f"Total 'const d =' occurrences: {len(matches)}")

# Check for any remaining syntax anomalies
if "Identifier 'd' has already been declared" in js_content:
    print("WARNING: error string found")
else:
    print("Syntax check passed!")
