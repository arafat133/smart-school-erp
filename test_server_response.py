"""
Test server HTTP response for school.html and app.js
"""
import urllib.request

urls = [
    'http://localhost:8000/school.html',
    'http://localhost:8000/app.js',
    'http://localhost:8000/style.css',
    'http://localhost:8000/api/health'
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            content = resp.read()
            print(f"✅ {url}: HTTP {resp.status} - Length: {len(content)} bytes")
    except Exception as e:
        print(f"❌ {url}: Error -> {e}")
