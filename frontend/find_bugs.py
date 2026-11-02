import re
import sys

file_path = r"c:\Users\LENOVO\Desktop\stu\secure_school_system\frontend\app.js"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "} ;" in line:
        print(f"Line {i+1}: {line.strip()}")
    elif "else if (type" in line and "const " in line:
        print(f"Line {i+1}: {line.strip()}")
