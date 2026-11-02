with open('frontend/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

stack = [] # (line_num, line_text)
in_template = False

for idx, line in enumerate(lines, 1):
    clean = line.split('//')[0]
    
    # We trace { and } when not in raw string literal (or accounting for ${...} inside template strings)
    # Simple token scanner for JS
    i = 0
    while i < len(clean):
        char = clean[i]
        if char == '`':
            in_template = not in_template
        elif char == '{':
            stack.append((idx, line.strip()))
        elif char == '}':
            if stack:
                stack.pop()
            else:
                print(f"Extra closing brace at line {idx}: {line.strip()}")
        i += 1

print(f"Total unclosed braces at EOF: {len(stack)}")
print("Unclosed braces stack:")
for lnum, ltxt in stack:
    print(f"  Line {lnum}: {ltxt}")
