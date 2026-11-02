with open('frontend/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

stack = []

for l_idx in range(2351, 4197):
    line = lines[l_idx]
    clean = line.split('//')[0]
    for char in clean:
        if char == '{':
            stack.append((l_idx+1, line.strip()))
        elif char == '}':
            if stack:
                stack.pop()

print("Inside saveForm, unclosed stack:")
for l_idx, l_txt in stack:
    print(f"Line {l_idx}: {l_txt}")
