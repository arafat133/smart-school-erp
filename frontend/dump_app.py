import re

file_path = r"c:\Users\LENOVO\Desktop\stu\secure_school_system\frontend\app.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find openForm
start_idx = content.find("function openForm(type, editId = null) {")
if start_idx != -1:
    end_idx = content.find("function", start_idx + 10)
    if end_idx == -1:
        end_idx = len(content)
    print("Found openForm:")
    # print(content[start_idx:start_idx+2000])

import sys
sys.exit(0)
