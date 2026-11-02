import re
import os
import time

def process_file():
    with open('frontend/app.js', 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply task 2
    validation_code = """
// ==================== FIELD VALIDATION SYSTEM ====================

// Arabic/English letters only (no numbers, no symbols except spaces)
function validateTextOnly(input) {
    input.value = input.value.replace(/[0-9!@#$%^&*()_+=\[\]{}|\\\\;:'",.<>?/~`]/g, '');
}

// Numbers only (no letters, no symbols)
function validateNumberOnly(input) {
    input.value = input.value.replace(/[^0-9.]/g, '');
}

// Phone validation: exactly 9 digits, must start with 7
function validatePhone(input) {
    input.value = input.value.replace(/[^0-9]/g, '');
    if (input.value.length > 0 && input.value[0] !== '7') {
        input.value = '7' + input.value.substring(1);
    }
    if (input.value.length > 9) {
        input.value = input.value.substring(0, 9);
    }
    // Visual feedback
    if (input.value.length === 9 && input.value[0] === '7') {
        input.style.borderColor = '#10b981';
        input.style.boxShadow = '0 0 0 2px rgba(16,185,129,0.2)';
    } else if (input.value.length > 0) {
        input.style.borderColor = '#ef4444';
        input.style.boxShadow = '0 0 0 2px rgba(239,68,68,0.2)';
    } else {
        input.style.borderColor = '';
        input.style.boxShadow = '';
    }
}

// Integer only (no decimals, no letters)
function validateIntegerOnly(input) {
    input.value = input.value.replace(/[^0-9]/g, '');
}

// Currency/money validation (numbers with up to 2 decimal places)
function validateCurrency(input) {
    input.value = input.value.replace(/[^0-9.]/g, '');
    const parts = input.value.split('.');
    if (parts.length > 2) input.value = parts[0] + '.' + parts.slice(1).join('');
    if (parts[1] && parts[1].length > 2) input.value = parts[0] + '.' + parts[1].substring(0, 2);
}

// National ID validation (exactly 10 digits)
function validateNationalId(input) {
    input.value = input.value.replace(/[^0-9]/g, '');
    if (input.value.length > 10) input.value = input.value.substring(0, 10);
    if (input.value.length === 10) {
        input.style.borderColor = '#10b981';
    } else if (input.value.length > 0) {
        input.style.borderColor = '#ef4444';
    }
}

window.validateTextOnly = validateTextOnly;
window.validateNumberOnly = validateNumberOnly;
window.validatePhone = validatePhone;
window.validateIntegerOnly = validateIntegerOnly;
window.validateCurrency = validateCurrency;
window.validateNationalId = validateNationalId;
"""
    if "validateTextOnly" not in content:
        content += validation_code

    def robust_replace_input(match):
        label_open = match.group(1)
        label_text = match.group(2)
        label_close = match.group(3)
        between = match.group(4)
        input_attrs = match.group(5)
        
        if 'oninput' in input_attrs:
            return match.group(0)
            
        new_attrs = input_attrs
        added = False
        
        if any(x in label_text for x in ['اسم', 'عنوان', 'بيان', 'ملاحظات', 'وصف', 'مادة']):
            new_attrs += ' oninput="validateTextOnly(this)"'
            added = True
        elif any(x in label_text for x in ['هاتف', 'جوال', 'تواصل']):
            new_attrs += ' oninput="validatePhone(this)" maxlength="9" placeholder="7XXXXXXXX"'
            added = True
        elif any(x in label_text for x in ['مبلغ', 'رسوم', 'سعر', 'راتب', 'تكلفة']):
            new_attrs += ' oninput="validateCurrency(this)"'
            added = True
        elif any(x in label_text for x in ['عدد', 'كمية', 'سعة', 'رقم']) and not ('هاتف' in label_text):
            new_attrs += ' oninput="validateIntegerOnly(this)"'
            added = True

        if added:
            return f"{label_open}{label_text}{label_close}{between}<input{new_attrs}>"
        else:
            return match.group(0)
            
    content = re.sub(r'(<label[^>]*>)(.*?)(</label>)(\s*)<input([^>]+)>', robust_replace_input, content, flags=re.IGNORECASE)

    def replace_placeholder_input(match):
        attrs1 = match.group(1)
        placeholder = match.group(2)
        attrs2 = match.group(3)
        full_attrs = attrs1 + 'placeholder="' + placeholder + '"' + attrs2
        
        if 'oninput' in full_attrs:
            return match.group(0)
            
        if 'رقم وطني' in placeholder or 'هوية' in placeholder:
            return f'<input{attrs1}placeholder="{placeholder}"{attrs2} oninput="validateNationalId(this)" maxlength="10">'
            
        return match.group(0)

    content = re.sub(r'<input([^>]*)placeholder="([^"]+)"([^>]*)>', replace_placeholder_input, content, flags=re.IGNORECASE)

    def replace_placeholder_input_sq(match):
        attrs1 = match.group(1)
        placeholder = match.group(2)
        attrs2 = match.group(3)
        full_attrs = attrs1 + "placeholder='" + placeholder + "'" + attrs2
        
        if 'oninput' in full_attrs:
            return match.group(0)
            
        if 'رقم وطني' in placeholder or 'هوية' in placeholder:
            return f"<input{attrs1}placeholder='{placeholder}'{attrs2} oninput=\"validateNationalId(this)\" maxlength=\"10\">"
            
        return match.group(0)

    content = re.sub(r"<input([^>]*)placeholder='([^']+)'([^>]*)>", replace_placeholder_input_sq, content, flags=re.IGNORECASE)

    with open('frontend/app.js', 'w', encoding='utf-8') as f:
        f.write(content)

    print("app.js updated.")

    # Task 1: Append CSS
    css_code = """
/* ========== GLOBAL SCROLLBAR FOR ALL INTERFACES ========== */
* {
    scrollbar-width: thin;
    scrollbar-color: rgba(59, 130, 246, 0.5) rgba(15, 23, 42, 0.3);
}
*::-webkit-scrollbar { width: 8px; height: 8px; }
*::-webkit-scrollbar-track { background: rgba(15, 23, 42, 0.4); border-radius: 4px; }
*::-webkit-scrollbar-thumb { background: rgba(59, 130, 246, 0.5); border-radius: 4px; min-height: 30px; }
*::-webkit-scrollbar-thumb:hover { background: rgba(59, 130, 246, 0.8); }
*::-webkit-scrollbar-corner { background: transparent; }

.page { overflow-y: auto !important; max-height: calc(100vh - 65px); padding-bottom: 30px; }
.table-wrapper { overflow-x: auto !important; overflow-y: auto !important; max-height: 70vh; }
.modal-body { overflow-y: auto !important; max-height: 70vh; }
textarea { overflow-y: auto !important; }

/* ========== PRINT STYLES - SHOW ALL COLUMNS ========== */
@media print {
    body, html { background: #fff !important; color: #000 !important; }
    .sidebar, .topbar, .toolbar, .btn-back, .btn-add, .btn-edit, .btn-delete, .btn-cancel, .btn-save, .act, .page-header button, #toastBox, .modal-overlay, .tab-nav, .search-box, .stats-row { display: none !important; }
    .page-container { margin: 0 !important; padding: 0 !important; width: 100% !important; max-width: 100% !important; }
    .page { display: block !important; overflow: visible !important; max-height: none !important; padding: 10px !important; }
    .page.active { display: block !important; }
    .page:not(.active) { display: none !important; }
    .page-header { background: none !important; border: none !important; padding: 5px 0 !important; margin-bottom: 10px !important; }
    .page-header h2 { color: #000 !important; font-size: 16pt !important; text-align: center !important; }
    .page-header h2 i { display: none !important; }
    .table-wrapper { overflow: visible !important; max-height: none !important; max-width: 100% !important; }
    table { width: 100% !important; border-collapse: collapse !important; font-size: 9pt !important; page-break-inside: auto !important; }
    table th, table td { border: 1px solid #333 !important; padding: 4px 6px !important; color: #000 !important; background: #fff !important; text-align: center !important; white-space: normal !important; word-wrap: break-word !important; }
    table th { background: #e5e7eb !important; font-weight: 700 !important; }
    table thead { display: table-header-group !important; }
    table tr { page-break-inside: avoid !important; }
    .form-card, .stat-card, .stats-row { background: #fff !important; border: 1px solid #ccc !important; color: #000 !important; }
    .form-card h3, .form-card h4, .form-card label, .form-card span, .form-card p { color: #000 !important; }
    span[style*='background'], span[style*='color'] { background: none !important; color: #000 !important; border: 1px solid #999 !important; }
    @page { size: landscape; margin: 8mm; }
}
"""
    with open('frontend/style.css', 'r', encoding='utf-8') as f:
        style_content = f.read()
    if 'GLOBAL SCROLLBAR FOR ALL INTERFACES' not in style_content:
        with open('frontend/style.css', 'a', encoding='utf-8') as f:
            f.write('\n' + css_code)
        print("style.css updated.")

    # Update HTML Timestamps & Sync
    ts = str(int(time.time()))
    # Assuming frontend is the directory for html files, Wait, the original instructions say "frontend/school.html"
    for html_file in ['frontend/school.html', 'frontend/admin.html', 'frontend/parent.html']:
        if not os.path.exists(html_file): continue
        with open(html_file, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # update style.css and app.js links
        html = re.sub(r'style\.css\?v=\d+', f'style.css?v={ts}', html)
        html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
        
        # if there are no ?v=, add them
        html = re.sub(r'href="style\.css"', f'href="style.css?v={ts}"', html)
        html = re.sub(r'src="app\.js"', f'src="app.js?v={ts}"', html)

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html)
            
    print("HTML files synced and timestamps updated.")

    # Verify braces in app.js
    with open('frontend/app.js', 'r', encoding='utf-8') as f:
        app_text = f.read()
        open_braces = app_text.count('{')
        close_braces = app_text.count('}')
        print(f"Brace balance: {open_braces} open, {close_braces} close. Match: {open_braces == close_braces}")

if __name__ == '__main__':
    process_file()
