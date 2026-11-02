"""
Fix closing braces in app.js after replacing handleLoginSubmit
"""
import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Let's inspect the duplicate handleLoginSubmit definitions or trailing braces
matches = list(re.finditer(r'handleLoginSubmit', js))
print(f"Occurrences of handleLoginSubmit: {len(matches)}")
for idx, m in enumerate(matches):
    print(f"Match {idx+1} at char {m.start()}")

# Find orphaned closing braces after window.handleLoginSubmit
idx = js.find('window.handleLoginSubmit')
if idx >= 0:
    end_idx = js.find('const loginFormEl', idx)
    if end_idx >= 0:
        chunk = js[idx:end_idx]
        print("Chunk between window.handleLoginSubmit and loginFormEl:")
        print(repr(chunk[-200:]))
