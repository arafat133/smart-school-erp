with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

lines = js.splitlines()
stack = []

for idx, line in enumerate(lines, 1):
    # Ignore comments and template strings roughly
    clean_line = line.split('//')[0]
    for char in clean_line:
        if char == '{':
            stack.append((idx, line.strip()))
        elif char == '}':
            if stack:
                stack.pop()
            else:
                print(f"Extra closing brace at line {idx}: {line.strip()}")

print(f"Unclosed braces count: {len(stack)}")
if stack:
    print("Unclosed braces locations (last 10):")
    for line_num, l in stack[-10:]:
        print(f"  Line {line_num}: {l}")
