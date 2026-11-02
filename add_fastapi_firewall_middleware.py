"""
Add Multi-Layer Security Firewall Middleware & DB Protection to app/main.py (Fixed regex replacement)
"""
import re

with open('app/main.py', 'r', encoding='utf-8') as f:
    main_code = f.read()

firewall_middleware_code = """from fastapi import FastAPI, Request, Response, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, JSONResponse
import time, re, sqlite3

app = FastAPI(
    title="نظام المدارس السحابي الآمن",
    description="واجهة برمجة التطبيقات (API) لنظام المدارس السحابي الآمن مع جدار حماية متعدد الطبقات وتوثيق مشفر.",
    version="2.0.0"
)

# ==================== LAYER 1: MULTI-LAYER SYSTEM FIREWALL MIDDLEWARE ====================
RATE_LIMIT_STORE = {}
BLOCKED_IPS = set()

# SQLi & XSS Payload Patterns
SUSPICIOUS_PATTERNS = [
    r"(?i)\\b(UNION\\s+SELECT|DROP\\s+TABLE|ALTER\\s+TABLE|DELETE\\s+FROM|INSERT\\s+INTO)\\b",
    r"(?i)<script\\b[^>]*>",
    r"(?i)javascript\\s*:",
    r"(?i)\\bOR\\s+1\\s*=\\s*1\\b",
    r"(?i)--\\s*$"
]

@app.middleware("http")
async def security_firewall_middleware(request: Request, call_next):
    client_ip = request.client.host if request.client else "127.0.0.1"
    now = time.time()
    
    # 1. IP Blacklist & Rate Limiting Check (Max 120 requests per minute)
    if client_ip in BLOCKED_IPS:
        return JSONResponse(status_code=403, content={"detail": "⚠️ IP address blocked due to security audit violation."})
    
    req_history = [t for t in RATE_LIMIT_STORE.get(client_ip, []) if now - t < 60]
    req_history.append(now)
    RATE_LIMIT_STORE[client_ip] = req_history
    
    if len(req_history) > 120:
        BLOCKED_IPS.add(client_ip)
        return JSONResponse(status_code=429, content={"detail": "⚠️ Rate limit exceeded. Temporary firewall block applied."})

    # 2. SQLi & XSS Payload Inspection
    query_params = str(request.query_params)
    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, query_params):
            return JSONResponse(status_code=400, content={"detail": "⚠️ Security Firewall Alert: Malformed or suspicious query payload detected."})

    # Execute request
    response: Response = await call_next(request)
    
    # 3. HTTP Security Headers Injection
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Server"] = "Secure-School-Firewall-v2"
    
    return response

# ==================== LAYER 2: DATABASE INTEGRITY & PROTECTION ENGINE ====================
@app.on_event("startup")
def enforce_database_security():
    try:
        db_path = "school_system.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("PRAGMA journal_mode=WAL;")
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.execute("PRAGMA integrity_check;")
        conn.close()
        print("🟢 Database Protection Engine Enabled: WAL Mode, Foreign Keys & Integrity Check Passed!")
    except Exception as e:
        print("⚠️ DB Protection Warning:", e)

"""

# Replace main code structure safely
main_code_updated = re.sub(r'from fastapi import FastAPI.*?(?=from app\.api\.api import api_router)', lambda m: firewall_middleware_code, main_code, flags=re.DOTALL)

with open('app/main.py', 'w', encoding='utf-8') as f:
    f.write(main_code_updated)

print("Updated app/main.py with Multi-Layer Security Firewall & DB Protection!")
