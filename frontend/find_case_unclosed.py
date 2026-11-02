with open('frontend/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

case_stack = []

for l_idx in range(2351, 4196):
    line = lines[l_idx]
    clean = line.split('//')[0]
    if 'if (' in clean or 'else if (' in clean or 'else {' in clean:
        opens = clean.count('{')
        closes = clean.count('}')
        if opens > closes:
            case_stack.append((l_idx+1, line.strip(), opens - closes))
    elif '}' in clean:
        closes = clean.count('}')
        opens = clean.count('{')
        diff = closes - opens
        while diff > 0 and case_stack:
            case_stack[-1] = (case_stack[-1][0], case_stack[-1][1], case_stack[-1][2] - 1)
            if case_stack[-1][2] <= 0:
                case_stack.pop()
            diff -= 1

print("Remaining case stack:")
for l_idx, l_txt, count in case_stack:
    print(f"Line {l_idx} (unclosed count {count}): {l_txt[:60]}")
