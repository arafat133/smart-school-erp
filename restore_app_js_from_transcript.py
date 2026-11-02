"""
Search transcripts in C:/Users/LENOVO/.gemini/antigravity/brain/ for app.js content
"""
import glob, os, re

transcripts = glob.glob('C:/Users/LENOVO/.gemini/antigravity/brain/**/transcript*.jsonl', recursive=True)

print(f"Found {len(transcripts)} transcript files")

for t in transcripts:
    try:
        with open(t, 'r', encoding='utf-8') as f:
            content = f.read()
            if 'function goTo(' in content and len(content) > 500000:
                print(f"Found match in transcript: {t} (size {len(content)})")
                # Search for target file app.js write_to_file call
                matches = re.findall(r'"TargetFile":\s*"[^"]*app\.js"[^}]*"CodeContent":\s*"([^"]+)"', content)
                print(f"Matches count in {t}: {len(matches)}")
    except Exception as e:
        pass
