import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

types_to_check = [
    'chart-accounts', 'cashbox', 'cost-centers', 
    'account-ceiling', 'vreceipt', 'vpayment', 'vtransfer', 
    'journal'
]

print("Checking form modal definitions in app.js:")
for t in types_to_check:
    pat1 = f"type === '{t}'"
    pat2 = f'type === "{t}"'
    is_def = pat1 in js or pat2 in js
    print(f"  {t}: {'DEFINED' if is_def else 'MISSING'}")

print(f"\nBraces balance: open={js.count('{')} close={js.count('}')} diff={js.count('{') - js.count('}')}")
