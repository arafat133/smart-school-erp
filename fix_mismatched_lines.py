"""
Remove leftover broken handleLoginSubmit block between lines 530 and 728
"""
with open('frontend/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
print("Line 530:", lines[529].strip())
print("Line 727:", lines[726].strip())

# Slice out lines 529 to 727 (0-indexed: 528 to 727)
new_lines = lines[:528] + lines[727:]

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Sliced out broken lines successfully!")
