from sqlalchemy import Column, String, Numeric, ForeignKey, Date, DateTime, Enum, func
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import TenantModel
from sqlalchemy.orm import relationship
import enum
from decimal import Decimal

class AccountType(str, enum.Enum):
    ASSET = "ASSET"          # أصول (صندوق، بنك، ذمم طلاب)
    LIABILITY = "LIABILITY"  # التزامات (رسوم مستلمة مقدماً)
    EQUITY = "EQUITY"        # حقوق ملكية
    REVENUE = "REVENUE"      # إيرادات (رسوم دراسية، أنشطة، كتب)
    EXPENSE = "EXPENSE"      # مصروفات (رواتب، إيجار، صيانة)

class JournalEntryStatus(str, enum.Enum):
    DRAFT = "DRAFT"          # مسودة
    POSTED = "POSTED"        # مرحل (معتمد محاسبياً وغير قابل للتعديل)
    VOIDED = "VOIDED"        # ملغى بقيد عكسي

class Account(TenantModel):
    """
    دليل الحسابات المالي للمدرسة (Chart of Accounts)
    """
    __tablename__ = "accounts"

    code = Column(String(50), nullable=False, index=True) # e.g. "1010", "4010"
    name = Column(String(200), nullable=False)
    account_type = Column(Enum(AccountType), nullable=False)
    balance = Column(Numeric(18, 4), default=Decimal("0.0000"), nullable=False)
    currency = Column(String(10), default="YER", nullable=False)
    is_active = Column(String, default="true", nullable=False)

    lines = relationship("JournalEntryLine", back_populates="account")

class JournalEntry(TenantModel):
    """
    سند القيد المحاسبي العام (Double-Entry General Journal Entry)
    القيد الصلب: مجموع المدين (Debit) يجب أن يساوي تماماً مجموع الدائن (Credit)
    """
    __tablename__ = "journal_entries"

    entry_number = Column(String(100), nullable=False, index=True) # رقـم القيد المتسلسل
    entry_date = Column(Date, nullable=False, default=func.current_date())
    description = Column(String(500), nullable=False)
    status = Column(Enum(JournalEntryStatus), default=JournalEntryStatus.DRAFT, nullable=False)
    
    total_debit = Column(Numeric(18, 4), default=Decimal("0.0000"), nullable=False)
    total_credit = Column(Numeric(18, 4), default=Decimal("0.0000"), nullable=False)
    
    posted_at = Column(DateTime(timezone=True), nullable=True)
    posted_by_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    lines = relationship("JournalEntryLine", back_populates="entry", cascade="all, delete-orphan")

    def validate_atomic_balance(self) -> bool:
        """
        التحقق الصارم من التوازن المحاسبي:
        Debit == Credit بفارق صفري تماماً
        """
        total_d = sum((Decimal(str(line.debit)) for line in self.lines), Decimal("0.0000"))
        total_c = sum((Decimal(str(line.credit)) for line in self.lines), Decimal("0.0000"))
        self.total_debit = total_d
        self.total_credit = total_c
        return abs(total_d - total_c) == Decimal("0.0000") and total_d > Decimal("0.0000")

class JournalEntryLine(TenantModel):
    """
    طرف القيد المحاسبي (مدين / دائن)
    """
    __tablename__ = "journal_entry_lines"

    journal_entry_id = Column(UUID(as_uuid=True), ForeignKey("journal_entries.id", ondelete="CASCADE"), nullable=False, index=True)
    account_id = Column(UUID(as_uuid=True), ForeignKey("accounts.id", ondelete="RESTRICT"), nullable=False, index=True)
    
    debit = Column(Numeric(18, 4), default=Decimal("0.0000"), nullable=False)
    credit = Column(Numeric(18, 4), default=Decimal("0.0000"), nullable=False)
    memo = Column(String(255), nullable=True)

    entry = relationship("JournalEntry", back_populates="lines")
    account = relationship("Account", back_populates="lines")

class FinancialRecord(TenantModel):
    """
    السجل المالي للرسوم الدراسية للطلاب (Student Tuition Ledger)
    معدل لاستخدام الدقة المالية الصارمة Numeric(18, 4) بدلاً من Float
    """
    __tablename__ = "financial_records"

    academic_history_id = Column(UUID(as_uuid=True), ForeignKey("academic_history.id", ondelete="CASCADE"), nullable=False, index=True)
    grade_level = Column(String, nullable=False)
    academic_year = Column(String, nullable=False)
    
    total_required = Column(Numeric(18, 4), nullable=False)
    amount_paid = Column(Numeric(18, 4), default=Decimal("0.0000"), nullable=False)
    payment_status = Column(String, nullable=False) # Paid, Unpaid, Partial

    academic_record = relationship("AcademicHistory", back_populates="financial_record")
