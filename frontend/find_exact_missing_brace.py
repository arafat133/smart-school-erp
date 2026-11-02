with open('frontend/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

stack = []

for l_idx, line in enumerate(lines, 1):
    clean = line.split('//')[0]
    for char in clean:
        if char == '{':
            stack.append((l_idx, line.strip()))
        elif char == '}':
            if stack:
                stack.pop()

print("Unclosed brace stack:")
for l_idx, l_txt in stack:
    print(f"Line {l_idx}: {l_txt}")
