"""
Build Official School Letterhead Print Engine in app.js and style.css
"""
import re, time

print("=" * 60)
print("Building Official School Letterhead Print Engine...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

official_print_engine_js = """
// ==================== OFFICIAL SCHOOL LETTERHEAD PRINT ENGINE ====================
function printOfficialDocument(options) {
    const title = options.title || 'تقرير رسمي';
    const subtitle = options.subtitle || '';
    const schoolName = me?.schoolName || (window.currentSchoolId === 2 ? 'مدارس المستقبل الحديثة' : 'مدرسة المتفوقين الأهلية');
    const academicYear = 'العام الدراسي 2025/2026 - الفصل الثاني';
    const dateStr = new Date().toLocaleDateString('ar-EG', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
    const timeStr = new Date().toLocaleTimeString('ar-EG');
    const issuer = me?.name || me?.username || 'مدير النظام';
    const contentHtml = options.contentHtml || '';

    // Build standalone clean printable HTML string
    const printDoc = `
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="UTF-8">
    <title>${title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        @page {
            size: ${options.landscape ? 'landscape' : 'portrait'};
            margin: 10mm;
        }
        body {
            font-family: 'Cairo', 'Segoe UI', sans-serif;
            background: #fff;
            color: #000;
            margin: 0;
            padding: 0;
            direction: rtl;
            font-size: 10pt;
        }
        /* Official Header / Letterhead */
        .print-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 3px double #1e3a8a;
            padding-bottom: 12px;
            margin-bottom: 16px;
        }
        .header-col {
            flex: 1;
        }
        .header-col.center {
            text-align: center;
        }
        .header-col.left {
            text-align: left;
        }
        .school-logo {
            max-height: 75px;
            object-fit: contain;
        }
        .doc-title-box {
            text-align: center;
            margin-bottom: 16px;
            background: #f1f5f9;
            border: 1px solid #cbd5e1;
            padding: 8px 14px;
            border-radius: 6px;
        }
        .doc-title-box h1 {
            margin: 0;
            font-size: 15pt;
            color: #1e3a8a;
            font-weight: 800;
        }
        .doc-meta-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 16px;
            font-size: 9pt;
        }
        .doc-meta-table td {
            padding: 4px 8px;
            border: 1px solid #cbd5e1;
            background: #f8fafc;
        }
        /* Tables */
        table.print-data-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
            font-size: 9pt;
            page-break-inside: auto;
        }
        table.print-data-table th, table.print-data-table td {
            border: 1px solid #334155;
            padding: 6px 8px;
            text-align: center;
            white-space: normal;
            word-wrap: break-word;
        }
        table.print-data-table th {
            background: #e2e8f0;
            font-weight: 700;
            color: #0f172a;
        }
        table.print-data-table tr:nth-child(even) {
            background: #f8fafc;
        }
        /* Official Signatures Footer */
        .print-footer-signatures {
            margin-top: 30px;
            display: flex;
            justify-content: space-between;
            text-align: center;
            page-break-inside: avoid;
        }
        .sig-box {
            flex: 1;
            padding: 10px;
        }
        .sig-box strong {
            display: block;
            margin-bottom: 40px;
            font-size: 9.5pt;
        }
        .stamp-box {
            border: 2px dashed #94a3b8;
            border-radius: 50%;
            width: 80px;
            height: 80px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #64748b;
            font-size: 7.5pt;
            font-weight: 700;
        }
        .doc-timestamp {
            margin-top: 20px;
            border-top: 1px solid #e2e8f0;
            padding-top: 6px;
            display: flex;
            justify-content: space-between;
            font-size: 8pt;
            color: #64748b;
        }
    </style>
</head>
<body>
    <!-- Official Header / Letterhead -->
    <div class="print-header">
        <div class="header-col">
            <h3 style="margin:0;color:#1e3a8a;font-size:12pt;font-weight:800;">الجمهورية اليمنية</h3>
            <h4 style="margin:2px 0;color:#475569;font-size:10pt;">وزارة التربية والتعليم</h4>
            <h4 style="margin:0;color:#1e3a8a;font-size:11pt;font-weight:800;">${schoolName}</h4>
        </div>
        <div class="header-col center">
            <img src="images/logo.png" alt="الشعار الرسمي" class="school-logo" onerror="this.style.display='none'">
        </div>
        <div class="header-col left">
            <p style="margin:0;font-size:8.5pt;"><strong>التاريخ:</strong> ${dateStr}</p>
            <p style="margin:2px 0;font-size:8.5pt;"><strong>الوقت:</strong> ${timeStr}</p>
            <p style="margin:0;font-size:8.5pt;"><strong>المُصدر:</strong> ${issuer}</p>
        </div>
    </div>

    <!-- Document Title Box -->
    <div class="doc-title-box">
        <h1>${title}</h1>
        ${subtitle ? `<p style="margin:4px 0 0 0;font-size:9.5pt;color:#475569;">${subtitle}</p>` : ''}
    </div>

    <!-- Document Metadata Row -->
    <table class="doc-meta-table">
        <tr>
            <td><strong>العام الدراسي:</strong> ${academicYear}</td>
            <td><strong>المدرسة:</strong> ${schoolName}</td>
            <td><strong>حالة التقرير:</strong> معتمد ورسمي 🟢</td>
        </tr>
    </table>

    <!-- Main Report Data Table Content -->
    ${contentHtml}

    <!-- Official Signatures & Stamp Footer -->
    <div class="print-footer-signatures">
        <div class="sig-box">
            <strong>الموظف المختص / المحرر</strong>
            <span>.....................................</span>
        </div>
        <div class="sig-box">
            <strong>توقيع رئيس القسم</strong>
            <span>.....................................</span>
        </div>
        <div class="sig-box">
            <strong>اعتماد مدير المدرسة والختم</strong>
            <div class="stamp-box">الختم الرسمي</div>
        </div>
    </div>

    <!-- Timestamp Footer -->
    <div class="doc-timestamp">
        <span>تم استخراج هذا التقرير آلياً من نظام إدارة المدارس السحابي - ${schoolName}</span>
        <span>صفحة 1 من 1</span>
    </div>

    <script>
        window.onload = function() {
            setTimeout(function() {
                window.print();
            }, 300);
        };
    </script>
</body>
</html>
    `;

    // Open dedicated hidden print window or printIframe
    let printFrame = document.getElementById('officialPrintFrame');
    if (!printFrame) {
        printFrame = document.createElement('iframe');
        printFrame.id = 'officialPrintFrame';
        printFrame.style.cssText = 'position:fixed;top:-9999px;left:-9999px;width:1px;height:1px;border:none;';
        document.body.appendChild(printFrame);
    }

    const doc = printFrame.contentWindow.document;
    doc.open();
    doc.write(printDoc);
    doc.close();
}
window.printOfficialDocument = printOfficialDocument;
"""

if 'window.printOfficialDocument = printOfficialDocument' not in js:
    js += "\n" + official_print_engine_js + "\n"
    print("  ✓ Appended Official School Letterhead Print Engine to app.js")

# Override window.print or print button triggers to use printOfficialDocument for active page
print_override_js = """
// Override default print behavior to trigger Official Letterhead Document Print
function triggerOfficialPrint() {
    const activePage = document.querySelector('.page.active');
    if (!activePage) return window.print();

    const pageTitle = activePage.querySelector('.page-header h2')?.innerText || 'تقرير رسمي';
    const tableEl = activePage.querySelector('.table-wrapper table') || activePage.querySelector('table');
    
    if (tableEl) {
        // Clone table and strip action columns (edit/delete)
        const tableClone = tableEl.cloneNode(true);
        tableClone.className = 'print-data-table';
        
        // Remove action buttons column from headers and rows
        tableClone.querySelectorAll('th:last-child, td:last-child').forEach(cell => {
            if (cell.innerText.includes('إجراءات') || cell.querySelector('.act') || cell.querySelector('.btn-edit') || cell.querySelector('.btn-delete')) {
                cell.remove();
            }
        });

        printOfficialDocument({
            title: pageTitle,
            subtitle: 'كشف بيانات رسمي معتمد ومتروّس',
            landscape: true,
            contentHtml: tableClone.outerHTML
        });
    } else {
        printOfficialDocument({
            title: pageTitle,
            subtitle: 'مستند رسمي معتمد',
            landscape: false,
            contentHtml: activePage.innerHTML
        });
    }
}
window.triggerOfficialPrint = triggerOfficialPrint;
"""

if 'window.triggerOfficialPrint = triggerOfficialPrint' not in js:
    js += "\n" + print_override_js + "\n"
    print("  ✓ Appended triggerOfficialPrint function to app.js")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js with Official Print Engine!")
