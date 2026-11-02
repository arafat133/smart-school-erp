from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any, Optional
from app.core.encryption import data_encryption_shield

router = APIRouter()

class EncryptTestRequest(BaseModel):
    plain_text: str

class DecryptTestRequest(BaseModel):
    cipher_text: str

@router.get("/status")
def get_encryption_status() -> Dict[str, Any]:
    """Return the cryptographic audit report for Data-at-Rest AES-256."""
    return data_encryption_shield.get_security_audit_report()

@router.post("/test-encrypt")
def test_encryption(payload: EncryptTestRequest) -> Dict[str, Any]:
    """Test encrypting text live with AES-256-GCM."""
    encrypted = data_encryption_shield.encrypt_field(payload.plain_text)
    return {
        "plain_text": payload.plain_text,
        "cipher_text": encrypted,
        "algorithm": "AES-256-GCM",
        "protected": True
    }

@router.post("/test-decrypt")
def test_decryption(payload: DecryptTestRequest) -> Dict[str, Any]:
    """Test decrypting ciphertext live."""
    decrypted = data_encryption_shield.decrypt_field(payload.cipher_text)
    return {
        "cipher_text": payload.cipher_text,
        "decrypted_text": decrypted,
        "verified": True
    }
