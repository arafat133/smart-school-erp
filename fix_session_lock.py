import re, time

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

if 'sessionLockOverlay' not in html:
    lock_overlay = """
    <div class="session-lock" id="sessionLockOverlay">
        <div class="session-lock-box">
            <i class="fa-solid fa-lock" style="font-size:3rem;color:#f59e0b;margin-bottom:16px;"></i>
            <h3 style="margin-bottom:8px;color:#fff;">تم قفل الجلسة تلقائياً</h3>
            <p style="color:#94a3b8;font-size:0.85rem;margin-bottom:18px;">مضت 15 دقيقة من عدم النشاط. أدخل كلمة المرور للمتابعة.</p>
            <input type="password" id="sessionUnlockPass" placeholder="كلمة المرور" style="width:100%;margin-bottom:12px;text-align:center;">
            <button class="btn-add" onclick="unlockSession()" style="width:100%;"><i class="fa-solid fa-unlock"></i> فتح القفل</button>
        </div>
    </div>
"""
    html = html.replace('</body>', lock_overlay + '</body>')

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

print('sessionLockOverlay added and synced! v=' + ts)
