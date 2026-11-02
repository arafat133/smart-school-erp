import os
import re

app_js_path = r"c:\Users\LENOVO\Desktop\stu\secure_school_system\frontend\app.js"

with open(app_js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Global Variables
global_vars = """
let currentScheduleTerm = 'الفصل الدراسي الأول';
let currentExamTerm = 'الفصل الدراسي الأول';
let pendingTermTargetPage = null;

function promptTermSelection(targetPageId) {
    pendingTermTargetPage = targetPageId;
    const m = document.getElementById('termModal');
    if (m) m.classList.add('active');
}

function selectTerm(termName) {
    if (pendingTermTargetPage === 'pg-schedule') currentScheduleTerm = termName;
    else if (pendingTermTargetPage === 'pg-exam-schedule') currentExamTerm = termName;
    const m = document.getElementById('termModal');
    if (m) m.classList.remove('active');
    if (pendingTermTargetPage) goTo(pendingTermTargetPage);
}
"""

if "let currentScheduleTerm" not in content:
    content = global_vars + "\n" + content

# 2. Update goTo function
goto_replacements = """
if (id === 'pg-schedule') { promptTermSelection('pg-schedule'); renderSchedule(); }
if (id === 'pg-exam-schedule') { promptTermSelection('pg-exam-schedule'); renderExamSchedule(); }
"""

content = re.sub(r"if\s*\(\s*id\s*===\s*'pg-schedule'\s*\)\s*renderSchedule\(\s*\);", "", content)
content = re.sub(r"if\s*\(\s*id\s*===\s*'pg-exam-schedule'\s*\)\s*renderExamSchedule\(\s*\);", "", content)

new_pages = """
if (id === 'pg-db-management') renderDbManagement();
if (id === 'pg-operation-lock') renderOperationLock();
if (id === 'pg-system-settings') renderSystemSettings();
if (id === 'pg-alerts') renderAlerts();
if (id === 'pg-archive') renderArchive();
if (id === 'pg-change-password') renderChangePassword();
if (id === 'pg-posting') renderPosting();
if (id === 'pg-currencies') renderCurrencies();
if (id === 'pg-cost-centers') renderCostCenters();
if (id === 'pg-account-ceiling') renderAccountCeiling();
if (id === 'pg-cashbox-inventory') renderCashboxInventory();
if (id === 'pg-closings') renderClosings();
if (id === 'pg-banks') renderBanks();
if (id === 'pg-checks') renderChecks();
if (id === 'pg-balance-sheet') renderBalanceSheet();
if (id === 'pg-academic-years') renderAcademicYears();
if (id === 'pg-departments') renderDepartments();
if (id === 'pg-required-docs') renderRequiredDocs();
if (id === 'pg-nationalities') renderNationalities();
if (id === 'pg-violations-catalog') renderViolationsCatalog();
if (id === 'pg-visitors') renderVisitors();
if (id === 'pg-academic-calendar') renderAcademicCalendar();
if (id === 'pg-classrooms') renderClassrooms();
if (id === 'pg-grade-progression') renderGradeProgression();
if (id === 'pg-subject-distribution') renderSubjectDistribution();
if (id === 'pg-grade-types') renderGradeTypes();
if (id === 'pg-grade-ratings') renderGradeRatings();
if (id === 'pg-fee-categories') renderFeeCategories();
if (id === 'pg-discount-categories') renderDiscountCategories();
if (id === 'pg-installment-plans') renderInstallmentPlans();
if (id === 'pg-grade-fees') renderGradeFees();
if (id === 'pg-parents') renderParents();
if (id === 'pg-student-docs') renderStudentDocs();
if (id === 'pg-section-distribution') renderSectionDistribution();
if (id === 'pg-discontinued') renderDiscontinued();
if (id === 'pg-behavior') renderBehavior();
if (id === 'pg-class-notes') renderClassNotes();
if (id === 'pg-guarantors') renderGuarantors();
if (id === 'pg-teacher-subjects') renderTeacherSubjects();
if (id === 'pg-emp-notices') renderEmpNotices();
if (id === 'pg-exam-halls') renderExamHalls();
if (id === 'pg-seat-numbers') renderSeatNumbers();
if (id === 'pg-secret-numbers') renderSecretNumbers();
if (id === 'pg-hall-distribution') renderHallDistribution();
if (id === 'pg-roll-call') renderRollCall();
if (id === 'pg-seat-cards') renderSeatCards();
if (id === 'pg-substitute') renderSubstitute();
if (id === 'pg-activity-types') renderActivityTypes();
if (id === 'pg-activity-supervisors') renderActivitySupervisors();
if (id === 'pg-activity-enrollment') renderActivityEnrollment();
if (id === 'pg-activity-reports') renderActivityReports();
if (id === 'pg-transport-routes') renderTransportRoutes();
if (id === 'pg-buses') renderBuses();
if (id === 'pg-transport-enrollment') renderTransportEnrollment();
if (id === 'pg-demand-letters') renderDemandLetters();
if (id === 'pg-item-categories') renderItemCategories();
if (id === 'pg-inventory-items') renderInventoryItems();
if (id === 'pg-supply-orders') renderSupplyOrders();
if (id === 'pg-issue-orders') renderIssueOrders();
if (id === 'pg-suppliers') renderSuppliers();
if (id === 'pg-inventory-reports') renderInventoryReports();
if (id === 'pg-sms-settings') renderSmsSettings();
if (id === 'pg-sms-send') renderSmsSend();
if (id === 'pg-sms-templates') renderSmsTemplates();
if (id === 'pg-sms-balance') renderSmsBalance();
if (id === 'pg-monthly-report') renderMonthlyReport();
if (id === 'pg-semester-report') renderSemesterReport();
if (id === 'pg-class-details') renderClassDetails();
if (id === 'pg-top-students') renderTopStudents();
if (id === 'pg-success-rate-subject') renderSuccessRateSubject();
if (id === 'pg-success-rate-section') renderSuccessRateSection();
if (id === 'pg-control-reports') renderControlReports();
if (id === 'pg-admin-messages') renderAdminMessages();
if (id === 'pg-shortcuts') renderShortcuts();
if (id === 'pg-faq') renderFaq();
if (id === 'pg-dictionary') renderDictionary();
if (id === 'pg-personal-info') renderPersonalInfo();
"""

goto_match = re.search(r'(function\s+goTo\s*\([^\)]*\)\s*\{[^\}]*)(\})', content)
if goto_match:
    if "if (id === 'pg-db-management')" not in content:
        new_goto = goto_match.group(1) + goto_replacements + new_pages + "\n" + goto_match.group(2)
        content = content[:goto_match.start()] + new_goto + content[goto_match.end():]

# 3 & 4. Enhanced renderSchedule & renderExamSchedule
schedule_func = """
function renderSchedule() {
    const termBadge = document.getElementById('schedule-term-badge');
    if (termBadge) termBadge.textContent = currentScheduleTerm;
    
    const tb = document.getElementById('tbl-schedule');
    if (!tb) return;
    tb.innerHTML = '';
    if (!DB.schedule) DB.schedule = [];
    
    let filtered = DB.schedule.filter(s => s.term === currentScheduleTerm);
    
    const days = ['السبت', 'الأحد', 'الاثنين', 'الثلاثاء', 'الأربعاء'];
    days.forEach(day => {
        let row = `<tr><td>${day}</td>`;
        for (let p=1; p<=7; p++) {
            let entry = filtered.find(s => s.day === day && parseInt(s.period) === p);
            if (entry) {
                row += `<td>${entry.subject}<br><small>${entry.teacher}</small></td>`;
            } else {
                row += `<td>-</td>`;
            }
        }
        row += `<td>
            <button class="btn-edit" onclick="editItem('schedule_day', '${day}')"><i class="fa-solid fa-pen"></i></button>
        </td></tr>`;
        tb.innerHTML += row;
    });
}
"""

exam_schedule_func = """
function renderExamSchedule() {
    const termBadge = document.getElementById('exam-term-badge');
    if (termBadge) termBadge.textContent = currentExamTerm;
    
    const tb = document.getElementById('tbl-exam-schedule');
    if (!tb) return;
    tb.innerHTML = '';
    if (!DB.exams) DB.exams = [];
    
    let filtered = DB.exams.filter(e => e.term === currentExamTerm);
    
    filtered.forEach(item => {
        tb.innerHTML += `<tr>
            <td>${item.term || ''}</td>
            <td>${item.examType || ''}</td>
            <td>${item.grade || ''}</td>
            <td>${item.section || ''}</td>
            <td>${item.subject || ''}</td>
            <td>${item.date || ''}</td>
            <td>${item.time || ''}</td>
            <td>${item.hall || ''}</td>
            <td><div class="act">
                <button class="btn-edit" onclick="editItem('exam_schedule',${item.id})"><i class="fa-solid fa-pen"></i></button>
                <button class="btn-delete" onclick="delItem('exam_schedule',${item.id},'${item.subject}')"><i class="fa-solid fa-trash"></i></button>
            </div></td>
        </tr>`;
    });
}
"""

content = re.sub(r'function\s+renderSchedule\s*\(\s*\)\s*\{[\s\S]*?\n\}', schedule_func, content, count=1)
content = re.sub(r'function\s+renderExamSchedule\s*\(\s*\)\s*\{[\s\S]*?\n\}', exam_schedule_func, content, count=1)

# 5. Enhanced openForm and saveForm
open_form_replacements = """
        if (type === 'schedule') {
            document.getElementById('form-fields').innerHTML = `
                <div class="form-group">
                    <label>الفصل الدراسي</label>
                    <select id="f-term" required><option>الفصل الدراسي الأول</option><option>الفصل الدراسي الثاني</option></select>
                </div>
                <div class="form-group"><label>الصف</label><select id="f-grade" required>` + (DB.stages||[]).map(s=>`<option>${s.name}</option>`).join('') + `</select></div>
                <div class="form-group"><label>الشعبة</label><select id="f-section" required>` + (DB.sections||[]).map(s=>`<option>${s.name}</option>`).join('') + `</select></div>
                <div class="form-group"><label>اليوم</label><select id="f-day" required><option>السبت</option><option>الأحد</option><option>الاثنين</option><option>الثلاثاء</option><option>الأربعاء</option></select></div>
                <div class="form-group"><label>الحصة</label><select id="f-period" required>` + [1,2,3,4,5,6,7].map(p=>`<option>${p}</option>`).join('') + `</select></div>
                <div class="form-group"><label>المادة</label><select id="f-subject" required>` + (DB.subjects||[]).map(s=>`<option>${s.name}</option>`).join('') + `</select></div>
                <div class="form-group"><label>المعلم</label><select id="f-teacher" required>` + (DB.employees||[]).map(e=>`<option>${e.name}</option>`).join('') + `</select></div>
            `;
        } else if (type === 'exam_schedule') {
            document.getElementById('form-fields').innerHTML = `
                <div class="form-group"><label>الفصل الدراسي</label><select id="f-term" required><option>الفصل الدراسي الأول</option><option>الفصل الدراسي الثاني</option></select></div>
                <div class="form-group"><label>نوع الامتحان</label><select id="f-examType" required><option>اختبارات شهرية</option><option>اختبارات نهاية الفصل الدراسي</option></select></div>
                <div class="form-group"><label>الصف</label><select id="f-grade" required>` + (DB.stages||[]).map(s=>`<option>${s.name}</option>`).join('') + `</select></div>
                <div class="form-group"><label>الشعبة</label><select id="f-section" required>` + (DB.sections||[]).map(s=>`<option>${s.name}</option>`).join('') + `</select></div>
                <div class="form-group"><label>المادة</label><select id="f-subject" required>` + (DB.subjects||[]).map(s=>`<option>${s.name}</option>`).join('') + `</select></div>
                <div class="form-group"><label>التاريخ</label><input type="date" id="f-date" required></div>
                <div class="form-group"><label>الوقت</label><input type="time" id="f-time" required></div>
                <div class="form-group"><label>القاعة/ملاحظات</label><input type="text" id="f-hall" required></div>
            `;
        }
"""

open_form_match = re.search(r'function\s+openForm\s*\([^)]*\)\s*\{', content)
if open_form_match:
    insert_pos = open_form_match.end()
    content = content[:insert_pos] + open_form_replacements + content[insert_pos:]

save_form_replacements = """
        if (currentFormType === 'schedule') {
            const newItem = {
                id: document.getElementById('f-id') ? document.getElementById('f-id').value : Date.now(),
                term: document.getElementById('f-term').value,
                grade: document.getElementById('f-grade').value,
                section: document.getElementById('f-section').value,
                day: document.getElementById('f-day').value,
                period: document.getElementById('f-period').value,
                subject: document.getElementById('f-subject').value,
                teacher: document.getElementById('f-teacher').value
            };
            if(!DB.schedule) DB.schedule = [];
            let idx = DB.schedule.findIndex(x => x.id == newItem.id);
            if(idx > -1) DB.schedule[idx] = newItem; else DB.schedule.push(newItem);
            renderSchedule();
        } else if (currentFormType === 'exam_schedule') {
            const newItem = {
                id: document.getElementById('f-id') ? document.getElementById('f-id').value : Date.now(),
                term: document.getElementById('f-term').value,
                examType: document.getElementById('f-examType').value,
                grade: document.getElementById('f-grade').value,
                section: document.getElementById('f-section').value,
                subject: document.getElementById('f-subject').value,
                date: document.getElementById('f-date').value,
                time: document.getElementById('f-time').value,
                hall: document.getElementById('f-hall').value
            };
            if(!DB.exams) DB.exams = [];
            let idx = DB.exams.findIndex(x => x.id == newItem.id);
            if(idx > -1) DB.exams[idx] = newItem; else DB.exams.push(newItem);
            renderExamSchedule();
        }
"""
content = re.sub(r"if\s*\(\s*currentFormType\s*===\s*'schedule'\s*\)\s*\{[\s\S]*?\}", "", content)
content = re.sub(r"else\s+if\s*\(\s*currentFormType\s*===\s*'exam_schedule'\s*\)\s*\{[\s\S]*?\}", "", content)
content = re.sub(r"if\s*\(\s*currentFormType\s*===\s*'exam_schedule'\s*\)\s*\{[\s\S]*?\}", "", content)

save_form_match = re.search(r'function\s+saveForm\s*\([^)]*\)\s*\{', content)
if save_form_match:
    insert_pos = save_form_match.end()
    content = content[:insert_pos] + save_form_replacements + content[insert_pos:]

# 6. DB Demo Data
db_additions = """
DB.schedule = DB.schedule || [{id:1, term:'الفصل الدراسي الأول', grade:'الأول', section:'أ', day:'السبت', period:1, subject:'رياضيات', teacher:'أحمد'}];
DB.exams = DB.exams || [{id:1, term:'الفصل الدراسي الأول', examType:'اختبارات شهرية', grade:'الأول', section:'أ', subject:'رياضيات', date:'2025-10-10', time:'08:00', hall:'قاعة 1'}];
DB.academic_years = DB.academic_years || [{id:1, name:'2025-2026', isCurrent: true}];
DB.departments = DB.departments || [{id:1, name:'بنين'}, {id:2, name:'بنات'}];
DB.class_times = DB.class_times || [{id:1, period:1, from:'07:30', to:'08:15'}];
DB.nationalities = DB.nationalities || [{id:1, name:'يمني'}, {id:2, name:'سعودي'}];
DB.violations_catalog = DB.violations_catalog || [{id:1, name:'تأخر عن الحصة', severity:'خفيف'}];
DB.exam_halls = DB.exam_halls || [{id:1, name:'قاعة 1', capacity:30}];
DB.item_categories = DB.item_categories || [{id:1, name:'زي مدرسي'}, {id:2, name:'كتب'}, {id:3, name:'قرطاسية'}];
DB.inventory_items = DB.inventory_items || [{id:1, name:'قميص مدرسي - مقاس M', category:'زي مدرسي', qty:150, price:5000}];
DB.suppliers = DB.suppliers || [{id:1, name:'مؤسسة النور للقرطاسية', phone:'777111222'}];
DB.buses = DB.buses || [{id:1, name:'حافلة رقم 1', plate:'1234-أب', driver:'سالم عبدالله', capacity:25}];
DB.sms_templates = DB.sms_templates || [{id:1, name:'قالب المطالبة', text:'السلام عليكم، يرجى سداد الرسوم المتبقية للطالب {student_name}'}];
DB.admin_messages = DB.admin_messages || [{id:1, title:'إعلان هام', text:'غداً إجازة رسمية', priority:'عاجل', date:'2025-10-01'}];
"""

if "DB.academic_years" not in content:
    content += "\n" + db_additions + "\n"

# 7. Render functions for all new pages
pages = [
"DbManagement", "UserGroups", "Permissions", "OperationLock", "ProtectedGroups", "SystemSettings", "Alerts", "Archive",
"ChangePassword", "Posting", "Currencies", "CostCenters", "AccountCeiling", "SimpleEntry", "DoubleEntry", "CashboxInventory",
"Closings", "Banks", "Checks", "BalanceSheet", "AcademicYears", "Departments", "ClassTimes", "RequiredDocs", "Nationalities",
"ViolationsCatalog", "Visitors", "AcademicCalendar", "Classrooms", "GradeProgression", "SubjectDistribution", "GradeTypes",
"GradeRatings", "FeeCategories", "DiscountCategories", "InstallmentPlans", "GradeFees", "StudentRegister", "SimpleRegister",
"Parents", "StudentDocs", "SectionDistribution", "Discontinued", "Behavior", "ClassNotes", "Guarantors", "TeacherSubjects",
"EmpNotices", "MonthlyGrades", "TermGrades", "ExamHalls", "SeatNumbers", "SecretNumbers", "HallDistribution", "RollCall",
"SeatCards", "Substitute", "ActivityTypes", "ActivitySupervisors", "ActivityEnrollment", "ActivityReports", "TransportRoutes",
"Buses", "TransportEnrollment", "DemandLetters", "ItemCategories", "InventoryItems", "SupplyOrders", "IssueOrders", "Suppliers",
"InventoryReports", "SmsSettings", "SmsSend", "SmsTemplates", "SmsBalance", "MonthlyReport", "SemesterReport", "ClassDetails",
"TopStudents", "SuccessRateSubject", "SuccessRateSection", "AttendanceReports", "ControlReports", "AdminMessages", "Shortcuts",
"Faq", "Dictionary", "PersonalInfo"
]

def camel_to_snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\\1_\\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\\1_\\2', s1).lower()

render_funcs = ""
for page in pages:
    page_snake = camel_to_snake(page)
    if f"function render{page}()" not in content:
        if page in ["DbManagement", "ChangePassword", "SystemSettings", "Shortcuts", "Faq", "SmsBalance"]:
            render_funcs += f"function render{page}() {{ console.log('render{page}'); }}\n"
        elif page == "AdminMessages":
            render_funcs += f"""
function render{page}() {{
    const tb = document.getElementById('tbl-{page_snake.replace('_', '-')}');
    if (!tb) return;
    tb.innerHTML = '';
    if (!DB.admin_messages) DB.admin_messages = [];
    DB.admin_messages.forEach(item => {{
        tb.innerHTML += `<tr>
            <td>${{item.title || ''}}</td>
            <td>${{item.priority || ''}}</td>
            <td><div class="act">
                <button class="btn-edit" onclick="editItem('admin_messages',${{item.id}})"><i class="fa-solid fa-pen"></i></button>
                <button class="btn-delete" onclick="delItem('admin_messages',${{item.id}},'${{item.title}}')"><i class="fa-solid fa-trash"></i></button>
            </div></td>
        </tr>`;
    }});
}}\n"""
        else:
            render_funcs += f"""
function render{page}() {{
    const tb = document.getElementById('tbl-{page_snake.replace('_', '-')}');
    if (!tb) return;
    tb.innerHTML = '';
    const db_key = '{page_snake}';
    if (!DB[db_key]) DB[db_key] = [];
    DB[db_key].forEach(item => {{
        tb.innerHTML += `<tr>
            <td>${{item.name || ''}}</td>
            <td>${{item.field2 || ''}}</td>
            <td><div class="act">
                <button class="btn-edit" onclick="editItem('${{db_key}}',${{item.id}})"><i class="fa-solid fa-pen"></i></button>
                <button class="btn-delete" onclick="delItem('${{db_key}}',${{item.id}},'${{item.name || ''}}')"><i class="fa-solid fa-trash"></i></button>
            </div></td>
        </tr>`;
    }});
}}\n"""

content += render_funcs

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Modified app.js successfully.")
