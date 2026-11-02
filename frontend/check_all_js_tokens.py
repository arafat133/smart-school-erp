with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Check total backticks count
backticks = js.count('`')
print(f"Total backticks: {backticks} (Even? {backticks % 2 == 0})")

# Check parentheses
open_p = js.count('(')
close_p = js.count(')')
print(f"Parentheses: ( = {open_p}, ) = {close_p} (Diff: {open_p - close_p})")

# Check square brackets
open_b = js.count('[')
close_b = js.count(']')
print(f"Square brackets: [ = {open_b}, ] = {close_b} (Diff: {open_b - close_b})")

# Check curly braces
open_c = js.count('{')
close_c = js.count('}')
print(f"Curly braces: {{ = {open_c}, }} = {close_c} (Diff: {open_c - close_c})")
