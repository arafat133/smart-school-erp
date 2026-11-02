# -*- coding: utf-8 -*-
"""
================================================================================
🛡️ SECURITY ACTIONS & SOC MANAGEMENT ENDPOINTS
================================================================================
Provides one-click IP banning, unbanning, Honeypot management,
and real-time SOC Daily Digest reporting for administrators.
================================================================================
"""
from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import HTMLResponse, JSONResponse
import hashlib
import time

from app.core.config import settings
from app.services.security_alert_service import security_alert_service

router = APIRouter()

def get_action_token(ip: str) -> str:
    """Generates cryptographic authentication token for remote Telegram actions."""
    secret = getattr(settings, "SECRET_KEY", "DEFAULT_SECRET")
    return hashlib.sha256(f"{secret}::SECURITY_ACTION::{ip}".encode('utf-8')).hexdigest()[:16]

def verify_action_token(ip: str, token: str) -> bool:
    expected = get_action_token(ip)
    return token == expected

@router.get("/ban-ip", response_class=HTMLResponse)
def ban_ip_action(ip: str, token: str, request: Request):
    """One-click Ban IP action triggered from Telegram or admin dashboard."""
    if not verify_action_token(ip, token):
        raise HTTPException(status_code=403, detail="رمز التحقق الأمني غير صالح أو منتهي الصلاحية")
    
    # Import BLOCKED_IPS from main
    from app.main import BLOCKED_IPS
    BLOCKED_IPS.add(ip)
    
    # Send confirmation notice to Telegram
    security_alert_service.send_incident_alert(
        incident_type="BRUTE_FORCE",
        client_ip=ip,
        target_endpoint="Firewall Action Center",
        payload_details=f"✅ تأكيد إداري: تم حظر هذا العنوان نهائياً بنقرة واحدة بواسطة مدير النظام.",
        user_identity="مدير النظام (Security Admin)"
    )
    
    html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>تأكيد حظر العنوان - Secure School ERP</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, sans-serif; background: #0f172a; color: #f8fafc; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }}
        .card {{ background: #1e293b; padding: 40px; border-radius: 16px; border: 1px solid #334155; text-align: center; max-width: 500px; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5); }}
        .badge {{ background: #ef4444; color: white; padding: 6px 14px; border-radius: 9999px; font-weight: bold; font-size: 14px; }}
        h1 {{ margin: 20px 0 10px; font-size: 24px; }}
        p {{ color: #94a3b8; line-height: 1.6; }}
        .ip-box {{ background: #0f172a; border: 1px dashed #ef4444; color: #fca5a5; font-family: monospace; font-size: 18px; padding: 12px; border-radius: 8px; margin: 20px 0; }}
        .btn {{ display: inline-block; background: #3b82f6; color: white; text-decoration: none; padding: 10px 24px; border-radius: 8px; font-weight: bold; margin-top: 15px; }}
    </style>
</head>
<body>
    <div class="card">
        <span class="badge">🛡️ جدار الحماية السيبراني</span>
        <h1>تم حظر عنوان IP بنجاح!</h1>
        <div class="ip-box">{ip}</div>
        <p>تم إدراج هذا العنوان في القائمة السوداء الدائمة لجدار حماية المدرسة، وتم إسقاط أي اتصالات قادمة منه فورياً.</p>
        <p style="font-size: 13px; color: #64748b;">تم توثيق الإجراء وإرسال تأكيد إلى حسابك في التلجرام.</p>
    </div>
</body>
</html>"""
    return HTMLResponse(content=html_content)

@router.get("/unban-ip", response_class=HTMLResponse)
def unban_ip_action(ip: str, token: str):
    """Unban IP action."""
    if not verify_action_token(ip, token):
        raise HTTPException(status_code=403, detail="رمز التحقق الأمني غير صالح")
        
    from app.main import BLOCKED_IPS
    if ip in BLOCKED_IPS:
        BLOCKED_IPS.remove(ip)
        
    return HTMLResponse(f"<div dir='rtl' style='font-family:sans-serif;padding:30px;'>✅ تم فك الحظر عن عنوان IP: <b>{ip}</b> بنجاح.</div>")

@router.post("/digest")
def trigger_soc_digest():
    """Triggers the full 24-hour SOC security briefing to Telegram."""
    success = security_alert_service.send_soc_daily_digest()
    return {"status": "success" if success else "failed", "message": "تم إرسال التقرير الأمني اليومي إلى التلجرام بنجاح"}

# ══════════════════════════════════════════════════════════════════════════
# 🧠 CYBER AI GUARDIAN & AUTONOMOUS DEFENSE ENDPOINTS
# ══════════════════════════════════════════════════════════════════════════
@router.get("/ai/status")
def get_cyber_ai_status():
    """Returns real-time status of the Cyber Guardian AI agent."""
    from app.services.cyber_ai_agent import cyber_guardian_ai
    from app.main import BLOCKED_IPS
    return {
        "agent": cyber_guardian_ai.agent_name,
        "status": cyber_guardian_ai.status,
        "last_audit": cyber_guardian_ai.last_audit_time,
        "last_self_heal": cyber_guardian_ai.last_self_heal_time,
        "blocked_ips_count": len(BLOCKED_IPS),
        "virtual_patches_active": len(cyber_guardian_ai.virtual_patches),
        "timestamp": time.time()
    }

@router.post("/ai/chat")
async def chat_with_cyber_ai(request: Request):
    """Direct API to interact with the Cyber Guardian AI Agent."""
    from app.services.cyber_ai_agent import cyber_guardian_ai
    body = await request.json()
    query = body.get("message", "")
    user = body.get("user", "مدير النظام")
    reply = cyber_guardian_ai.chat_with_agent(query, user)
    return {"reply": reply}

@router.post("/ai/audit")
def trigger_autonomous_audit():
    """Triggers full autonomous vulnerability audit."""
    from app.services.cyber_ai_agent import cyber_guardian_ai
    report = cyber_guardian_ai.autonomous_system_audit()
    return report

@router.post("/ai/self-heal")
def trigger_autonomous_self_heal():
    """Triggers autonomous self-healing, virtual patching, and package security baseline check."""
    from app.services.cyber_ai_agent import cyber_guardian_ai
    result = cyber_guardian_ai.autonomous_self_heal()
    return result

@router.get("/ai/code-scan")
@router.post("/ai/code-scan")
def trigger_code_error_scan():
    """Triggers deep static code analysis, AST syntax validation, and SAST error detection."""
    from app.services.cyber_ai_agent import cyber_guardian_ai
    report = cyber_guardian_ai.scan_codebase_for_errors()
    return report

@router.post("/ai/panic")
def trigger_panic_mode(request: Request):
    """Triggers emergency lockdown and encrypted backup snapshot."""
    from app.services.emergency_snapshot_service import emergency_snapshot_service
    res = emergency_snapshot_service.activate_panic_mode(triggered_by="Web Admin Dashboard")
    return res

@router.post("/ai/unpanic")
async def trigger_unpanic_mode(request: Request):
    """Deactivates emergency lockdown using recovery token."""
    from app.services.emergency_snapshot_service import emergency_snapshot_service
    body = await request.json()
    token = body.get("token", "")
    ok, msg = emergency_snapshot_service.deactivate_panic_mode(token)
    return {"success": ok, "message": msg}

@router.get("/ai/forensic-report-pdf")
def get_forensic_report_pdf():
    """Generates official forensics PDF and serves download."""
    from app.services.forensic_pdf_service import forensic_report_service
    from fastapi.responses import FileResponse
    rep = forensic_report_service.generate_incident_report()
    pdf_path = rep["pdf_path"]
    return FileResponse(
        path=pdf_path,
        media_type="application/pdf",
        filename=rep["pdf_filename"]
    )

@router.get("/ai/canary-status")
def get_honeytoken_status():
    """Returns database honeytokens and canary trap status."""
    from app.services.honeytoken_service import honeytoken_service
    return honeytoken_service.get_canary_status()

