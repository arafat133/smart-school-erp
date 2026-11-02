import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")

class Settings:
    PROJECT_NAME: str = "Secure Cloud School System"
    # Local high-speed SQLite async database for reliable offline testing, or remote via env
    DEFAULT_DB_PATH = (BASE_DIR / "secure_school.db").as_posix()
    DATABASE_URL: str = os.getenv("DATABASE_URL", f"sqlite+aiosqlite:///{DEFAULT_DB_PATH}")
    
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey_for_jwt_tokens_generation")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # 7 days

    # Telegram & WhatsApp Security Incident Alerting
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    TELEGRAM_CHAT_ID: str = os.getenv("TELEGRAM_CHAT_ID", "")
    WHATSAPP_PHONE: str = os.getenv("WHATSAPP_PHONE", "")
    WHATSAPP_APIKEY: str = os.getenv("WHATSAPP_APIKEY", "")
    ENABLE_SECURITY_ALERTS: bool = os.getenv("ENABLE_SECURITY_ALERTS", "true").lower() in ("true", "1", "yes")

settings = Settings()
