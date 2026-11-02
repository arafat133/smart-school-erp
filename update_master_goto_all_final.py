"""
Update Master goTo Dispatcher in app.js for all pages including Goods Issue Notes & reported pages
"""
import re, time

print("=" * 60)
print("Updating Master goTo Dispatcher in app.js for All Pages...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

master_goto_code = """
// Master Central Dispatcher for Page Renders
const _origMasterGoTo = window.goTo;
window.goTo = function(id) {
    if (_origMasterGoTo) {
        try { _origMasterGoTo(id); } catch(e){}
    }
    
    // Explicit guaranteed dispatcher for all pages
    if (id === 'pg-issue-orders') renderIssueOrdersGrid();
    if (id === 'pg-class-times') renderClassTimesGrid();
    if (id === 'pg-timetable-builder' || id === 'pg-schedule') renderInteractiveTimetable();
    if (id === 'pg-student-register') renderStudentRegister();
    if (id === 'pg-simple-register') renderSimpleRegister();
    if (id === 'pg-promotion-workflow' || id === 'pg-promotion') renderPromotionBatch();
    if (id === 'pg-permissions') renderPermissions();
    if (id === 'pg-audit') renderAuditLogs();
    if (id === 'pg-vouchers') renderVouchers();
    if (id === 'pg-journal') renderJournalList();
    if (id === 'pg-leave-management') renderLeaveManagementGrid();
    if (id === 'pg-performance-eval') renderPerformanceEvals();
    if (id === 'pg-homework-tracker') renderHomeworkList();
    if (id === 'pg-custom-reports') renderCustomReportsGrid();
    if (id === 'pg-admin-messages') renderAdminMessagesGrid();
    if (id === 'pg-shortcuts') renderShortcutsGrid();
    if (id === 'pg-faq') renderFaqGrid();
    if (id === 'pg-dictionary') renderDictionaryGrid();
    if (id === 'pg-personal-info') renderPersonalInfoGrid();
    if (id === 'pg-sms-send') renderSmsSendGrid();
    if (id === 'pg-sms-templates') renderSmsTemplatesGrid();
    if (id === 'pg-sms-settings') renderSmsSettingsGrid();
    if (id === 'pg-monthly-report') renderMonthlyReportGrid();
    if (id === 'pg-semester-report') renderSemesterReportGrid();
    if (id === 'pg-class-details') renderClassDetailsGrid();
    if (id === 'pg-top-students') renderTopStudentsGrid();
    if (id === 'pg-success-rate-subject') renderSuccessRateSubjectGrid();
    if (id === 'pg-control-reports') renderControlReportsGrid();
    if (id === 'pg-item-categories') renderItemCategoriesGrid();
    if (id === 'pg-inventory-items') renderInventoryItemsGrid();
    if (id === 'pg-supply-orders') renderSupplyOrdersGrid();
    if (id === 'pg-suppliers') renderSuppliersGrid();
    if (id === 'pg-inventory-reports') renderInventoryReportsGrid();
    if (id === 'pg-activities') renderActivitiesGrid();
    if (id === 'pg-transport-routes') renderTransportRoutesGrid();
    if (id === 'pg-buses') renderBusesGrid();
    if (id === 'pg-transport-enrollment') renderTransportEnrollmentGrid();
    if (id === 'pg-transport') renderTransportManifestGrid();
    if (id === 'pg-grading') renderInteractiveGradingGrid();
    if (id === 'pg-results') renderFinalResultsGrid();
    if (id === 'pg-certificates') renderCertificatesGrid();
    if (id === 'pg-exam-halls') renderExamHallsGrid();
    if (id === 'pg-seat-numbers') renderSeatNumbersGrid();
    if (id === 'pg-secret-numbers') renderSecretNumbersGrid();
    if (id === 'pg-hall-distribution') renderHallDistributionGrid();
    if (id === 'pg-exam-schedule') renderExamScheduleGrid();
    if (id === 'pg-roll-call') renderRollCallGrid();
    if (id === 'pg-seat-cards') renderSeatCardsGrid();
    if (id === 'pg-substitute') renderSubstituteGrid();
    if (id === 'pg-guarantors') renderGuarantorsList();
    if (id === 'pg-teacher-subjects') renderTeacherSubjectsMatrix();
    if (id === 'pg-emp-attendance') renderEmpAttendanceGrid();
    if (id === 'pg-emp-notices') renderEmpNoticesGrid();
    if (id === 'pg-emp-contracts') renderEmpContractsGrid();
    if (id === 'pg-emp-advances') renderEmpAdvancesGrid();
    if (id === 'pg-payroll') renderPayrollMasterGrid();
    if (id === 'pg-academic-calendar') renderAcademicCalendar();
    if (id === 'pg-classrooms') renderClassroomsGrid();
    if (id === 'pg-student-docs') renderStudentDocs();
    if (id === 'pg-section-distribution') renderSectionDistributionWorkspace();
    if (id === 'pg-discontinued') renderDiscontinuedList();
    if (id === 'pg-class-notes') renderClassNotesTimeline();
    if (id === 'pg-enrollment') renderEnrollmentList();
    if (id === 'pg-operation-lock') renderOperationLock();
    if (id === 'pg-chart-accounts') renderChartAccountsTree();
    if (id === 'pg-cashboxes') renderCashboxes();
    if (id === 'pg-cost-centers') renderCostCenters();
    if (id === 'pg-account-ceiling') renderAccountCeiling();
    if (id === 'pg-student-account') renderStatementOfAccount();
};
"""

# Replace Master Central Dispatcher
pattern = r'// Master Central Dispatcher for Page Renders.*?\};'
if re.search(pattern, js, re.DOTALL):
    js = re.sub(pattern, master_goto_code.strip(), js, flags=re.DOTALL)
    print("  ✓ Replaced Master Central Dispatcher")
else:
    js += "\n" + master_goto_code.strip() + "\n"
    print("  ✓ Appended Master Central Dispatcher")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Sync HTML cache version
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

print(f"Updated Master goTo Dispatcher for All Pages! Timestamp v={ts}")
