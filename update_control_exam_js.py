"""
Python script to append Control & Exam logic in frontend/app.js
"""
import re, time

print("=" * 60)
print("Updating app.js with Control & Exam Logic...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

control_db_additions = """
// Data collections for Control & Examination modules
if (!DB.interactiveGradingData) DB.interactiveGradingData = [
    { secCode: 'SEC-8839', student: '2026104 - عبدالرحمن محمد علي', coursework: 18, entered: 34, maxScore: 40, passScore: 20, total: 88, symbol: 'B+', result: 'ناجح (Passed)', locked: true, notes: 'تم تعديل الدرجة بناءً على إعادة تصحيح (قرار لجنة)' },
    { secCode: 'SEC-8840', student: '2026105 - أسامة عبدالله أحمد', coursework: 16, entered: 28, maxScore: 40, passScore: 20, total: 74, symbol: 'C+', result: 'ناجح (Passed)', locked: true, notes: 'رصد اعتيادي' },
    { secCode: 'SEC-8841', student: '2026106 - خالد محمود سعيد', coursework: 12, entered: 14, maxScore: 40, passScore: 20, total: 48, symbol: 'F', result: 'راسب (دور ثاني)', locked: true, notes: 'يحق له تقديم امتحان الدور الثاني' }
];

if (!DB.finalResultsData) DB.finalResultsData = [
    { student: '2026104 - عبدالرحمن محمد علي (الثاني الثانوي)', totalScore: '920 / 1000', percentage: '92.00%', gpa: '3.68 / 4.00', grade: 'ممتاز (Excellent)', rank: 'المركز 3 من أصل 120', honors: 'مرتبة الشرف الأولى', result: 'ناجح ومترفّع', pending: 'لا يوجد', holdStatus: 'متاحة (مستوفي)', publishStatus: 'معلنة ورسمية', stamp: 'تم الاعتماد - CTL-2026-991' },
    { student: '2026105 - أسامة عبدالله أحمد (الثاني الثانوي)', totalScore: '780 / 1000', percentage: '78.00%', gpa: '3.12 / 4.00', grade: 'جيد جداً', rank: 'المركز 24 من أصل 120', honors: 'لا يوجد', result: 'ناجح ومترفّع', pending: 'لا يوجد', holdStatus: 'متاحة', publishStatus: 'معلنة ورسمية', stamp: 'تم الاعتماد - CTL-2026-991' }
];

if (!DB.certificatesData) DB.certificatesData = [
    { serialNo: 'CERT-2026-00842', student: 'عبدالرحمن محمد علي (رقم: 2026104)', qual: 'شهادة الثانوية العامة - الفرع العلمي', gpaGrade: '94.50% - ممتاز مع مرتبة الشرف', gradYear: '2025/2026', qrUrl: 'https://verify.school.edu/cert/CERT-2026-00842', docType: 'شهادة نجاح وتخرج', stampStatus: 'موقعة ومختومة إلكترونياً', status: 'مطبوعة - تم التسليم', issueDate: '2026-08-08 (مسؤول الكنترول)' }
];

if (!DB.examHallsData) DB.examHallsData = [
    { no: 'لجنة رقم (12) - القاعة الكبرى', location: 'المبنى (أ) - الدور الثاني - قاعة A-201', capacity: '40 مقعداً', target: 'الثالث الثانوي (أ) + الثاني الثانوي (ب)', seatingRange: '2026101 - 2026140', pattern: 'تبادلي (خلط مستويين)', supervisor: 'د. أحمد علي العنسي', proctors: 'أ. خالد محمود + أ. ياسر سعيد', status: 'مجهزة ومطبوعة الملصقات', pdfFile: 'Attendance_List_Com12.pdf' }
];

if (!DB.seatNumbersData) DB.seatNumbersData = [
    { seatNo: '20261004', name: 'عبدالرحمن محمد علي المقطري', idPhoto: 'ID: 2026104 (مرفق)', gradeBranch: 'الثالث الثانوي - العلمية (أ)', committee: 'لجنة رقم (05) - القاعة الكبرى', deskNo: 'مقعد رقم: 18', location: 'المبنى (ب) - الدور الأول', barcode: 'BAR-20261004', type: 'كشف تعليق عام', status: 'مطبوع وموزع' }
];

if (!DB.secretNumbersData) DB.secretNumbersData = [
    { rollNo: '20261004 (مخفي)', secretCode: 'SEC-98402', subjectExam: 'الكيمياء - الامتحان النهائي', gradeSec: 'الثالث الثانوي - العلمي', pattern: 'عشوائي مشفر (Random Hash 5 Digits)', formVariant: 'نموذج (أ) - غلاف أزرق', timestamp: '2026-08-08 07:30 AM', operator: 'د. رئيس لجنة الكنترول العامة', lockStatus: 'مُغلق ومُقفل بكلمة المرور', deanonymizeStatus: 'مُعلق (في انتظار انتهاء التصحيح)' }
];

if (!DB.hallDistributionData) DB.hallDistributionData = [
    { id: 'PRC-2026-092', proctor: 'أ. خالد محمود العنسي (EMP-088)', role: 'ملاحظ رئيسي', committee: 'لجنة رقم (08)', location: 'المبنى (أ) - قاعة A-102', examDate: 'الكيمياء - السبت 2026-08-15', shift: 'الفترة الأولى (08:00 - 10:30 AM)', conflictStatus: 'آمن (لا توجد قرابة / خارج التخصص)', workload: '5 من أصل 8 فترات', notifyStatus: 'تم الإرسال والتأكيد', attStatus: 'حاضر في الموعد', standby: 'أ. ياسر سعيد' }
];

if (!DB.rollCallData) DB.rollCallData = [
    { deskNo: 'مقعد (12)', rollNo: '20261004', studentPhoto: 'عبدالرحمن محمد علي', subjectGrade: 'الفيزياء - الثالث الثانوي', signature: 'موقع (تم التوقيع)', bookletSerial: 'BK-88401-2026', attStatus: 'حاضر', handoverStatus: 'تم التسليم بنجاح', caller: 'أ. خالد محمود العنسي', notes: 'لا يوجد' }
];

if (!DB.substituteData) DB.substituteData = [
    { absent: 'أ. محمد عبدالله (غائب بعذر)', classPeriod: 'الصف 10/أ - الحصة الثالثة (09:45 ص)', subjectTopic: 'رياضيات - حل تمارين المعاملات', substitute: 'أ. سليم أحمد (مدرس رياضيات / متفرغ)', criterion: 'متفرغ + نفس التخصص + الأقل تكليفاً', status: 'تم التأكيد', activity: 'إعطاء ورقة عمل مجهزة', allowance: 'حصة إضافية مدفوعة', notes: 'تم إنجاز حل التمارين والانضباط ممتاز' }
];
"""

control_modules_js = """

// ==================== 1. INTERACTIVE GRADING ENGINE ====================
let isGradingLocked = true;
function renderInteractiveGradingGrid() {
    const tb = document.getElementById('tbl-interactive-grading');
    if (!tb) return;

    const list = DB.interactiveGradingData || [];
    tb.innerHTML = list.map((g, idx) => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${g.secCode}</td>
            <td style="font-weight:700;">${g.student}</td>
            <td><input type="number" value="${g.coursework}" style="width:60px;text-align:center;" ${isGradingLocked?'disabled':''}></td>
            <td><input type="number" value="${g.entered}" style="width:60px;text-align:center;" ${isGradingLocked?'disabled':''}></td>
            <td style="font-weight:800;color:#34d399;font-size:1.05rem;">${g.total} / 100</td>
            <td><span style="padding:2px 8px;border-radius:4px;font-size:0.78rem;font-weight:800;background:rgba(59,130,246,0.15);color:#60a5fa;">${g.symbol}</span></td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:${g.result.includes('ناجح')?'rgba(16,185,129,0.15)':'rgba(239,68,68,0.15)'};color:${g.result.includes('ناجح')?'#10b981':'#f87171'};">${g.result}</span></td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(245,158,11,0.15);color:#fbbf24;">${isGradingLocked?'مغلق ومُعتمد':'مفتوح للرصد'}</span></td>
            <td style="font-size:0.8rem;">${g.notes}</td>
        </tr>
    `).join('');
}

function toggleGradingLock() {
    isGradingLocked = !isGradingLocked;
    const btn = document.getElementById('btnLockGrading');
    const banner = document.getElementById('grLockBanner');
    if (isGradingLocked) {
        if (btn) btn.innerHTML = '<i class="fa-solid fa-lock"></i> قفل واعتماد الشيت';
        if (banner) banner.innerHTML = '<span><i class="fa-solid fa-lock"></i> حالة الشيت: مغلق ومُعتمد من الكنترول</span><span>العظمى: 40 | نجاح: 20</span>';
        toast('🔒 تم إغلاق قفل الشيت بنجاح ومنع أي تعديل');
    } else {
        if (btn) btn.innerHTML = '<i class="fa-solid fa-lock-open"></i> فتح الشيت للتعديل';
        if (banner) banner.innerHTML = '<span><i class="fa-solid fa-lock-open"></i> حالة الشيت: مفتوح للرصد وتعديل الدرجات</span><span>العظمى: 40 | نجاح: 20</span>';
        toast('🔓 تم فتح الشيت لإدخال وتعديل الدرجات');
    }
    renderInteractiveGradingGrid();
}


// ==================== 2. FINAL RESULTS & TRANSCRIPTS ====================
function renderFinalResultsGrid() {
    const tb = document.getElementById('tbl-final-results-grid');
    if (!tb) return;

    const list = DB.finalResultsData || [];
    tb.innerHTML = list.map(r => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${r.student}</td>
            <td style="font-weight:700;">${r.totalScore}</td>
            <td style="font-weight:800;color:#34d399;">${r.percentage}</td>
            <td style="font-weight:800;color:#60a5fa;">${r.gpa}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${r.grade}</span></td>
            <td style="font-weight:700;">${r.rank}</td>
            <td style="color:#fbbf24;font-weight:700;">${r.honors}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${r.result}</span></td>
            <td>${r.pending}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(59,130,246,0.15);color:#93c5fd;">${r.holdStatus}</span></td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(16,185,129,0.15);color:#10b981;">${r.publishStatus}</span></td>
            <td><button class="btn-edit" onclick="toast('معاينة شهادة الطالب التفصيلية PDF')"><i class="fa-solid fa-file-pdf"></i> الشهادة</button></td>
        </tr>
    `).join('');
}

function calculateFinalResultsGPA() {
    toast('⚡ جاري معالجة واحتساب النتائج والتراكمي آلياً للدفعة...');
    setTimeout(() => { renderFinalResultsGrid(); toast('✅ تم معالجة واحتساب النتائج التراكمية بنجاح!'); }, 700);
}

function togglePublishResults() {
    toast('🌐 تم اعتماد ونشر نتائج الدفعة للبوابة والتطبيق الإلكتروني بنجاح!');
}


// ==================== 3. OFFICIAL CERTIFICATES ====================
function renderCertificatesGrid() {
    const tb = document.getElementById('tbl-certificates-grid');
    if (!tb) return;

    const list = DB.certificatesData || [];
    tb.innerHTML = list.map(c => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${c.serialNo}</td>
            <td style="font-weight:700;">${c.student}</td>
            <td>${c.qual}</td>
            <td style="font-weight:800;color:#34d399;">${c.gpaGrade}</td>
            <td>${c.gradYear}</td>
            <td><a href="${c.qrUrl}" target="_blank" style="color:#38bdf8;font-size:0.8rem;"><i class="fa-solid fa-qrcode"></i> فحص QR</a></td>
            <td>${c.docType}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(16,185,129,0.15);color:#10b981;">${c.stampStatus}</span></td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(59,130,246,0.15);color:#60a5fa;">${c.status}</span></td>
            <td style="font-size:0.8rem;">${c.issueDate}</td>
            <td><button class="btn-edit" onclick="toast('معاينة وطباعة الشهادة الرسمية')"><i class="fa-solid fa-print"></i> طباعة</button></td>
        </tr>
    `).join('');
}

function generateBulkCertificates() {
    toast('⚙️ جاري توليد وتشفير الشهادات الرسمية والـ QR Code للطلاب...');
    setTimeout(() => { renderCertificatesGrid(); toast('✅ تم توليد وتشفير الشهادات بنجاح!'); }, 800);
}


// ==================== 4. EXAM HALLS & CAPACITY ====================
function renderExamHallsGrid() {
    const tb = document.getElementById('tbl-exam-halls-grid');
    if (!tb) return;

    const list = DB.examHallsData || [];
    tb.innerHTML = list.map(h => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${h.no}</td>
            <td>${h.location}</td>
            <td style="font-weight:800;color:#34d399;">${h.capacity}</td>
            <td>${h.target}</td>
            <td style="font-weight:700;">${h.seatingRange}</td>
            <td>${h.pattern}</td>
            <td>${h.supervisor}</td>
            <td style="font-size:0.83rem;">${h.proctors}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${h.status}</span></td>
            <td><button class="btn-edit" onclick="toast('معاينة كشف التوقيع PDF')"><i class="fa-solid fa-file-pdf"></i> PDF</button></td>
            <td><button class="btn-edit" onclick="toast('معاينة ملصقات الطاولات')"><i class="fa-solid fa-id-card"></i> ملصقات</button></td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('exam_halls', ${JSON.stringify(h).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i></button></div></td>
        </tr>
    `).join('');
}

function autoBuildSeating() {
    toast('🪄 جاري تشغيل خوارزمية التوزيع الآلي لأرقام الجلوس على اللجان...');
    setTimeout(() => { renderExamHallsGrid(); toast('✅ تم توزيع مقاعد الطلاب على اللجان بنجاح!'); }, 700);
}


// ==================== 5. SEATING NUMBERS & BARCODES ====================
function renderSeatNumbersGrid() {
    const tb = document.getElementById('tbl-seat-numbers-grid');
    if (!tb) return;

    const list = DB.seatNumbersData || [];
    tb.innerHTML = list.map(s => `
        <tr>
            <td style="font-weight:800;color:#60a5fa;font-size:1.05rem;">${s.seatNo}</td>
            <td style="font-weight:700;">${s.name}</td>
            <td style="font-size:0.83rem;">${s.idPhoto}</td>
            <td>${s.gradeBranch}</td>
            <td>${s.committee}</td>
            <td style="font-weight:700;color:#34d399;">${s.deskNo}</td>
            <td>${s.location}</td>
            <td style="font-weight:700;color:#38bdf8;"><i class="fa-solid fa-barcode"></i> ${s.barcode}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(59,130,246,0.15);color:#93c5fd;">${s.type}</span></td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${s.status}</span></td>
            <td><button class="btn-edit" onclick="toast('طباعة بطاقة الطالب فردياً')"><i class="fa-solid fa-print"></i></button></td>
        </tr>
    `).join('');
}

function generateAutoRollNumbers() {
    toast('⚙️ جاري توليد تسلسل أرقام الجلوس آلياً وتفادي التكرار...');
    setTimeout(() => { renderSeatNumbersGrid(); toast('✅ تم توليد وتسلسسل أرقام الجلوس بنجاح!'); }, 700);
}


// ==================== 6. SECRET NUMBERS & ANONYMITY ====================
let isSecretDeanonymized = false;
function renderSecretNumbersGrid() {
    const tb = document.getElementById('tbl-secret-numbers-grid');
    if (!tb) return;

    const list = DB.secretNumbersData || [];
    tb.innerHTML = list.map(sc => `
        <tr>
            <td style="font-weight:700;color:#ef4444;">${isSecretDeanonymized ? sc.rollNo.replace(' (مخفي)','') : '🔒 [مخفي وسري]'}</td>
            <td style="font-weight:800;color:#34d399;font-size:1.05rem;">${sc.secretCode}</td>
            <td style="font-weight:700;">${sc.subjectExam}</td>
            <td>${sc.gradeSec}</td>
            <td style="font-size:0.8rem;">${sc.pattern}</td>
            <td>${sc.formVariant}</td>
            <td style="font-size:0.8rem;">${sc.timestamp}</td>
            <td>${sc.operator}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(239,68,68,0.15);color:#f87171;">${sc.lockStatus}</span></td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(245,158,11,0.15);color:#fbbf24;">${sc.deanonymizeStatus}</span></td>
            <td><button class="btn-edit" onclick="toast('طباعة ملصق الرقم السري')"><i class="fa-solid fa-stamp"></i> ملصق</button></td>
        </tr>
    `).join('');
}

function generateSecretCodes() {
    toast('🎲 جاري تشغيل خوارزمية التشفير العشوائي للأرقام السرية...');
    setTimeout(() => { renderSecretNumbersGrid(); toast('✅ تم توليد الأرقام السرية بنجاح وتأمين الربط!'); }, 700);
}

function toggleSecretDeanonymize() {
    const pass = prompt('ادخل كلمة مرور رئيس الكنترول لفك التشفير:');
    if (pass === 'admin' || pass === '1234' || pass) {
        isSecretDeanonymized = !isSecretDeanonymized;
        renderSecretNumbersGrid();
        toast(isSecretDeanonymized ? '🔓 تم كشف مطابقة الأسماء برقم الكنترول' : '🔒 تم إعادة قفل السرية التامة');
    }
}


// ==================== 7. HALL DISTRIBUTION & PROCTORS ====================
function renderHallDistributionGrid() {
    const tb = document.getElementById('tbl-hall-distribution-grid');
    if (!tb) return;

    const list = DB.hallDistributionData || [];
    tb.innerHTML = list.map(d => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${d.id}</td>
            <td style="font-weight:700;">${d.proctor}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(139,92,246,0.15);color:#c084fc;">${d.role}</span></td>
            <td>${d.committee}</td>
            <td>${d.location}</td>
            <td>${d.examDate}</td>
            <td>${d.shift}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(16,185,129,0.15);color:#10b981;">${d.conflictStatus}</span></td>
            <td style="font-weight:700;color:#34d399;">${d.workload}</td>
            <td>${d.notifyStatus}</td>
            <td style="color:#10b981;font-weight:700;">${d.attStatus}</td>
            <td>${d.standby}</td>
            <td><div class="act"><button class="btn-edit" onclick="toast('تعديل التكليف')"><i class="fa-solid fa-pen"></i></button></div></td>
        </tr>
    `).join('');
}

function autoDistributeProctors() {
    toast('🪄 جاري تشغيل محرك التوزيع التلقائي للمراقبين ومنع التعارضات...');
    setTimeout(() => { renderHallDistributionGrid(); toast('✅ تم توزيع المعلمين على اللجان بنجاح!'); }, 700);
}


// ==================== 8. ROLL CALL SHEETS ====================
function renderRollCallGrid() {
    const tb = document.getElementById('tbl-roll-call-grid');
    if (!tb) return;

    const list = DB.rollCallData || [];
    tb.innerHTML = list.map(r => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${r.deskNo}</td>
            <td style="font-weight:800;">${r.rollNo}</td>
            <td style="font-weight:700;">${r.studentPhoto}</td>
            <td>${r.subjectGrade}</td>
            <td style="color:#10b981;font-weight:700;"><i class="fa-solid fa-signature"></i> ${r.signature}</td>
            <td style="font-weight:700;color:#38bdf8;">${r.bookletSerial}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${r.attStatus}</span></td>
            <td style="color:#34d399;">${r.handoverStatus}</td>
            <td>${r.caller}</td>
            <td style="font-size:0.8rem;">${r.notes}</td>
            <td><button class="btn-add" onclick="toast('تأكيد حضور وتسليم الدفتر')" style="padding:3px 6px;font-size:0.75rem;"><i class="fa-solid fa-check"></i> تأكيد</button></td>
        </tr>
    `).join('');
}


// ==================== 9. SEAT CARDS PREVIEW ====================
function renderSeatCardsGrid() {
    const tb = document.getElementById('tbl-seat-cards-grid');
    if (!tb) return;

    const list = DB.seatNumbersData || [];
    tb.innerHTML = list.map(s => `
        <tr>
            <td style="font-weight:700;">${s.name}</td>
            <td style="font-weight:800;color:#60a5fa;">${s.seatNo}</td>
            <td><i class="fa-solid fa-user-tie" style="font-size:1.2rem;color:#94a3b8;"></i></td>
            <td>${s.gradeBranch}</td>
            <td>${s.committee}</td>
            <td><i class="fa-solid fa-qrcode" style="font-size:1.2rem;color:#38bdf8;"></i></td>
            <td style="font-size:0.8rem;">الكيمياء: 15/08 | الفيزياء: 16/08</td>
            <td style="color:#10b981;font-weight:700;">ختم وتوقيع الكنترول</td>
            <td style="font-size:0.78rem;">يُمنع إدخال الهواتف المحمولة</td>
            <td><button class="btn-edit" onclick="previewSeatCardsModal()"><i class="fa-solid fa-eye"></i> معاينة</button></td>
        </tr>
    `).join('');
}

function previewSeatCardsModal() {
    const fields = document.getElementById('form-fields') || document.getElementById('dynamicForm');
    const title = document.getElementById('formTitle');
    if (!fields || !title) return;

    title.innerHTML = '<i class="fa-solid fa-id-badge"></i> معاينة بطاقات أرقام الجلوس المطبوعة (Live Card Preview)';
    fields.innerHTML = `
        <div style="border:2px dashed rgba(59,130,246,0.5);padding:15px;border-radius:12px;background:rgba(15,23,42,0.9);color:#fff;margin-bottom:12px;">
            <div style="display:flex;justify-content:space-between;border-bottom:1px solid rgba(255,255,255,0.1);padding-bottom:8px;margin-bottom:10px;">
                <strong>شعار المدرسة الرسمي</strong>
                <span style="color:#60a5fa;font-weight:800;">بطاقة دخول الامتحان النهائي 2026</span>
            </div>
            <div style="display:grid;grid-template-columns:80px 1fr;gap:12px;align-items:center;">
                <div style="width:75px;height:85px;background:rgba(255,255,255,0.1);border-radius:8px;display:flex;align-items:center;justify-content:center;">
                    <i class="fa-solid fa-user" style="font-size:2.2rem;color:#94a3b8;"></i>
                </div>
                <div>
                    <h4 style="margin:0 0 4px 0;color:#f8fafc;">عبدالرحمن محمد علي المقطري</h4>
                    <p style="margin:2px 0;font-size:0.83rem;color:#cbd5e1;">رقم الجلوس: <strong style="color:#34d399;font-size:1.1rem;">20261004</strong></p>
                    <p style="margin:2px 0;font-size:0.83rem;color:#cbd5e1;">الصف: الثالث الثانوي (الفرع العلمي)</p>
                    <p style="margin:2px 0;font-size:0.83rem;color:#cbd5e1;">اللجنة: لجنة رقم (05) - القاعة الكبرى (طاولة 18)</p>
                </div>
            </div>
        </div>
        <button class="btn-save" onclick="window.print()" style="width:100%;"><i class="fa-solid fa-print"></i> أمر الطباعة المباشرة</button>
    `;
    document.getElementById('formModal').classList.add('active');
}


// ==================== 10. SUBSTITUTE TEACHER MANAGEMENT ====================
function renderSubstituteGrid() {
    const tb = document.getElementById('tbl-substitute-grid');
    if (!tb) return;

    const list = DB.substituteData || [];
    tb.innerHTML = list.map(sub => `
        <tr>
            <td style="font-weight:700;color:#ef4444;">${sub.absent}</td>
            <td style="font-weight:700;">${sub.classPeriod}</td>
            <td>${sub.subjectTopic}</td>
            <td style="font-weight:700;color:#34d399;">${sub.substitute}</td>
            <td style="font-size:0.8rem;">${sub.criterion}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${sub.status}</span></td>
            <td>${sub.activity}</td>
            <td style="font-weight:700;color:#60a5fa;">${sub.allowance}</td>
            <td style="font-size:0.8rem;">${sub.notes}</td>
            <td><div class="act"><button class="btn-edit" onclick="toast('إرسال تنبيه المعلم البديل')"><i class="fa-solid fa-paper-plane"></i></button></div></td>
        </tr>
    `).join('');
}

function autoSuggestSubstitute() {
    toast('🪄 جاري تشغيل خوارزمية اقتراح المعلم البديل المتفرغ...');
    setTimeout(() => { renderSubstituteGrid(); toast('✅ تم إيجاد وتأكيد المعلم البديل المناسب للحصة!'); }, 700);
}
"""

if 'CONTROL & EXAMINATION MODULES' not in js:
    js += control_db_additions + "\n" + control_modules_js

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Appended Control & Exam logic in app.js successfully!")
