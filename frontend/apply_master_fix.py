import os
import re
from master_fix_all import MODULES

# 1. Read files
js_path = 'frontend/app.js'
html_path = 'frontend/school.html'

with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Generate DB initializations
db_inits = []
for mod_type, cfg in MODULES.items():
    key = cfg['db_key']
    if f"DB.{key}" not in js_content and f"'{key}'" not in js_content:
        # Sample items
        f1_label = cfg['fields'][0][1].split('(')[0].strip()
        f2_label = cfg['fields'][1][1].split('(')[0].strip() if len(cfg['fields']) > 1 else 'تفاصيل'
        sample_item = f"    {key}: [\n        {{id: 1, name: 'سجل تجريبي - {cfg['title']}', field2: 'بيانات أساسية'}},\n        {{id: 2, name: 'سجل نُفذ بنجاح', field2: 'عمليات معتمدة'}}\n    ],"
        db_inits.append(sample_item)

if db_inits:
    db_init_str = "\n" + "\n".join(db_inits)
    js_content = js_content.replace("const DB = {", "const DB = {" + db_init_str)

# Generate openForm handlers
open_form_cases = []
for mod_type, cfg in MODULES.items():
    key = cfg['db_key']
    title_ic = cfg['title']
    
    field_html_lines = []
    for fid, flabel, ftype, *rest in cfg['fields']:
        clean_label = flabel.split('(')[0].strip()
        if ftype == 'select':
            opts = rest[0]
            opts_html = "".join([f"<option ${{d.{fid}==='{opt}'?'selected':''}}>{opt}</option>" for opt in opts])
            field_html_lines.append(f'<div class="fg"><label>{flabel}</label><select id="{fid}">${opts_html}</select></div>')
        elif ftype == 'date':
            field_html_lines.append(f'<div class="fg"><label>{flabel}</label><input type="date" id="{fid}" value="${{d.{fid}||new Date().toLocaleDateString(\'en-CA\')}}"></div>')
        elif ftype == 'number':
            field_html_lines.append(f'<div class="fg"><label>{flabel}</label><input type="number" id="{fid}" value="${{d.{fid}||\'\'}}"></div>')
        else:
            field_html_lines.append(f'<div class="fg"><label>{flabel}</label><input id="{fid}" value="${{d.{fid}||\'\'}}"></div>')

    fields_joined = "\n        ".join(field_html_lines)
    case_code = f'''    }} else if (type === '{mod_type}') {{
        const d = editId ? (DB.{key}||[]).find(x=>x.id==editId)||{{}} : {{}};
        title.innerHTML = `<i class="fa-solid fa-pen-to-square"></i> ${{editId?'تعديل':'إضافة'}} {title_ic}`;
        h = `{fields_joined}`;'''
    open_form_cases.append(case_code)

# Insert openForm cases
open_form_block = "\n" + "\n".join(open_form_cases)
if "else if (type === 'transport') {" in js_content:
    js_content = js_content.replace("} else if (type === 'transport') {", "} else if (type === 'transport') {" + open_form_block)

# Generate saveForm handlers
save_form_cases = []
for mod_type, cfg in MODULES.items():
    key = cfg['db_key']
    title_ic = cfg['title']
    f0_id = cfg['fields'][0][0]
    
    extractors = []
    for fid, flabel, ftype, *rest in cfg['fields']:
        if ftype == 'number':
            extractors.append(f"                {fid}: parseFloat(document.getElementById('{fid}')?.value)||0")
        else:
            extractors.append(f"                {fid}: document.getElementById('{fid}')?.value||''")

    ext_str = ",\n".join(extractors)
    first_val = f"document.getElementById('{f0_id}')?.value"
    
    case_code = f'''        }} else if (type === '{mod_type}') {{
            const val0 = {first_val};
            if (!val0) return toast('⚠️ يرجى إدخال البيانات المطلوبة', 1);
            const item = {{
                id: formEditId || Date.now(),
                name: val0,
{ext_str}
            }};
            if (!DB.{key}) DB.{key} = [];
            if (formEditId) {{
                const idx = DB.{key}.findIndex(x => x.id == formEditId);
                if (idx >= 0) DB.{key}[idx] = item;
            }} else {{
                DB.{key}.push(item);
            }}
            closeModal('formModal');
            if (typeof render{mod_type.replace('-', '').capitalize()} === 'function') render{mod_type.replace('-', '').capitalize()}();
            toast('تم حفظ البيانات بنجاح ✅');
            return;'''
    save_form_cases.append(case_code)

save_form_block = "\n" + "\n".join(save_form_cases)
if "function saveForm() {" in js_content:
    js_content = js_content.replace("function saveForm() {", "function saveForm() {" + save_form_block)

# Generate confirmDel handlers
del_cases = []
for mod_type, cfg in MODULES.items():
    key = cfg['db_key']
    func_name = f"render{mod_type.replace('-', '').capitalize()}"
    del_cases.append(f"    if (delType === '{mod_type}') {{ DB.{key} = (DB.{key}||[]).filter(s=>s.id!=delId); if(typeof {func_name}==='function') {func_name}(); closeModal('deleteModal'); toast('تم الحذف 🗑️'); return; }}")

del_block = "\n" + "\n".join(del_cases)
if "function confirmDel() {" in js_content:
    js_content = js_content.replace("function confirmDel() {", "function confirmDel() {" + del_block)

# Generate render functions
render_funcs = []
for mod_type, cfg in MODULES.items():
    key = cfg['db_key']
    func_name = f"render{mod_type.replace('-', '').capitalize()}"
    tb_id = f"tbl-{mod_type}"
    srch_id = f"search{mod_type.replace('-', '').capitalize()}"
    
    tds = []
    for idx, (fid, flabel, ftype, *rest) in enumerate(cfg['fields']):
        if idx == 0:
            tds.append(f"<td style=\"font-weight:bold;color:var(--text);\">${{item.{fid} || item.name || ''}}</td>")
        elif ftype == 'select':
            tds.append(f"<td><span class=\"badge\" style=\"background:rgba(59,130,246,0.15);color:#3b82f6;padding:4px 8px;border-radius:6px;\">${{item.{fid} || ''}}</span></td>")
        else:
            tds.append(f"<td>${{item.{fid} || item.field2 || ''}}</td>")

    td_str = "\n            ".join(tds)
    
    fn_code = f'''
function {func_name}() {{
    const tb = document.getElementById('{tb_id}');
    if (!tb) return;
    tb.innerHTML = '';
    const q = (document.getElementById('{srch_id}')?.value || '').toLowerCase();
    if (!DB.{key}) DB.{key} = [];
    let list = DB.{key};
    if (q) list = list.filter(item => Object.values(item).some(v => String(v).toLowerCase().includes(q)));
    list.forEach(item => {{
        tb.innerHTML += `<tr>
            {td_str}
            <td><div class="act">
                <button class="btn-edit" onclick="editItem('{mod_type}',${{item.id}})"><i class="fa-solid fa-pen"></i></button>
                <button class="btn-delete" onclick="delItem('{mod_type}',${{item.id}},'${{item.name || item.{cfg['fields'][0][0]} || ''}}')"><i class="fa-solid fa-trash"></i></button>
            </div></td>
        </tr>`;
    }});
}}'''
    render_funcs.append(fn_code)

js_content += "\n" + "\n".join(render_funcs)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Master JS fixes applied successfully!")
