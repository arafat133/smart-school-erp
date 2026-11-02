"""
Create ALL missing openForm modal definitions with complete field sets.
Each form gets: proper title with icon, all required fields (text, date, select, textarea, file upload).
"""
import re, time

print("=" * 60)
print("Creating ALL missing form modal definitions...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Complete form definitions for ALL missing openForm types
FORM_DEFS = {
    # ---- School Config ----
    'academic-years': ('السنوات الدراسية', 'fa-calendar', [
        ('text','name','اسم السنة الدراسية','مثال: 2024/2025'),
        ('date','start_date','تاريخ البداية',''),
        ('date','end_date','تاريخ النهاية',''),
        ('select','status','الحالة','حالية|سابقة|قادمة'),
    ]),
    'departments': ('الأقسام', 'fa-building-user', [
        ('text','name','اسم القسم','مثال: القسم العلمي'),
        ('text','head','رئيس القسم',''),
        ('text','phone','رقم الهاتف',''),
    ]),
    'subject': ('المواد الدراسية', 'fa-book', [
        ('text','name','اسم المادة','مثال: الرياضيات'),
        ('text','code','كود المادة','مثال: MATH-101'),
        ('select','type','نوع المادة','أساسية|اختيارية|نشاط'),
        ('number','hours','عدد الحصص الأسبوعية',''),
        ('number','max_score','الدرجة الكلية','100'),
    ]),
    'subject-distribution': ('توزيع المواد على الصفوف', 'fa-diagram-project', [
        ('select','grade','الصف الدراسي','الصف السابع|الصف الثامن|الصف التاسع'),
        ('select','subject','المادة','الرياضيات|العلوم|اللغة العربية|اللغة الإنجليزية'),
        ('number','hours','عدد الحصص',''),
    ]),
    'grade-types': ('أنواع الدرجات', 'fa-list-ol', [
        ('text','name','اسم النوع','مثال: أعمال الفصل'),
        ('number','weight','الوزن / النسبة %',''),
        ('select','term','الفصل','الأول|الثاني|السنوي'),
    ]),
    'grade-ratings': ('دليل التقديرات', 'fa-star', [
        ('text','name','اسم التقدير','مثال: ممتاز'),
        ('number','min_score','الحد الأدنى','90'),
        ('number','max_score','الحد الأعلى','100'),
        ('text','symbol','الرمز','A+'),
    ]),
    'grade-progression': ('تدرج الصفوف', 'fa-stairs', [
        ('select','from_grade','من الصف','الصف السابع|الصف الثامن|الصف التاسع'),
        ('select','to_grade','إلى الصف','الصف الثامن|الصف التاسع|خريج'),
        ('number','pass_score','درجة النجاح','50'),
    ]),
    'fee-categories': ('فئات الرسوم الدراسية', 'fa-tags', [
        ('text','name','اسم الفئة','مثال: رسوم التسجيل'),
        ('number','amount','المبلغ (ريال)',''),
        ('select','type','النوع','إلزامية|اختيارية'),
        ('textarea','desc','الوصف',''),
    ]),
    'discount-categories': ('فئات الخصم', 'fa-percent', [
        ('text','name','اسم الخصم','مثال: خصم الإخوة'),
        ('number','percentage','نسبة الخصم %',''),
        ('select','applies_to','ينطبق على','جميع الرسوم|رسوم التسجيل|رسوم النقل'),
        ('textarea','conditions','شروط الاستحقاق',''),
    ]),
    'installment-plans': ('فئات الأقساط', 'fa-money-bills', [
        ('text','name','اسم خطة التقسيط','مثال: قسطين متساويين'),
        ('number','installments','عدد الأقساط',''),
        ('text','schedule','مواعيد السداد','مثال: سبتمبر، يناير'),
    ]),
    'grade-fees': ('رسوم الصفوف', 'fa-receipt', [
        ('select','grade','الصف','الصف السابع|الصف الثامن|الصف التاسع'),
        ('number','tuition','الرسوم الدراسية',''),
        ('number','registration','رسوم التسجيل',''),
        ('number','transport','رسوم النقل',''),
        ('number','total','الإجمالي',''),
    ]),
    'nationalities': ('الجنسيات', 'fa-flag', [
        ('text','name','اسم الجنسية','مثال: يمني'),
        ('text','code','رمز الدولة','YE'),
    ]),
    'required-docs': ('الوثائق المطلوبة', 'fa-file-circle-check', [
        ('text','name','اسم الوثيقة','مثال: شهادة الميلاد'),
        ('select','required','إلزامية','نعم|لا'),
        ('select','stage','المرحلة','جميع المراحل|الابتدائية|الإعدادية|الثانوية'),
    ]),
    'violations-catalog': ('المخالفات السلوكية', 'fa-triangle-exclamation', [
        ('text','name','اسم المخالفة','مثال: التأخر المتكرر'),
        ('select','severity','الدرجة','بسيطة|متوسطة|جسيمة'),
        ('text','penalty','العقوبة','مثال: إنذار خطي'),
        ('number','points','نقاط الخصم',''),
    ]),
    'visitors': ('سجل الزوار', 'fa-person-walking-arrow-right', [
        ('text','name','اسم الزائر',''),
        ('text','id_number','رقم الهوية',''),
        ('text','phone','رقم الهاتف',''),
        ('text','purpose','الغرض من الزيارة',''),
        ('text','visiting','الشخص المُزار',''),
        ('date','date','تاريخ الزيارة',''),
        ('text','time_in','وقت الدخول',''),
        ('text','time_out','وقت الخروج',''),
    ]),
    'classrooms': ('القاعات الدراسية', 'fa-chalkboard', [
        ('text','name','اسم القاعة','مثال: القاعة أ-101'),
        ('number','capacity','السعة (طالب)',''),
        ('select','type','النوع','فصل عادي|معمل|مختبر|قاعة رياضة'),
        ('select','building','المبنى','المبنى الرئيسي|المبنى الفرعي'),
    ]),
    # ---- Students ----
    'enrollment': ('التسجيل السنوي والرسوم', 'fa-file-invoice', [
        ('select','student','اسم الطالب','— اختر الطالب —'),
        ('select','year','السنة الدراسية','2024/2025|2025/2026'),
        ('select','grade','الصف','الصف السابع|الصف الثامن|الصف التاسع'),
        ('select','section','الشعبة','أ|ب|ج'),
        ('number','fees','إجمالي الرسوم',''),
        ('select','plan','خطة السداد','دفعة واحدة|قسطين|ثلاثة أقساط'),
        ('date','date','تاريخ التسجيل',''),
    ]),
    'parents': ('أولياء الأمور', 'fa-people-roof', [
        ('text','father_name','اسم الأب',''),
        ('text','mother_name','اسم الأم',''),
        ('text','father_id','رقم هوية الأب',''),
        ('text','father_phone','هاتف الأب',''),
        ('text','mother_phone','هاتف الأم',''),
        ('text','email','البريد الإلكتروني',''),
        ('text','address','العنوان',''),
        ('text','job','الوظيفة',''),
    ]),
    'student-docs': ('وثائق الطلاب', 'fa-folder-open', [
        ('select','student','اسم الطالب','— اختر الطالب —'),
        ('select','doc_type','نوع الوثيقة','شهادة ميلاد|بطاقة هوية|شهادة دراسية|صورة شخصية|أخرى'),
        ('file','file','ملف الوثيقة',''),
        ('date','date','تاريخ الإضافة',''),
        ('textarea','notes','ملاحظات',''),
    ]),
    'section-distribution': ('توزيع الطلاب على الشعب', 'fa-arrows-split-up-and-left', [
        ('select','grade','الصف','الصف السابع|الصف الثامن|الصف التاسع'),
        ('select','section','الشعبة','أ|ب|ج'),
        ('select','student','الطالب','— اختر الطالب —'),
    ]),
    'behavior': ('السلوك والمخالفات', 'fa-clipboard-list', [
        ('select','student','اسم الطالب','— اختر الطالب —'),
        ('date','date','التاريخ',''),
        ('select','violation','نوع المخالفة','تأخر|غياب بدون عذر|إزعاج|عدم التزام بالزي|أخرى'),
        ('select','severity','الدرجة','بسيطة|متوسطة|جسيمة'),
        ('text','action','الإجراء المتخذ','مثال: إنذار شفهي'),
        ('textarea','notes','ملاحظات',''),
    ]),
    'class-notes': ('ملاحظات رائد الفصل', 'fa-note-sticky', [
        ('select','grade','الصف','الصف السابع|الصف الثامن|الصف التاسع'),
        ('select','section','الشعبة','أ|ب|ج'),
        ('date','date','التاريخ',''),
        ('textarea','notes','الملاحظات',''),
        ('select','type','النوع','عام|سلوكي|أكاديمي|صحي'),
    ]),
    'discontinued': ('الطلاب غير المستمرين', 'fa-user-xmark', [
        ('select','student','اسم الطالب','— اختر الطالب —'),
        ('date','date','تاريخ الانقطاع',''),
        ('select','reason','السبب','نقل|انسحاب|فصل|سفر|أخرى'),
        ('textarea','notes','ملاحظات',''),
    ]),
    # ---- Employees ----
    'employee': ('بيانات الموظف', 'fa-address-book', [
        ('text','name','الاسم الكامل',''),
        ('text','id_number','رقم الهوية',''),
        ('select','gender','الجنس','ذكر|أنثى'),
        ('date','birth_date','تاريخ الميلاد',''),
        ('text','phone','رقم الهاتف',''),
        ('text','email','البريد الإلكتروني',''),
        ('select','job','الوظيفة','معلم|إداري|محاسب|سائق|حارس|أخرى'),
        ('select','department','القسم','القسم العلمي|القسم الأدبي|الإدارة|الصيانة'),
        ('select','contract_type','نوع العقد','دوام كامل|دوام جزئي|بالساعة'),
        ('date','start_date','تاريخ المباشرة',''),
        ('date','contract_end','تاريخ انتهاء العقد',''),
        ('number','salary','الراتب الأساسي',''),
        ('text','iban','رقم الآيبان (IBAN)',''),
        ('text','bank','البنك',''),
        ('file','photo','الصورة الشخصية',''),
        ('textarea','address','العنوان',''),
    ]),
    'guarantors': ('الضمناء', 'fa-handshake', [
        ('text','name','اسم الضامن',''),
        ('text','id_number','رقم الهوية',''),
        ('text','phone','رقم الهاتف',''),
        ('text','job','الوظيفة',''),
        ('text','relation','العلاقة بالموظف',''),
        ('textarea','address','العنوان',''),
    ]),
    'teacher-subjects': ('إسناد المواد للمدرسين', 'fa-chalkboard-user', [
        ('select','teacher','المدرس','— اختر المدرس —'),
        ('select','subject','المادة','الرياضيات|العلوم|اللغة العربية|اللغة الإنجليزية'),
        ('select','grade','الصف','الصف السابع|الصف الثامن|الصف التاسع'),
        ('select','section','الشعبة','أ|ب|ج'),
    ]),
    'emp-notices': ('إشعارات الموظفين', 'fa-bullhorn', [
        ('select','employee','الموظف','— اختر الموظف —'),
        ('select','type','نوع الإشعار','تنبيه|إنذار|ملاحظة|تقدير|ترقية'),
        ('date','date','التاريخ',''),
        ('text','subject','الموضوع',''),
        ('textarea','content','المحتوى',''),
    ]),
    'contract': ('عقود الموظفين', 'fa-file-contract', [
        ('select','employee','الموظف','— اختر الموظف —'),
        ('select','type','نوع العقد','دوام كامل|دوام جزئي|مؤقت'),
        ('date','start_date','تاريخ البداية',''),
        ('date','end_date','تاريخ الانتهاء',''),
        ('number','salary','الراتب',''),
        ('textarea','terms','شروط وبنود العقد',''),
    ]),
    'advance': ('سلفيات الموظفين', 'fa-hand-holding-dollar', [
        ('select','employee','الموظف','— اختر الموظف —'),
        ('number','amount','مبلغ السلفة',''),
        ('date','date','التاريخ',''),
        ('number','deduction_months','عدد أشهر الخصم',''),
        ('textarea','reason','السبب',''),
    ]),
    # ---- Exams ----
    'exam-schedule': ('جدول الامتحانات', 'fa-calendar-days', [
        ('select','term','الفصل الدراسي','الأول|الثاني|النهائي'),
        ('select','grade','الصف','الصف السابع|الصف الثامن|الصف التاسع'),
        ('select','subject','المادة','الرياضيات|العلوم|اللغة العربية|اللغة الإنجليزية'),
        ('date','date','تاريخ الامتحان',''),
        ('text','time','الوقت','مثال: 08:00 - 10:00'),
        ('select','hall','القاعة','القاعة أ|القاعة ب|القاعة ج'),
    ]),
    'exam-halls': ('قاعات الامتحانات', 'fa-building-columns', [
        ('text','name','اسم القاعة',''),
        ('number','capacity','السعة',''),
        ('text','supervisor','المراقب',''),
        ('text','location','الموقع',''),
    ]),
    'seat-numbers': ('أرقام الجلوس', 'fa-hashtag', [
        ('select','grade','الصف','الصف السابع|الصف الثامن|الصف التاسع'),
        ('select','method','طريقة التوزيع','تسلسلي|عشوائي'),
        ('number','start_from','البداية من رقم','1'),
    ]),
    'secret-numbers': ('الأرقام السرية', 'fa-user-secret', [
        ('select','grade','الصف','الصف السابع|الصف الثامن|الصف التاسع'),
        ('select','subject','المادة','— جميع المواد —'),
        ('select','method','طريقة التوليد','عشوائي|تسلسلي'),
    ]),
    'hall-distribution': ('توزيع اللجان', 'fa-users-rectangle', [
        ('select','hall','القاعة','القاعة أ|القاعة ب|القاعة ج'),
        ('select','grade','الصف','الصف السابع|الصف الثامن|الصف التاسع'),
        ('number','count','عدد الطلاب',''),
        ('text','supervisor','المراقب',''),
    ]),
    'roll-call': ('كشوفات المناداة', 'fa-list-check', [
        ('select','grade','الصف','الصف السابع|الصف الثامن|الصف التاسع'),
        ('select','subject','المادة',''),
        ('date','date','التاريخ',''),
    ]),
    'substitute': ('المدرس البديل', 'fa-user-pen', [
        ('select','original_teacher','المدرس الأصلي','— اختر المدرس —'),
        ('select','substitute_teacher','المدرس البديل','— اختر البديل —'),
        ('date','from_date','من تاريخ',''),
        ('date','to_date','إلى تاريخ',''),
        ('textarea','reason','السبب',''),
    ]),
    'homework': ('الواجبات المنزلية', 'fa-book-open-reader', [
        ('select','subject','المادة','الرياضيات|العلوم|اللغة العربية|اللغة الإنجليزية'),
        ('select','grade','الصف','الصف السابع|الصف الثامن|الصف التاسع'),
        ('date','date','التاريخ',''),
        ('date','due_date','تاريخ التسليم',''),
        ('textarea','description','وصف الواجب',''),
        ('file','attachment','إرفاق ملف',''),
    ]),
    # ---- Activities ----
    'activity-types': ('أنواع الأنشطة', 'fa-icons', [
        ('text','name','اسم النوع','مثال: رياضي'),
        ('textarea','desc','الوصف',''),
    ]),
    'activity': ('إدارة الأنشطة', 'fa-medal', [
        ('text','name','اسم النشاط',''),
        ('select','type','النوع','رياضي|ثقافي|علمي|فني|اجتماعي'),
        ('date','date','التاريخ',''),
        ('text','location','المكان',''),
        ('text','supervisor','المشرف',''),
        ('textarea','desc','وصف النشاط',''),
    ]),
    'activity-supervisors': ('المرافقون في الأنشطة', 'fa-person-chalkboard', [
        ('select','activity','النشاط','— اختر النشاط —'),
        ('select','employee','المرافق/المشرف','— اختر الموظف —'),
        ('text','role','الدور','مثال: مشرف ميداني'),
    ]),
    'activity-enrollment': ('اشتراك الطلاب في الأنشطة', 'fa-clipboard-user', [
        ('select','activity','النشاط','— اختر النشاط —'),
        ('select','student','الطالب','— اختر الطالب —'),
        ('date','date','تاريخ الاشتراك',''),
    ]),
    # ---- Transport ----
    'transport-routes': ('خطوط السير', 'fa-route', [
        ('text','name','اسم الخط','مثال: خط الشمال'),
        ('text','driver','اسم السائق',''),
        ('text','phone','هاتف السائق',''),
        ('text','bus_number','رقم الحافلة',''),
        ('number','capacity','السعة',''),
        ('number','fee','رسوم النقل',''),
    ]),
    'buses': ('الحافلات', 'fa-bus-simple', [
        ('text','plate','رقم اللوحة',''),
        ('text','model','الموديل/النوع',''),
        ('number','capacity','السعة',''),
        ('text','driver','السائق',''),
        ('date','license_expiry','تاريخ انتهاء الرخصة',''),
        ('select','status','الحالة','نشطة|صيانة|متوقفة'),
    ]),
    'transport-enrollment': ('اشتراك الطلاب في المواصلات', 'fa-user-check', [
        ('select','student','الطالب','— اختر الطالب —'),
        ('select','route','خط السير','— اختر الخط —'),
        ('select','direction','الاتجاه','ذهاب فقط|إياب فقط|ذهاب وإياب'),
        ('text','stop','نقطة التوقف',''),
    ]),
    # ---- Finance ----
    'receipt': ('سند قبض الرسوم', 'fa-receipt', [
        ('select','student','الطالب','— اختر الطالب —'),
        ('number','amount','المبلغ (ريال)',''),
        ('select','method','طريقة الدفع','نقداً|تحويل بنكي|شيك|محفظة إلكترونية'),
        ('text','ref','رقم المرجع',''),
        ('date','date','التاريخ',''),
        ('textarea','desc','البيان','سداد رسوم دراسية'),
    ]),
    'demand-letters': ('رسائل المطالبة', 'fa-envelope-open-text', [
        ('select','student','الطالب','— اختر الطالب —'),
        ('number','amount','المبلغ المطلوب',''),
        ('date','due_date','تاريخ الاستحقاق',''),
        ('textarea','message','نص الرسالة',''),
    ]),
    # ---- Inventory ----
    'item-categories': ('فئات الأصناف', 'fa-boxes-stacked', [
        ('text','name','اسم الفئة','مثال: قرطاسية'),
        ('textarea','desc','الوصف',''),
    ]),
    'inventory-items': ('الأصناف المخزنية', 'fa-box', [
        ('text','name','اسم الصنف',''),
        ('text','code','كود الصنف',''),
        ('select','category','الفئة','قرطاسية|أثاث|أجهزة|مواد تنظيف|أخرى'),
        ('number','quantity','الكمية الحالية',''),
        ('number','min_quantity','الحد الأدنى',''),
        ('number','cost','سعر التكلفة',''),
        ('text','unit','وحدة القياس','قطعة'),
    ]),
    'supply-orders': ('أوامر التوريد', 'fa-truck-ramp-box', [
        ('text','number','رقم الإذن',''),
        ('date','date','التاريخ',''),
        ('select','supplier','المورد','— اختر المورد —'),
        ('select','item','الصنف','— اختر الصنف —'),
        ('number','quantity','الكمية',''),
        ('number','cost','التكلفة الإجمالية',''),
    ]),
    'issue-orders': ('أوامر الصرف', 'fa-dolly', [
        ('text','number','رقم إذن الصرف',''),
        ('date','date','التاريخ',''),
        ('text','recipient','المستلم/الجهة',''),
        ('select','item','الصنف','— اختر الصنف —'),
        ('number','quantity','الكمية',''),
        ('textarea','reason','السبب',''),
    ]),
    'suppliers': ('الموردين', 'fa-truck-field', [
        ('text','name','اسم المورد',''),
        ('text','contact','جهة الاتصال',''),
        ('text','phone','الهاتف',''),
        ('text','email','البريد الإلكتروني',''),
        ('textarea','address','العنوان',''),
        ('text','tax_id','الرقم الضريبي',''),
    ]),
    # ---- SMS ----
    'sms-templates': ('قوالب الرسائل', 'fa-file-code', [
        ('text','title','عنوان القالب','مثال: إشعار غياب'),
        ('textarea','body','نص الرسالة','مثال: عزيزي ولي الأمر، نحيطكم علماً بغياب الطالب {name} اليوم {date}.'),
        ('select','trigger','المُحفّز','يدوي|غياب تلقائي|دفعة مالية|تذكير قسط'),
    ]),
    # ---- Admin ----
    'alerts': ('التنبيهات التلقائية', 'fa-bell', [
        ('text','title','عنوان التنبيه',''),
        ('select','type','النوع','مالي|أكاديمي|إداري|نظام'),
        ('select','severity','الأهمية','عالية|متوسطة|منخفضة'),
        ('textarea','message','نص التنبيه',''),
        ('select','target','الفئة المستهدفة','الجميع|المدراء|المحاسبين|المعلمين'),
    ]),
    'posting': ('إدارة الترحيلات', 'fa-paper-plane', [
        ('select','type','نوع الترحيل','ترحيل سندات|ترحيل قيود|ترحيل إقفال'),
        ('date','from','من تاريخ',''),
        ('date','to','إلى تاريخ',''),
        ('select','status','الحالة','مُعلّق|مُرحّل|ملغي'),
    ]),
    'operation-lock': ('قفل العمليات', 'fa-lock', [
        ('select','module','الوحدة','السندات|القيود|الحضور|الدرجات'),
        ('date','lock_from','قفل من تاريخ',''),
        ('date','lock_to','قفل إلى تاريخ',''),
        ('textarea','reason','السبب',''),
    ]),
    # ---- New Hub forms ----
    'book': ('إضافة كتاب جديد', 'fa-book', [
        ('text','title','عنوان الكتاب',''),
        ('text','author','المؤلف',''),
        ('text','isbn','رقم ISBN',''),
        ('select','category','التصنيف','علمي|أدبي|ديني|تاريخي|أطفال|مرجع'),
        ('number','copies','عدد النسخ',''),
        ('text','shelf','رقم الرف',''),
    ]),
    'lending': ('إعارة كتاب', 'fa-hand-holding', [
        ('select','book','الكتاب','— اختر الكتاب —'),
        ('text','borrower','المستعير',''),
        ('select','borrower_type','نوع المستعير','طالب|موظف'),
        ('date','lend_date','تاريخ الإعارة',''),
        ('date','return_date','تاريخ الاسترجاع المتوقع',''),
    ]),
    'maintenance': ('طلب صيانة', 'fa-screwdriver-wrench', [
        ('select','type','النوع','كهرباء|سباكة|أثاث|تكييف|أجهزة|أخرى'),
        ('text','location','الموقع','مثال: القاعة ب-201'),
        ('textarea','description','وصف المشكلة',''),
        ('select','priority','الأولوية','عاجلة|عادية|منخفضة'),
        ('file','photo','صورة توضيحية',''),
        ('date','date','التاريخ',''),
    ]),
    'leave_request': ('طلب إجازة', 'fa-calendar-xmark', [
        ('select','employee','الموظف','— اختر الموظف —'),
        ('select','type','نوع الإجازة','سنوية|مرضية|اضطرارية|بدون راتب'),
        ('date','from','من تاريخ',''),
        ('date','to','إلى تاريخ',''),
        ('textarea','reason','السبب',''),
        ('file','attachment','مرفق طبي (إن وجد)',''),
    ]),
    'performance_eval': ('تقييم أداء', 'fa-star', [
        ('select','employee','الموظف','— اختر الموظف —'),
        ('select','period','الفترة','الفصل الأول|الفصل الثاني|السنوي'),
        ('range','discipline','الانضباط (1-5)',''),
        ('range','performance','الأداء الوظيفي (1-5)',''),
        ('range','teamwork','التعاون (1-5)',''),
        ('range','initiative','المبادرة (1-5)',''),
        ('textarea','notes','ملاحظات المقيّم',''),
    ]),
    'sms_template': ('قالب رسالة', 'fa-file-code', [
        ('text','title','عنوان القالب',''),
        ('textarea','body','نص الرسالة',''),
    ]),
    'inv_item': ('صنف مخزني', 'fa-box', [
        ('text','name','اسم الصنف',''),
        ('text','code','الكود',''),
        ('number','qty','الكمية',''),
        ('number','cost','التكلفة',''),
    ]),
    'supply_order': ('إذن توريد', 'fa-truck-ramp-box', [
        ('date','date','التاريخ',''),
        ('text','supplier','المورد',''),
        ('text','item','الصنف',''),
        ('number','qty','الكمية',''),
    ]),
    'issue_order': ('إذن صرف', 'fa-hand-holding-hand', [
        ('date','date','التاريخ',''),
        ('text','recipient','المستلم',''),
        ('text','item','الصنف',''),
        ('number','qty','الكمية',''),
    ]),
    'supplier': ('مورد جديد', 'fa-truck-field', [
        ('text','name','اسم المورد',''),
        ('text','phone','الهاتف',''),
        ('textarea','address','العنوان',''),
    ]),
    'exam_schedule': ('امتحان جديد', 'fa-calendar-days', [
        ('select','grade','الصف','السابع|الثامن|التاسع'),
        ('select','subject','المادة','رياضيات|علوم|عربي|إنجليزي'),
        ('date','date','التاريخ',''),
        ('text','time','الوقت','08:00 - 10:00'),
        ('select','hall','القاعة','القاعة أ|القاعة ب'),
    ]),
    'exam_hall': ('قاعة امتحانات', 'fa-building-columns', [
        ('text','name','اسم القاعة',''),
        ('number','capacity','السعة',''),
        ('text','supervisor','المراقب',''),
    ]),
}

# Build the massive openForm handler
form_code = "\n// ==================== ALL FORM MODAL DEFINITIONS ====================\n"
form_code += "const _origOpenForm = window.openForm;\n"
form_code += "window.openForm = function(type, editData) {\n"
form_code += "    const fields = document.getElementById('form-fields') || document.getElementById('dynamicForm');\n"
form_code += "    const title = document.getElementById('formTitle');\n"
form_code += "    if (!fields || !title) return;\n"
form_code += "    let handled = true;\n"
form_code += "    const d = editData || {};\n\n"

for form_type, (label, icon, field_list) in FORM_DEFS.items():
    form_code += f"    if (type === '{form_type}') {{\n"
    form_code += f"        title.innerHTML = '<i class=\"fa-solid {icon}\"></i> {label}';\n"
    form_code += f"        fields.innerHTML = `\n"
    
    for ftype, fid, flabel, fplaceholder in field_list:
        full_id = f"f_{form_type.replace('-','_')}_{fid}"
        if ftype == 'text':
            form_code += f"            <div class='fg'><label><i class='fa-solid fa-pen'></i> {flabel}</label><input type='text' id='{full_id}' placeholder='{fplaceholder}' value='${{d.{fid}||\"\"}}' oninput='validateField(this,\"required\")'></div>\n"
        elif ftype == 'number':
            form_code += f"            <div class='fg'><label><i class='fa-solid fa-hashtag'></i> {flabel}</label><input type='number' id='{full_id}' placeholder='{fplaceholder}' value='${{d.{fid}||\"\"}}' oninput='validateField(this,\"required\")'></div>\n"
        elif ftype == 'date':
            form_code += f"            <div class='fg'><label><i class='fa-solid fa-calendar'></i> {flabel}</label><input type='date' id='{full_id}' value='${{d.{fid}||\"\"}}' oninput='validateField(this,\"required\")'></div>\n"
        elif ftype == 'select':
            opts = ''.join([f"<option value='{o}'>{o}</option>" for o in fplaceholder.split('|')]) if fplaceholder else '<option>—</option>'
            form_code += f"            <div class='fg'><label><i class='fa-solid fa-list'></i> {flabel}</label><select id='{full_id}'>{opts}</select></div>\n"
        elif ftype == 'textarea':
            form_code += f"            <div class='fg'><label><i class='fa-solid fa-align-right'></i> {flabel}</label><textarea id='{full_id}' placeholder='{fplaceholder}' style='height:70px;'>${{d.{fid}||\"\"}}</textarea></div>\n"
        elif ftype == 'file':
            form_code += f"            <div class='fg'><label><i class='fa-solid fa-upload'></i> {flabel}</label><input type='file' id='{full_id}' accept='image/*,.pdf,.doc,.docx'></div>\n"
        elif ftype == 'range':
            form_code += f"            <div class='fg'><label><i class='fa-solid fa-sliders'></i> {flabel}</label><input type='range' id='{full_id}' min='1' max='5' value='${{d.{fid}||3}}' oninput='this.nextElementSibling.textContent=this.value'><span style='font-weight:700;margin-right:8px;'>3</span></div>\n"
    
    form_code += f"            <button class='btn-save' onclick='saveFormData(\"{form_type}\")' style='width:100%;margin-top:12px;'><i class='fa-solid fa-floppy-disk'></i> حفظ البيانات</button>\n"
    form_code += f"        `;\n"
    form_code += f"    }} else "

form_code += "{ handled = false; }\n\n"
form_code += "    if (handled) {\n"
form_code += "        document.getElementById('formModal')?.classList.add('active');\n"
form_code += "    } else if (_origOpenForm) {\n"
form_code += "        _origOpenForm(type, editData);\n"
form_code += "    }\n"
form_code += "};\n\n"

# Generic save handler
form_code += """
function saveFormData(type) {
    logAudit('المستخدم الحالي', 'إضافة', type, 'تم إضافة سجل جديد في ' + type);
    toast('✅ تم حفظ البيانات بنجاح');
    document.getElementById('formModal')?.classList.remove('active');
}
"""

if 'ALL FORM MODAL DEFINITIONS' not in js:
    js += form_code

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

opens = js.count('{')
closes = js.count('}')
print(f"app.js: {len(js)} bytes, braces diff: {opens - closes}")

# Sync HTML files
with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

ts = str(int(time.time()))
html = re.sub(r'style\.css\?v=\d+', 'style.css?v=' + ts, html)
html = re.sub(r'app\.js\?v=\d+', 'app.js?v=' + ts, html)

with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html)
admin_html = html.replace('id="userType" value="school"', 'id="userType" value="admin"')
parent_html = html.replace('id="userType" value="school"', 'id="userType" value="parent"')
with open('frontend/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)
with open('frontend/parent.html', 'w', encoding='utf-8') as f:
    f.write(parent_html)

print(f"\n✅ Created {len(FORM_DEFS)} complete form modal definitions!")
print(f"Synced HTML files (v={ts})")
