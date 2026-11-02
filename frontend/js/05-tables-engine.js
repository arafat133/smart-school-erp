
// ============================================================================
// Universal Table Row Long-Press Handler (Touch & Mouse)
// ============================================================================
(function initLongPressEngine() {
    let longPressTimer = null;
    let isLongPressTriggered = false;

    function startPress(e) {
        const row = e.target.closest('tr');
        if (!row || e.target.closest('button') || e.target.closest('input') || e.target.closest('select') || e.target.closest('a')) return;
        
        isLongPressTriggered = false;
        const coll = row.getAttribute('data-collection') || 'postingBatches';
        const id = row.getAttribute('data-id') || row.querySelector('code')?.textContent?.trim() || row.cells[1]?.textContent?.trim();

        if (!id) return;

        longPressTimer = setTimeout(() => {
            isLongPressTriggered = true;
            if (navigator.vibrate) navigator.vibrate(50);
            if (typeof deleteItem === 'function') {
                deleteItem(coll, id);
            }
        }, 550);
    }

    function cancelPress() {
        if (longPressTimer) {
            clearTimeout(longPressTimer);
            longPressTimer = null;
        }
    }

    document.addEventListener('touchstart', startPress, { passive: true });
    document.addEventListener('touchend', cancelPress, { passive: true });
    document.addEventListener('touchmove', cancelPress, { passive: true });

    document.addEventListener('mousedown', (e) => {
        if (e.button === 0) startPress(e); // Left click hold
    });
    document.addEventListener('mouseup', cancelPress);
    document.addEventListener('mousemove', cancelPress);
})();

/**
 * ============================================================================
 * 05-TABLES-ENGINE.JS - Universal Table Interactions (DblClick & LongPress)
 * ============================================================================
 */
(function initUniversalTableInteractionsEngine() {
    const tableToEntityMap = {
        'tbl-students-grid': { entity: 'student', coll: 'students' },
        'tbl-students': { entity: 'student', coll: 'students' },
        'tbl-employees-grid': { entity: 'employee', coll: 'employees' },
        'tbl-employees': { entity: 'employee', coll: 'employees' },
        'tbl-users-grid': { entity: 'user', coll: 'users' },
        'tbl-vouchers-grid': { entity: 'voucher', coll: 'vouchers' },
        'tbl-journal-entries-grid': { entity: 'journal', coll: 'journalEntries' },
        'tbl-banks-grid': { entity: 'banks', coll: 'banks' },
        'tbl-checks-grid': { entity: 'checks', coll: 'checks' },
        'tbl-account-ceiling-grid': { entity: 'account-ceiling', coll: 'accountCeiling' },
        'tbl-demand-letters-grid': { entity: 'demand_letters', coll: 'demandLetters' },
        'tbl-academic-calendar-grid': { entity: 'academic-calendar', coll: 'calendar' },
        'tbl-subject-distribution-grid': { entity: 'subject-distribution', coll: 'subjectDistribution' },
        'tbl-classrooms-grid': { entity: 'classrooms', coll: 'classrooms' },
        'tbl-class-times-grid': { entity: 'class-times', coll: 'classTimes' },
        'tbl-discount-categories-grid': { entity: 'discount-categories', coll: 'discounts' },
        'tbl-installment-plans-grid': { entity: 'installment-plans', coll: 'installmentPlans' },
        'tbl-required-docs-grid': { entity: 'required-docs', coll: 'requiredDocs' },
        'tbl-discontinued-grid': { entity: 'discontinued', coll: 'discontinued' },
        'tbl-guarantors-grid': { entity: 'guarantors', coll: 'guarantors' },
        'tbl-emp-contracts-grid': { entity: 'contracts', coll: 'contracts' },
        'tbl-emp-advances-grid': { entity: 'advances', coll: 'advances' },
        'tbl-performance-grid': { entity: 'performance', coll: 'performance' },
        'tbl-activities-grid': { entity: 'activities', coll: 'activities' },
        'tbl-suppliers-grid': { entity: 'suppliers', coll: 'suppliers' },
        'tbl-faq-articles-grid': { entity: 'faq', coll: 'faq' },
        'tbl-operation-lock': { entity: 'operation-lock', coll: 'operationLocks' },
        'tbl-system-settings-grid': { entity: 'system_settings', coll: 'systemSettingsData' },
        'tbl-alerts-grid': { entity: 'alerts', coll: 'alertsData' }
    };

    function resolveTableMapping(tr) {
        if (!tr) return null;
        const tbody = tr.closest('tbody');
        if (tbody && tbody.id && tableToEntityMap[tbody.id]) {
            return tableToEntityMap[tbody.id];
        }
        const page = tr.closest('.page');
        if (page && page.id) {
            const pageMap = {
                'pg-students': { entity: 'student', coll: 'students' },
                'pg-employees': { entity: 'employee', coll: 'employees' },
                'pg-users': { entity: 'user', coll: 'users' },
                'pg-vouchers': { entity: 'voucher', coll: 'vouchers' },
                'pg-banks': { entity: 'banks', coll: 'banks' },
                'pg-checks': { entity: 'checks', coll: 'checks' },
                'pg-account-ceiling': { entity: 'account-ceiling', coll: 'accountCeiling' },
                'pg-demand-letters': { entity: 'demand_letters', coll: 'demandLetters' },
                'pg-academic-calendar': { entity: 'academic-calendar', coll: 'calendar' },
                'pg-subject-distribution': { entity: 'subject-distribution', coll: 'subjectDistribution' },
                'pg-classrooms': { entity: 'classrooms', coll: 'classrooms' },
                'pg-class-times': { entity: 'class-times', coll: 'classTimes' },
                'pg-discount-categories': { entity: 'discount-categories', coll: 'discounts' },
                'pg-installment-plans': { entity: 'installment-plans', coll: 'installmentPlans' },
                'pg-required-docs': { entity: 'required-docs', coll: 'requiredDocs' },
                'pg-discontinued': { entity: 'discontinued', coll: 'discontinued' },
                'pg-guarantors': { entity: 'guarantors', coll: 'guarantors' },
                'pg-emp-contracts': { entity: 'contracts', coll: 'contracts' },
                'pg-emp-advances': { entity: 'advances', coll: 'advances' },
                'pg-performance-eval': { entity: 'performance', coll: 'performance' },
                'pg-activities': { entity: 'activities', coll: 'activities' },
                'pg-suppliers': { entity: 'suppliers', coll: 'suppliers' },
                'pg-faq': { entity: 'faq', coll: 'faq' },
                'pg-operation-lock': { entity: 'operation-lock', coll: 'operationLocks' },
                'pg-system-settings': { entity: 'system_settings', coll: 'systemSettingsData' },
                'pg-alerts': { entity: 'alerts', coll: 'alertsData' }
            };
            if (pageMap[page.id]) return pageMap[page.id];
        }
        return null;
    }

    function findRowItemInDB(tr, collKey) {
        if (!window.DB || !window.DB[collKey]) return null;
        const list = window.DB[collKey];
        if (!Array.isArray(list) || list.length === 0) return null;

        const cells = Array.from(tr.cells || []).map(c => c.textContent.trim().toLowerCase());
        const matched = list.find(item => {
            const idVal = String(item.id || item.code || item.keyId || '').trim().toLowerCase();
            const nameVal = String(item.name || item.studentName || item.employeeName || item.title || item.nameArEn || '').trim().toLowerCase();
            return cells.some(c => (idVal && (c === idVal || c.includes(idVal))) || (nameVal && (c === nameVal || c.includes(nameVal))));
        });

        if (matched) return matched;
        const rowIndex = tr.rowIndex ? tr.rowIndex - 1 : 0;
        return list[rowIndex] || list[0];
    }

    window.attachUniversalRowInteractions = function() {
        const rows = document.querySelectorAll('table tbody tr');
        rows.forEach(tr => {
            if (tr.dataset.smartBound === 'true') return;
            tr.dataset.smartBound = 'true';
            tr.style.cursor = 'pointer';

            const mapping = resolveTableMapping(tr);
            if (!mapping) return;

            tr.title = '💡 انقر مرتين للتعديل، أو اضغط مطولاً / انقر باليمين للحذف';

            tr.addEventListener('dblclick', function(e) {
                if (e.target.closest('button, input, select, textarea, a, label')) return;
                const matched = findRowItemInDB(tr, mapping.coll);
                if (matched && (matched.id || matched.code || matched.keyId)) {
                    const idToPass = matched.id || matched.code || matched.keyId;
                    if (typeof window.openForm === 'function') {
                        window.openForm(mapping.entity, idToPass);
                    }
                } else if (typeof window.openForm === 'function') {
                    window.openForm(mapping.entity);
                }
            });

            let pressTimer = null;
            const triggerDelete = function() {
                const matched = findRowItemInDB(tr, mapping.coll);
                const displayName = matched ? (matched.name || matched.studentName || matched.employeeName || matched.title || matched.id || 'هذا السجل') : 'هذا السجل';
                
                if (confirm(`❓ هل أنت متأكد من رغبتك في حذف (${displayName}) نهائياً من النظام؟`)) {
                    if (matched && window.DB && window.DB[mapping.coll]) {
                        const idx = window.DB[mapping.coll].findIndex(x => x === matched || (x.id && x.id === matched.id));
                        if (idx !== -1) {
                            window.DB[mapping.coll].splice(idx, 1);
                        }
                    }
                    tr.style.transition = 'all 0.3s ease';
                    tr.style.opacity = '0';
                    tr.style.transform = 'scale(0.95)';
                    setTimeout(() => {
                        tr.remove();
                        toast(`🗑️ تم بنجاح حذف السجل: (${displayName})!`);
                        if (typeof hydrateAndMountAllGrids === 'function') hydrateAndMountAllGrids();
                    }, 300);
                }
            };

            const startPress = function(e) {
                if (e.target.closest('button, input, select, textarea, a, label')) return;
                if (pressTimer) clearTimeout(pressTimer);
                pressTimer = setTimeout(() => {
                    triggerDelete();
                }, 600);
            };

            const cancelPress = function() {
                if (pressTimer) {
                    clearTimeout(pressTimer);
                    pressTimer = null;
                }
            };

            tr.addEventListener('mousedown', startPress);
            tr.addEventListener('mouseup', cancelPress);
            tr.addEventListener('mouseleave', cancelPress);
            tr.addEventListener('touchstart', startPress, { passive: true });
            tr.addEventListener('touchend', cancelPress);
            tr.addEventListener('touchcancel', cancelPress);

            tr.addEventListener('contextmenu', function(e) {
                if (e.target.closest('button, input, select, textarea, a, label')) return;
                e.preventDefault();
                triggerDelete();
            });
        });
    };

    setInterval(() => {
        if (typeof window.attachUniversalRowInteractions === 'function') {
            window.attachUniversalRowInteractions();
        }
    }, 1000);

    setTimeout(() => {
        window.attachUniversalRowInteractions();
    }, 300);
})();


/* ===== MASTER UNIVERSAL TABLE ALIGNMENT & RENDERER ENGINE ===== */
(function initMasterTableAlignerEngine() {
    window.renderTableGridSmart = function(tableOrTbodyId, collectionKey, customColumnMapper) {
        const tb = document.getElementById(tableOrTbodyId);
        if (!tb) return;

        const table = tb.closest('table');
        if (!table) return;

        const ths = Array.from(table.querySelectorAll('thead th'));
        if (ths.length === 0) return;

        const thTexts = ths.map(th => th.textContent.trim().replace(/\s+/g, ' '));
        const thCount = ths.length;

        // Fetch data array from window.DB
        let data = [];
        if (Array.isArray(collectionKey)) {
            data = collectionKey;
        } else if (window.DB && window.DB[collectionKey]) {
            data = window.DB[collectionKey];
        } else if (window.DB) {
            const keyMap = {
                'users': window.DB.users || window.DB.usersData,
                'students': window.DB.students || window.DB.studentsData,
                'employees': window.DB.employees || window.DB.employeesData,
                'vouchers': window.DB.vouchers || window.DB.vouchersData,
                'journal': window.DB.journalEntries,
                'stages': window.DB.stages,
                'sections': window.DB.sections,
                'subjects': window.DB.subjects,
                'parents': window.DB.parents,
                'activities': window.DB.activities,
                'operation-lock': window.DB.operationLocks,
                'system-settings': window.DB.systemSettingsData,
                'alerts': window.DB.alertsData,
                'archive': window.DB.archiveDocs,
                'audit': window.DB.auditTrailData || window.DB.auditLogs,
                'backup': window.DB.backupHistory
            };
            data = keyMap[collectionKey] || window.DB[collectionKey] || [];
        }

        if (!Array.isArray(data)) data = [];

        // Generate rows with EXACT match to thCount
        const rowsHtml = data.map((item, idx) => {
            const rowCells = new Array(thCount).fill('');

            ths.forEach((th, colIdx) => {
                const header = thTexts[colIdx];
                let cellVal = '---';

                // Check custom mapper first
                if (typeof customColumnMapper === 'function') {
                    const customRes = customColumnMapper(item, idx, header, colIdx);
                    if (customRes !== undefined && customRes !== null) {
                        rowCells[colIdx] = customRes;
                        return;
                    }
                }

                // Standard smart mappers by header text
                if (header === '#' || header.includes('م') || header.includes('الترتيب')) {
                    cellVal = `<span style="font-weight:700;color:#94a3b8;text-align:center;">${idx + 1}</span>`;
                } else if (header.includes('كود') || header.includes('رقم السجل') || header.includes('المعرف') || header.includes('الرقم')) {
                    const idVal = item.id || item.code || item.refNo || item.nationalId || ('REC-' + (idx + 101));
                    cellVal = `<span style="font-weight:700;color:#60a5fa;font-family:monospace;"><i class="fa-solid fa-hashtag" style="font-size:0.75rem;color:#38bdf8;"></i> ${idVal}</span>`;
                } else if (header.includes('اسم المستخدم') || header.includes('حساب الدخول')) {
                    cellVal = `<span style="font-weight:800;color:#38bdf8;font-family:monospace;"><i class="fa-solid fa-id-badge" style="color:#60a5fa;"></i> ${item.username || item.nationalId || item.id || '---'}</span>`;
                } else if (header.includes('اسم') || header.includes('الطالب') || header.includes('الموظف') || header.includes('العنوان') || header.includes('البيان')) {
                    const nameVal = item.name || item.studentName || item.employeeName || item.title || item.payer || item.payee || item.description || 'سجل جديد';
                    cellVal = `<span style="font-weight:700;color:#f8fafc;">${nameVal}</span>`;
                } else if (header.includes('نوع') || header.includes('الدور') || header.includes('الرتبة') || header.includes('المسمى')) {
                    const roleVal = item.roleName || item.role || item.type || item.category || 'عام';
                    const isDanger = String(roleVal).includes('مدير') || String(roleVal).includes('Super');
                    const badgeClass = isDanger ? 'badge-danger' : 'badge-info';
                    cellVal = `<span class="badge ${badgeClass}"><i class="fa-solid fa-user-shield"></i> ${roleVal}</span>`;
                } else if (header.includes('قسم') || header.includes('إدارة') || header.includes('الجهة') || header.includes('المرحلة')) {
                    const deptVal = item.dept || item.department || item.stage || item.grade || 'الإدارة العامة';
                    cellVal = `<span style="color:#cbd5e1;font-size:0.85rem;"><i class="fa-solid fa-building" style="color:#a855f7;font-size:0.75rem;"></i> ${deptVal}</span>`;
                } else if (header.includes('هاتف') || header.includes('جوال') || header.includes('تلفون')) {
                    cellVal = `<span style="font-family:monospace;color:#38bdf8;"><i class="fa-solid fa-phone" style="font-size:0.75rem;"></i> ${item.phone || item.guardianPhone || '---'}</span>`;
                } else if (header.includes('بريد') || header.includes('إيميل') || header.includes('Email')) {
                    cellVal = `<span style="color:#94a3b8;font-size:0.82rem;"><i class="fa-solid fa-envelope" style="font-size:0.75rem;"></i> ${item.email || (item.username ? item.username + '@school.edu.ye' : '---')}</span>`;
                } else if (header.includes('حالة') || header.includes('الحالة') || header.includes('الوضع')) {
                    const st = item.status || 'نشط 🟢';
                    const isSuccess = String(st).includes('نشط') || String(st).includes('🟢') || String(st).includes('مكتمل') || String(st).includes('مسموح');
                    const isWarn = String(st).includes('قيد') || String(st).includes('🟡') || String(st).includes('أقساط');
                    const badgeCls = isSuccess ? 'badge-success' : (isWarn ? 'badge-warning' : 'badge-danger');
                    cellVal = `<span class="badge ${badgeCls}"><i class="fa-solid fa-circle-dot"></i> ${st}</span>`;
                } else if (header.includes('تاريخ') || header.includes('التاريخ') || header.includes('تنسيق')) {
                    cellVal = `<span style="font-size:0.8rem;color:#94a3b8;">📅 ${item.date || item.created_at || '2026-08-19'}</span>`;
                } else if (header.includes('واجهات') || header.includes('صلاحيات') || header.includes('عدد')) {
                    const countVal = item.permissions ? (item.permissions.length + ' واجهة 🟢') : (item.allowedPagesCount || 'جميع الواجهات (60+) 🟢');
                    cellVal = `<span class="badge badge-info" style="font-size:0.75rem;"><i class="fa-solid fa-shield-halved"></i> ${countVal}</span>`;
                } else if (header.includes('إجراء') || header.includes('عمليات') || header.includes('خيارات')) {
                    const entityType = collectionKey.replace('tbl-', '').replace('-grid', '');
                    const recId = item.id || item.code || item.username || idx;
                    cellVal = `
                        <div style="display:flex;gap:6px;justify-content:center;">
                            <button class="btn-action btn-edit" title="تعديل" onclick="openForm('${entityType}', '${recId}')"><i class="fa-solid fa-pen-to-square"></i></button>
                            <button class="btn-action btn-delete" title="حذف" onclick="deleteRecord('${entityType}', '${recId}')"><i class="fa-solid fa-trash-can"></i></button>
                        </div>
                    `;
                } else {
                    // Fallback to item property matching header
                    const propVal = item[header] || item[header.toLowerCase()] || item.notes || item.amount || item.balance || '---';
                    cellVal = `<span style="color:#cbd5e1;font-size:0.85rem;">${propVal}</span>`;
                }

                rowCells[colIdx] = `<td>${cellVal}</td>`;
            });

            return `<tr>${rowCells.join('')}</tr>`;
        }).join('');

        tb.innerHTML = rowsHtml;
    };

    // Auto-Hook into hydrateAndMountAllGrids to guarantee 100% alignment across ALL tables
    window.hydrateAndMountAllGrids = function() {
        // Core Grid Renders
                if (typeof renderUsersGrid === 'function') renderUsersGrid();
        if (typeof renderStudentsGrid === 'function') renderStudentsGrid();
        if (typeof renderEmployeesGrid === 'function') renderEmployeesGrid();
        if (typeof renderVouchersGrid === 'function') renderVouchersGrid();
        if (typeof renderJournalGrid === 'function') renderJournalGrid();
        if (typeof renderCostCentersGrid === 'function') renderCostCentersGrid();
        if (typeof renderAccountCeilingGrid === 'function') renderAccountCeilingGrid();
        if (typeof renderCurrenciesGrid === 'function') renderCurrenciesGrid();
        if (typeof renderCashboxInventoryGrid === 'function') renderCashboxInventoryGrid();
        if (typeof renderClosingsGrid === 'function') renderClosingsGrid();
        if (typeof renderBanksGrid === 'function') renderBanksGrid();
        if (typeof renderChecksGrid === 'function') renderChecksGrid();
        if (typeof renderDemandLettersGrid === 'function') renderDemandLettersGrid();
        if (typeof renderFinanceReportsGrid === 'function') renderFinanceReportsGrid();
        if (typeof renderAcademicYearsGrid === 'function') renderAcademicYearsGrid();
        if (typeof renderAcademicCalendarGrid === 'function') renderAcademicCalendarGrid();
        if (typeof renderStagesGrid === 'function') renderStagesGrid();
        if (typeof renderSectionsGrid === 'function') renderSectionsGrid();
        if (typeof renderSubjectsGrid === 'function') renderSubjectsGrid();
        if (typeof renderSubjectDistributionGrid === 'function') renderSubjectDistributionGrid();
        if (typeof renderClassroomsGrid === 'function') renderClassroomsGrid();
        if (typeof renderClassTimesGrid === 'function') renderClassTimesGrid();
        if (typeof renderTimetableBuilderGrid === 'function') renderTimetableBuilderGrid();
        if (typeof renderRequiredDocsGrid === 'function') renderRequiredDocsGrid();
        if (typeof renderFeeCategoriesGrid === 'function') renderFeeCategoriesGrid();
        if (typeof renderDiscountCategoriesGrid === 'function') renderDiscountCategoriesGrid();
        if (typeof renderInstallmentPlansGrid === 'function') renderInstallmentPlansGrid();
        if (typeof renderGradeFeesGrid === 'function') renderGradeFeesGrid();
        if (typeof renderStatementOfAccount === 'function') renderStatementOfAccount();
        if (typeof renderCashboxesGrid === 'function') renderCashboxesGrid();
        if (typeof renderChartAccountsTree === 'function') renderChartAccountsTree();
        if (typeof renderOperationLockGrid === 'function') renderOperationLockGrid();
        if (typeof renderAuditTrailGrid === 'function') renderAuditTrailGrid();
        if (typeof renderBackupHistory === 'function') renderBackupHistory();
        if (typeof renderAlertsGrid === 'function') renderAlertsGrid();
        if (typeof renderSystemSettingsGrid === 'function') renderSystemSettingsGrid();
        if (typeof renderArchiveGrid === 'function') renderArchiveGrid();

        // Universal alignment for all remaining tables
        const allTables = document.querySelectorAll('table tbody[id]');
        allTables.forEach(tb => {
            const tbId = tb.id;
            const collKey = tbId.replace('tbl-', '').replace('-grid', '');
            if (window.DB && (window.DB[collKey] || window.DB[collKey + 's'])) {
                window.renderTableGridSmart(tbId, collKey);
            }
        });

        if (typeof attachUniversalRowInteractions === 'function') {
            attachUniversalRowInteractions();
        }
    };
})();
