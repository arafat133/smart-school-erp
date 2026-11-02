"""
Fix end of school.html cleanly
"""
import re

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Clean up trailing duplicate div tags before </body>
idx_cr = html.find('id="pg-custom-reports"')

# Find the end of pg-custom-reports page (where the modal starts or main-content ends)
idx_modal = html.find('<!-- ===== MODAL', idx_cr)
if idx_modal == -1:
    idx_modal = html.find('<!-- =====', idx_cr)

cr_sub = html[idx_cr-20:idx_modal]
open_cr = cr_sub.count('<div')
close_cr = cr_sub.count('</div>')
diff_cr = open_cr - close_cr
print(f"pg-custom-reports inside diff: Open {open_cr}, Close {close_cr}, Diff {diff_cr}")

if diff_cr > 0:
    cr_sub += '</div>\n' * diff_cr
elif diff_cr < 0:
    for _ in range(abs(diff_cr)):
        pos = cr_sub.rfind('</div>')
        if pos != -1:
            cr_sub = cr_sub[:pos] + cr_sub[pos+6:]

# Reconstruct HTML cleanly
html_new = html[:idx_cr-20] + cr_sub + """
    </div> <!-- End page-container -->
</div> <!-- End main-content -->
</div> <!-- End app-container -->

</body>
</html>
"""

with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html_new)

admin_html = html_new.replace('id="userType" value="school"', 'id="userType" value="admin"')
parent_html = html_new.replace('id="userType" value="school"', 'id="userType" value="parent"')

with open('frontend/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)
with open('frontend/parent.html', 'w', encoding='utf-8') as f:
    f.write(parent_html)

print("Updated HTML files successfully!")
