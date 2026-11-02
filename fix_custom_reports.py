import re
import time

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

page = """
    <div class="page" id="pg-custom-reports">
        <div class="page-header">
            <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
            <h2><i class="fa-solid fa-file-invoice"></i> <span data-i18n="title_custom_reports">منشئ التقارير المخصصة (PDF / Excel)</span></h2>
        </div>
        
        <div class="form-card" style="margin-bottom:20px;">
            <h3 style="margin-bottom:15px;color:var(--secondary);font-size:1.1rem;"><i class="fa-solid fa-sliders"></i> <span data-i18n="rep_settings">إعدادات ونطاق التقرير</span></h3>
            
            <div class="form-row">
                <div class="fg">
                    <label><i class="fa-solid fa-database"></i> <span data-i18n="rep_entity">نوع البيانات / الكيان</span></label>
                    <select id="reportEntity" onchange="updateReportColumns()">
                        <option value="students">دليل الطلاب (Students)</option>
                        <option value="employees">دليل الموظفين (Employees)</option>
                        <option value="vouchers">السندات المالية (Financial Vouchers)</option>
                        <option value="attendance">حضور وغياب الطلاب (Attendance)</option>
                        <option value="grades">ترصيد الدرجات والنتائج (Grades)</option>
                    </select>
                </div>
                
                <div class="fg">
                    <label><i class="fa-solid fa-filter"></i> <span data-i18n="rep_stage">المرحلة الدراسية</span></label>
                    <select id="reportStageFilter">
                        <option value="all">جميع المراحل</option>
                        <option value="ابتدائي">الابتدائية</option>
                        <option value="إعدادي">الإعدادية</option>
                        <option value="ثانوي">الثانوية</option>
                    </select>
                </div>
            </div>
            
            <div class="form-row">
                <div class="fg">
                    <label><i class="fa-solid fa-calendar"></i> <span data-i18n="rep_from">من تاريخ</span></label>
                    <input type="date" id="reportDateFrom">
                </div>
                <div class="fg">
                    <label><i class="fa-solid fa-calendar"></i> <span data-i18n="rep_to">إلى تاريخ</span></label>
                    <input type="date" id="reportDateTo">
                </div>
            </div>
            
            <div style="margin-top:10px;">
                <label style="font-weight:700;margin-bottom:8px;display:block;"><i class="fa-solid fa-list-check"></i> <span data-i18n="rep_cols">الأعمدة المراد تضمينها</span></label>
                <div id="reportColumnCheckboxes" style="display:flex;flex-wrap:wrap;gap:12px;background:rgba(0,0,0,0.2);padding:12px;border-radius:9px;border:1px solid var(--border);">
                </div>
            </div>
            
            <div style="display:flex;gap:10px;margin-top:20px;flex-wrap:wrap;">
                <button class="btn-add" onclick="generateCustomReportPreview()" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-eye"></i> <span data-i18n="btn_preview">معاينة التقرير</span></button>
                <button class="btn-add" onclick="exportCustomReportExcel()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-file-excel"></i> <span data-i18n="btn_excel">تصدير Excel</span></button>
                <button class="btn-add" onclick="exportCustomReportPDF()" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-file-pdf"></i> <span data-i18n="btn_pdf">تصدير PDF / طباعة</span></button>
            </div>
        </div>
        
        <div class="table-wrapper" style="position:relative;" id="customReportTableWrapper">
            <div class="spinner-overlay hidden" id="customReportSpinner">
                <div class="glass-spinner"></div>
                <div class="spinner-text">جاري معالجة واستخراج البيانات...</div>
            </div>
            <table>
                <thead id="tbl-custom-reports-head"></thead>
                <tbody id="tbl-custom-reports-body"></tbody>
            </table>
        </div>
    </div>"""

# Add link to sidebar if missing
if 'pg-custom-reports' not in html:
    link = """<a href="#" onclick="goTo('pg-custom-reports')"><i class="fa-solid fa-file-invoice"></i> <span data-i18n="nav_custom_reports">تقارير مخصصة (PDF/Excel)</span></a>\n"""
    html = html.replace("""onclick="goTo('pg-control-reports')">""", """onclick="goTo('pg-custom-reports')"><i class="fa-solid fa-file-invoice"></i> <span data-i18n="nav_custom_reports">تقارير مخصصة (PDF/Excel)</span></a>\n            <a href="#" onclick="goTo('pg-control-reports')">""")
    
    html = html.replace('<!-- ========== MAIN CONTENT ========== -->', '<!-- ========== MAIN CONTENT ========== -->\n' + page)

ts = str(int(time.time()))
html = re.sub(r'style\.css\?v=\d+', 'style.css?v=' + ts, html)
html = re.sub(r'app\.js\?v=\d+', 'app.js?v=' + ts, html)

with open('frontend/school.html', 'w', encoding='utf-8') as fh:
    fh.write(html)
    
admin_html = html.replace('id="userType" value="school"', 'id="userType" value="admin"')
parent_html = html.replace('id="userType" value="school"', 'id="userType" value="parent"')

with open('frontend/admin.html', 'w', encoding='utf-8') as fh:
    fh.write(admin_html)
with open('frontend/parent.html', 'w', encoding='utf-8') as fh:
    fh.write(parent_html)

print('Successfully added pg-custom-reports to school.html!')
