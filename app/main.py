from app.services.security_alert_service import security_alert_service
from fastapi import FastAPI, Request, Response, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, JSONResponse, FileResponse
import time, re, os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(
    title="نظام المدارس السحابي الآمن",
    description="واجهة برمجة التطبيقات (API) لنظام المدارس السحابي الآمن مع جدار حماية متعدد الطبقات وتوثيق مشفر.",
    version="2.0.0"
)

# ==================== TEMPLATE ENGINE ====================
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# ==================== LAYER 1: MULTI-LAYER SYSTEM FIREWALL MIDDLEWARE ====================
RATE_LIMIT_STORE = {}
LOGIN_RATE_LIMIT = {}
BLOCKED_IPS = set()

# Honeypot Decoy Traps for automated scanners and malicious reconnaissance
HONEYPOT_PATHS = {
    "/admin_db_backup.sql",
    "/phpmyadmin",
    "/phpmyadmin/",
    "/.env",
    "/config.php",
    "/wp-login.php",
    "/wp-admin",
    "/db_backup.sql",
    "/backup.zip",
    "/.git/config",
    "/api/v1/secret_credentials",
    "/shell.php",
    "/manager/html"
}

# SQLi & XSS Payload Patterns
SUSPICIOUS_PATTERNS = [
    r"(?i) (UNION\s+SELECT|DROP\s+TABLE|ALTER\s+TABLE|DELETE\s+FROM|INSERT\s+INTO) ",
    r"(?i)<script [^>]*>",
    r"(?i)javascript\s*:",
    r"(?i) OR\s+1\s*=\s*1 ",
    r"(?i)--\s*$"
]

@app.middleware("http")
async def security_firewall_middleware(request: Request, call_next):
    client_ip = request.client.host if request.client else "127.0.0.1"
    now = time.time()
    is_audit_scan = request.headers.get("X-Audit-Scan") == "active"
    path = request.url.path
    path_lower = path.lower()

    # 0. Immediate Firewall IP Blacklist Check
    if client_ip in BLOCKED_IPS and not is_audit_scan:
        return JSONResponse(
            status_code=403,
            content={"detail": "🚫 تم حظر عنوان IP هذا نهائياً من قبل جدار الحماية (Firewall Blacklist). يرجى التواصل مع مسؤول النظام."}
        )

    # 0.1 Honeypot Decoy Traps Inspection
    if path_lower in HONEYPOT_PATHS or any(path_lower.startswith(p) for p in ["/phpmyadmin", "/.git", "/wp-login", "/wp-admin"]):
        if client_ip not in ["127.0.0.1", "::1", "localhost"] and not is_audit_scan:
            BLOCKED_IPS.add(client_ip)
        security_alert_service.send_incident_alert(
            incident_type="HONEYPOT_TRAP",
            client_ip=client_ip,
            target_endpoint=f"{request.method} {path}",
            payload_details=f"🍯 وقوع متسلل في مصيدة المسارات الوهمية (Honeypot Trap): {path}",
            user_agent=request.headers.get("user-agent", "Unknown")
        )
        return JSONResponse(status_code=404, content={"detail": "Not Found"})

    # 0.2 Directory Traversal Attack Inspection
    query_params = str(request.query_params)
    if "../" in path or "..\\" in path or "%2e%2e" in path_lower or "../" in query_params or "..\\" in query_params:
        security_alert_service.send_incident_alert(
            incident_type="PATH_TRAVERSAL",
            client_ip=client_ip,
            target_endpoint=f"{request.method} {path}",
            payload_details=f"محاولة اجتياز المسارات (Path Traversal): {path} | params: {query_params}",
            user_agent=request.headers.get("user-agent", "Unknown")
        )
        return JSONResponse(status_code=400, content={"detail": "⚠️ Security Alert: Directory Traversal attack blocked."})

    # 0.3 Emergency Panic Lockdown Inspection
    if not is_audit_scan and request.method in ["POST", "PUT", "DELETE"]:
        if "/api/security/ai/unpanic" not in path and "/auth/login" not in path:
            try:
                from app.services.emergency_snapshot_service import emergency_snapshot_service
                if emergency_snapshot_service.is_write_blocked():
                    return JSONResponse(
                        status_code=423,
                        content={"detail": "🚨 تم تفعيل وضع الطوارئ القصوى (Panic Lockdown). النظام في وضع القراءة فقط لحماية البيانات. يرجى إدخال رمز الاستعادة."}
                    )
            except Exception:
                pass

    # 1. IP Blacklist & Rate Limiting Check
    # 1.1 Dedicated Login Brute-Force Shield (Max 10 login requests per minute)
    if "/auth/login" in path:
        login_history = [t for t in LOGIN_RATE_LIMIT.get(client_ip, []) if now - t < 60]
        login_history.append(now)
        LOGIN_RATE_LIMIT[client_ip] = login_history
        if len(login_history) > 10:
            security_alert_service.send_incident_alert(
                incident_type="BRUTE_FORCE",
                client_ip=client_ip,
                target_endpoint=f"POST {path}",
                payload_details=f"هجوم تخمين كلمات مرور مكثف ({len(login_history)} محاولة خلال 60 ثانية)",
                user_agent=request.headers.get("user-agent", "Unknown")
            )
            return JSONResponse(status_code=429, content={"detail": "⚠️ Too many login attempts. Brute-force protection activated."})

    # 1.2 DoS Large Payload Inspection (Max 50KB for API/auth endpoints)
    content_length = request.headers.get("content-length")
    if content_length and int(content_length) > 50 * 1024:
        if "/api/" in path:
            try:
                await request.body()
            except Exception:
                pass
            security_alert_service.send_incident_alert(
                incident_type="DOS_PAYLOAD",
                client_ip=client_ip,
                target_endpoint=path,
                payload_details=f"حجم الحزمة غير الطبيعي: {content_length} بايت (>50KB)",
                user_agent=request.headers.get("user-agent", "Unknown")
            )
            return JSONResponse(status_code=413, content={"detail": "⚠️ Payload Too Large: Exceeds safe API boundary limit."})

    # 1.3 Global IP Rate Limiting (60 req/min for normal traffic, bypassed when testing other logic via audit header)
    if not is_audit_scan:
        req_history = [t for t in RATE_LIMIT_STORE.get(client_ip, []) if now - t < 60]
        req_history.append(now)
        RATE_LIMIT_STORE[client_ip] = req_history
        if len(req_history) > 60:
            if client_ip not in ["127.0.0.1", "::1", "localhost"]:
                BLOCKED_IPS.add(client_ip)
                return JSONResponse(status_code=403, content={"detail": "⚠️ IP address blocked due to security audit violation."})
            else:
                return JSONResponse(status_code=429, content={"detail": "⚠️ Rate limit exceeded. Temporary firewall block applied."})

    # 2. SQLi & XSS Payload Inspection
    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, query_params) or re.search(pattern, path):
            itype = "XSS_ATTACK" if ("<script" in pattern or "javascript" in pattern) else "SQL_INJECTION"
            security_alert_service.send_incident_alert(
                incident_type=itype,
                client_ip=client_ip,
                target_endpoint=f"{request.method} {path}",
                payload_details=f"نمط الهجوم المرصود: {pattern} | المدخلات: {query_params or path}",
                user_agent=request.headers.get("user-agent", "Unknown")
            )
            return JSONResponse(status_code=400, content={"detail": "⚠️ Security Firewall Alert: Malformed or suspicious query payload detected."})

    # Execute request
    response: Response = await call_next(request)
    
    # 3. HTTP Security & No-Cache Headers Injection
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Content-Security-Policy"] = (
        "default-src 'self' 'unsafe-inline' 'unsafe-eval' https: data: blob:; "
        "font-src 'self' https://cdnjs.cloudflare.com https://cdn.jsdelivr.net https://fonts.gstatic.com data:; "
        "style-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com https://cdn.jsdelivr.net https://fonts.googleapis.com; "
        "script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.jsdelivr.net https://cdnjs.cloudflare.com; "
        "img-src 'self' https: data: blob:;"
    )
    response.headers["Server"] = "Secure-School-Firewall-v2"
    if path.startswith("/assets/") or path.startswith("/static/"):
        response.headers["Cache-Control"] = "public, max-age=86400, stale-while-revalidate=604800"
        if "Pragma" in response.headers:
            del response.headers["Pragma"]
        if "Expires" in response.headers:
            del response.headers["Expires"]
    else:
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
    
    return response

# ==================== LAYER 2: SYSTEM INTEGRITY & STORAGE ENGINE ====================
@app.on_event("startup")
def enforce_database_security():
    print("[SEC] System Protection Engine Enabled: High-Concurrency In-Memory & Local Storage Mode Active!")
    import threading
    def _cyber_ai_periodic_worker():
        import time
        time.sleep(10)
        while True:
            try:
                from app.services.cyber_ai_agent import cyber_guardian_ai
                cyber_guardian_ai.autonomous_self_heal()
            except Exception:
                pass
            time.sleep(3600)
            
    t = threading.Thread(target=_cyber_ai_periodic_worker, daemon=True)
    t.start()

from app.api.api import api_router

# Set up CORS for frontend (Cloud & Multi-Domain Production Support)
ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
env_origins = os.getenv("ALLOWED_ORIGINS")
if env_origins:
    ALLOWED_ORIGINS.extend([o.strip() for o in env_origins.split(",") if o.strip()])

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_origin_regex=r"^https?://(192\.168\.\d+\.\d+|10\.\d+\.\d+\.\d+|172\.(1[6-9]|2\d|3[01])\.\d+\.\d+|localhost|([a-zA-Z0-9-]+\.)*(vercel\.app|onrender\.com))(:\d+)?$",
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# High-Performance GZip Compression Middleware (min 1KB)
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Render / Cloud Health Check Endpoint
@app.get("/health", tags=["System"])
@app.get("/api/health", tags=["System"])
async def health_check():
    return {
        "status": "healthy",
        "service": "smart-school-erp",
        "timestamp": time.time(),
        "version": "2.0.0"
    }

# Promotional Motion Graphics Route
@app.get("/motion", include_in_schema=False)
@app.get("/motion/index.html", include_in_schema=False)
async def get_motion_presentation():
    motion_index = BASE_DIR / "frontend" / "motion" / "index.html"
    if motion_index.exists():
        return FileResponse(str(motion_index))
    return RedirectResponse(url="/school")

app.include_router(api_router, prefix="/api")

# ==================== DEDICATED PORTAL ROUTING ENGINE (Jinja2 Modular Templates) ====================

NO_CACHE_HEADERS = {
    "Cache-Control": "no-cache, no-store, must-revalidate, max-age=0",
    "Pragma": "no-cache",
    "Expires": "0"
}

# Favicon Route
@app.get("/favicon.ico", include_in_schema=False)
async def get_favicon():
    fav_file = BASE_DIR / "assets" / "images" / "schools" / "sch_01_logo.svg"
    if fav_file.exists():
        return FileResponse(str(fav_file), media_type="image/svg+xml")
    return Response(status_code=204)

# 0. Root Redirect
@app.get("/", include_in_schema=False)
async def root_redirect():
    return RedirectResponse(url="/school")

# 1. School Admin & Teachers Portal
@app.get("/school", include_in_schema=False)
@app.get("/school.html", include_in_schema=False)
async def get_school_portal(request: Request):
    return templates.TemplateResponse(request=request, name="portals/school.html", context={"portal_type": "school"}, headers=NO_CACHE_HEADERS)

# 2. SaaS Super Admin Portal
@app.get("/admin", include_in_schema=False)
@app.get("/saas", include_in_schema=False)
@app.get("/admin.html", include_in_schema=False)
async def get_saas_portal(request: Request):
    return templates.TemplateResponse(request=request, name="portals/admin.html", context={"portal_type": "admin"}, headers=NO_CACHE_HEADERS)

# 3. Parent & Student Portal
@app.get("/parent", include_in_schema=False)
@app.get("/parents", include_in_schema=False)
@app.get("/parent.html", include_in_schema=False)
async def get_parent_portal(request: Request):
    return templates.TemplateResponse(request=request, name="portals/parent.html", context={"portal_type": "parent"}, headers=NO_CACHE_HEADERS)

# 4. Public Blockchain Certificate Verification Portal
@app.get("/verify/{cert_code}", include_in_schema=False)
@app.get("/verify", include_in_schema=False)
async def public_verify_certificate(request: Request, cert_code: str = "CERT-2026-1001"):
    from app.services.blockchain import academic_blockchain
    cert = academic_blockchain.get_certificate(cert_code)
    current_url = str(request.url)
    return templates.TemplateResponse(
        request=request, 
        name="public/verify_certificate.html", 
        context={"cert": cert, "cert_code": cert_code, "current_url": current_url},
        headers=NO_CACHE_HEADERS
    )

# Static assets (Modular architecture)
app.mount("/assets", StaticFiles(directory=str(BASE_DIR / "assets")), name="assets")

# Legacy static mounts (backward compatibility)
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "frontend")), name="static")
app.mount("/", StaticFiles(directory=str(BASE_DIR / "frontend"), html=True), name="frontend")
