import os
import base64
import hashlib
from typing import Dict, Any, List, Optional
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from app.core.config import settings

PREFIX = "enc::aes256::"

class AES256DataShield:
    def __init__(self):
        # Derive a 256-bit (32 bytes) master key deterministically from app settings.SECRET_KEY
        master_secret = getattr(settings, "SECRET_KEY", "DEFAULT_SUPER_SECURE_ERP_MASTER_KEY_2026")
        self.key = hashlib.sha256(f"SMART_SCHOOL_AES256_SALT::{master_secret}".encode('utf-8')).digest()
        self.aesgcm = AESGCM(self.key)
        self.protected_fields = [
            "salary", "basic_salary", "allowances", "advance_amount", "net_salary",
            "bank_account", "iban", "account_number", "credit_ceiling", "balance",
            "medical_notes", "chronic_conditions", "blood_group", "emergency_contact_phone",
            "national_id", "passport_number"
        ]

    def encrypt_field(self, plain_text: str) -> str:
        """Encrypt plain text with AES-256-GCM authenticated encryption."""
        if plain_text is None:
            return ""
        str_val = str(plain_text)
        if self.is_encrypted(str_val):
            return str_val  # Already encrypted
        
        nonce = os.urandom(12)  # 96-bit unique nonce for AES-GCM
        ciphertext = self.aesgcm.encrypt(nonce, str_val.encode('utf-8'), None)
        encoded_payload = base64.b64encode(nonce + ciphertext).decode('utf-8')
        return f"{PREFIX}{encoded_payload}"

    def decrypt_field(self, cipher_text: str) -> str:
        """Decrypt AES-256-GCM payload and verify integrity."""
        if not cipher_text:
            return ""
        str_val = str(cipher_text).strip()
        if not self.is_encrypted(str_val):
            return str_val  # Return as is if not encrypted
        
        try:
            raw_b64 = str_val[len(PREFIX):]
            combined = base64.b64decode(raw_b64)
            nonce = combined[:12]
            ciphertext = combined[12:]
            decrypted_bytes = self.aesgcm.decrypt(nonce, ciphertext, None)
            return decrypted_bytes.decode('utf-8')
        except Exception as e:
            try:
                from app.services.security_alert_service import security_alert_service
                security_alert_service.send_incident_alert(
                    incident_type="CRYPTO_TAMPERING",
                    client_ip="Database-Storage-Engine",
                    target_endpoint="AES-256-GCM Decryption Core",
                    payload_details=f"فشل التحقق من توقيع المصادقة AEAD (تلاعب مباشر بالبيانات): {str(e)}",
                    user_identity="Direct DB Access / Tampered Record"
                )
            except Exception:
                pass
            return f"[ERROR: Decryption/Tamper Failed: {str(e)}]"

    def is_encrypted(self, val: str) -> bool:
        return isinstance(val, str) and val.startswith(PREFIX)

    def encrypt_sensitive_dict(self, data: Dict[str, Any], custom_fields: Optional[List[str]] = None) -> Dict[str, Any]:
        """Encrypt all sensitive keys inside a dictionary."""
        fields_to_check = custom_fields or self.protected_fields
        result = {}
        for k, v in data.items():
            if k in fields_to_check and v is not None:
                result[k] = self.encrypt_field(str(v))
            else:
                result[k] = v
        return result

    def decrypt_sensitive_dict(self, data: Dict[str, Any], custom_fields: Optional[List[str]] = None) -> Dict[str, Any]:
        """Decrypt all sensitive keys inside a dictionary."""
        fields_to_check = custom_fields or self.protected_fields
        result = {}
        for k, v in data.items():
            if k in fields_to_check and isinstance(v, str) and self.is_encrypted(v):
                result[k] = self.decrypt_field(v)
            else:
                result[k] = v
        return result

    def get_security_audit_report(self) -> Dict[str, Any]:
        """Generate status report for Data-at-Rest encryption."""
        # Perform live round-trip test
        sample = "Test-Salary-450,000-YER"
        enc = self.encrypt_field(sample)
        dec = self.decrypt_field(enc)
        is_healthy = (dec == sample)

        return {
            "algorithm": "AES-256-GCM (Authenticated Galois/Counter Mode)",
            "key_length_bits": 256,
            "status": "ACTIVE & OPERATIONAL 🟢" if is_healthy else "ERROR 🔴",
            "tamper_proof": True,
            "protected_fields_count": len(self.protected_fields),
            "protected_fields_list": self.protected_fields,
            "prefix": PREFIX,
            "sample_verification_passed": is_healthy
        }

data_encryption_shield = AES256DataShield()
