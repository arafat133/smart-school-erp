"""
Analyze app.js for openForm and saveForm block structures and syntax anomalies
"""
import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

lines = js.split('\n')

# Check lines 2680 to 2735
print("=== Lines 2690 to 2735 ===")
for i in range(2689, min(2735, len(lines))):
    print(f"L{i+1}: {lines[i]}")

