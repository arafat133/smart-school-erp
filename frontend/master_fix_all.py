import os
import re

# Comprehensive configuration for all modules in the school system
MODULES = {
    # 1. Financial & Accounting
    'currencies': {
        'title': 'دليل العملات وأسعار الصرف',
        'db_key': 'currencies',
        'headers': ['رمز العملة', 'اسم العملة', 'سعر الصرف (ريال)', 'الحالة', 'إجراءات'],
        'fields': [
            ('f_cur_code', 'رمز العملة (مثال: USD)', 'text'),
            ('f_cur_name', 'اسم العملة', 'text'),
            ('f_cur_rate', 'سعر الصرف مقابل الريال', 'number'),
            ('f_cur_status', 'الحالة', 'select', ['نشط', 'موقوف'])
        ]
    },
    'cost-centers': {
        'title': 'مراكز التكلفة',
        'db_key': 'cost_centers',
        'headers': ['رمز المركز', 'اسم مركز التكلفة', 'الميزانية المخصصة', 'الفرع/القسم', 'إجراءات'],
        'fields': [
            ('f_cc_code', 'رمز المركز', 'text'),
            ('f_cc_name', 'اسم مركز التكلفة', 'text'),
            ('f_cc_budget', 'الميزانية المخصصة (ريال)', 'number'),
            ('f_cc_dept', 'الفرع / القسم', 'text')
        ]
    },
    'account-ceiling': {
        'title': 'تسقيف الحسابات',
        'db_key': 'account_ceiling',
        'headers': ['اسم الحساب', 'الحد الأعلى (السقف)', 'نوع السقف', 'الملاحظات', 'إجراءات'],
        'fields': [
            ('f_ac_name', 'اسم الحساب', 'text'),
            ('f_ac_limit', 'الحد الأعلى للمبلغ (ريال)', 'number'),
            ('f_ac_type', 'نوع السقف', 'select', ['سقف مدين', 'سقف دائن', 'سقف سحب']),
            ('f_ac_notes', 'الملاحظات', 'text')
        ]
    },
    'cashbox-inventory': {
        'title': 'جرد الصناديق',
        'db_key': 'cashbox_inventory',
        'headers': ['الصندوق', 'تاريخ الجرد', 'الرصيد الدفتري', 'الرصيد الفعلي', 'الفارق', 'إجراءات'],
        'fields': [
            ('f_ci_box', 'الصندوق', 'text'),
            ('f_ci_date', 'تاريخ الجرد', 'date'),
            ('f_ci_book', 'الرصيد الدفتري', 'number'),
            ('f_ci_actual', 'الرصيد الفعلي', 'number')
        ]
    },
    'closings': {
        'title': 'الإقفالات المحاسبية',
        'db_key': 'closings',
        'headers': ['الفترة المالية', 'نوع الإقفال', 'تاريخ الإقفال', 'الحالة', 'إجراءات'],
        'fields': [
            ('f_clo_period', 'الفترة المالية', 'text'),
            ('f_clo_type', 'نوع الإقفال', 'select', ['إقفال شهري', 'إقفال سنوي', 'إقفال حسابات']),
            ('f_clo_date', 'تاريخ الإقفال', 'date'),
            ('f_clo_status', 'الحالة', 'select', ['مكتمـل', 'قيد الإجراء'])
        ]
    },
    'banks': {
        'title': 'دليل البنوك',
        'db_key': 'banks',
        'headers': ['اسم البنك', 'رقم الحساب / IBAN', 'الفرع', 'الرصيد الحالي', 'إجراءات'],
        'fields': [
            ('f_bnk_name', 'اسم البنك', 'text'),
            ('f_bnk_account', 'رقم الحساب / IBAN', 'text'),
            ('f_bnk_branch', 'الفرع', 'text'),
            ('f_bnk_balance', 'الرصيد الحالي (ريال)', 'number')
        ]
    },
    'checks': {
        'title': 'إدارة الشيكات',
        'db_key': 'checks',
        'headers': ['رقم الشيك', 'البنك', 'المستفيد / الساحب', 'المبلغ', 'تاريخ الاستحقاق', 'الحالة', 'إجراءات'],
        'fields': [
            ('f_chk_num', 'رقم الشيك', 'text'),
            ('f_chk_bank', 'البنك', 'text'),
            ('f_chk_payee', 'المستفيد / الساحب', 'text'),
            ('f_chk_amount', 'المبلغ', 'number'),
            ('f_chk_date', 'تاريخ الاستحقاق', 'date'),
            ('f_chk_status', 'الحالة', 'select', ['تحت الصرف', 'صُرف', 'مرتجع', 'ملغى'])
        ]
    },
    'fee-categories': {
        'title': 'فئات الرسوم الدراسية',
        'db_key': 'fee_categories',
        'headers': ['اسم الفئة / الرسم', 'المبلغ الافتراضي', 'الدورية', 'ملاحظات', 'إجراءات'],
        'fields': [
            ('f_fc_name', 'اسم فئة الرسم', 'text'),
            ('f_fc_amount', 'المبلغ الافتراضي (ريال)', 'number'),
            ('f_fc_period', 'الدورية', 'select', ['سنوي', 'فصلي', 'شهري', 'دفعة واحدة']),
            ('f_fc_notes', 'ملاحظات', 'text')
        ]
    },
    'discount-categories': {
        'title': 'فئات الخصومات',
        'db_key': 'discount_categories',
        'headers': ['اسم الخصم', 'نوع الخصم', 'النسبة / القيمة', 'السبب', 'إجراءات'],
        'fields': [
            ('f_dc_name', 'اسم الخصم', 'text'),
            ('f_dc_type', 'نوع الخصم', 'select', ['نسبة مئوية %', 'مبلغ ثابت']),
            ('f_dc_value', 'النسبة / القيمة', 'number'),
            ('f_dc_reason', 'سبب الخصم', 'text')
        ]
    },
    'installment-plans': {
        'title': 'خطط الأقساط',
        'db_key': 'installment_plans',
        'headers': ['اسم الخطة', 'عدد الأقساط', 'فترات الاستحقاق', 'ملاحظات', 'إجراءات'],
        'fields': [
            ('f_ip_name', 'اسم خطة الأقساط', 'text'),
            ('f_ip_count', 'عدد الأقساط', 'number'),
            ('f_ip_interval', 'فترة الاستحقاق', 'select', ['شهري', 'كل شهرين', 'كل 3 أشهر']),
            ('f_ip_notes', 'ملاحظات', 'text')
        ]
    },
    'grade-fees': {
        'title': 'رسوم الصفوف الدراسية',
        'db_key': 'grade_fees',
        'headers': ['الصف الدراسي', 'الرسوم الأساسية', 'رسوم الكتب', 'رسوم الأنشطة', 'إجراءات'],
        'fields': [
            ('f_gf_grade', 'الصف الدراسي', 'text'),
            ('f_gf_base', 'الرسوم الأساسية (ريال)', 'number'),
            ('f_gf_books', 'رسوم الكتب (ريال)', 'number'),
            ('f_gf_act', 'رسوم الأنشطة (ريال)', 'number')
        ]
    },

    # 2. Administrative & Academic Setup
    'academic-years': {
        'title': 'دليل السنوات الدراسية',
        'db_key': 'academic_years',
        'headers': ['السنة الدراسية', 'تاريخ البداية', 'تاريخ النهاية', 'الحالة', 'إجراءات'],
        'fields': [
            ('f_ay_name', 'السنة الدراسية (مثال: 2025-2026)', 'text'),
            ('f_ay_start', 'تاريخ البداية', 'date'),
            ('f_ay_end', 'تاريخ النهاية', 'date'),
            ('f_ay_status', 'الحالة', 'select', ['الحالية', 'مغلقة', 'قادمة'])
        ]
    },
    'departments': {
        'title': 'دليل الأقسام الإدارية',
        'db_key': 'departments',
        'headers': ['اسم القسم', 'رئيس القسم', 'الموقع / المبنى', 'ملاحظات', 'إجراءات'],
        'fields': [
            ('f_dep_name', 'اسم القسم', 'text'),
            ('f_dep_head', 'رئيس القسم / المشرف', 'text'),
            ('f_dep_loc', 'الموقع / المبنى', 'text'),
            ('f_dep_notes', 'ملاحظات', 'text')
        ]
    },
    'classrooms': {
        'title': 'القاعات والدورات الدراسية',
        'db_key': 'classrooms',
        'headers': ['اسم القاعة / الفصل', 'المبنى / الدور', 'السعة الاستيعابية', 'نوع القاعة', 'إجراءات'],
        'fields': [
            ('f_clr_name', 'اسم القاعة / الفصل', 'text'),
            ('f_clr_bld', 'المبنى / الدور', 'text'),
            ('f_clr_cap', 'السعة الاستيعابية', 'number'),
            ('f_clr_type', 'نوع القاعة', 'select', ['فصل دراسي', 'معمل حاسوب', 'مختبر علوم', 'قاعة اجتماعات'])
        ]
    },
    'grade-progression': {
        'title': 'الترفيع والتتابع الدراسي',
        'db_key': 'grade_progression',
        'headers': ['من صف', 'إلى صف', 'شرط النجاح / الترفيع', 'ملاحظات', 'إجراءات'],
        'fields': [
            ('f_gp_from', 'من صف (الحالي)', 'text'),
            ('f_gp_to', 'إلى صف (التالي)', 'text'),
            ('f_gp_cond', 'شرط الترفيع', 'select', ['النجاح في كافة المواد', 'إكمال درجات الكنترول']),
            ('f_gp_notes', 'ملاحظات', 'text')
        ]
    },
    'subject-distribution': {
        'title': 'توزيع المواد والخطط',
        'db_key': 'subject_distribution',
        'headers': ['الصف الدراسي', 'اسم المادة', 'عدد الحصص الأسبوعية', 'المعلم المسؤول', 'إجراءات'],
        'fields': [
            ('f_sd_grade', 'الصف الدراسي', 'text'),
            ('f_sd_subject', 'اسم المادة', 'text'),
            ('f_sd_periods', 'عدد الحصص الأسبوعية', 'number'),
            ('f_sd_teacher', 'المعلم المسؤول', 'text')
        ]
    },
    'grade-types': {
        'title': 'أنواع الاختبارات والقياس',
        'db_key': 'grade_types',
        'headers': ['نوع الاختبار', 'الوزن / الدرجة العظمى', 'الفصل الدراسي', 'ملاحظات', 'إجراءات'],
        'fields': [
            ('f_gt_name', 'نوع الاختبار (مثال: محصلة شهرية)', 'text'),
            ('f_gt_max', 'الدرجة العظمى', 'number'),
            ('f_gt_term', 'الفصل الدراسي', 'select', ['الفصل الأول', 'الفصل الثاني', 'كلا الفصلين']),
            ('f_gt_notes', 'ملاحظات', 'text')
        ]
    },
    'grade-ratings': {
        'title': 'تقديرات الدرجات',
        'db_key': 'grade_ratings',
        'headers': ['التقدير (الرمز)', 'الحد الأدنى للنسبة %', 'الحد الأعلى %', 'الوصف', 'إجراءات'],
        'fields': [
            ('f_gr_name', 'التقدير (مثال: ممتاز، جيد جداً)', 'text'),
            ('f_gr_min', 'الحد الأدنى للنسبة %', 'number'),
            ('f_gr_max', 'الحد الأعلى للنسبة %', 'number'),
            ('f_gr_desc', 'الوصف / ملاحظة', 'text')
        ]
    },
    'academic-calendar': {
        'title': 'التقويم الأكاديمي',
        'db_key': 'academic_calendar',
        'headers': ['الحدث / الفعالية', 'تاريخ البداية', 'تاريخ النهاية', 'الفئة المستهدفة', 'إجراءات'],
        'fields': [
            ('f_cal_title', 'اسم الفعالية / الحدث', 'text'),
            ('f_cal_start', 'تاريخ البداية', 'date'),
            ('f_cal_end', 'تاريخ النهاية', 'date'),
            ('f_cal_target', 'الفئة المستهدفة', 'select', ['الجميع', 'الطلاب', 'المعلمون', 'أولياء الأمور'])
        ]
    },
    'required-docs': {
        'title': 'الوثائق المطلوبة للتسجيل',
        'db_key': 'required_docs',
        'headers': ['اسم الوثيقة', 'الفئة المستهدفة', 'الإلزامية', 'ملاحظات', 'إجراءات'],
        'fields': [
            ('f_rd_name', 'اسم الوثيقة (مثال: شهادة الميلاد)', 'text'),
            ('f_rd_target', 'الفئة المستهدفة', 'select', ['الطلاب الجدد', 'الموظفون والمعلمون', 'الجميع']),
            ('f_rd_req', 'الإلزامية', 'select', ['إجباري', 'اختياري']),
            ('f_rd_notes', 'ملاحظات', 'text')
        ]
    },
    'nationalities': {
        'title': 'دليل الجنسيات',
        'db_key': 'nationalities',
        'headers': ['الجنسية', 'رمز الدولة', 'ملاحظات', 'إجراءات'],
        'fields': [
            ('f_nat_name', 'اسم الجنسية', 'text'),
            ('f_nat_code', 'رمز الدولة (مثال: YEM)', 'text'),
            ('f_nat_notes', 'ملاحظات', 'text')
        ]
    },
    'violations-catalog': {
        'title': 'لائحة المخالفات والجزاءات',
        'db_key': 'violations_catalog',
        'headers': ['نوع المخالفة', 'درجة المخالفة', 'العقوبة / الجزاء المترتب', 'ملاحظات', 'إجراءات'],
        'fields': [
            ('f_vc_name', 'اسم المخالفة', 'text'),
            ('f_vc_degree', 'درجة المخالفة', 'select', ['بسيطة (درجة 1)', 'متوسطة (درجة 2)', 'جسيمة (درجة 3)']),
            ('f_vc_penalty', 'العقوبة / الجزاء', 'text'),
            ('f_vc_notes', 'ملاحظات', 'text')
        ]
    },
    'visitors': {
        'title': 'سجل الزوار',
        'db_key': 'visitors',
        'headers': ['اسم الزائر', 'سبب الزيارة', 'الشخص المطلوب', 'الهاتف', 'وقت الزيارة', 'إجراءات'],
        'fields': [
            ('f_vis_name', 'اسم الزائر الرباعي', 'text'),
            ('f_vis_reason', 'سبب الزيارة', 'text'),
            ('f_vis_target', 'الشخص المطلوب / القسم', 'text'),
            ('f_vis_phone', 'رقم الهاتف', 'text'),
            ('f_vis_date', 'التاريخ والوقت', 'date')
        ]
    },

    # 3. Student Affairs & Guidance
    'parents': {
        'title': 'دليل أولياء الأمور',
        'db_key': 'parents',
        'headers': ['اسم ولي الأمر', 'رقم الهوية', 'رقم الهاتف الرئيسي', 'صلة القرابة', 'المهنة', 'إجراءات'],
        'fields': [
            ('f_par_name', 'اسم ولي الأمر الكامل', 'text'),
            ('f_par_nid', 'رقم الهوية / الوطنية', 'text'),
            ('f_par_phone', 'رقم الهاتف الرئيسي', 'text'),
            ('f_par_rel', 'صلة القرابة', 'select', ['أب', 'أم', 'أخ/عم/كفيل']),
            ('f_par_job', 'المهنة / جهة العمل', 'text')
        ]
    },
    'student-docs': {
        'title': 'وثائق وملفات الطلاب',
        'db_key': 'student_docs',
        'headers': ['اسم الطالب', 'نوع الوثيقة', 'حالة الاستلام', 'ملاحظات', 'إجراءات'],
        'fields': [
            ('f_sd_student', 'اسم الطالب', 'text'),
            ('f_sd_doc', 'نوع الوثيقة', 'text'),
            ('f_sd_status', 'حالة الاستلام', 'select', ['مستلمة وموثقة', 'ناقصة', 'تحت المراجعة']),
            ('f_sd_notes', 'ملاحظات', 'text')
        ]
    },
    'section-distribution': {
        'title': 'توزيع الشعب والفصول',
        'db_key': 'section_distribution',
        'headers': ['الصف الدراسي', 'اسم الشعبة', 'عدد الطلاب', 'رائد الفصل', 'إجراءات'],
        'fields': [
            ('f_sec_grade', 'الصف الدراسي', 'text'),
            ('f_sec_name', 'اسم الشعبة (أ، ب، ج)', 'text'),
            ('f_sec_count', 'عدد الطلاب الحالي', 'number'),
            ('f_sec_leader', 'رائد الفصل / المربّي', 'text')
        ]
    },
    'discontinued': {
        'title': 'الطلاب المنقطعون والمغادرون',
        'db_key': 'discontinued',
        'headers': ['اسم الطالب', 'الصف الدراسي', 'سبب الانقطاع / المغادرة', 'تاريخ الانقطاع', 'إجراءات'],
        'fields': [
            ('f_disc_student', 'اسم الطالب', 'text'),
            ('f_disc_grade', 'الصف الدراسي', 'text'),
            ('f_disc_reason', 'سبب الانقطاع / المغادرة', 'text'),
            ('f_disc_date', 'تاريخ الانقطاع', 'date')
        ]
    },
    'behavior': {
        'title': 'السلوك والمواظبة',
        'db_key': 'behavior',
        'headers': ['اسم الطالب', 'نوع السلوك / الملاحظة', 'التاريخ', 'الإجراء المتخذ', 'إجراءات'],
        'fields': [
            ('f_beh_student', 'اسم الطالب', 'text'),
            ('f_beh_type', 'نوع الملاحظة', 'select', ['ملاحظة إيجابية / تميز', 'ملاحظة سلوكية / إشعار', 'مخالفة انضباطية']),
            ('f_beh_date', 'التاريخ', 'date'),
            ('f_beh_action', 'الإجراء المتخذ', 'text')
        ]
    },
    'class-notes': {
        'title': 'ملاحظات الفصل والمدرسين',
        'db_key': 'class_notes',
        'headers': ['الصف / الشعبة', 'المادة', 'المعلم', 'الملاحظة / التوجيه', 'التاريخ', 'إجراءات'],
        'fields': [
            ('f_cn_class', 'الصف والشعبة', 'text'),
            ('f_cn_subject', 'المادة', 'text'),
            ('f_cn_teacher', 'المعلم', 'text'),
            ('f_cn_note', 'الملاحظة / التوجيه', 'text'),
            ('f_cn_date', 'التاريخ', 'date')
        ]
    },
    'guarantors': {
        'title': 'الكفلاء الضامنون',
        'db_key': 'guarantors',
        'headers': ['اسم الكفيل الضامن', 'اسم الطالب المكفول', 'رقم الهاتف', 'رقم الهوية', 'إجراءات'],
        'fields': [
            ('f_gua_name', 'اسم الكفيل الكامل', 'text'),
            ('f_gua_student', 'اسم الطالب المكفول', 'text'),
            ('f_gua_phone', 'رقم الهاتف', 'text'),
            ('f_gua_nid', 'رقم الهوية الوطنية', 'text')
        ]
    },

    # 4. Control, Exams & Staff Setup
    'teacher-subjects': {
        'title': 'توزيع المعلمين على المواد',
        'db_key': 'teacher_subjects',
        'headers': ['اسم المعلم', 'المادة الدراسية', 'الصف والشعبة', 'نصاب الحصص', 'إجراءات'],
        'fields': [
            ('f_ts_teacher', 'اسم المعلم', 'text'),
            ('f_ts_subject', 'المادة الدراسية', 'text'),
            ('f_ts_class', 'الصف والشعبة', 'text'),
            ('f_ts_quota', 'نصاب الحصص الأسبوعية', 'number')
        ]
    },
    'emp-notices': {
        'title': 'إنذارات وإشعارات الموظفين',
        'db_key': 'emp_notices',
        'headers': ['اسم الموظف', 'نوع الإشعار / الإنذار', 'السبب / التوضيح', 'التاريخ', 'إجراءات'],
        'fields': [
            ('f_en_emp', 'اسم الموظف', 'text'),
            ('f_en_type', 'نوع الإشعار', 'select', ['تنبيه شفهي', 'إنذار كتابي أول', 'إنذار كتابي ثاني', 'شكر وتقدير']),
            ('f_en_reason', 'السبب / التوضيح', 'text'),
            ('f_en_date', 'التاريخ', 'date')
        ]
    },
    'exam-halls': {
        'title': 'قاعات الامتحانات',
        'db_key': 'exam_halls',
        'headers': ['اسم القاعة الامتحانية', 'المبنى / الدور', 'عدد المقاعد', 'المشرف المسؤول', 'إجراءات'],
        'fields': [
            ('f_eh_name', 'اسم القاعة الامتحانية', 'text'),
            ('f_eh_bld', 'المبنى / الدور', 'text'),
            ('f_eh_seats', 'عدد المقاعد الامتحانية', 'number'),
            ('f_eh_supervisor', 'المشرف المسؤول', 'text')
        ]
    },
    'seat-numbers': {
        'title': 'أرقام الجلوس',
        'db_key': 'seat_numbers',
        'headers': ['اسم الطالب', 'الصف الدراسي', 'رقم الجلوس', 'قاعة الامتحان', 'إجراءات'],
        'fields': [
            ('f_sn_student', 'اسم الطالب', 'text'),
            ('f_sn_grade', 'الصف الدراسي', 'text'),
            ('f_sn_num', 'رقم الجلوس', 'number'),
            ('f_sn_hall', 'قاعة الامتحان', 'text')
        ]
    },
    'secret-numbers': {
        'title': 'الأرقام السرية للكنترول',
        'db_key': 'secret_numbers',
        'headers': ['اسم الطالب', 'المادة', 'الرقم السري للكنترول', 'الصف الدراسي', 'إجراءات'],
        'fields': [
            ('f_sec_student', 'اسم الطالب', 'text'),
            ('f_sec_subject', 'المادة', 'text'),
            ('f_sec_code', 'الرقم السري', 'text'),
            ('f_sec_grade', 'الصف الدراسي', 'text')
        ]
    },
    'hall-distribution': {
        'title': 'توزيع الطلاب على القاعات',
        'db_key': 'hall_distribution',
        'headers': ['اسم الطالب', 'قاعة الامتحان', 'رقم المقعد', 'الفترة الامتحانية', 'إجراءات'],
        'fields': [
            ('f_hd_student', 'اسم الطالب', 'text'),
            ('f_hd_hall', 'قاعة الامتحان', 'text'),
            ('f_hd_seat', 'رقم المقعد', 'number'),
            ('f_hd_shift', 'الفترة الامتحانية', 'select', ['الفترة الأولى (صباحاً)', 'الفترة الثانية'])
        ]
    },
    'roll-call': {
        'title': 'كشوف المناداة الامتحانية',
        'db_key': 'roll_call',
        'headers': ['القاعة الامتحانية', 'الصف الدراسي', 'الملاحظ المسؤول', 'عدد الطلاب', 'إجراءات'],
        'fields': [
            ('f_rc_hall', 'القاعة الامتحانية', 'text'),
            ('f_rc_grade', 'الصف الدراسي', 'text'),
            ('f_rc_proctor', 'الملاحظ المسؤول', 'text'),
            ('f_rc_count', 'عدد الطلاب', 'number')
        ]
    },
    'seat-cards': {
        'title': 'بطاقات أرقام الجلوس',
        'db_key': 'seat_cards',
        'headers': ['اسم الطالب', 'رقم الجلوس', 'القاعة', 'حالة الطباعة', 'إجراءات'],
        'fields': [
            ('f_sc_student', 'اسم الطالب', 'text'),
            ('f_sc_num', 'رقم الجلوس', 'number'),
            ('f_sc_hall', 'القاعة', 'text'),
            ('f_sc_status', 'حالة الطباعة', 'select', ['جاهزة للطباعة', 'تمت الطباعة'])
        ]
    },
    'substitute': {
        'title': 'حصص الاحتياط والبدلاء',
        'db_key': 'substitutes',
        'headers': ['التاريخ', 'اليوم', 'الحصة / الشعبة', 'المعلم الغائب', 'المعلم البديل', 'إجراءات'],
        'fields': [
            ('f_sub_date', 'التاريخ', 'date'),
            ('f_sub_day', 'اليوم', 'select', ['السبت', 'الأحد', 'الاثنين', 'الثلاثاء', 'الأربعاء']),
            ('f_sub_period', 'الحصة والشعبة', 'text'),
            ('f_sub_absent', 'المعلم الغائب', 'text'),
            ('f_sub_substitute', 'المعلم البديل', 'text')
        ]
    },

    # 5. Activities & Transport Setup
    'activity-types': {
        'title': 'أنواع الأنشطة الطلابية',
        'db_key': 'activity_types',
        'headers': ['اسم النشاط', 'التصنيف', 'الميزانية المخصصة', 'المشرف المسؤول', 'إجراءات'],
        'fields': [
            ('f_act_name', 'اسم النشاط', 'text'),
            ('f_act_cat', 'التصنيف', 'select', ['ثقافي', 'رياضي', 'علمي', 'اجتماعي/ترفيهي']),
            ('f_act_budget', 'الميزانية المخصصة (ريال)', 'number'),
            ('f_act_sup', 'المشرف المسؤول', 'text')
        ]
    },
    'activity-supervisors': {
        'title': 'مشرفو الأنشطة',
        'db_key': 'activity_supervisors',
        'headers': ['اسم المشرف', 'النشاط المكلف به', 'رقم الهاتف', 'القسم / التخصص', 'إجراءات'],
        'fields': [
            ('f_as_name', 'اسم المشرف', 'text'),
            ('f_as_activity', 'النشاط المكلف به', 'text'),
            ('f_as_phone', 'رقم الهاتف', 'text'),
            ('f_as_dept', 'القسم / التخصص', 'text')
        ]
    },
    'activity-enrollment': {
        'title': 'تسجيل الطلاب في الأنشطة',
        'db_key': 'activity_enrollment',
        'headers': ['اسم الطالب', 'النشاط الطلابي', 'تاريخ التسجيل', 'حالة الاشتراك', 'إجراءات'],
        'fields': [
            ('f_ae_student', 'اسم الطالب', 'text'),
            ('f_ae_activity', 'النشاط الطلابي', 'text'),
            ('f_ae_date', 'تاريخ التسجيل', 'date'),
            ('f_ae_status', 'حالة الاشتراك', 'select', ['مشارك نشط', 'معلق', 'منسحب'])
        ]
    },
    'activity-reports': {
        'title': 'تقارير الأنشطة الطلابية',
        'db_key': 'activity_reports',
        'headers': ['اسم النشاط', 'تاريخ التنفيذ', 'عدد المشاركين', 'التقييم العام', 'إجراءات'],
        'fields': [
            ('f_ar_name', 'اسم النشاط', 'text'),
            ('f_ar_date', 'تاريخ التنفيذ', 'date'),
            ('f_ar_count', 'عدد المشاركين الفعلي', 'number'),
            ('f_ar_eval', 'التقييم العام', 'select', ['ممتاز', 'جيد جداً', 'جيد', 'مقبول'])
        ]
    },
    'transport-routes': {
        'title': 'خطوط سير الحافلات',
        'db_key': 'transport_routes',
        'headers': ['اسم الخط / المنطقة', 'اسم السائق', 'رقم الحافلة', 'رسوم الاشتراك', 'إجراءات'],
        'fields': [
            ('f_tr_name', 'اسم الخط / المنطقة', 'text'),
            ('f_tr_driver', 'اسم السائق', 'text'),
            ('f_tr_bus', 'رقم الحافلة', 'text'),
            ('f_tr_fee', 'رسوم الاشتراك (ريال)', 'number')
        ]
    },
    'buses': {
        'title': 'دليل الحافلات المدرسية',
        'db_key': 'buses',
        'headers': ['رقم الحافلة / اللوحة', 'نوع الحافلة / الموديل', 'عدد المقاعد', 'السائق المسؤول', 'إجراءات'],
        'fields': [
            ('f_bus_num', 'رقم اللوحة / الحافلة', 'text'),
            ('f_bus_model', 'الموديل / النوع', 'text'),
            ('f_bus_seats', 'عدد المقاعد', 'number'),
            ('f_bus_driver', 'السائق المسؤول', 'text')
        ]
    },
    'transport-enrollment': {
        'title': 'اشتراكات المواصلات',
        'db_key': 'transport_enrollment',
        'headers': ['اسم الطالب', 'خط السير', 'نقطة الانطلاق', 'رسوم الاشتراك', 'إجراءات'],
        'fields': [
            ('f_te_student', 'اسم الطالب', 'text'),
            ('f_te_route', 'خط السير / المنطقة', 'text'),
            ('f_te_pickup', 'نقطة الانطلاق / المحطة', 'text'),
            ('f_te_fee', 'رسوم الاشتراك (ريال)', 'number')
        ]
    },
    'demand-letters': {
        'title': 'مطالبات وأوامر الصرف',
        'db_key': 'demand_letters',
        'headers': ['الجهة / العميل', 'المبلغ المطالب به', 'البيان / التوضيح', 'تاريخ الاستحقاق', 'إجراءات'],
        'fields': [
            ('f_dl_target', 'الجهة / العميل', 'text'),
            ('f_dl_amount', 'المبلغ (ريال)', 'number'),
            ('f_dl_desc', 'البيان / التوضيح', 'text'),
            ('f_dl_date', 'تاريخ الاستحقاق', 'date')
        ]
    },

    # 6. Inventory & Warehouse Setup
    'item-categories': {
        'title': 'تصنيفات الأصناف والمخزون',
        'db_key': 'item_categories',
        'headers': ['اسم التصنيف', 'الوصف', 'موقع التخزين الرئيسي', 'إجراءات'],
        'fields': [
            ('f_ic_name', 'اسم التصنيف (مثال: قرطاسية، أثاث)', 'text'),
            ('f_ic_desc', 'الوصف', 'text'),
            ('f_ic_loc', 'موقع التخزين الرئيسي', 'text')
        ]
    },
    'inventory-items': {
        'title': 'دليل الأصناف والمستلزمات',
        'db_key': 'inventory_items',
        'headers': ['رمز الصنف', 'اسم الصنف', 'التصنيف', 'الكمية الحالية', 'وحدة القياس', 'إجراءات'],
        'fields': [
            ('f_ii_code', 'رمز الصنف', 'text'),
            ('f_ii_name', 'اسم الصنف', 'text'),
            ('f_ii_cat', 'التصنيف', 'text'),
            ('f_ii_qty', 'الكمية الحالية', 'number'),
            ('f_ii_unit', 'وحدة القياس', 'select', ['قطعة', 'كرتون', 'حزمة', 'طقم', 'متر'])
        ]
    },
    'supply-orders': {
        'title': 'أوامر التوريد والإدخال المخزني',
        'db_key': 'supply_orders',
        'headers': ['رقم أمر التوريد', 'المورد / الشركة', 'تاريخ التوريد', 'إجمالي القيمة', 'الحالة', 'إجراءات'],
        'fields': [
            ('f_so_num', 'رقم أمر التوريد', 'text'),
            ('f_so_supplier', 'المورد / الشركة', 'text'),
            ('f_so_date', 'تاريخ التوريد', 'date'),
            ('f_so_amount', 'إجمالي القيمة (ريال)', 'number'),
            ('f_so_status', 'الحالة', 'select', ['مستلم ومفحوص', 'قيد التوريد', 'معلق'])
        ]
    },
    'issue-orders': {
        'title': 'أوامر الصرف والتوزيع المخزني',
        'db_key': 'issue_orders',
        'headers': ['رقم أمر الصرف', 'المستلم / القسم', 'التاريخ', 'البيان', 'الحالة', 'إجراءات'],
        'fields': [
            ('f_io_num', 'رقم أمر الصرف', 'text'),
            ('f_io_receiver', 'المستلم / القسم', 'text'),
            ('f_io_date', 'تاريخ الصرف', 'date'),
            ('f_io_desc', 'البيان / المستلزمات', 'text'),
            ('f_io_status', 'الحالة', 'select', ['تم الصرف', 'قيد الإجراء'])
        ]
    },
    'suppliers': {
        'title': 'دليل الموردين والشركات',
        'db_key': 'suppliers',
        'headers': ['اسم المورد / الشركة', 'شخص التواصل', 'رقم الهاتف', 'العنوان', 'إجراءات'],
        'fields': [
            ('f_sup_name', 'اسم المورد / الشركة', 'text'),
            ('f_sup_contact', 'شخص التواصل المسؤول', 'text'),
            ('f_sup_phone', 'رقم الهاتف', 'text'),
            ('f_sup_address', 'العنوان / المدينة', 'text')
        ]
    },
    'inventory-reports': {
        'title': 'تقارير جرد المخزون',
        'db_key': 'inventory_reports',
        'headers': ['اسم الصنف', 'الكمية الدفترية', 'الكمية الفعلية', 'الفارق', 'تاريخ الجرد', 'إجراءات'],
        'fields': [
            ('f_ir_item', 'اسم الصنف', 'text'),
            ('f_ir_book', 'الكمية الدفترية', 'number'),
            ('f_ir_actual', 'الكمية الفعلية', 'number'),
            ('f_ir_date', 'تاريخ الجرد', 'date')
        ]
    },

    # 7. SMS & Communication Setup
    'sms-settings': {
        'title': 'إعدادات بوابات SMS',
        'db_key': 'sms_settings',
        'headers': ['مزود الخدمة', 'اسم المرسل (Sender ID)', 'حالة الاتصال', 'ملاحظات', 'إجراءات'],
        'fields': [
            ('f_sms_provider', 'اسم مزود الخدمة', 'text'),
            ('f_sms_sender', 'اسم المرسل الرسمي (Sender ID)', 'text'),
            ('f_sms_status', 'حالة الاتصال', 'select', ['متصل ونشط', 'معطل', 'تجريبي']),
            ('f_sms_notes', 'ملاحظات المفتاح / API Key', 'text')
        ]
    },
    'sms-send': {
        'title': 'إرسال رسائل جماعية',
        'db_key': 'sms_send',
        'headers': ['الفئة المستهدفة', 'نص الرسالة', 'عدد المستلمين', 'تاريخ الإرسال', 'إجراءات'],
        'fields': [
            ('f_ss_target', 'الفئة المستهدفة', 'select', ['أولياء الأمور', 'المعلمون والجمهور', 'الطلاب المتأخرين', 'الجميع']),
            ('f_ss_msg', 'نص الرسالة', 'text'),
            ('f_ss_count', 'عدد المستلمين المتوقع', 'number'),
            ('f_ss_date', 'تاريخ الإرسال', 'date')
        ]
    },
    'sms-templates': {
        'title': 'قوالب الرسائل الجاهزة',
        'db_key': 'sms_templates',
        'headers': ['اسم القالب', 'المناسبة / الاستخدام', 'نص القالب', 'إجراءات'],
        'fields': [
            ('f_st_title', 'اسم القالب (مثال: إشعار غياب)', 'text'),
            ('f_st_use', 'المناسبة / الاستخدام', 'text'),
            ('f_st_body', 'نص القالب (استخدم {اسم_الطالب})', 'text')
        ]
    },

    # 8. Reports & Personal Pages
    'monthly-report': {
        'title': 'التقرير الشهري الأكاديمي',
        'db_key': 'monthly_report',
        'headers': ['الشهر', 'الصف الدراسي', 'نسبة الحضور %', 'متوسط الدرجات', 'إجراءات'],
        'fields': [
            ('f_mr_month', 'الشهر', 'text'),
            ('f_mr_grade', 'الصف الدراسي', 'text'),
            ('f_mr_att', 'نسبة الحضور %', 'number'),
            ('f_mr_avg', 'متوسط الدرجات %', 'number')
        ]
    },
    'semester-report': {
        'title': 'تقرير الفصل الدراسي',
        'db_key': 'semester_report',
        'headers': ['الفصل الدراسي', 'إجمالي الطلاب', 'الناجحون', 'نسبة النجاح %', 'إجراءات'],
        'fields': [
            ('f_sr_term', 'الفصل الدراسي', 'select', ['الفصل الأول', 'الفصل الثاني']),
            ('f_sr_total', 'إجمالي الطلاب', 'number'),
            ('f_sr_passed', 'عدد الناجحين', 'number'),
            ('f_sr_rate', 'نسبة النجاح %', 'number')
        ]
    },
    'class-details': {
        'title': 'تفاصيل الفصول والشُعَب',
        'db_key': 'class_details',
        'headers': ['الصف والشعبة', 'رائد الفصل', 'عدد الطلاب', 'الحالة العامة', 'إجراءات'],
        'fields': [
            ('f_cd_class', 'الصف والشعبة', 'text'),
            ('f_cd_leader', 'رائد الفصل', 'text'),
            ('f_cd_count', 'عدد الطلاب', 'number'),
            ('f_cd_status', 'الحالة العامة', 'select', ['مكتمل ونشط', 'بحاجة لمتابعة'])
        ]
    },
    'top-students': {
        'title': 'قائمة الأوائل والمتفوقين',
        'db_key': 'top_students',
        'headers': ['اسم الطالب', 'الصف الدراسي', 'النسبة المئوية %', 'الترتيب', 'إجراءات'],
        'fields': [
            ('f_ts_student', 'اسم الطالب المتفوق', 'text'),
            ('f_ts_grade', 'الصف الدراسي', 'text'),
            ('f_ts_pct', 'النسبة المئوية %', 'number'),
            ('f_ts_rank', 'الترتيب (الأول، الثاني...)', 'text')
        ]
    },
    'success-rate-subject': {
        'title': 'نسب النجاح حسب المادة',
        'db_key': 'success_rate_subject',
        'headers': ['اسم المادة', 'الصف الدراسي', 'عدد الطلاب', 'نسبة النجاح %', 'إجراءات'],
        'fields': [
            ('f_srs_subj', 'اسم المادة', 'text'),
            ('f_srs_grade', 'الصف الدراسي', 'text'),
            ('f_srs_count', 'عدد الطلاب الخاضعين', 'number'),
            ('f_srs_rate', 'نسبة النجاح %', 'number')
        ]
    },
    'success-rate-section': {
        'title': 'نسب النجاح حسب الشعبة',
        'db_key': 'success_rate_section',
        'headers': ['اسم الشعبة / الفصل', 'الصف الدراسي', 'إجمالي الطلاب', 'نسبة النجاح %', 'إجراءات'],
        'fields': [
            ('f_ssec_sec', 'اسم الشعبة', 'text'),
            ('f_ssec_grade', 'الصف الدراسي', 'text'),
            ('f_ssec_total', 'إجمالي الطلاب', 'number'),
            ('f_ssec_rate', 'نسبة النجاح %', 'number')
        ]
    },
    'control-reports': {
        'title': 'تقارير الكنترول والامتحانات',
        'db_key': 'control_reports',
        'headers': ['عنوان التقرير', 'تاريخ التقرير', 'المُعد بواسطة', 'التقييم العام', 'إجراءات'],
        'fields': [
            ('f_cr_title', 'عنوان التقرير', 'text'),
            ('f_cr_date', 'تاريخ التقرير', 'date'),
            ('f_cr_author', 'المُعد بواسطة', 'text'),
            ('f_cr_eval', 'التقييم العام', 'select', ['مكتمل ومعتمد', 'تحت المراجعة'])
        ]
    },
    'admin-messages': {
        'title': 'الرسائل الإدارية الداخلية',
        'db_key': 'admin_messages',
        'headers': ['عنوان الرسالة', 'المرسل', 'الأولوية', 'التاريخ', 'إجراءات'],
        'fields': [
            ('f_am_title', 'عنوان الرسالة', 'text'),
            ('f_am_sender', 'المرسل / القسم', 'text'),
            ('f_am_priority', 'الأولوية', 'select', ['عاجل وهام', 'عادي', 'تذكير']),
            ('f_am_date', 'التاريخ', 'date')
        ]
    },
    'dictionary': {
        'title': 'معجم المصطلحات والمفهومات',
        'db_key': 'dictionary',
        'headers': ['المصطلح المدرسي', 'الشرح / التعريف', 'الفئة المعرفية', 'ملاحظات', 'إجراءات'],
        'fields': [
            ('f_dic_term', 'المصطلح المدرسي', 'text'),
            ('f_dic_def', 'الشرح / التعريف', 'text'),
            ('f_dic_cat', 'الفئة المعرفية', 'select', ['إداري', 'أكاديمي', 'مالي', 'كنترول'])
        ]
    },
    'personal-info': {
        'title': 'البيانات الشخصية والمعلومات',
        'db_key': 'personal_info',
        'headers': ['اسم صاحب الملف', 'الصف / الوظيفة', 'رقم الهاتف', 'ملاحظات', 'إجراءات'],
        'fields': [
            ('f_pi_name', 'الاسم الكامل', 'text'),
            ('f_pi_role', 'الصف / الوظيفة', 'text'),
            ('f_pi_phone', 'رقم الهاتف', 'text'),
            ('f_pi_notes', 'ملاحظات إضافية', 'text')
        ]
    }
}

print(f"Configured total custom modules: {len(MODULES)}")
