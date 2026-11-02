/**
 * ============================================================================
 * 03-ROUTER-NAV.JS - Single Page Application Router & Dynamic View Dispatcher
 * ============================================================================
 */
function toggleSub(el) {
    if (!el) return;
    const navSection = el.closest('.nav-section') || el.parentElement;
    if (!navSection) return;
    const subMenu = navSection.querySelector('.sub-menu');
    const chevron = navSection.querySelector('.fa-chevron-down, .fa-chevron-up');
    
    if (navSection.classList.contains('open')) {
        navSection.classList.remove('open');
        if (subMenu) subMenu.style.display = 'none';
        if (chevron) {
            chevron.classList.remove('fa-chevron-up');
            chevron.classList.add('fa-chevron-down');
        }
    } else {
        navSection.classList.add('open');
        if (subMenu) subMenu.style.display = 'flex';
        if (chevron) {
            chevron.classList.remove('fa-chevron-down');
            chevron.classList.add('fa-chevron-up');
        }
    }
}
window.toggleSub = toggleSub;

function goTo(pageId, extraParam) {
    if (!pageId) return;
    let target = String(pageId).trim();
    if (target.startsWith('#')) target = target.substring(1);

    // Comprehensive Arabic & English Alias Mapping Dictionary
    const aliasMap = {
        // Operation Lock
        'قفل العمليات': 'pg-operation-lock',
        'قفل العمليات والموديلات': 'pg-operation-lock',
        'قفل العمليات والموديولات': 'pg-operation-lock',
        'قفل العمليات والموديول': 'pg-operation-lock',
        'قفل الموديولات': 'pg-operation-lock',
        'operation-lock': 'pg-operation-lock',
        'operation_lock': 'pg-operation-lock',
        'operationlocks': 'pg-operation-lock',
        'lock': 'pg-operation-lock',
        
        // Database
        'قواعد البيانات': 'pg-db-management',
        'إدارة قواعد البيانات': 'pg-db-management',
        'ادارة قواعد البيانات': 'pg-db-management',
        'قاعدة البيانات': 'pg-db-management',
        'النسخ الاحتياطي': 'pg-db-management',
        'db-management': 'pg-db-management',
        'database': 'pg-db-management',
        'db': 'pg-db-management',
        'backup': 'pg-db-management',

        // Audit Trail
        'سجل العمليات': 'pg-audit',
        'سجل التدقيق': 'pg-audit',
        'التدقيق الأمني': 'pg-audit',
        'audit': 'pg-audit',
        'audit-trail': 'pg-audit',
        'pg-audit-trail': 'pg-audit',

        // Posting
        'إدارة الترحيلات': 'pg-posting',
        'ادارة الترحيلات': 'pg-posting',
        'الترحيلات': 'pg-posting',
        'الترحيل المالي': 'pg-posting',
        'posting': 'pg-posting',

        // Settings & Alerts & Archive & Password
        'إعدادات النظام': 'pg-system-settings',
        'اعدادات النظام': 'pg-system-settings',
        'الإعدادات': 'pg-system-settings',
        'settings': 'pg-system-settings',
        'system-settings': 'pg-system-settings',
        'pg-settings': 'pg-system-settings',
        'التنبيهات': 'pg-alerts',
        'التنبيهات التلقائية': 'pg-alerts',
        'alerts': 'pg-alerts',
        'الأرشيف': 'pg-archive',
        'الارشيف': 'pg-archive',
        'archive': 'pg-archive',
        'تغيير كلمة المرور': 'pg-change-password',
        'تغيير الباسورد': 'pg-change-password',
        'change-password': 'pg-change-password',

        // Academic & School Config
        'معلومات المدرسة': 'pg-school-info',
        'school-info': 'pg-school-info',
        'دليل المستخدمين': 'pg-users',
        'المستخدمين': 'pg-users',
        'users': 'pg-users',
        'السنوات الدراسية': 'pg-academic-years',
        'academic-years': 'pg-academic-years',
        'التقويم المدرسي': 'pg-academic-calendar',
        'academic-calendar': 'pg-academic-calendar',
        'المراحل والصفوف': 'pg-stages',
        'stages': 'pg-stages',
        'الشعب': 'pg-sections',
        'الشُعَب': 'pg-sections',
        'sections': 'pg-sections',
        'توزيع الشعب': 'pg-section-distribution',
        'توزيع الطلاب على الشعب': 'pg-section-distribution',
        'section-distribution': 'pg-section-distribution',
        'المواد الدراسية': 'pg-subjects',
        'subjects': 'pg-subjects',
        'توزيع المواد': 'pg-subject-distribution',
        'القاعات الدراسية': 'pg-classrooms',
        'classrooms': 'pg-classrooms',
        'أوقات الحصص': 'pg-class-times',
        'فئات الخصومات': 'pg-discount-categories',
        'خطط الأقساط': 'pg-installment-plans',
        'الوثائق المطلوبة': 'pg-required-docs',

        // Students & Admission
        'سجل الطلاب': 'pg-students',
        'الطلاب': 'pg-students',
        'students': 'pg-students',
        'تسجيل طالب جديد': 'pg-student-register',
        'طلبات القبول': 'pg-enrollment',
        'المنقطعون': 'pg-discontinued',
        'الضامنون': 'pg-guarantors',
        'أولياء الأمور': 'pg-parents',
        'parents': 'pg-parents',
        'وثائق الطلاب': 'pg-student-docs',
        'student-docs': 'pg-student-docs',

        // HR & Teachers
        'دليل الموظفين': 'pg-employees',
        'الموظفين': 'pg-employees',
        'employees': 'pg-employees',
        'عقود الموظفين': 'pg-emp-contracts',
        'سلف الموظفين': 'pg-emp-advances',
        'إجازات الموظفين': 'pg-leave-management',
        'leave-management': 'pg-leave-management',
        'تقييم الأداء': 'pg-performance-eval',
        'performance-eval': 'pg-performance-eval',

        // Finance & Accounts
        'دليل الحسابات': 'pg-chart-accounts',
        'شجرة الحسابات': 'pg-chart-accounts',
        'chart-accounts': 'pg-chart-accounts',
        'السندات': 'pg-vouchers',
        'vouchers': 'pg-vouchers',
        'القيود اليومية': 'pg-journal',
        'journal': 'pg-journal',
        'الصناديق': 'pg-cashboxes',
        'cashboxes': 'pg-cashboxes',
        'مراكز التكلفة': 'pg-cost-centers',
        'cost-centers': 'pg-cost-centers',
        'تسقيف الحسابات': 'pg-account-ceiling',
        'كشف الحساب': 'pg-student-account',
        'student-account': 'pg-student-account',
        'العملات': 'pg-currencies',
        'جرد الصناديق': 'pg-cashbox-inventory',
        'الإقفالات': 'pg-closings',
        'البنوك': 'pg-banks',
        'الشيكات': 'pg-checks',
        'رسائل المطالبة': 'pg-demand-letters',
        'التقارير المالية': 'pg-finance-reports',

        // Control & Exams
        'جدول الحصص': 'pg-timetable-builder',
        'timetable': 'pg-timetable-builder',
        'رصد الدرجات': 'pg-grading',
        'grading': 'pg-grading',
        'النتائج النهائية': 'pg-results',
        'results': 'pg-results',
        'الشهادات': 'pg-certificates',
        'certificates': 'pg-certificates',
        'الواجبات': 'pg-homework-tracker',
        'homework-tracker': 'pg-homework-tracker',
        'ملاحظات الفصل': 'pg-class-notes',
        'class-notes': 'pg-class-notes',
        'التقارير المخصصة': 'pg-custom-reports',
        'custom-reports': 'pg-custom-reports',
        
        // Parent Portal
        'لوحة ولي الأمر': 'pg-parent-dashboard',
        'رسوم الطالب': 'pg-parent-fees',
        'حضور الطالب': 'pg-parent-attendance',
        'درجات الطالب': 'pg-parent-grades',
        'واجبات الطالب': 'pg-parent-homework'
    };

    let targetId = aliasMap[target] || target;
    if (!targetId.startsWith('pg-') && document.getElementById('pg-' + targetId)) {
        targetId = 'pg-' + targetId;
    }

    // Hide all pages
    const pages = document.querySelectorAll('.page');
    pages.forEach(p => {
        p.classList.remove('active');
        p.style.display = 'none';
    });

    // Ensure Target Element Exists in DOM
    let targetEl = document.getElementById(targetId);
    if (!targetEl) {
        const mainContent = document.getElementById('mainContent') || document.querySelector('.main-content') || document.body;
        if (mainContent) {
            targetEl = document.createElement('div');
            targetEl.className = 'page';
            targetEl.id = targetId;
            mainContent.appendChild(targetEl);
        }
    }

    if (targetEl) {
        targetEl.classList.add('active');
        targetEl.style.display = 'block';
        window.scrollTo({ top: 0, behavior: 'smooth' });

        try {
            history.replaceState(null, null, '#' + targetId);
        } catch(e) {
            window.location.hash = '#' + targetId;
        }

        // Highlight Active Link in Sidebar
        document.querySelectorAll('.sidebar-nav a').forEach(a => {
            const oc = a.getAttribute('onclick') || '';
            if (oc.includes(targetId) || (aliasMap[target] && oc.includes(aliasMap[target]))) {
                a.classList.add('active');
                const parentSection = a.closest('.nav-section');
                if (parentSection) {
                    parentSection.classList.add('open');
                    const subMenu = parentSection.querySelector('.sub-menu');
                    if (subMenu) subMenu.style.display = 'flex';
                }
            } else {
                a.classList.remove('active');
            }
        });
    }

    // Dynamic Renderers Execution Map
    const dynamicRenderers = {
        'pg-operation-lock': () => {
            if (typeof window.renderOperationLockGrid === 'function') window.renderOperationLockGrid();
        },
        'pg-db-management': () => {
            if (typeof window.renderDbManagementPanel === 'function') window.renderDbManagementPanel();
        },
        'pg-posting': () => {
            if (typeof window.renderPostingGrid === 'function') window.renderPostingGrid();
        },
        'pg-system-settings': () => {
            if (typeof window.renderSystemSettingsGrid === 'function') window.renderSystemSettingsGrid();
        },
        'pg-settings': () => {
            if (typeof window.renderSystemSettingsGrid === 'function') window.renderSystemSettingsGrid();
        },
        'pg-alerts': () => {
            if (typeof window.renderAlertsGrid === 'function') window.renderAlertsGrid();
        },
        'pg-archive': () => {
            if (typeof window.renderArchiveGrid === 'function') window.renderArchiveGrid();
        },
        'pg-change-password': () => {
            if (typeof window.renderChangePassword === 'function') window.renderChangePassword();
        },
        'pg-section-distribution': () => {
            if (typeof window.renderSectionDistribution === 'function') window.renderSectionDistribution();
        },
        'pg-grading': () => {
            if (typeof window.renderGradingSheetGrid === 'function') window.renderGradingSheetGrid();
        },
        'pg-student-docs': () => {
            if (typeof window.renderStudentDocs === 'function') window.renderStudentDocs();
        },
        'pg-leave-management': () => {
            if (typeof window.renderLeaveManagement === 'function') window.renderLeaveManagement();
        },
        'pg-homework-tracker': () => {
            if (typeof window.renderHomeworkTracker === 'function') window.renderHomeworkTracker();
        },
        'pg-certificates': () => {
            if (typeof window.renderCertificatesGrid === 'function') window.renderCertificatesGrid();
        },
        'pg-custom-reports': () => {
            if (typeof window.renderCustomReports === 'function') window.renderCustomReports();
        },
        'pg-class-notes': () => {
            if (typeof window.renderClassNotes === 'function') window.renderClassNotes();
        },
        'pg-parents': () => {
            if (typeof window.renderParents === 'function') window.renderParents();
        },
        'pg-discontinued': () => {
            if (typeof window.renderDiscontinuedList === 'function') window.renderDiscontinuedList();
        },
        'pg-results': () => {
            if (typeof window.renderFinalResultsGrid === 'function') window.renderFinalResultsGrid();
        },
        'pg-performance-eval': () => {
            if (typeof window.renderPerformanceEvalGrid === 'function') window.renderPerformanceEvalGrid();
        },
        'pg-cost-centers': () => typeof window.renderCostCentersGrid === 'function' && window.renderCostCentersGrid(),
        'pg-cashboxes': () => typeof window.renderCashboxesGrid === 'function' && window.renderCashboxesGrid(),
        'pg-chart-accounts': () => typeof window.renderChartAccountsTree === 'function' && window.renderChartAccountsTree(),
        'pg-journal': () => typeof window.renderJournalGrid === 'function' && window.renderJournalGrid(),
        'pg-audit': () => typeof window.renderAuditGrid === 'function' && window.renderAuditGrid(),
        'pg-students': () => typeof window.renderStudents === 'function' && window.renderStudents(),
        'pg-student-register': () => typeof window.renderStudents === 'function' && window.renderStudents(),
        'pg-enrollment': () => typeof window.renderEnrollmentList === 'function' && window.renderEnrollmentList(),
        'pg-employees': () => typeof window.renderEmployeesGrid === 'function' && window.renderEmployeesGrid(),
        'pg-users': () => typeof window.renderUsersGrid === 'function' && window.renderUsersGrid(),
        'pg-vouchers': () => typeof window.renderVouchersGrid === 'function' && window.renderVouchersGrid(),
        'pg-banks': () => typeof window.renderBanksGrid === 'function' && window.renderBanksGrid(),
        'pg-checks': () => typeof window.renderChecksGrid === 'function' && window.renderChecksGrid(),
        'pg-account-ceiling': () => typeof window.renderAccountCeilingGrid === 'function' && window.renderAccountCeilingGrid(),
        'pg-demand-letters': () => typeof window.renderDemandLettersGrid === 'function' && window.renderDemandLettersGrid(),
        'pg-stages': () => typeof window.renderStagesGrid === 'function' && window.renderStagesGrid(),
        'pg-sections': () => typeof window.renderSectionsGrid === 'function' && window.renderSectionsGrid(),
        'pg-subjects': () => typeof window.renderSubjectsGrid === 'function' && window.renderSubjectsGrid(),
        'pg-subject-distribution': () => typeof window.renderSubjectDistGrid === 'function' && window.renderSubjectDistGrid(),
        'pg-classrooms': () => typeof window.renderClassroomsGrid === 'function' && window.renderClassroomsGrid(),
        'pg-class-times': () => typeof window.renderClassTimesGrid === 'function' && window.renderClassTimesGrid(),
        'pg-academic-calendar': () => typeof window.renderAcademicCalendarGrid === 'function' && window.renderAcademicCalendarGrid(),
        'pg-academic-years': () => typeof window.renderAcademicYearsGrid === 'function' && window.renderAcademicYearsGrid(),
        'pg-discount-categories': () => typeof window.renderDiscountCategoriesGrid === 'function' && window.renderDiscountCategoriesGrid(),
        'pg-installment-plans': () => typeof window.renderInstallmentPlansGrid === 'function' && window.renderInstallmentPlansGrid(),
        'pg-required-docs': () => typeof window.renderRequiredDocsGrid === 'function' && window.renderRequiredDocsGrid(),
        'pg-guarantors': () => typeof window.renderGuarantorsGrid === 'function' && window.renderGuarantorsGrid(),
        'pg-emp-contracts': () => typeof window.renderEmpContractsGrid === 'function' && window.renderEmpContractsGrid(),
        'pg-emp-advances': () => typeof window.renderEmpAdvancesGrid === 'function' && window.renderEmpAdvancesGrid(),
        'pg-activities': () => typeof window.renderActivitiesGrid === 'function' && window.renderActivitiesGrid(),
        'pg-suppliers': () => typeof window.renderSuppliersGrid === 'function' && window.renderSuppliersGrid(),
        'pg-faq': () => typeof window.renderFaqArticlesGrid === 'function' && window.renderFaqArticlesGrid(),
        'pg-inventory-items': () => typeof window.renderInventoryItemsGrid === 'function' && window.renderInventoryItemsGrid(),
        'pg-transport-routes': () => typeof window.renderTransportRoutesGrid === 'function' && window.renderTransportRoutesGrid(),
        'pg-buses': () => typeof window.renderBusesGrid === 'function' && window.renderBusesGrid(),
        'pg-closings': () => typeof window.renderClosingsGrid === 'function' && window.renderClosingsGrid()
    };

    if (dynamicRenderers[targetId]) {
        try { dynamicRenderers[targetId](); } catch(e) { console.error('Renderer error on ' + targetId, e); }
    } else if (typeof hydrateAndMountAllGrids === 'function') {
        try { hydrateAndMountAllGrids(); } catch(e) {}
    }

    if (typeof attachUniversalRowInteractions === 'function') {
        setTimeout(() => { attachUniversalRowInteractions(); }, 150);
    }
}
window.goTo = goTo;
window.showPage = goTo;
window.navTo = goTo;
window.switchPage = goTo;

function triggerOfficialPrint() {
    window.print();
}
window.triggerOfficialPrint = triggerOfficialPrint;
