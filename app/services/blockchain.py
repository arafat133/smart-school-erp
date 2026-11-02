import hashlib
import json
import time
from typing import Dict, Any, List, Optional

class BlockchainSimulator:
    @staticmethod
    def generate_hash(data: Dict[str, Any], previous_hash: str = "0") -> str:
        block = {
            "data": data,
            "previous_hash": previous_hash
        }
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @staticmethod
    def verify_integrity(data: Dict[str, Any], previous_hash: str, current_hash: str) -> bool:
        recalculated_hash = BlockchainSimulator.generate_hash(data, previous_hash)
        return recalculated_hash == current_hash

blockchain = BlockchainSimulator()


class AcademicBlock:
    def __init__(self, index: int, cert_code: str, student_data: Dict[str, Any], previous_hash: str):
        self.index = index
        self.cert_code = cert_code
        self.timestamp = int(time.time())
        self.student_data = student_data
        self.previous_hash = previous_hash
        # Use Cryptographically Sound Institutional Digital Signature
        from app.services.crypto_signature_service import academic_crypto_service
        signed_bundle = academic_crypto_service.sign_certificate({
            "index": self.index,
            "cert_code": self.cert_code,
            "timestamp": self.timestamp,
            "student_data": self.student_data
        })
        self.authority_signature = signed_bundle["digital_signature"]
        self.qr_token = signed_bundle["qr_verification_token"]
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        block_content = {
            "index": self.index,
            "cert_code": self.cert_code,
            "timestamp": self.timestamp,
            "student_data": self.student_data,
            "previous_hash": self.previous_hash,
            "authority_signature": self.authority_signature
        }
        block_bytes = json.dumps(block_content, sort_keys=True, ensure_ascii=False).encode('utf-8')
        return hashlib.sha256(block_bytes).hexdigest()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "index": self.index,
            "cert_code": self.cert_code,
            "timestamp": self.timestamp,
            "student_data": self.student_data,
            "previous_hash": self.previous_hash,
            "hash": self.hash,
            "authority_signature": self.authority_signature,
            "qr_verification_token": getattr(self, "qr_token", ""),
            "verified": True
        }


class AcademicBlockchain:
    def __init__(self):
        self.chain: List[AcademicBlock] = []
        self._initialize_genesis_block()
        self._seed_initial_certificates()

    def _initialize_genesis_block(self):
        genesis_data = {
            "title": "Genesis Block - National Academic Blockchain Ledger",
            "issuer": "Ministry of Education & Smart School Cloud Network",
            "version": "2.0.0"
        }
        genesis_block = AcademicBlock(0, "GENESIS-BLOCK", genesis_data, "0" * 64)
        self.chain.append(genesis_block)

    def _seed_initial_certificates(self):
        seeds = [
            {
                "cert_code": "CERT-2026-1001",
                "student_name": "محمد عبد الله أحمد الأهدل",
                "national_id": "01010098421",
                "seat_no": "2026101",
                "school_name": "مدرسة المتفوقين الأهلية النموذجية",
                "grade": "الثالث الثانوي (القسم العلمي)",
                "academic_year": "2026-2027",
                "percentage": "99.38%",
                "gpa": "3.98 / 4.00",
                "rank": "المركز الأول على مستوى المدرسة",
                "honors": "ممتاز مع مرتبة الشرف الأولى 🏆",
                "issue_date": "2026-08-30"
            },
            {
                "cert_code": "CERT-2026-1002",
                "student_name": "أحمد علي مسعد الريمي",
                "national_id": "01010088192",
                "seat_no": "2026102",
                "school_name": "مدرسة المتفوقين الأهلية النموذجية",
                "grade": "الثالث الثانوي (القسم العلمي)",
                "academic_year": "2026-2027",
                "percentage": "98.75%",
                "gpa": "3.95 / 4.00",
                "rank": "المركز الثاني على مستوى المدرسة",
                "honors": "ممتاز مع مرتبة الشرف 🥈",
                "issue_date": "2026-08-30"
            },
            {
                "cert_code": "CERT-2026-1003",
                "student_name": "سارة خالد المنصوري",
                "national_id": "01010077331",
                "seat_no": "2026103",
                "school_name": "مدرسة المتفوقين الأهلية النموذجية",
                "grade": "الثالث الثانوي (القسم العلمي)",
                "academic_year": "2026-2027",
                "percentage": "98.50%",
                "gpa": "3.94 / 4.00",
                "rank": "المركز الثالث على مستوى المدرسة",
                "honors": "ممتاز مع مرتبة الشرف 🥉",
                "issue_date": "2026-08-30"
            },
            {
                "cert_code": "CERT-2026-1004",
                "student_name": "فاطمة محمد باحيدرة",
                "national_id": "01010099452",
                "seat_no": "2026201",
                "school_name": "مدرسة المتفوقين الأهلية النموذجية",
                "grade": "الصف التاسع (المرحلة الأساسية)",
                "academic_year": "2026-2027",
                "percentage": "98.85%",
                "gpa": "3.96 / 4.00",
                "rank": "المركز الأول على مستوى المرحلة الأساسية",
                "honors": "ممتاز مع مرتبة الشرف الأولى 🏆",
                "issue_date": "2026-08-30"
            }
        ]
        for seed in seeds:
            cert_code = seed.pop("cert_code")
            self.add_certificate_block(cert_code, seed)

    def get_latest_block(self) -> AcademicBlock:
        return self.chain[-1]

    def add_certificate_block(self, cert_code: str, student_data: Dict[str, Any]) -> AcademicBlock:
        prev_block = self.get_latest_block()
        new_block = AcademicBlock(len(self.chain), cert_code, student_data, prev_block.hash)
        self.chain.append(new_block)
        return new_block

    def get_certificate(self, cert_code: str) -> Optional[Dict[str, Any]]:
        cert_code_clean = cert_code.strip().upper()
        for block in self.chain:
            if block.cert_code.upper() == cert_code_clean:
                data = block.to_dict()
                is_valid = self.verify_block_integrity(block)
                data["tamper_free"] = is_valid
                return data
        return None

    def verify_block_integrity(self, block: AcademicBlock) -> bool:
        recomputed = block.calculate_hash()
        return recomputed == block.hash

    def verify_full_chain(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i - 1]
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != prev.hash:
                return False
        return True

    def get_ledger_summary(self) -> Dict[str, Any]:
        return {
            "total_blocks": len(self.chain),
            "chain_valid": self.verify_full_chain(),
            "latest_block_hash": self.get_latest_block().hash,
            "blocks": [b.to_dict() for b in self.chain]
        }

academic_blockchain = AcademicBlockchain()
