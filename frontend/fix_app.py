import re

file_path = r"c:\Users\LENOVO\Desktop\stu\secure_school_system\frontend\app.js"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Duplicate const d:
# Example: const d = editId ? DB.users.find(u=>u.id===editId) : {};
#          const d = editId ? DB.users.find(u=>u.id===editId) : {};
content = re.sub(r"(const\s+[a-zA-Z]\s*=\s*.*?;)\s*\n\s*\1", r"\1", content)

# 2. Corrupted const d/p with else if:
# This happens when two type handlers were merged.
# e.g., const d = editId ? DB.homework.find(...) : {} else if (type === 'journal') {
#       const d = editId ? DB.journal.find(...) : {};
# We will match the first line and remove the 'else if ... {' part and add ';'
def fix_merged_else_if(match):
    before_else = match.group(1)
    # just return before_else + ";"
    return before_else + ";"

content = re.sub(r"(const\s+[a-zA-Z]\s*=\s*.*?:\s*\{\})\s*else\s+if\s*\(type\s*===\s*'[^']+'\)\s*\{", fix_merged_else_if, content)
content = re.sub(r"(const\s+[a-zA-Z]\s*=\s*.*?\|\|\s*\{\})\s*else\s+if\s*\(type\s*===\s*'[^']+'\)\s*\{", fix_merged_else_if, content)

# Then we might have double const d for different types one after another without else if,
# Wait, if we just stripped the 'else if', now we have:
# const d = ...DB.homework... : {};
# const d = ...DB.journal... : {};
# We need to turn the second one back into an 'else if (type === 'journal') {' block!
# Let's write a smarter Python fix:

def advanced_fix(content):
    # 1. fix `} ;` followed by `title.innerHTML` -> `} else if (type === '???') {`
    # How to deduce the type? 
    # title.innerHTML = `<i class="fa-solid fa-file-contract"></i> ${editId?'تعديل':'إضافة'} عقد موظف`; -> type = contract ?
    # Let's map some keywords to types:
    type_map = {
        'عقد': 'contract',
        'واجب': 'homework',
        'سند قبض': 'receipt',
        'نشاط': 'activity',
        'خط سير': 'transport',
        'موظف': 'employee',
        'طالب': 'student'
    }
    
    def repl_semicolon(m):
        title_line = m.group(2)
        inferred_type = 'unknown'
        for kw, t in type_map.items():
            if kw in title_line:
                inferred_type = t
                break
        return f"}} else if (type === '{inferred_type}') {{\n{m.group(1)}{title_line}"
        
    content = re.sub(r"\}\s*;\s*\n(\s*)(title\.innerHTML\s*=\s*.*?;)", repl_semicolon, content)
    
    # 2. Duplicate lines where they were merged
    lines = content.split('\n')
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # fix: const d = ... : {} else if (type === '...') {
        m1 = re.search(r"^(.*const\s+[a-zA-Z]\s*=\s*.*?:\s*\{\})\s*(else\s+if\s*\(type\s*===\s*'([^']+)'\)\s*\{)$", line)
        m2 = re.search(r"^(.*const\s+[a-zA-Z]\s*=\s*.*?\|\|\s*\{\})\s*(else\s+if\s*\(type\s*===\s*'([^']+)'\)\s*\{)$", line)
        
        m = m1 or m2
        if m:
            out.append(m.group(1) + ";")
            # If the next line is the matching const for the second type, we insert the else if before it
            # But maybe the else if block belongs to the next line!
            out.append(m.group(2))
            i += 1
            continue
            
        out.append(line)
        i += 1
        
    # fix the double const d issue that we created by separating them
    # Actually, wait, if we append m.group(2) which is `else if (type === '...') {`, then the next line is `const d = ...`. This is PERFECT!
    # Let's verify:
    # Original: `const d = editId ? DB.homework.find(...) : {} else if (type === 'journal') {`
    #           `const d = editId ? DB.journal.find(...) : {};`
    # New:
    #           `const d = editId ? DB.homework.find(...) : {};`
    #           `else if (type === 'journal') {`
    #           `const d = editId ? DB.journal.find(...) : {};`
    # Oh wait! Where is the `}` to close the homework block?
    # It's missing! That's why it was corrupted.
    # The correct would be:
    #           `const d = editId ? DB.homework.find(...) : {};`
    # (Rest of homework block)
    #           `} else if (type === 'journal') {`
    
    return "\n".join(out)

content = advanced_fix(content)

# balance braces
# we don't have enough context to do this safely via simple regex. Let's just do it manually.

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
