import hmac
import hashlib
import time
import struct
import base64
import secrets
import string
from typing import List, Dict, Any, Tuple

class TOTPService:
    def __init__(self, issuer: str = "SmartSchoolERP"):
        self.issuer = issuer

    def generate_secret(self, length: int = 32) -> str:
        """Generate a cryptographically secure Base32 secret key."""
        random_bytes = secrets.token_bytes(20)
        return base64.b32encode(random_bytes).decode('utf-8').rstrip('=')

    def get_totp_uri(self, secret: str, username: str) -> str:
        """Format the otpauth:// URI for Google Authenticator QR Code."""
        clean_secret = secret.strip().replace(" ", "").upper()
        return f"otpauth://totp/{self.issuer}:{username}?secret={clean_secret}&issuer={self.issuer}&algorithm=SHA1&digits=6&period=30"

    def generate_totp_code(self, secret: str, for_time: int = None, time_step: int = 30, digits: int = 6) -> str:
        """Generate 6-digit TOTP code according to RFC 6238."""
        if for_time is None:
            for_time = int(time.time())
        
        clean_secret = secret.strip().replace(" ", "").upper()
        # Add padding if needed
        padding = (8 - len(clean_secret) % 8) % 8
        clean_secret += "=" * padding
        
        try:
            key = base64.b32decode(clean_secret, casefold=True)
        except Exception:
            return ""

        counter = int(for_time // time_step)
        msg = struct.pack(">Q", counter)
        h = hmac.new(key, msg, hashlib.sha1).digest()
        offset = h[19] & 15
        token = (struct.unpack(">I", h[offset:offset+4])[0] & 0x7fffffff) % (10 ** digits)
        return f"{token:0{digits}d}"

    def verify_totp(self, secret: str, code: str, window: int = 1) -> bool:
        """Verify the 6-digit code with +/- window drift tolerance."""
        if not code or not secret:
            return False
        
        clean_code = str(code).strip().replace(" ", "")
        if len(clean_code) != 6 or not clean_code.isdigit():
            return False

        now = int(time.time())
        # Check current, previous, and next intervals (drift protection)
        for offset in range(-window, window + 1):
            valid_code = self.generate_totp_code(secret, for_time=now + (offset * 30))
            if valid_code == clean_code:
                return True
        return False

    def generate_backup_codes(self, count: int = 6) -> List[str]:
        """Generate emergency recovery backup codes."""
        codes = []
        alphabet = string.ascii_uppercase + string.digits
        for _ in range(count):
            part1 = ''.join(secrets.choice(alphabet) for _ in range(4))
            part2 = ''.join(secrets.choice(alphabet) for _ in range(4))
            codes.append(f"{part1}-{part2}")
        return codes

totp_service = TOTPService()
