with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

print(f"app.js size: {len(js)} bytes")
print(f"Open braces: {js.count('{')}")
print(f"Close braces: {js.count('}')}")
print(f"Difference: {js.count('{') - js.count('}')}")
