"""
Search all files in c:/Users/LENOVO/Desktop/stu/ for app.js or original files
"""
import os

for root, dirs, files in os.walk('c:/Users/LENOVO/Desktop/stu/'):
    for file in files:
        if file.endswith('.js') or file.endswith('.bak') or file.endswith('.py'):
            p = os.path.join(root, file)
            try:
                sz = os.path.getsize(p)
                if sz > 100000:
                    print(f"File: {p} - Size: {sz} bytes")
            except: pass
