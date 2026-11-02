import re
with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()
print('app.js:', len(js), 'bytes')
print('Braces diff:', js.count('{') - js.count('}'))
print('ALL FORM MODAL DEFINITIONS:', 'ALL FORM MODAL DEFINITIONS' in js)
print('saveFormData:', 'saveFormData' in js)

idx = js.find('ALL FORM MODAL')
if idx >= 0:
    chunk = js[idx:idx+50000]
    types = re.findall(r"type === '([^']+)'", chunk)
    print('Form types handled:', len(types))
