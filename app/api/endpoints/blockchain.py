from fastapi import APIRouter, HTTPException
from typing import Dict, Any
from app.services.blockchain import academic_blockchain

router = APIRouter()

@router.get("/verify/{cert_code}")
def verify_certificate_api(cert_code: str) -> Dict[str, Any]:
    """Verify certificate hash and integrity against the blockchain ledger."""
    cert = academic_blockchain.get_certificate(cert_code)
    if not cert:
        raise HTTPException(status_code=404, detail="الشهادة غير موجودة في سجلات البلوكشين المعتمدة.")
    return cert

@router.get("/ledger")
def get_full_ledger() -> Dict[str, Any]:
    """Retrieve full blockchain ledger of academic certificates."""
    return academic_blockchain.get_ledger_summary()
