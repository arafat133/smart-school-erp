"""
Fix performance_eval_html variable in update_hr_staff_html.py
"""
import re, time

with open('update_hr_staff_html.py', 'r', encoding='utf-8') as f:
    script_text = f.read()

performance_eval_html = """
<div class="page" id="pg-performance-eval">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-star"></i> نظام تقييم الأداء والكفاءة الوظيفية (Performance Appraisal)</h2>
    </div>

    <!-- Executive KPI Summary Cards -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>التقدير العام للدورة</h3><p style="color:#10b981;font-weight:800;font-size:1.2rem;">يتجاوز التوقعات (92.5%)</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>المُقيّمون المكتملون</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">18 / 20 موظف</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info"><h3>مراجعات HR المعلقة</h3><p style="color:#fbbf24;font-weight:800;font-size:1.2rem;">2 نموذج</p></div>
        </div>
    </div>

    <div class="toolbar">
        <select id="evalCycleSelect" onchange="renderPerformanceEvals()" style="width:200px;">
            <option>تقييم النصف الأول 2026</option>
            <option>التقييم السنوي 2025</option>
        </select>
        <button class="btn-add" onclick="openForm('performance_eval')"><i class="fa-solid fa-plus"></i> تقييم جديد</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>المُقيَّم (الموظف)</th>
                    <th>المسمى الوظيفي</th>
                    <th>المُقيّم (المدير)</th>
                    <th>دورة التقييم</th>
                    <th>الدرجة الموزونة</th>
                    <th>التقدير النهائي</th>
                    <th>حالة الاعتماد</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-performance-list"></tbody>
        </table>
    </div>
</div>
"""

script_text = script_text.replace("html = replace_or_add_page(html, 'pg-performance-eval', performance_html)", "performance_html = '''" + performance_eval_html.strip() + "'''\nhtml = replace_or_add_page(html, 'pg-performance-eval', performance_html)")

with open('update_hr_staff_html.py', 'w', encoding='utf-8') as f:
    f.write(script_text)

print("Fixed update_hr_staff_html.py!")
