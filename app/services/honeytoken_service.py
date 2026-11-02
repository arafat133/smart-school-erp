# -*- coding: utf-8 -*-
"""
================================================================================
🍯 DECEPTION TECHNOLOGY: DATABASE HONEYTOKENS & CANARY TRAP ENGINE
================================================================================
Plants decoy records inside user, student, and financial databases.
If an attacker exploits an SQL injection or IDOR or internal query to extract
these decoy records, an immediate Red Incident Alert is triggered!
================================================================================
"""
import os
import json
import time
from typing import Dict, Any, Optional

CANARY_USERS = {
    "usr-canary-honeytoken-root-999": {
        "id": "usr-canary-honeytoken-root-999",
        "username": "super_backup_admin",
        "email": "canary_admin_root@school.internal",
        "role": "super_admin",
        "is_canary": True
    },
    "usr-canary-database-dump-000": {
        "id": "usr-canary-database-dump-000",
        "username": "db_replication_operator",
        "email": "decoy_db_sync@school.internal",
        "role": "school_admin",
        "is_canary": True
    }
}

CANARY_STUDENTS = {
    "stu-canary-decoy-000": {
        "id": "stu-canary-decoy-000",
        "student_name": "Canary Honeytoken Decoy Student",
        "national_id": "CANARY-998877-SECRET",
        "guardian_phone": "+967-770000000",
        "is_canary": True
    }
}

CANARY_IDENTIFIERS = {
    "usr-canary-honeytoken-root-999",
    "usr-canary-database-dump-000",
    "super_backup_admin",
    "db_replication_operator",
    "stu-canary-decoy-000",
    "CANARY-998877-SECRET"
}


class HoneytokenService:
    def __init__(self):
        self.canary_hits = 0

    def is_canary_hit(self, identifier: str) -> bool:
        if not identifier:
            return False
        id_str = str(identifier).strip()
        return id_str in CANARY_IDENTIFIERS

    def trigger_canary_alert(self, identifier: str, client_ip: str, endpoint: str, user_agent: str = "Unknown"):
        self.canary_hits += 1
        try:
            from app.services.security_alert_service import security_alert_service
            from app.main import BLOCKED_IPS
            
            # Automatically block the attacker
            if client_ip not in ["127.0.0.1", "::1", "localhost"]:
                BLOCKED_IPS.add(client_ip)

            security_alert_service.send_incident_alert(
                incident_type="HONEYTOKEN_TRAP",
                client_ip=client_ip,
                target_endpoint=endpoint,
                payload_details=f"🚨 محاولة وصول/استخراج سجل تمويهي سري (Honeytoken Canary): {identifier}",
                user_identity="متسلل يحاول استخراج بيانات مخفية (Canary Hunter)",
                user_agent=user_agent
            )
        except Exception as e:
            print(f"[CANARY] Alert error: {e}")

    def get_canary_status(self) -> Dict[str, Any]:
        return {
            "active_honeytokens_count": len(CANARY_IDENTIFIERS),
            "total_canary_triggers": self.canary_hits,
            "status": "ARMED_AND_WATCHING"
        }


honeytoken_service = HoneytokenService()
