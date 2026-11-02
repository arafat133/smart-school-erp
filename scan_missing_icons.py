"""Show detailed tab info with actual text content"""
import re

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

lines = html.split('\n')
count = 0
print("TABS WITHOUT ICONS - DETAILED")
print("=" * 70)

for i, line in enumerate(lines, 1):
    # Find tab class patterns
    matches = re.finditer(r'class="tab[^"]*"[^>]*>(.*?)</', line)
    for m in matches:
        content = m.group(1)
        if '<i ' not in content and 'fa-' not in content:
            text = re.sub(r'<[^>]+>', '', content).strip()
            if text and len(text) > 1:
                count += 1
                # Get the surrounding to find data-target
                start = max(0, m.start() - 150)
                ctx = line[start:m.end() + 50]
                target = re.search(r'data-target="([^"]+)"', ctx)
                onclick = re.search(r'onclick="([^"]{1,80})"', ctx)
                target_str = target.group(1) if target else ''
                onclick_str = onclick.group(1)[:60] if onclick else ''
                print(f"Line {i}: [{text}]")
                if target_str:
                    print(f"  target: {target_str}")
                if onclick_str:
                    print(f"  onclick: {onclick_str}")

print(f"\nTotal tabs without icons: {count}")
