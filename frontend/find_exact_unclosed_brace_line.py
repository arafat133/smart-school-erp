with open('frontend/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

stack = []

for l_num, line in enumerate(lines, 1):
    i = 0
    while i < len(line):
        char = line[i]
        # Ignore inline comments //
        if char == '/' and i + 1 < len(line) and line[i+1] == '/':
            break
        
        if char == '{':
            stack.append((l_num, line.strip()))
        elif char == '}':
            if stack:
                stack.pop()
            else:
                print(f"Extra closing brace at line {l_num}: {line.strip()}")
        i += 1

print(f"Unclosed braces count: {len(stack)}")
for l_num, l_text in stack:
    print(f"  Unclosed '{l_text[:70]}' opened at line {l_num}")
