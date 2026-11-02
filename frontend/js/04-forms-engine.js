

function deleteItem(collectionKey, itemId) {
    if (!collectionKey || !itemId) return;
    window.itemToDelete = { collectionKey, itemId };
    
    const modal = document.getElementById('deleteModal');
    if (modal) {
        const msgEl = document.getElementById('deleteMessage');
        if (msgEl) {
            msgEl.innerHTML = `هل أنت متأكد من رغبتك في حذف السجل <strong style="color:#ef4444;font-family:monospace;">(#${itemId})</strong> نهائياً من النظام؟<br><small style="color:#94a3b8;font-size:0.82rem;margin-top:6px;display:block;">⚠️ لا يمكن التراجع عن هذا الإجراء بعد الحذف.</small>`;
        }
        openModal('deleteModal');
    } else {
        if (confirm(`🗑️ هل أنت متأكد من رغبتك في حذف السجل (#${itemId}) نهائياً؟`)) {
            confirmDelete();
        }
    }
}
window.deleteItem = deleteItem;

function confirmDelete() {
    if (!window.itemToDelete) {
        closeModal('deleteModal');
        return;
    }
    const { collectionKey, itemId } = window.itemToDelete;
    const collKey = typeof getCollectionKey === 'function' ? getCollectionKey(collectionKey) : collectionKey;
    
    if (window.DB && window.DB[collKey]) {
        const initialLen = window.DB[collKey].length;
        window.DB[collKey] = window.DB[collKey].filter(x => 
            String(x.id) !== String(itemId) && 
            String(x.code) !== String(itemId) && 
            String(x.nationalId) !== String(itemId) && 
            String(x.username) !== String(itemId) && 
            String(x.key) !== String(itemId) && 
            String(x.keyId) !== String(itemId)
        );
        
        if (window.DB[collKey].length < initialLen) {
            if (typeof toast === 'function') toast(`🗑️ تم بنجاح حذف السجل (#${itemId}) من النظام!`, 0);
            if (typeof addAudit === 'function') {
                addAudit('حذف سجل', `تم حذف السجل ${itemId} من ${collKey}`, 'النظام', 'تحذير (WARNING) 🟡');
            }
        }
    }
    
    closeModal('deleteModal');
    window.itemToDelete = null;
    
        if (collKey === 'postingBatches' || collKey === 'posting') {
        if (typeof renderPostingGrid === 'function') renderPostingGrid();
    } else if (type === 'currency' || type === 'currencies') {
        if (typeof renderCurrenciesGrid === 'function') renderCurrenciesGrid();
    } else if (type === 'cashbox_inventory' || type === 'cashboxInventory') {
        if (typeof renderCashboxInventoryGrid === 'function') renderCashboxInventoryGrid();
    } else if (type === 'closing' || type === 'closings') {
        if (typeof renderClosingsGrid === 'function') renderClosingsGrid();
    } else if (type === 'banks' || type === 'bank') {
        if (typeof renderBanksGrid === 'function') renderBanksGrid();
    } else if (type === 'checks' || type === 'check') {
        if (typeof renderChecksGrid === 'function') renderChecksGrid();
    } else if (type === 'demand_letters' || type === 'demandLetters') {
        if (typeof renderDemandLettersGrid === 'function') renderDemandLettersGrid();
    } else if (type === 'finance_reports' || type === 'financeReports') {
        if (typeof renderFinanceReportsGrid === 'function') renderFinanceReportsGrid();
    } else if (type === 'academic_years' || type === 'academicYears' || type === 'academic-years') {
        if (typeof renderAcademicYearsGrid === 'function') renderAcademicYearsGrid();
    } else if (type === 'academic_calendar' || type === 'academicCalendar' || type === 'academic-calendar') {
        if (typeof renderAcademicCalendarGrid === 'function') renderAcademicCalendarGrid();
    } else if (type === 'stages' || type === 'stage' || type === 'grades') {
        if (typeof renderStagesGrid === 'function') renderStagesGrid();
    } else if (type === 'sections' || type === 'section') {
        if (typeof renderSectionsGrid === 'function') renderSectionsGrid();
    } else if (type === 'subjects' || type === 'subject') {
        if (typeof renderSubjectsGrid === 'function') renderSubjectsGrid();
    } else if (type === 'subject_distribution' || type === 'subject-distribution' || type === 'subjectDistribution') {
        if (typeof renderSubjectDistributionGrid === 'function') renderSubjectDistributionGrid();
    } else if (type === 'classrooms' || type === 'classroom' || type === 'labs') {
        if (typeof renderClassroomsGrid === 'function') renderClassroomsGrid();
    } else if (type === 'class_times' || type === 'class-times' || type === 'classTimes') {
        if (typeof renderClassTimesGrid === 'function') renderClassTimesGrid();
    } else if (type === 'timetable_builder' || type === 'timetable-builder' || type === 'timetableBuilder') {
        if (typeof renderTimetableBuilderGrid === 'function') renderTimetableBuilderGrid();
    } else if (type === 'required_docs' || type === 'required-docs' || type === 'requiredDocs') {
        if (typeof renderRequiredDocsGrid === 'function') renderRequiredDocsGrid();
    } else if (type === 'fee_categories' || type === 'fee-categories' || type === 'feeCategories') {
        if (typeof renderFeeCategoriesGrid === 'function') renderFeeCategoriesGrid();
    } else if (type === 'discount_categories' || type === 'discount-categories' || type === 'discountCategories' || type === 'discounts') {
        if (typeof renderDiscountCategoriesGrid === 'function') renderDiscountCategoriesGrid();
    } else if (type === 'installment_plans' || type === 'installment-plans' || type === 'installmentPlans') {
        if (typeof renderInstallmentPlansGrid === 'function') renderInstallmentPlansGrid();
    } else if (type === 'grade_fees' || type === 'grade-fees' || type === 'gradeFees') {
        if (typeof renderGradeFeesGrid === 'function') renderGradeFeesGrid();
    } else if (type === 'account-ceiling' || type === 'accountCeiling' || type === 'account_ceiling') {
        if (typeof renderAccountCeilingGrid === 'function') renderAccountCeilingGrid();
    } else if (collKey === 'costCenters' || collKey === 'cost_center' || collKey === 'cost_centers') {
        if (typeof renderCostCentersGrid === 'function') renderCostCentersGrid();
    } else if (collKey === 'cashboxes' || collKey === 'cashbox') {
        if (typeof renderCashboxesGrid === 'function') renderCashboxesGrid();
    } else if (collKey === 'journalEntries' || collKey === 'journal' || collKey === 'journal_entry') {
        if (typeof renderJournalGrid === 'function') renderJournalGrid();
    } else if (collKey === 'vouchers' || collKey === 'voucher') {
        if (typeof renderVouchersGrid === 'function') renderVouchersGrid();
    } else if (collKey === 'accounts' || collKey === 'chart-accounts') {
        if (typeof renderChartAccountsTree === 'function') renderChartAccountsTree();
    } else if (collKey === 'systemSettingsData' || collKey === 'system_settings') {
        if (typeof renderSystemSettingsGrid === 'function') renderSystemSettingsGrid();
    } else if (collKey === 'alertsData' || collKey === 'alerts') {
        if (typeof renderAlertsGrid === 'function') renderAlertsGrid();
    } else if (collKey === 'archiveDocs' || collKey === 'archive') {
        if (typeof renderArchiveGrid === 'function') renderArchiveGrid();
    } else if (collKey === 'users' || collKey === 'user') {
        if (typeof renderUsersGrid === 'function') renderUsersGrid();
    } else if (typeof hydrateAndMountAllGrids === 'function') {
        hydrateAndMountAllGrids();
    }
}
window.confirmDelete = confirmDelete;
window.confirmDel = confirmDelete;


/**
 * ============================================================================
 * 04-FORMS-ENGINE.JS - Universal Dynamic Form Schema, Validation & Modals
 * With Eye Toggle for Passwords & Granular Action Permissions (CRUD + Search + Print)
 * ============================================================================
 */

function openModal(id) {
    let m = document.getElementById(id);
    if (m) {
        m.classList.add('active');
        m.style.display = 'flex';
        m.style.zIndex = '99999';
        m.style.opacity = '1';
        m.style.visibility = 'visible';
    }
}
window.openModal = openModal;

function closeModal(id) {
    let m = document.getElementById(id);
    if (m) {
        m.classList.remove('active');
        m.style.display = 'none';
        m.style.opacity = '0';
        m.style.visibility = 'hidden';
    }
}
window.closeModal = closeModal;
window.closeForm = function() { closeModal('formModal'); };

function minModal(id) {
    closeModal(id);
}
window.minModal = minModal;

function togglePasswordVisibility(fieldId) {
    const input = document.getElementById(fieldId);
    const icon = document.getElementById('eye-' + fieldId);
    if (!input) return;
    if (input.type === 'password') {
        input.type = 'text';
        if (icon) {
            icon.classList.remove('fa-eye');
            icon.classList.add('fa-eye-slash');
            icon.style.color = '#38bdf8';
        }
    } else {
        input.type = 'password';
        if (icon) {
            icon.classList.remove('fa-eye-slash');
            icon.classList.add('fa-eye');
            icon.style.color = '#94a3b8';
        }
    }
}
window.togglePasswordVisibility = togglePasswordVisibility;

function openForm(entity, editId) {
    entity = entity || 'student';
    window.currentEditingType = entity;
    window.currentEditingId = editId || null;

    let modal = document.getElementById('formModal');
    let title = document.getElementById('formTitle');
    let container = document.getElementById('dynamicForm') || document.getElementById('form-fields') || document.getElementById('formFieldsContainer');

    // Self-healing: if modal is missing in DOM, create it dynamically
    if (!modal || !title || !container) {
        const existing = document.getElementById('formModal');
        if (existing) existing.remove();

        const modalDiv = document.createElement('div');
        modalDiv.className = 'modal-overlay active';
        modalDiv.id = 'formModal';
        modalDiv.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.65);z-index:99999;display:flex;justify-content:center;align-items:center;padding:12px;backdrop-filter:blur(6px);';
        modalDiv.innerHTML = `
            <div class="modal-content glass-panel" style="max-width:850px;width:95%;max-height:90vh;display:flex;flex-direction:column;border-radius:14px;background:rgba(15,23,42,0.95);border:1px solid rgba(255,255,255,0.15);box-shadow:0 25px 50px -12px rgba(0,0,0,0.8);">
                <div class="modal-header" style="border-bottom:1px solid rgba(255,255,255,0.1);padding:14px 20px;display:flex;justify-content:space-between;align-items:center;">
                    <h3 id="formTitle" style="margin:0;font-size:1.1rem;color:#f8fafc;"><i class="fa-solid fa-pen-to-square" style="color:#38bdf8;"></i> نموذج</h3>
                    <div class="window-controls" style="display:flex;gap:6px;">
                        <button class="btn-min" onclick="closeModal('formModal')" title="تصغير" style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);color:#94a3b8;width:28px;height:28px;border-radius:6px;cursor:pointer;"><i class="fa-solid fa-minus"></i></button>
                        <button class="btn-close" onclick="closeModal('formModal')" title="إغلاق" style="background:rgba(239,68,68,0.2);border:1px solid rgba(239,68,68,0.4);color:#ef4444;width:28px;height:28px;border-radius:6px;cursor:pointer;"><i class="fa-solid fa-xmark"></i></button>
                    </div>
                </div>
                <div class="modal-body" style="overflow-y:auto;padding:20px;flex:1;">
                    <form id="dynamicForm" class="modern-form" onsubmit="event.preventDefault();saveForm();"></form>
                    <div class="modal-actions" style="margin-top:20px;display:flex;gap:10px;justify-content:flex-end;border-top:1px solid rgba(255,255,255,0.08);padding-top:14px;">
                        <button type="button" class="btn-save" onclick="saveForm()" style="background:linear-gradient(135deg,#10b981,#059669);color:#fff;font-weight:700;padding:10px 22px;border-radius:8px;border:none;cursor:pointer;display:flex;align-items:center;gap:6px;"><i class="fa-solid fa-floppy-disk"></i> حفظ ومزامنة</button>
                        <button type="button" class="btn-cancel" onclick="closeModal('formModal')" style="background:rgba(255,255,255,0.08);color:#cbd5e1;padding:10px 18px;border-radius:8px;border:1px solid rgba(255,255,255,0.12);cursor:pointer;display:flex;align-items:center;gap:6px;"><i class="fa-solid fa-xmark"></i> إلغاء</button>
                    </div>
                </div>
            </div>
        `;
        document.body.appendChild(modalDiv);
        modal = modalDiv;
        title = document.getElementById('formTitle');
        container = document.getElementById('dynamicForm');
    }

    const fields = typeof getFormFields === 'function' ? getFormFields(entity) : [];
    const entityLabels = {
        'student': 'طالب جديد وحساب ولي الأمر',
        'employee': 'بيانات موظف / معلم',
        'user': 'بيانات مستخدم وصلاحيات الوصول',
        'users': 'بيانات مستخدم وصلاحيات الوصول',
        'voucher': 'سند مالي',
        'voucher_receipt': 'سند قبض مالي',
        'voucher_payment': 'سند صرف مالي',
        'banks': 'بيانات حساب بنكي',
        'checks': 'شيك بنكي',
        'account-ceiling': 'تسقيف حساب ائتماني',
        'demand_letters': 'رسالة مطالبة مالية',
        'academic-calendar': 'فعالية بالتقويم المدرسي',
        'subject-distribution': 'توزيع مادة على الصفوف',
        'classrooms': 'قاعة / معمل دراسي',
        'class-times': 'توقيت حصة دراسية',
        'discount-categories': 'فئة خصم ومنحة',
        'installment-plans': 'خطة أقساط ودفعات',
        'required-docs': 'وثيقة قبول مطلوبة',
        'discontinued': 'سجل طالب غير مستمر',
        'guarantors': 'بيانات ضامن معتمد',
        'contracts': 'عقد عمل وظيفي',
        'advances': 'سلفة مالية لموظف',
        'performance': 'تقييم أداء وظيفي',
        'activities': 'نشاط مدرسي',
        'suppliers': 'بيانات مورد وتاجر',
        'faq': 'سؤال وجواب شائع',
        'operation-lock': 'قاعدة قفل عمليات',
        'system_settings': 'إعداد وتكوين سيادي',
        'systemSettingsData': 'إعداد وتكوين سيادي',
        'alerts': 'قاعدة تنبيه ومحفز',
        'archive': 'وثيقة أرشيف رقمي'
    };

    const label = entityLabels[entity] || entity;
    title.innerHTML = editId ? 
        `<i class="fa-solid fa-pen-to-square" style="color:#38bdf8;"></i> تعديل ${label} (#${editId})` : 
        `<i class="fa-solid fa-user-plus" style="color:#10b981;"></i> إضافة ${label}`;

    // Load existing record if editing
    let existingData = {};
    if (editId && window.DB) {
        const collKey = typeof getCollectionKey === 'function' ? getCollectionKey(entity) : entity;
        if (window.DB[collKey]) {
            existingData = window.DB[collKey].find(x => 
                x.id == editId || x.code == editId || x.nationalId == editId || x.username == editId || x.key == editId
            ) || {};
        }
    }

    let fieldsHtml = '<div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; width: 100%;">';

    fields.forEach(f => {
        const reqAttr = f.required ? 'required' : '';
        const reqStar = f.required ? '<span style="color:#ef4444;margin-right:4px;">*</span>' : '';
        const currentVal = existingData[f.key] !== undefined ? existingData[f.key] : (f.default || '');
        const hintText = f.hint ? `<span style="display:block; font-size:0.75rem; color:#94a3b8; margin-top:4px;">${f.hint}</span>` : '';

        if (f.type === 'select') {
            const optionsHtml = (f.options || []).map(opt => {
                const isSelected = String(currentVal) === String(opt) ? 'selected' : '';
                return `<option value="${opt}" ${isSelected}>${opt}</option>`;
            }).join('');

            fieldsHtml += `
                <div class="form-group" style="margin-bottom:8px; ${f.fullWidth ? 'grid-column: 1 / -1;' : ''}">
                    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
                        <label style="font-weight:700;font-size:0.85rem;color:#f8fafc;">${f.label} ${reqStar}</label>
                        ${f.id === 'f_ctm_bell_tone' ? '<button type="button" onclick="if(typeof window.playSchoolBellSound===\'function\')window.playSchoolBellSound(document.getElementById(\'f_ctm_bell_tone\')?.value);" style="cursor:pointer;background:rgba(59,130,246,0.2);border:1px solid #3b82f6;color:#60a5fa;border-radius:6px;padding:2px 8px;font-size:0.75rem;"><i class="fa-solid fa-volume-high"></i> تجربة الصوت</button>' : ''}
                    </div>
                    <select id="${f.id}" data-key="${f.key}" class="form-control" ${reqAttr} onchange="${f.id === 'f_ctm_bell_tone' ? 'if(typeof window.playSchoolBellSound===\'function\')window.playSchoolBellSound(this.value);' : ''}" style="width:100%;padding:10px 14px;border-radius:9px;border:1px solid rgba(255,255,255,0.12);background:rgba(15,23,42,0.85);color:#f8fafc;outline:none;">
                        ${optionsHtml}
                    </select>
                    ${hintText}
                </div>
            `;
        } else if (f.type === 'textarea') {
            fieldsHtml += `
                <div class="form-group" style="margin-bottom:8px; grid-column: 1 / -1;">
                    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
                        <label style="font-weight:700;font-size:0.85rem;color:#f8fafc;">${f.label} ${reqStar}</label>
                        ${f.id === 'f_ctm_bell_tone' ? '<button type="button" onclick="if(typeof window.playSchoolBellSound===\'function\')window.playSchoolBellSound(document.getElementById(\'f_ctm_bell_tone\')?.value);" style="cursor:pointer;background:rgba(59,130,246,0.2);border:1px solid #3b82f6;color:#60a5fa;border-radius:6px;padding:2px 8px;font-size:0.75rem;"><i class="fa-solid fa-volume-high"></i> تجربة الصوت</button>' : ''}
                    </div>
                    <textarea id="${f.id}" data-key="${f.key}" class="form-control" placeholder="${f.placeholder || ''}" ${reqAttr} rows="3" style="width:100%;padding:10px 14px;border-radius:9px;border:1px solid rgba(255,255,255,0.12);background:rgba(15,23,42,0.85);color:#f8fafc;outline:none;">${currentVal}</textarea>
                    ${hintText}
                </div>
            `;
        } else if (f.type === 'password') {
            fieldsHtml += `
                <div class="form-group" style="margin-bottom:8px; ${f.fullWidth ? 'grid-column: 1 / -1;' : ''}">
                    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
                        <label style="font-weight:700;font-size:0.85rem;color:#f8fafc;">${f.label} ${reqStar}</label>
                        ${f.id === 'f_ctm_bell_tone' ? '<button type="button" onclick="if(typeof window.playSchoolBellSound===\'function\')window.playSchoolBellSound(document.getElementById(\'f_ctm_bell_tone\')?.value);" style="cursor:pointer;background:rgba(59,130,246,0.2);border:1px solid #3b82f6;color:#60a5fa;border-radius:6px;padding:2px 8px;font-size:0.75rem;"><i class="fa-solid fa-volume-high"></i> تجربة الصوت</button>' : ''}
                    </div>
                    <div style="position:relative;width:100%;">
                        <input type="password" id="${f.id}" data-key="${f.key}" value="${currentVal}" class="form-control" placeholder="${f.placeholder || ''}" ${reqAttr} style="width:100%;padding:10px 42px 10px 14px;border-radius:9px;border:1px solid rgba(255,255,255,0.12);background:rgba(15,23,42,0.85);color:#f8fafc;outline:none;">
                        <button type="button" onclick="togglePasswordVisibility('${f.id}')" style="position:absolute;left:10px;top:50%;transform:translateY(-50%);background:none;border:none;color:#94a3b8;cursor:pointer;font-size:1.1rem;padding:4px;" title="إظهار / إخفاء كلمة السر">
                            <i class="fa-solid fa-eye" id="eye-${f.id}"></i>
                        </button>
                    </div>
                    ${hintText}
                </div>
            `;
        } else {
            fieldsHtml += `
                <div class="form-group" style="margin-bottom:8px; ${f.fullWidth ? 'grid-column: 1 / -1;' : ''}">
                    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
                        <label style="font-weight:700;font-size:0.85rem;color:#f8fafc;">${f.label} ${reqStar}</label>
                        ${f.id === 'f_ctm_bell_tone' ? '<button type="button" onclick="if(typeof window.playSchoolBellSound===\'function\')window.playSchoolBellSound(document.getElementById(\'f_ctm_bell_tone\')?.value);" style="cursor:pointer;background:rgba(59,130,246,0.2);border:1px solid #3b82f6;color:#60a5fa;border-radius:6px;padding:2px 8px;font-size:0.75rem;"><i class="fa-solid fa-volume-high"></i> تجربة الصوت</button>' : ''}
                    </div>
                    <input type="${f.type || 'text'}" id="${f.id}" data-key="${f.key}" value="${currentVal}" class="form-control" placeholder="${f.placeholder || ''}" ${reqAttr} style="width:100%;padding:10px 14px;border-radius:9px;border:1px solid rgba(255,255,255,0.12);background:rgba(15,23,42,0.85);color:#f8fafc;outline:none;">
                    ${hintText}
                </div>
            `;
        }
    });

    fieldsHtml += '</div>';

    // Inject Action Permissions (CRUD, Search, Print) & RBAC Matrix for Users
    if (entity === 'user' || entity === 'users') {
        const userActions = existingData.actions || { create: true, edit: true, delete: true, search: true, print: true };

        fieldsHtml += `
            <div id="actionPermissionsSection" style="grid-column:1/-1;margin-top:16px;border:1px solid rgba(16,185,129,0.35);background:rgba(15,23,42,0.85);border-radius:12px;padding:16px;">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;border-bottom:1px solid rgba(255,255,255,0.1);padding-bottom:8px;flex-wrap:wrap;gap:8px;">
                    <div style="font-weight:800;color:#34d399;font-size:1rem;">
                        <i class="fa-solid fa-sliders"></i> صلاحيات العمليات الإجرائية على البيانات (Data Operations Permissions)
                    </div>
                    <div style="display:flex;gap:6px;">
                        <button type="button" class="btn-action" style="background:#10b981;color:#fff;padding:4px 10px;font-size:0.75rem;border-radius:6px;" onclick="document.querySelectorAll('.act-chk').forEach(c => c.checked = true)">تفعيل الكل ✅</button>
                        <button type="button" class="btn-action" style="background:#ef4444;color:#fff;padding:4px 10px;font-size:0.75rem;border-radius:6px;" onclick="document.querySelectorAll('.act-chk').forEach(c => c.checked = false)">تعطيل الكل ❌</button>
                    </div>
                </div>
                <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;">
                    <label style="display:flex;align-items:center;gap:8px;background:rgba(255,255,255,0.04);padding:10px;border-radius:8px;cursor:pointer;border:1px solid rgba(255,255,255,0.06);">
                        <input type="checkbox" class="act-chk" id="perm_act_create" value="create" ${userActions.create !== false ? 'checked' : ''} style="accent-color:#10b981;width:18px;height:18px;cursor:pointer;">
                        <div>
                            <strong style="color:#f8fafc;font-size:0.85rem;display:block;"><i class="fa-solid fa-plus-circle" style="color:#10b981;"></i> الإضافة والإنشاء</strong>
                            <span style="color:#94a3b8;font-size:0.72rem;">إضافة سجلات جديدة</span>
                        </div>
                    </label>
                    <label style="display:flex;align-items:center;gap:8px;background:rgba(255,255,255,0.04);padding:10px;border-radius:8px;cursor:pointer;border:1px solid rgba(255,255,255,0.06);">
                        <input type="checkbox" class="act-chk" id="perm_act_edit" value="edit" ${userActions.edit !== false ? 'checked' : ''} style="accent-color:#3b82f6;width:18px;height:18px;cursor:pointer;">
                        <div>
                            <strong style="color:#f8fafc;font-size:0.85rem;display:block;"><i class="fa-solid fa-pen-to-square" style="color:#3b82f6;"></i> التعديل والتحديث</strong>
                            <span style="color:#94a3b8;font-size:0.72rem;">تعديل البيانات المحفوظة</span>
                        </div>
                    </label>
                    <label style="display:flex;align-items:center;gap:8px;background:rgba(255,255,255,0.04);padding:10px;border-radius:8px;cursor:pointer;border:1px solid rgba(255,255,255,0.06);">
                        <input type="checkbox" class="act-chk" id="perm_act_delete" value="delete" ${userActions.delete !== false ? 'checked' : ''} style="accent-color:#ef4444;width:18px;height:18px;cursor:pointer;">
                        <div>
                            <strong style="color:#f8fafc;font-size:0.85rem;display:block;"><i class="fa-solid fa-trash-can" style="color:#ef4444;"></i> الحذف والتعطيل</strong>
                            <span style="color:#94a3b8;font-size:0.72rem;">حذف السجلات نهائياً</span>
                        </div>
                    </label>
                    <label style="display:flex;align-items:center;gap:8px;background:rgba(255,255,255,0.04);padding:10px;border-radius:8px;cursor:pointer;border:1px solid rgba(255,255,255,0.06);">
                        <input type="checkbox" class="act-chk" id="perm_act_search" value="search" ${userActions.search !== false ? 'checked' : ''} style="accent-color:#f59e0b;width:18px;height:18px;cursor:pointer;">
                        <div>
                            <strong style="color:#f8fafc;font-size:0.85rem;display:block;"><i class="fa-solid fa-magnifying-glass" style="color:#f59e0b;"></i> البحث والفلترة</strong>
                            <span style="color:#94a3b8;font-size:0.72rem;">الاستعلام والفرز الفوري</span>
                        </div>
                    </label>
                    <label style="display:flex;align-items:center;gap:8px;background:rgba(255,255,255,0.04);padding:10px;border-radius:8px;cursor:pointer;border:1px solid rgba(255,255,255,0.06);">
                        <input type="checkbox" class="act-chk" id="perm_act_print" value="print" ${userActions.print !== false ? 'checked' : ''} style="accent-color:#a855f7;width:18px;height:18px;cursor:pointer;">
                        <div>
                            <strong style="color:#f8fafc;font-size:0.85rem;display:block;"><i class="fa-solid fa-print" style="color:#a855f7;"></i> الطباعة والتصدير</strong>
                            <span style="color:#94a3b8;font-size:0.72rem;">طباعة PDF وتصدير Excel</span>
                        </div>
                    </label>
                </div>
            </div>
        `;

        const allSystemPages = [
            { group: '📊 1. الإدارة واللوحات المركزية', pages: [
                { id: 'pg-dashboard', label: 'لوحة التحكم الرئيسية' },
                { id: 'pg-saas-admin', label: 'لوحة إدارة SaaS السحابية' },
                { id: 'pg-school-info', label: 'معلومات وبيانات المدرسة' },
                { id: 'pg-users', label: 'دليل المستخدمين والصلاحيات' },
                { id: 'pg-system-settings', label: 'إعدادات النظام العامة' },
                { id: 'pg-alerts', label: 'مركز التنبيهات الآلية' },
                { id: 'pg-archive', label: 'الأرشيف الرقمي والوثائق' },
                { id: 'pg-audit-trail', label: 'سجل الأمان والتدقيق الأمني' },
                { id: 'pg-db-management', label: 'إدارة قاعدة البيانات والنسخ' }
            ]},
            { group: '💰 2. المالية والمحاسبة والقيود ERP', pages: [
                { id: 'pg-chart-accounts', label: 'دليل الحسابات الشجري' },
                { id: 'pg-vouchers', label: 'سندات القبض والصرف' },
                { id: 'pg-journal', label: 'دفتر القيود اليومية' },
                { id: 'pg-cashboxes', label: 'دليل الصناديق والخزائن' },
                { id: 'pg-cost-centers', label: 'مراكز التكلفة والموازنة' },
                { id: 'pg-account-ceiling', label: 'تسقيف الحسابات الائتماني' },
                { id: 'pg-currencies', label: 'دليل العملات وأسعار الصرف' },
                { id: 'pg-cashbox-inventory', label: 'جرد الصناديق النقدية' },
                { id: 'pg-closings', label: 'الإقفالات المحاسبية الدورية' },
                { id: 'pg-banks', label: 'دليل البنوك والحسابات المصرفية' },
                { id: 'pg-demand-letters', label: 'المطالبات المالية والإنذارات' },
                { id: 'pg-finance-reports', label: 'التقارير المالية والأستاذ' }
            ]},
            { group: '🏫 3. التهيئة والمدخلات الأكاديمية', pages: [
                { id: 'pg-academic-years', label: 'دليل السنوات الدراسية' },
                { id: 'pg-academic-calendar', label: 'التقويم الأكاديمي والفعاليات' },
                { id: 'pg-stages', label: 'المراحل والصفوف الدراسية' },
                { id: 'pg-sections', label: 'دليل الشُعَب الدراسية' },
                { id: 'pg-subjects', label: 'دليل المواد الدراسية' },
                { id: 'pg-subject-distribution', label: 'توزيع المواد على الصفوف' },
                { id: 'pg-classrooms', label: 'القاعات والمعامل والمختبرات' },
                { id: 'pg-class-times', label: 'توقيت وبدايات الحصص' },
                { id: 'pg-required-docs', label: 'دليل الوثائق المطلوبة' },
                { id: 'pg-fee-categories', label: 'فئات الرسوم المدرسية' },
                { id: 'pg-discount-categories', label: 'فئات الخصومات والمنح' },
                { id: 'pg-installment-plans', label: 'خطط وجداول الأقساط' },
                { id: 'pg-grade-fees', label: 'جدول رسوم الصفوف' }
            ]},
            { group: '👨‍🎓 4. شؤون الطلاب والقبول والتسجيل', pages: [
                { id: 'pg-student-register', label: 'تسجيل طالب جديد' },
                { id: 'pg-enrollment', label: 'إدارة القبول والرسوم' },
                { id: 'pg-students', label: 'دليل الطلاب الشامل والملف' },
                { id: 'pg-parents', label: 'دليل أولياء الأمور والربط' },
                { id: 'pg-student-tree', label: 'الشجرة الأكاديمية للطلاب' },
                { id: 'pg-section-distribution', label: 'توزيع الطلاب على الشعب' },
                { id: 'pg-discontinued', label: 'سجل الطلاب غير المستمرين' },
                { id: 'pg-promotion-workflow', label: 'مسار ترفيع الطلاب' },
                { id: 'pg-class-notes', label: 'ملاحظات رائد الفصل اليومية' },
                { id: 'pg-homework-tracker', label: 'متابعة الواجبات المدرسية' }
            ]},
            { group: '👨‍🏫 5. الموارد البشرية والرواتب HR', pages: [
                { id: 'pg-employees', label: 'دليل الموظفين والمعلمين' },
                { id: 'pg-guarantors', label: 'دليل الضمناء والكفلاء' },
                { id: 'pg-teacher-subjects', label: 'إسناد المواد للمعلمين' },
                { id: 'pg-emp-notices', label: 'إشعارات وتنبيهات الموظفين' },
                { id: 'pg-emp-contracts', label: 'عقود العمل والتوظيف' },
                { id: 'pg-emp-advances', label: 'سلفيات وقروض الموظفين' },
                { id: 'pg-leave-management', label: 'نظام إدارة الإجازات' },
                { id: 'pg-performance-eval', label: 'تقييم الأداء والكفاءة' },
                { id: 'pg-payroll', label: 'مسير ومعالجة الرواتب' }
            ]},
            { group: '⏱️ 6. الحضور والانضباط السلوكي', pages: [
                { id: 'pg-attendance', label: 'تحضير وغياب الطلاب اليومي' },
                { id: 'pg-emp-attendance', label: 'حضور وانضباط الموظفين' },
                { id: 'pg-violations-catalog', label: 'لائحة المخالفات والجزاءات' }
            ]},
            { group: '📅 7. الجدول الدراسي والامتحانات والكنترول', pages: [
                { id: 'pg-timetable-builder', label: 'بناء الجدول الدراسي المباشر' },
                { id: 'pg-substitute', label: 'إدارة المدرس البديل' },
                { id: 'pg-grading', label: 'رصد الدرجات والتقييمات' },
                { id: 'pg-results', label: 'النتائج والشهادات برمز QR' },
                { id: 'pg-certificates', label: 'طباعة الشهادات المعتمدة' },
                { id: 'pg-exam-halls', label: 'أماكن ولجان الامتحانات' },
                { id: 'pg-hall-distribution', label: 'توزيع اللجان والمراقبين' },
                { id: 'pg-exam-schedule', label: 'جدول الامتحانات الرسمية' }
            ]},
            { group: '🚌 8. المواصلات والمستودعات والأنشطة', pages: [
                { id: 'pg-activities', label: 'إدارة الأنشطة والرحلات' },
                { id: 'pg-transport-routes', label: 'دليل خطوط سير الحافلات' },
                { id: 'pg-buses', label: 'دليل حافلات المدرسة' },
                { id: 'pg-transport-enrollment', label: 'اشتراك مواصلات الطلاب' },
                { id: 'pg-item-categories', label: 'فئات الأصناف المخزنية' },
                { id: 'pg-inventory-items', label: 'دليل الأصناف والمنتجات SKU' },
                { id: 'pg-supply-orders', label: 'أذونات التوريد المخزني GRN' },
                { id: 'pg-issue-orders', label: 'أذونات الصرف المخزني GIN' },
                { id: 'pg-suppliers', label: 'دليل الموردين المعتمدين' }
            ]},
            { group: '💬 9. الرسائل والتقارير والدعم', pages: [
                { id: 'pg-sms-send', label: 'إرسال رسائل SMS وواتساب' },
                { id: 'pg-admin-messages', label: 'الرسائل والتعاميم الإدارية' },
                { id: 'pg-shortcuts', label: 'اختصارات النظام المفضلة' },
                { id: 'pg-faq', label: 'الأسئلة المتكررة وتذاكر الدعم' },
                { id: 'pg-dictionary', label: 'قاموس المصطلحات والترجمة' },
                { id: 'pg-custom-reports', label: 'التقارير المخصصة والتحليلية' }
            ]}
        ];

        let userPerms = existingData.permissions || [];

        fieldsHtml += `
            <div id="rbacMatrixSection" style="grid-column:1/-1;margin-top:16px;border:1px solid rgba(59,130,246,0.35);background:rgba(15,23,42,0.7);border-radius:12px;padding:16px;">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;border-bottom:1px solid rgba(255,255,255,0.1);padding-bottom:10px;flex-wrap:wrap;gap:8px;">
                    <div style="font-weight:800;color:#38bdf8;font-size:1.05rem;"><i class="fa-solid fa-shield-halved"></i> مصفوفة صلاحيات الوصول للشاشات (RBAC Screen Access Matrix)</div>
                    <div style="display:flex;gap:8px;">
                        <button type="button" class="btn-action" style="background:#10b981;color:#fff;padding:6px 12px;font-size:0.8rem;border-radius:7px;" onclick="document.querySelectorAll('.rbac-chk').forEach(c => c.checked = true)">تحديد الكل ✅</button>
                        <button type="button" class="btn-action" style="background:#ef4444;color:#fff;padding:6px 12px;font-size:0.8rem;border-radius:7px;" onclick="document.querySelectorAll('.rbac-chk').forEach(c => c.checked = false)">إلغاء الكل ❌</button>
                    </div>
                </div>
                <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;max-height:350px;overflow-y:auto;padding-right:6px;">
        `;

        allSystemPages.forEach(g => {
            fieldsHtml += `
                <div style="background:rgba(30,41,59,0.7);border-radius:8px;padding:10px;border:1px solid rgba(255,255,255,0.06);">
                    <div style="font-weight:700;color:#f59e0b;font-size:0.85rem;margin-bottom:8px;border-bottom:1px dashed rgba(245,158,11,0.3);padding-bottom:4px;">${g.group}</div>
                    <div style="display:flex;flex-direction:column;gap:6px;">
            `;
            g.pages.forEach(p => {
                const isChecked = (!editId) || (userPerms.length === 0) || userPerms.includes(p.id);
                fieldsHtml += `
                    <label style="display:flex;align-items:center;gap:8px;font-size:0.8rem;color:#cbd5e1;cursor:pointer;">
                        <input type="checkbox" class="rbac-chk" value="${p.id}" ${isChecked ? 'checked' : ''} style="cursor:pointer;accent-color:#3b82f6;width:15px;height:15px;">
                        <span>${p.label}</span>
                    </label>
                `;
            });
            fieldsHtml += `</div></div>`;
        });

        fieldsHtml += `</div></div>`;
    }

    container.innerHTML = fieldsHtml;

    if (typeof openModal === 'function') openModal('formModal');
    else {
        modal.classList.add('active');
        modal.style.display = 'flex';
    }
    
    if (typeof toast === 'function') toast('✨ نافذة ' + (editId ? 'تعديل' : 'إضافة') + ' ' + label + ' جاهزة');
}
window.openForm = openForm;

function closeForm() {
    closeModal('formModal');
}
window.closeForm = closeForm;

function getCollectionKey(entity) {
    const map = {
        'student': 'students',
        'students': 'students',
        'employee': 'employees',
        'employees': 'employees',
        'user': 'users',
        'users': 'users',
        'parent': 'parents',
        'parents': 'parents',
        'voucher': 'vouchers',
        'voucher_receipt': 'vouchers',
        'voucher_payment': 'vouchers',
        'journal': 'journalEntries',
        'journal_entry': 'journalEntries',
        'journalEntries': 'journalEntries',
        'banks': 'banks',
        'checks': 'checks',
        'account-ceiling': 'accountCeiling',
        'demand_letters': 'demandLetters',
        'finance_reports': 'financeReports',
        'academic_years': 'academicYears',
        'academic_calendar': 'academicCalendar',
        'stages': 'stages',
        'sections': 'sections',
        'subjects': 'subjects',
        'subject_distribution': 'subjectDistribution',
        'subject-distribution': 'subjectDistribution',
        'subjectDistribution': 'subjectDistribution',
        'subject': 'subjects',
        'section': 'sections',
        'stage': 'stages',
        'grades': 'stages',
        'academicCalendar': 'academicCalendar',
        'academic-calendar': 'academicCalendar',
        'academicYears': 'academicYears',
        'academic-years': 'academicYears',
        'financeReports': 'financeReports',
        'academic-calendar': 'calendar',
        'subject-distribution': 'subjectDistribution',
        'classrooms': 'classrooms',
        'class_times': 'classTimes',
        'timetable_builder': 'timetableBuilder',
        'required_docs': 'requiredDocs',
        'fee_categories': 'feeCategories',
        'discount_categories': 'discountCategories',
        'installment_plans': 'installmentPlans',
        'grade_fees': 'gradeFees',
        'grade-fees': 'gradeFees',
        'gradeFees': 'gradeFees',
        'installment-plans': 'installmentPlans',
        'installmentPlans': 'installmentPlans',
        'discount-categories': 'discountCategories',
        'discountCategories': 'discountCategories',
        'discounts': 'discountCategories',
        'fee-categories': 'feeCategories',
        'feeCategories': 'feeCategories',
        'required-docs': 'requiredDocs',
        'requiredDocs': 'requiredDocs',
        'timetable-builder': 'timetableBuilder',
        'timetableBuilder': 'timetableBuilder',
        'class-times': 'classTimes',
        'classTimes': 'classTimes',
        'class-times': 'classTimes',
        'discount-categories': 'discounts',
        'installment-plans': 'installmentPlans',
        'required-docs': 'requiredDocs',
        'discontinued': 'discontinued',
        'guarantors': 'guarantors',
        'contracts': 'contracts',
        'advances': 'advances',
        'performance': 'performance',
        'activities': 'activities',
        'suppliers': 'suppliers',
        'faq': 'faq',
        'operation-lock': 'operationLocks',
        'system_settings': 'systemSettingsData',
        'systemSettingsData': 'systemSettingsData',
        'alerts': 'alertsData',
        'posting': 'postingBatches',
        'postingBatches': 'postingBatches',
        'currency': 'currencies',
        'currencies': 'currencies',
        'cashbox_inventory': 'cashboxInventory',
        'closing': 'closings',
        'closings': 'closings',
        'cashboxInventory': 'cashboxInventory',
        'cost_center': 'costCenters',
        'cost_centers': 'costCenters',
        'costCenters': 'costCenters',
        'cashbox': 'cashboxes',
        'cashboxes': 'cashboxes',
        'chart-accounts': 'accounts',
        'accounts': 'accounts',
        'archive': 'archiveDocs'
    };
    return map[entity] || entity;
}
window.getCollectionKey = getCollectionKey;

function getFormFields(entity) {
    if (entity === 'grade_fees' || entity === 'grade-fees' || entity === 'gradeFees') {
        return [
            { id: 'f_grf_code', key: 'code', label: 'كود الصف والرسوم المرجعي * (f_grf_code)', type: 'text', placeholder: 'مثال: FEE-GRD-09', required: true },
            { id: 'f_grf_stage', key: 'stage', label: 'المرحلة التعليمية التابع لها * (f_grf_stage)', type: 'select', options: ['المرحلة الأساسية العليا (7-9) 🎓', 'الأساسية الأولى (1-6) 📚', 'المرحلة الثانوية 🏛️', 'رياض الأطفال والتمهيدي 🧸'], required: true },
            { id: 'f_grf_grade_name', key: 'gradeName', label: 'اسم وتسمية الصف الدراسي * (f_grf_grade_name)', type: 'text', placeholder: 'مثال: الصف التاسع أساسي (شهادة أساسية)', required: true, fullWidth: true },
            { id: 'f_grf_grade_name_en', key: 'gradeNameEn', label: 'الاسم بالإنجليزية (f_grf_grade_name_en)', type: 'text', placeholder: 'Grade 9 - Basic Certificate Level', required: false },
            { id: 'f_grf_academic_year', key: 'academicYear', label: 'العام الدراسي المالي المعتمد * (f_grf_academic_year)', type: 'select', options: ['العام الدراسي 2026 / 2027 م', 'العام الدراسي 2027 / 2028 م'], required: true },
            { id: 'f_grf_tuition_fee', key: 'tuitionFee', label: 'القسط التعليمي والتدريس السنوي (ر.ي) * (f_grf_tuition_fee)', type: 'text', placeholder: '350000 ر.ي', required: true },
            { id: 'f_grf_registration_fee', key: 'registrationFee', label: 'رسوم التسجيل والملف للطلاب المستجدين * (f_grf_registration_fee)', type: 'text', placeholder: '20000 ر.ي', required: true },
            { id: 'f_grf_books_fee', key: 'booksFee', label: 'رسوم الكتب والمناهج الإثرائية * (f_grf_books_fee)', type: 'text', placeholder: '45000 ر.ي', required: true },
            { id: 'f_grf_uniform_fee', key: 'uniformFee', label: 'رسوم الزي المدرسي والرياضي الموحد * (f_grf_uniform_fee)', type: 'text', placeholder: '35000 ر.ي', required: true },
            { id: 'f_grf_activities_fee', key: 'activitiesFee', label: 'رسوم الأنشطة والمختبرات والتأمين * (f_grf_activities_fee)', type: 'text', placeholder: '15000 ر.ي', required: true },
            { id: 'f_grf_total_amount', key: 'totalAmount', label: 'الإجمالي الشامل التقديري للطالب (ر.ي) * (f_grf_total_amount)', type: 'text', placeholder: '450000 ر.ي 💰', required: true },
            { id: 'f_grf_installment_plan', key: 'paymentPlan', label: 'خطة الأقساط المعتمدة للصف * (f_grf_installment_plan)', type: 'select', options: ['3 أقساط سنوية (40% / 30% / 30%) 📅', 'خطة السداد الفصلي (دفعتان)', 'سداد كاش سنوي كامل 💵'], required: true },
            { id: 'f_grf_status', key: 'status', label: 'حالة الاعتماد والاعتماد المالي * (f_grf_status)', type: 'select', options: ['معتمد ومطبق 🟢', 'مسودة قيد المراجعة 🟡', 'موقف 🔴'], required: true },
            { id: 'f_grf_notes', key: 'notes', label: 'الملاحظات والاشتراطات المالية (f_grf_notes)', type: 'textarea', placeholder: 'اكتب تفاصيل إضافية حول رسوم الاختبارات الوزارية لشهادة تاسع وثانوية عامة...', required: false, fullWidth: true }
        ];
    }

    if (entity === 'installment_plans' || entity === 'installment-plans' || entity === 'installmentPlans') {
        return [
            { id: 'f_ins_code', key: 'code', label: 'كود خطة الأقساط المرجعي * (f_ins_code)', type: 'text', placeholder: 'مثال: PLN-TRI-01', required: true },
            { id: 'f_ins_name', key: 'name', label: 'اسم وتسمية خطة الأقساط بالعربية * (f_ins_name)', type: 'text', placeholder: 'مثال: خطة الأقساط الثلاثية القياسية (3 دفعات سنوية)', required: true, fullWidth: true },
            { id: 'f_ins_name_en', key: 'nameEn', label: 'اسم الخطة بالإنجليزية (f_ins_name_en)', type: 'text', placeholder: 'Standard 3-Term Installment Plan', required: false },
            { id: 'f_ins_installments_count', key: 'count', label: 'عدد الدفعات والأقساط السنوية * (f_ins_installments_count)', type: 'select', options: ['3 أقساط سنوية (خطة ثلاثية قياسية) 📅', 'دفعتان سنويتان (خطة فصلية - بداية كل فصل)', '10 أقساط شهرية ميسرة (خلال شهور الدراسة)', 'دفعة واحدة كاملة مقدماً (سداد كاش سنوي) 💵', '4 أقساط ربع سنوية (Quarterly)'], required: true },
            { id: 'f_ins_percentage_breakdown', key: 'breakdown', label: 'توزيع نسب الأقساط من إجمالي الرسوم * (f_ins_percentage_breakdown)', type: 'text', placeholder: '40% دفعة أولى + 30% قسط ثانٍ + 30% قسط ثالث', required: true, fullWidth: true },
            { id: 'f_ins_stages', key: 'stages', label: 'المراحل الدراسية المطبقة * (f_ins_stages)', type: 'select', options: ['كافة المراحل الدراسية والصفوف 👨‍🎓', 'المرحلة الأساسية فقط (1-9)', 'المرحلة الثانوية فقط (10-12)', 'مرحلة رياض الأطفال والتمهيدي KG'], required: true },
            { id: 'f_ins_due_first', key: 'dueFirst', label: 'تاريخ استحقاق الدفعة الأولى (المقدمة) * (f_ins_due_first)', type: 'text', placeholder: 'عند التسجيل وتأكيد القبول (أغسطس / سبتمبر)', required: true },
            { id: 'f_ins_due_second', key: 'dueSecond', label: 'تاريخ استحقاق القسط الثاني * (f_ins_due_second)', type: 'text', placeholder: '15 ديسمبر (قبل اختبارات الفصل الأول)', required: true },
            { id: 'f_ins_due_third', key: 'dueThird', label: 'تاريخ استحقاق القسط الثالث (f_ins_due_third)', type: 'text', placeholder: '15 مارس (خلال الفصل الدراسي الثاني)', required: false },
            { id: 'f_ins_grace_period', key: 'gracePeriod', label: 'فترة السماح بعد تاريخ الاستحقاق * (f_ins_grace_period)', type: 'select', options: ['14 يوماً فترة سماح ⏳', '7 أيام سماح', '30 يوماً', 'بدون فترة سماح'], required: true },
            { id: 'f_ins_reminder_channel', key: 'reminderChannel', label: 'نظام التذكير والإشعارات التلقائية * (f_ins_reminder_channel)', type: 'select', options: ['رسائل SMS فورية + إشعارات تطبيق ولي الأمر 📲', 'رسائل واتساب تلقائية + SMS', 'إشعار التطبيق فقط'], required: true },
            { id: 'f_ins_early_reward', key: 'rewards', label: 'حافز السداد المبكر قبل الاستحقاق (f_ins_early_reward)', type: 'select', options: ['خصم 5% عند السداد قبل الموعد بأسبوعين 🎁', 'خصم 3% عند الالتزام بالسداد الفصلي', 'إعفاء من رسوم الملف عند السداد الشهري', 'خصم فوري 10% للسداد الكاش الكامل', 'بدون حافز'], required: false },
            { id: 'f_ins_status', key: 'status', label: 'حالة التفعيل والاعتماد المالي * (f_ins_status)', type: 'select', options: ['معتمدة ومفعلة للعام الدراسي 🟢', 'موقفة ومؤرشفة 🔴'], required: true },
            { id: 'f_ins_notes', key: 'notes', label: 'الملاحظات والتعليمات المالية والتعثر (f_ins_notes)', type: 'textarea', placeholder: 'اكتب تعليمات متابعة الطلاب المتعثرين، كروت الاختبار، وسياسات التيسير...', required: false, fullWidth: true }
        ];
    }

    if (entity === 'discount_categories' || entity === 'discount-categories' || entity === 'discountCategories' || entity === 'discounts') {
        return [
            { id: 'f_dsc_code', key: 'code', label: 'كود فئة الخصم المرجعي * (f_dsc_code)', type: 'text', placeholder: 'مثال: DSC-SIB-01', required: true },
            { id: 'f_dsc_name', key: 'name', label: 'اسم وتسمية فئة الخصم / المنحة بالعربية * (f_dsc_name)', type: 'text', placeholder: 'مثال: خصم الأخوة والأقارب (للابن الثاني)', required: true, fullWidth: true },
            { id: 'f_dsc_name_en', key: 'nameEn', label: 'اسم فئة الخصم بالإنجليزية (f_dsc_name_en)', type: 'text', placeholder: 'Second Sibling Family Discount', required: false },
            { id: 'f_dsc_type', key: 'type', label: 'نوع وتصنيف الخصم / المنحة * (f_dsc_type)', type: 'select', options: ['خصم اجتماعي عائلي 👨‍👩‍👧', 'منحة تفوق أكاديمي 🎓', 'منحة قرآنية وإيمانية 🕌', 'خصم وظيفي للكوادر 👔', 'منحة إنسانية ورعاية أيتام 🤍', 'خصم سداد مبكر كاش 💵'], required: true },
            { id: 'f_dsc_calc_type', key: 'calcType', label: 'طريقة احتساب قيمة الخصم * (f_dsc_calc_type)', type: 'select', options: ['نسبة مئوية % من إجمالي الرسوم 📊', 'مبلغ مالي مقطوع وثابت (ر.ي) 💰'], required: true },
            { id: 'f_dsc_value', key: 'value', label: 'قيمة الخصم أو النسبة المعتمدة * (f_dsc_value)', type: 'text', placeholder: '15% خصم أو 50000 ر.ي أو 100%', required: true },
            { id: 'f_dsc_stages', key: 'stages', label: 'المراحل والصفوف المشمولة * (f_dsc_stages)', type: 'select', options: ['كافة المراحل الدراسية 👨‍🎓', 'المرحلة الأساسية (الصفوف 1-9)', 'المرحلة الثانوية فقط (10-12)', 'مرحلة رياض الأطفال والتمهيدي KG'], required: true },
            { id: 'f_dsc_eligibility_criteria', key: 'eligibility', label: 'شروط الاستحقاق ومعايير الأهلية * (f_dsc_eligibility_criteria)', type: 'text', placeholder: 'مثال: تسجيل أخ أكبر مسدد للرسوم / معدل 95% فما فوق', required: true, fullWidth: true },
            { id: 'f_dsc_required_documents', key: 'docs', label: 'المستندات والوثائق المطلوبة للإثبات (f_dsc_required_documents)', type: 'text', placeholder: 'مثال: شهادات الميلاد / كشف الدرجات / بطاقة العمل', required: false },
            { id: 'f_dsc_quota_limit', key: 'quota', label: 'الحد الأقصى للطلاب المستفيدين سنويّاً (f_dsc_quota_limit)', type: 'select', options: ['مفتوح لكافة المؤهلين ♾️', '10 مقاعد سنوية', '15 مقعداً', '25 مقعداً دراسياً', '50 مقعداً'], required: false },
            { id: 'f_dsc_combinable', key: 'combinable', label: 'إمكانية الجمع مع خصومات أخرى * (f_dsc_combinable)', type: 'select', options: ['لا يجوز الجمع بين أكثر من خصم (يطبق الخصم الأعلى) 🚫', 'يجوز الجمع مع خصم السداد المبكر الكاش'], required: true },
            { id: 'f_dsc_approval_authority', key: 'authority', label: 'جهة الاعتماد والتفويض المالي * (f_dsc_approval_authority)', type: 'text', placeholder: 'مثال: مجلس الإدارة والمدير العام', required: true },
            { id: 'f_dsc_status', key: 'status', label: 'حالة التفعيل وسريان الخصم * (f_dsc_status)', type: 'select', options: ['معتمدة وسارية 🟢', 'موقفة ومؤرشفة 🔴'], required: true },
            { id: 'f_dsc_notes', key: 'notes', label: 'الملاحظات والتعليمات والضوابط (f_dsc_notes)', type: 'textarea', placeholder: 'اكتب شروط الاستمرار في المنحة والحفاظ على المعدل الأكاديمي والانضباط...', required: false, fullWidth: true }
        ];
    }

    if (entity === 'fee_categories' || entity === 'fee-categories' || entity === 'feeCategories') {
        return [
            { id: 'f_fee_code', key: 'code', label: 'كود فئة الرسوم المرجعي * (f_fee_code)', type: 'text', placeholder: 'مثال: FEE-CAT-01', required: true },
            { id: 'f_fee_name', key: 'name', label: 'اسم وتسمية فئة الرسوم بالعربية * (f_fee_name)', type: 'text', placeholder: 'مثال: الرسوم الدراسية السنوية - المرحلة الأساسية العليا (7-9)', required: true, fullWidth: true },
            { id: 'f_fee_name_en', key: 'nameEn', label: 'اسم فئة الرسوم بالإنجليزية (f_fee_name_en)', type: 'text', placeholder: 'Annual Tuition - Upper Basic Stage (7-9)', required: false },
            { id: 'f_fee_type', key: 'type', label: 'نوع وتصنيف بند الرسوم * (f_fee_type)', type: 'select', options: ['رسوم تعليمية أساسية 📚', 'خدمات نقل ومواصلات 🚌', 'كتب ومقررات دراسية 📖', 'زي مدرسي ورياضي 👕', 'تسجيل وقبول وملف 📝', 'أنشطة وتأمين ومعامل 🏆'], required: true },
            { id: 'f_fee_stages', key: 'stages', label: 'المرحلة والصفوف المطبقة عليها * (f_fee_stages)', type: 'select', options: ['المرحلة الأساسية العليا (الصفوف 7-9)', 'المرحلة الأساسية الأولى (الصفوف 1-6)', 'المرحلة الثانوية العامة (10-12)', 'مرحلة رياض الأطفال والتمهيدي KG', 'كافة المراحل الدراسية والصفوف 👨‍🎓'], required: true },
            { id: 'f_fee_amount_local', key: 'amountLocal', label: 'المبلغ بالعملة المحلية (ر.ي) * (f_fee_amount_local)', type: 'text', placeholder: '350000 ر.ي', required: true },
            { id: 'f_fee_amount_foreign', key: 'amountForeign', label: 'المبلغ بالعملة الأجنبية (USD / SAR) (f_fee_amount_foreign)', type: 'text', placeholder: '$500 USD', required: false },
            { id: 'f_fee_payment_schedule', key: 'paymentSchedule', label: 'طريقة وجدولة السداد * (f_fee_payment_schedule)', type: 'select', options: ['أقساط سنوية (3 دفعات) 📅', 'أقساط سنوية (دفعتان فصليتان)', 'دفعة واحدة كاملة مقدماً عند التسجيل 💵', 'أقساط شهرية مجدولة (10 أشهر)'], required: true },
            { id: 'f_fee_is_mandatory', key: 'mandatoryLevel', label: 'درجة إلزامية الرسوم للطالب * (f_fee_is_mandatory)', type: 'select', options: ['إلزامية لكافة الطلاب 🔴', 'اختيارية حسب الطلب 🟢'], required: true },
            { id: 'f_fee_discount_policy', key: 'discountPolicy', label: 'شروط ونسب الخصم المتاحة * (f_fee_discount_policy)', type: 'select', options: ['خصم الأخوة 15% / التفوق 20% 🎁', 'خصم الأخ الثاني بنسبة 10% 🎁', 'إعفاء لأبناء الشهداء والمعلمين 🎁', 'لا ينطبق عليه أي خصم مالي'], required: true },
            { id: 'f_fee_late_penalty', key: 'penalty', label: 'غرامة التأخير عن موعد القسط (f_fee_late_penalty)', type: 'select', options: ['بدون غرامة مالية (تنبيه إلكتروني فقط)', 'غرامة 5% بعد 30 يوماً'], required: false },
            { id: 'f_fee_allow_online_pay', key: 'onlinePay', label: 'إمكانية السداد الإلكتروني عبر المحافظ (f_fee_allow_online_pay)', type: 'select', options: ['متاح السداد عبر كاش، ون كاش، وجوالي 📲', 'سداد نقدي في خزينة المدرسة فقط'], required: false },
            { id: 'f_fee_status', key: 'status', label: 'حالة التفعيل والاعتماد المالي * (f_fee_status)', type: 'select', options: ['معتمدة وفعالة 🟢', 'موقفة ومؤرشفة 🔴'], required: true },
            { id: 'f_fee_notes', key: 'notes', label: 'الملاحظات والسياسة المالية (f_fee_notes)', type: 'textarea', placeholder: 'اكتب تفاصيل سياسة استرداد الرسوم ومواعيد استحقاق الأقساط وحسابات المدرسة...', required: false, fullWidth: true }
        ];
    }

    if (entity === 'required_docs' || entity === 'required-docs' || entity === 'requiredDocs') {
        return [
            { id: 'f_doc_code', key: 'code', label: 'كود الوثيقة المرجعي * (f_doc_code)', type: 'text', placeholder: 'مثال: DOC-REQ-01', required: true },
            { id: 'f_doc_name', key: 'name', label: 'اسم وتسمية الوثيقة بالعربية * (f_doc_name)', type: 'text', placeholder: 'مثال: أصل شهادة الميلاد المميكنة (الرقم الوطني)', required: true, fullWidth: true },
            { id: 'f_doc_name_en', key: 'nameEn', label: 'اسم الوثيقة بالإنجليزية (f_doc_name_en)', type: 'text', placeholder: 'Original Computerized Birth Certificate', required: false },
            { id: 'f_doc_category', key: 'category', label: 'تصنيف ونوع الوثيقة * (f_doc_category)', type: 'select', options: ['وثائق ثبوتية شخصية 🆔', 'شهادات أكاديمية 🎓', 'تقارير طبية وصحية 🩺', 'وثائق النقل والتحويل 🚚', 'مستندات الإقامة وجوازات السفر للوافدين 🛂', 'مستندات إدارية وتعهدات 📝'], required: true },
            { id: 'f_doc_stages', key: 'stages', label: 'المراحل والصفوف المطبقة عليها * (f_doc_stages)', type: 'select', options: ['كافة المراحل الدراسية 👨‍🎓', 'مرحلة رياض الأطفال والتمهيدي KG', 'الصف الأول أساسي (المستجدين)', 'المرحلة الثانوية فقط (10-12)', 'الطلاب المحولين من مدارس أخرى'], required: true },
            { id: 'f_doc_mandatory_level', key: 'mandatoryLevel', label: 'درجة الإلزامية والأولوية * (f_doc_mandatory_level)', type: 'select', options: ['إلزامية أساسية 🔴', 'مشروطة بالتحويل 🟡', 'مشروطة بالجنسية 🟡', 'وثيقة اختيارية وتكميلية 🟢'], required: true },
            { id: 'f_doc_copies_count', key: 'copies', label: 'عدد النسخ المطلوبة للتسليم * (f_doc_copies_count)', type: 'select', options: ['الأصل للمطابقة + صورتان 📑', 'أصل الوثيقة النهائي', '4 صور شخصية حديثة بخلفية بيضاء', 'نسخة إلكترونية واضحة PDF'], required: true },
            { id: 'f_doc_allowed_formats', key: 'formats', label: 'الصيغ والامتدادات المسموح برفعها * (f_doc_allowed_formats)', type: 'select', options: ['PDF + JPG + PNG 📎', 'ملفات PDF فقط', 'صور JPG/PNG فقط', 'أصل ورقي فقط'], required: true },
            { id: 'f_doc_max_size', key: 'maxSize', label: 'الحد الأقصى لحجم الملف الرقمي * (f_doc_max_size)', type: 'select', options: ['5 ميجابايت (5MB) 💾', '10 ميجابايت (10MB)', '2 ميجابايت (2MB)', '1 ميجابايت (1MB)'], required: true },
            { id: 'f_doc_issuing_authority', key: 'issuingAuthority', label: 'الجهة الرسمية المعتمدة للإصدار * (f_doc_issuing_authority)', type: 'text', placeholder: 'مثال: مصلحة الأحوال المدنية والسجل المدني', required: true },
            { id: 'f_doc_attestation_required', key: 'attestation', label: 'اشتراط المصادقة والتصديق الوزاري * (f_doc_attestation_required)', type: 'select', options: ['يتطلب تصديق وزارة التربية والخارجية 🏛️', 'لا يشترط تصديق خارجي'], required: true },
            { id: 'f_doc_allow_portal_upload', key: 'allowUpload', label: 'إمكانية الرفع عبر بوابة ولي الأمر (f_doc_allow_portal_upload)', type: 'select', options: ['متاح الرفع الإلكتروني عبر تطبيق ولي الأمر 📲', 'تسليم ورقي مباشر للإدارة'], required: false },
            { id: 'f_doc_status', key: 'status', label: 'حالة التفعيل والطلب * (f_doc_status)', type: 'select', options: ['فعالة ومطلوبة 🟢', 'موقفة مؤقتاً 🔴'], required: true },
            { id: 'f_doc_guidelines', key: 'guidelines', label: 'الإرشادات والشروط التفصيلية (f_doc_guidelines)', type: 'textarea', placeholder: 'اكتب مواصفات فحص الوثيقة وشروط قبول الصورة والأختام المطلوبة...', required: false, fullWidth: true }
        ];
    }

    if (entity === 'timetable_builder' || entity === 'timetable-builder' || entity === 'timetableBuilder') {
        return [
            { id: 'f_ttb_code', key: 'code', label: 'كود الحصة المرجعي * (f_ttb_code)', type: 'text', placeholder: 'مثال: SCH-09A-SUN-1', required: true },
            { id: 'f_ttb_academic_year', key: 'academicYear', label: 'العام الدراسي المرتبط * (f_ttb_academic_year)', type: 'select', options: ['العام الدراسي 2026 / 2027 م', 'العام الدراسي 2027 / 2028 م'], required: true },
            { id: 'f_ttb_term', key: 'term', label: 'الفصل الدراسي المحدد * (f_ttb_term)', type: 'select', options: ['الفصل الدراسي الأول', 'الفصل الدراسي الثاني'], required: true },
            { id: 'f_ttb_section', key: 'section', label: 'الشعبة والفصل الدراسي المستهدف * (f_ttb_section)', type: 'select', options: ['شعبة التاسع أساسي (أ) - بنين', 'شعبة التاسع أساسي (ب) - بنات', 'شعبة الثالث ثانوي - علمي (1)', 'شعبة الثالث ثانوي - أدبي', 'شعبة الأول أساسي (أ) - تميز', 'شعبة الروضة الأولى KG1'], required: true },
            { id: 'f_ttb_day', key: 'day', label: 'اليوم الدراسي الأسبوعي * (f_ttb_day)', type: 'select', options: ['السبت (Saturday) 📅', 'الأحد (Sunday) 📅', 'الإثنين (Monday) 📅', 'الثلاثاء (Tuesday) 📅', 'الأربعاء (Wednesday) 📅'], required: true },
            { id: 'f_ttb_period', key: 'period', label: 'رقم الحصة والتوقيت الزمني * (f_ttb_period)', type: 'select', options: ['الحصة 1 (08:00 ص - 08:45 ص) ⏱️', 'الحصة 2 (08:45 ص - 09:30 ص) ⏱️', 'الحصة 3 (09:30 ص - 10:15 ص) ⏱️', 'الحصة 4 (10:45 ص - 11:30 ص) ⏱️', 'الحصة 5 (11:30 ص - 12:15 م) ⏱️', 'الحصة 6 (12:30 م - 01:15 م) ⏱️', 'الحصة 7 (إثرائية بعد الدوام)'], required: true },
            { id: 'f_ttb_subject', key: 'subject', label: 'المادة الدراسية المقررة * (f_ttb_subject)', type: 'select', options: ['الرياضيات المتقدمة والجبر', 'العلوم العامة والفيزياء', 'الفيزياء الحديثة والميكانيكا', 'الكيمياء العضوية', 'اللغة الإنجليزية (Crescent)', 'اللغة العربية والنحو', 'القرآن الكريم والتجويد', 'الحاسوب والذكاء الاصطناعي', 'الدراسات الاجتماعية'], required: true },
            { id: 'f_ttb_teacher', key: 'teacher', label: 'المعلم المدرس المسؤول * (f_ttb_teacher)', type: 'select', options: ['أ. إبراهيم الحداد', 'د. عبد العزيز الصبري', 'أ. سالم الحميري', 'أ. عادل عبد الله العولقي', 'أ. محمد طاهر اليافعي', 'الشيخ عبد الرحمن باعباد', 'م. خالد عبد الكريم'], required: true },
            { id: 'f_ttb_room', key: 'room', label: 'القاعة أو المعمل الدراسي * (f_ttb_room)', type: 'select', options: ['قاعة 104 (المبنى الرئيسي)', 'معمل العلوم والفيزياء 1 🔬', 'معمل الحاسوب والذكاء الاصطناعي 💻', 'معمل اللغات والصوتيات 🎧', 'معمل الفيزياء المتقدم 302', 'قاعة 101'], required: true },
            { id: 'f_ttb_lesson_type', key: 'lessonType', label: 'نوع الحصة التعليمية * (f_ttb_lesson_type)', type: 'select', options: ['شرح نظري فصلي 📖', 'تجارب وتطبيق عملي بالمعمل 🔬', 'تمارين وحل تدريبات 📝', 'اختبار قصير Quiz'], required: true },
            { id: 'f_ttb_conflict_check', key: 'conflictCheck', label: 'نظام فحص التعارض الفوري * (f_ttb_conflict_check)', type: 'select', options: ['فحص آلي مفعل (منع تعارض المعلم والقاعة) 🛡️', 'استثناء يدوي مؤقت'], required: true },
            { id: 'f_ttb_notify', key: 'notify', label: 'إشعار المعلم والطلاب بالجدول (f_ttb_notify)', type: 'select', options: ['تحديث جدول تطبيق ولي الأمر وبوابة المعلم 📲', 'بدون إشعار فوري'], required: false },
            { id: 'f_ttb_status', key: 'status', label: 'حالة الاعتماد والنشر * (f_ttb_status)', type: 'select', options: ['معتمد ومنشور للطلاب 🟢', 'مسودة قيد المراجعة 🟡', 'موقفة مؤقتاً 🔴'], required: true },
            { id: 'f_ttb_notes', key: 'notes', label: 'الملاحظات والتعليمات الميدانية (f_ttb_notes)', type: 'textarea', placeholder: 'اكتب تفاصيل إضافية حول احتياجات الحصة أو التجهيزات المطلوبة...', required: false, fullWidth: true }
        ];
    }

    if (entity === 'class_times' || entity === 'class-times' || entity === 'classTimes') {
        return [
            { id: 'f_ctm_code', key: 'code', label: 'كود الحصة / الفترة المرجعي * (f_ctm_code)', type: 'text', placeholder: 'مثال: PRD-MORN-01', required: true },
            { id: 'f_ctm_name', key: 'name', label: 'اسم وتسمية الحصة بالعربية * (f_ctm_name)', type: 'text', placeholder: 'مثال: الحصة الدراسية الأولى (Period 1)', required: true, fullWidth: true },
            { id: 'f_ctm_name_en', key: 'nameEn', label: 'اسم الحصة بالإنجليزية (f_ctm_name_en)', type: 'text', placeholder: 'First Academic Period (Period 1)', required: false },
            { id: 'f_ctm_type', key: 'type', label: 'نوع وطبيعة الفترة * (f_ctm_type)', type: 'select', options: ['حصة تعليمية صفية (Academic Period) 📚', 'طابور الصباح والإذاعة المدرسية (Morning Assembly) ☀️', 'استراحة وفسحة الإفطار (Recess & Breakfast Break) 🥪', 'فترة صلاة الظهر جماعة (Dhuhr Prayer Break) 🕌', 'نشاط لاصفي وإثرائي (Extracurricular Activity) 🏆'], required: true },
            { id: 'f_ctm_shift', key: 'shift', label: 'الفترة ونوع الدوام * (f_ctm_shift)', type: 'select', options: ['دوام صباحي قياسي (Morning Shift) ☀️', 'دوام مسائي (Afternoon Shift) 🌙', 'التوقيت الشتوي المعتمد ❄️', 'توقيت شهر رمضان المبارك 🌙'], required: true },
            { id: 'f_ctm_order', key: 'order', label: 'ترتيب وتسلسل الحصة باليوم * (f_ctm_order)', type: 'number', placeholder: '1', required: true },
            { id: 'f_ctm_start_time', key: 'startTime', label: 'وقت بداية الحصة / الفترة * (f_ctm_start_time)', type: 'text', placeholder: '08:00 ص', required: true },
            { id: 'f_ctm_end_time', key: 'endTime', label: 'وقت نهاية الحصة / الفترة * (f_ctm_end_time)', type: 'text', placeholder: '08:45 ص', required: true },
            { id: 'f_ctm_duration', key: 'duration', label: 'المدة الزمنية الإجمالية (بالدقائق) * (f_ctm_duration)', type: 'text', placeholder: '45 دقيقة', required: true },
            { id: 'f_ctm_stages', key: 'stages', label: 'المراحل الدراسية المطبقة * (f_ctm_stages)', type: 'select', options: ['كافة المراحل الدراسية 👨‍🎓', 'المرحلة الأساسية فقط (1-9)', 'المرحلة الثانوية فقط (10-12)', 'مرحلة رياض الأطفال والتمهيدي KG'], required: true },
            { id: 'f_ctm_bell_tone', key: 'bellTone', label: 'نغمة ونوع جرس التنبيه * (f_ctm_bell_tone)', type: 'select', options: ['رنين جرس كلاسيكي تلقائي 🔔', 'نغمة إلكترونية موسيقية 🎵', 'تنبيه صوتي إذاعي 📢', 'بدون جرس'], required: true },
            { id: 'f_ctm_auto_notify', key: 'autoNotify', label: 'إشعار تلقائي بالانتقال بين الحصص (f_ctm_auto_notify)', type: 'select', options: ['تنبيه على شاشات الفصول الذكية 📺', 'بدون إشعار شاشات'], required: false },
            { id: 'f_ctm_status', key: 'status', label: 'حالة التفعيل والتشغيل * (f_ctm_status)', type: 'select', options: ['مفعلة وتعمل بالجدول 🟢', 'موقفة مؤقتاً 🔴'], required: true },
            { id: 'f_ctm_notes', key: 'notes', label: 'الملاحظات والتعليمات الإدارية (f_ctm_notes)', type: 'textarea', placeholder: 'اكتب تعليمات ضبط الوقت والتنبيهات الموجهة للمعلمين والمناوبين...', required: false, fullWidth: true }
        ];
    }

    if (entity === 'classrooms' || entity === 'classroom' || entity === 'labs') {
        return [
            { id: 'f_cls_code', key: 'code', label: 'رقم / كود القاعة المرجعي * (f_cls_code)', type: 'text', placeholder: 'مثال: ROOM-101 أو LAB-SCI-01', required: true },
            { id: 'f_cls_name', key: 'name', label: 'اسم وتسمية القاعة / المعمل بالعربية * (f_cls_name)', type: 'text', placeholder: 'مثال: معمل الفيزياء والكيمياء المتطور (1)', required: true, fullWidth: true },
            { id: 'f_cls_name_en', key: 'nameEn', label: 'الاسم بالإنجليزية (f_cls_name_en)', type: 'text', placeholder: 'Advanced Physics & Chemistry Lab 1', required: false },
            { id: 'f_cls_type', key: 'type', label: 'نوع وطبيعة المرفق * (f_cls_type)', type: 'select', options: ['قاعة صفية قياسية (Standard Classroom) 🏫', 'معمل علوم وفيزياء وكيمياء (Science & Physics Lab) 🔬', 'معمل حاسوب وبرمجة وذكاء اصطناعي (Computer & AI Lab) 💻', 'معمل لغات وصوتيات (Language & Audio Lab) 🎧', 'صالة أنشطة ورياضة وتربية بدنية (Sports & Activity Hall) 🏆', 'مكتبة عامة وقاعة مطالعة وبحث (Library & Research Room) 📚', 'قاعة اجتماعات ومسرح مدرسي (Auditorium & Multi-purpose) 🎭'], required: true },
            { id: 'f_cls_building', key: 'building', label: 'المبنى والموقع الرئيسي * (f_cls_building)', type: 'select', options: ['المبنى الرئيسي - الطابق الأرضي', 'المبنى الرئيسي - الطابق الأول', 'المبنى الرئيسي - الطابق الثاني', 'مبنى المعامل والمختبرات المستقل', 'مبنى المرحلة الثانوية', 'مبنى الروضة والطفولة المبكرة'], required: true },
            { id: 'f_cls_capacity', key: 'capacity', label: 'السعة الطلابية القصوى للمقاعد * (f_cls_capacity)', type: 'number', placeholder: '35', required: true },
            { id: 'f_cls_assigned_section', key: 'assignedSection', label: 'الشعبة أو المرحلة المخصصة لها * (f_cls_assigned_section)', type: 'text', placeholder: 'مثال: شعبة الأول أساسي (أ) أو مشترك لكافة المراحل', required: true },
            { id: 'f_cls_ac_type', key: 'acType', label: 'نوع التكييف والتهوية * (f_cls_ac_type)', type: 'select', options: ['تكييف مركزي كامل ❄️', 'مكيفات سبليت منفصلة', 'مراوح وتهوية طبيعية'], required: true },
            { id: 'f_cls_smart_screen', key: 'equipment', label: 'التجهيزات والشاشات الذكية * (f_cls_smart_screen)', type: 'select', options: ['شاشة تفاعلية ذكية 75 بوصة 4K 📺', 'بروجكتر تفاعلي وجهاز عرض 📽️', 'سبورة بيضاء ذكية', 'بدون شاشة'], required: true },
            { id: 'f_cls_supervisor', key: 'supervisor', label: 'أمين المعمل / المشرف المسؤول * (f_cls_supervisor)', type: 'text', placeholder: 'مثال: م. خالد عبد الكريم', required: true },
            { id: 'f_cls_workstations', key: 'workstations', label: 'عدد أجهزة الحاسوب / محطات التجارب (f_cls_workstations)', type: 'number', placeholder: '30', required: false },
            { id: 'f_cls_operational_status', key: 'operationalStatus', label: 'حالة الجاهزية التشغيلية * (f_cls_operational_status)', type: 'select', options: ['مجهزة بالكامل وجاهزة للعمل 🟢', 'قيد الصيانة والترقية 🟡', 'خارج الخدمة مؤقتاً 🔴'], required: true },
            { id: 'f_cls_schedule_status', key: 'scheduleStatus', label: 'حالة الإشغال في الجدول * (f_cls_schedule_status)', type: 'select', options: ['مجدولة ومشغولة بالحصص ⏱️', 'متاحة للحجز والأنشطة 🟢'], required: true },
            { id: 'f_cls_notes', key: 'notes', label: 'الملاحظات ومواصفات الأمان والسلامة (f_cls_notes)', type: 'textarea', placeholder: 'اكتب مواصفات معدات السلامة وطفايات الحريق واشتراطات الوقاية...', required: false, fullWidth: true }
        ];
    }

    if (entity === 'subject_distribution' || entity === 'subject-distribution' || entity === 'subjectDistribution') {
        return [
            { id: 'f_sdt_code', key: 'code', label: 'كود التوزيع المرجعي * (f_sdt_code)', type: 'text', placeholder: 'مثال: DIST-09-MATH', required: true },
            { id: 'f_sdt_stage', key: 'stage', label: 'المرحلة الدراسية المستهدفة * (f_sdt_stage)', type: 'select', options: ['المرحلة الأساسية - صفوف 1-6', 'المرحلة الأساسية - صفوف 7-9', 'المرحلة الثانوية 10-12', 'مرحلة رياض الأطفال KG'], required: true },
            { id: 'f_sdt_grade', key: 'grade', label: 'الصف الدراسي المحدد * (f_sdt_grade)', type: 'select', options: ['الصف الأول الابتدائي', 'الصف الثاني الابتدائي', 'الصف الثالث الابتدائي', 'الصف الرابع الابتدائي', 'الصف الخامس الابتدائي', 'الصف السادس الابتدائي', 'الصف السابع أساسي', 'الصف الثامن أساسي', 'الصف التاسع أساسي (الشهادة الأساسية)', 'الصف الأول الثانوي (عام)', 'الصف الثاني الثانوي (علمي)', 'الصف الثاني الثانوي (أدبي)', 'الصف الثالث الثانوي (علمي)', 'الصف الثالث الثانوي (أدبي)', 'روضة أولى (KG1)', 'تمهيدي (KG2-KG3)'], required: true },
            { id: 'f_sdt_subject', key: 'subject', label: 'المادة الدراسية المرتبطة * (f_sdt_subject)', type: 'select', options: ['الرياضيات المتقدمة والجبر والهندسة', 'العلوم العامة والفيزياء والكيمياء', 'اللغة الإنجليزية والمحادثة (Crescent English)', 'اللغة العربية وفنون الأدب والنحو', 'القرآن الكريم وأحكام التلاوة والتجويد', 'الحاسوب وتقنية المعلومات والذكاء الاصطناعي', 'الفيزياء المتقدمة والميكانيكا والكهرباء', 'الكيمياء العضوية وغير العضوية', 'الأحياء والعلوم الحياتية', 'التربية الإسلامية والفقه والسيرة', 'الدراسات الاجتماعية والجغرافيا والتاريخ', 'التربية الفنية والرياضية'], required: true },
            { id: 'f_sdt_academic_year', key: 'academicYear', label: 'العام الدراسي المرتبط * (f_sdt_academic_year)', type: 'select', options: ['العام الدراسي 2026 / 2027 م', 'العام الدراسي 2027 / 2028 م'], required: true },
            { id: 'f_sdt_term', key: 'term', label: 'الفصل الدراسي المطبق * (f_sdt_term)', type: 'select', options: ['الفصلين معاً (العام كاملاً)', 'الفصل الدراسي الأول فقط', 'الفصل الدراسي الثاني فقط'], required: true },
            { id: 'f_sdt_weekly_periods', key: 'weeklyPeriods', label: 'عدد الحصص الأسبوعية للصف * (f_sdt_weekly_periods)', type: 'number', placeholder: '6', required: true },
            { id: 'f_sdt_max_mark', key: 'maxMark', label: 'النهاية العظمى لدرجة المادة (Max Mark) * (f_sdt_max_mark)', type: 'number', placeholder: '100', required: true },
            { id: 'f_sdt_min_mark', key: 'minMark', label: 'درجة النجاح الصغرى للصف (Min Mark) * (f_sdt_min_mark)', type: 'number', placeholder: '50', required: true },
            { id: 'f_sdt_weight', key: 'weight', label: 'وزن المادة ومعامل المعدل (Weight Factor) * (f_sdt_weight)', type: 'text', placeholder: 'معامل 4.0', required: true },
            { id: 'f_sdt_grade_breakdown', key: 'examType', label: 'طريقة رصد وتوزيع الدرجات * (f_sdt_grade_breakdown)', type: 'select', options: ['أعمال سنة 40% + اختبار نهائي 60% 📊', 'أعمال سنة 50% + نهائي 50%', 'تقييم مستمر 100%', 'تحريري + عملي وشفهي بالمعمل 🔬'], required: true },
            { id: 'f_sdt_is_counted', key: 'isCounted', label: 'هل المادة مضافة للمجموع والمعدل؟ * (f_sdt_is_counted)', type: 'select', options: ['نعم - مادة أساسية تدخل في المجموع 🟢', 'لا - مادة نجاح ورسوب بدون مجموع 🟡'], required: true },
            { id: 'f_sdt_status', key: 'status', label: 'حالة الاعتماد في الخطة * (f_sdt_status)', type: 'select', options: ['معتمدة وفعالة بالجدول 🟢', 'مسودة قيد المراجعة 🟡', 'موقفة مؤقتاً 🔴'], required: true },
            { id: 'f_sdt_notes', key: 'notes', label: 'الملاحظات والتعليمات الخاصة بالمنهج (f_sdt_notes)', type: 'textarea', placeholder: 'اكتب اشتراطات تدريس المادة لهذا الصف والتجارب العملية المقررة...', required: false, fullWidth: true }
        ];
    }

    if (entity === 'subjects' || entity === 'subject') {
        return [
            { id: 'f_sub_code', key: 'code', label: 'كود المادة الدراسي المرجعي * (f_sub_code)', type: 'text', placeholder: 'مثال: SUB-MATH-09', required: true },
            { id: 'f_sub_name', key: 'name', label: 'اسم المادة الدراسية بالعربية * (f_sub_name)', type: 'text', placeholder: 'مثال: الرياضيات المتقدمة والجبر والهندسة', required: true, fullWidth: true },
            { id: 'f_sub_name_en', key: 'nameEn', label: 'اسم المادة بالإنجليزية (f_sub_name_en)', type: 'text', placeholder: 'Advanced Mathematics & Geometry', required: false },
            { id: 'f_sub_stage', key: 'stage', label: 'المرحلة الدراسية الموجهة لها * (f_sub_stage)', type: 'select', options: ['المرحلة الأساسية - صفوف 1-6', 'المرحلة الأساسية - صفوف 7-9', 'المرحلة الثانوية 10-12', 'مرحلة رياض الأطفال KG'], required: true },
            { id: 'f_sub_grades', key: 'grades', label: 'الصفوف المطبقة للمادة * (f_sub_grades)', type: 'text', placeholder: 'مثال: الصف السابع، الصف الثامن، الصف التاسع', required: true, fullWidth: true },
            { id: 'f_sub_category', key: 'category', label: 'نوع وتصنيف المادة * (f_sub_category)', type: 'select', options: ['مواد علمية وتطبيقية (Scientific & Applied) 🔬', 'لغات وآداب (Languages & Literature) 📖', 'علوم شرعية وتربية إسلامية (Islamic Studies) 🟢', 'حاسوب وذكاء اصطناعي وتكنولوجيا (Technology & AI) 💻', 'دراسات اجتماعية وتاريخ وجغرافيا (Social Studies) 🌍', 'أنشطة وفنون ورياضة (Arts & Physical Education) 🎨'], required: true },
            { id: 'f_sub_weekly_periods', key: 'weeklyPeriods', label: 'عدد الحصص الأسبوعية المعتمدة * (f_sub_weekly_periods)', type: 'number', placeholder: '5', required: true },
            { id: 'f_sub_max_mark', key: 'maxMark', label: 'النهاية العظمى لدرجة المادة (Total Mark) * (f_sub_max_mark)', type: 'number', placeholder: '100', required: true },
            { id: 'f_sub_min_mark', key: 'minMark', label: 'درجة النجاح الصغرى (Pass Mark) * (f_sub_min_mark)', type: 'number', placeholder: '50', required: true },
            { id: 'f_sub_credit_hours', key: 'creditHours', label: 'وزن المادة في المعدل التراكمي (Credits / Weight) * (f_sub_credit_hours)', type: 'text', placeholder: '4.0', required: true },
            { id: 'f_sub_head', key: 'head', label: 'رئيس القسم الأكاديمي المشرف * (f_sub_head)', type: 'text', placeholder: 'مثال: أ. إبراهيم الحداد', required: true },
            { id: 'f_sub_exam_type', key: 'examType', label: 'نوع الاختبار ورصد الدرجات * (f_sub_exam_type)', type: 'select', options: ['اختبار تحريري + عملي وشفهي 📊', 'اختبار تحريري فقط', 'تقييم وصفي مستمر'], required: true },
            { id: 'f_sub_status', key: 'status', label: 'حالة المادة في الخطة * (f_sub_status)', type: 'select', options: ['معتمدة ونشطة بالجدول 🟢', 'مادة اختيارية إثرائية 🟡', 'موقفة مؤقتاً 🔴'], required: true },
            { id: 'f_sub_notes', key: 'notes', label: 'الملاحظات والمنهج والكتب المقررة (f_sub_notes)', type: 'textarea', placeholder: 'اكتب مواصفات الكتاب المدرسي الوزاري والمراجع والأنشطة العملية المقترحة...', required: false, fullWidth: true }
        ];
    }

    if (entity === 'sections' || entity === 'section') {
        return [
            { id: 'f_sec_code', key: 'code', label: 'كود الشعبة المرجعي * (f_sec_code)', type: 'text', placeholder: 'مثال: SEC-09A', required: true },
            { id: 'f_sec_name', key: 'name', label: 'اسم وتسمية الشعبة بالعربية * (f_sec_name)', type: 'text', placeholder: 'مثال: شعبة التاسع أساسي (أ) - بنين', required: true, fullWidth: true },
            { id: 'f_sec_name_en', key: 'nameEn', label: 'اسم الشعبة بالإنجليزية (f_sec_name_en)', type: 'text', placeholder: 'Grade 9 Section (A) - Boys', required: false },
            { id: 'f_sec_stage', key: 'stage', label: 'المرحلة الدراسية التابعة * (f_sec_stage)', type: 'select', options: ['المرحلة الأساسية - صفوف 1-6', 'المرحلة الأساسية - صفوف 7-9', 'المرحلة الثانوية 10-12', 'مرحلة رياض الأطفال KG'], required: true },
            { id: 'f_sec_grade', key: 'grade', label: 'الصف الدراسي المحدد * (f_sec_grade)', type: 'select', options: ['الصف الأول الابتدائي', 'الصف الثاني الابتدائي', 'الصف الثالث الابتدائي', 'الصف الرابع الابتدائي', 'الصف الخامس الابتدائي', 'الصف السادس الابتدائي', 'الصف السابع أساسي', 'الصف الثامن أساسي', 'الصف التاسع أساسي (الشهادة الأساسية)', 'الصف الأول الثانوي (عام)', 'الصف الثاني الثانوي (علمي)', 'الصف الثاني الثانوي (أدبي)', 'الصف الثالث الثانوي (علمي)', 'الصف الثالث الثانوي (أدبي)', 'روضة أولى (KG1)', 'تمهيدي (KG2-KG3)'], required: true },
            { id: 'f_sec_gender', key: 'gender', label: 'الفرع وتصنيف الطلاب * (f_sec_gender)', type: 'select', options: ['فرع البنين 👦', 'فرع البنات 👧', 'مشترك / مختلط تمهيدي 👶'], required: true },
            { id: 'f_sec_academic_year', key: 'academicYear', label: 'العام الدراسي المرتبط * (f_sec_academic_year)', type: 'select', options: ['العام الدراسي 2026 / 2027 م', 'العام الدراسي 2027 / 2028 م'], required: true },
            { id: 'f_sec_shift', key: 'shift', label: 'الفترة والدوام المدرسي * (f_sec_shift)', type: 'select', options: ['دوام صباحي كامل ☀️', 'دوام مسائي 🌙'], required: true },
            { id: 'f_sec_capacity', key: 'capacity', label: 'السعة الطلابية القصوى للفصل * (f_sec_capacity)', type: 'number', placeholder: '35', required: true },
            { id: 'f_sec_mentor', key: 'mentor', label: 'رائد ومربي الفصل (Class Teacher) * (f_sec_mentor)', type: 'text', placeholder: 'مثال: أ. عادل عبد الله العولقي', required: true },
            { id: 'f_sec_room', key: 'room', label: 'رقم القاعة وموقع الفصل * (f_sec_room)', type: 'text', placeholder: 'مثال: قاعة 104 - المبنى الرئيسي - الطابق الأول', required: true },
            { id: 'f_sec_counselor', key: 'counselor', label: 'مسؤول الإرشاد الطلابي للشعبة (f_sec_counselor)', type: 'text', placeholder: 'مثال: أ. نبيل القدسي', required: false },
            { id: 'f_sec_status', key: 'status', label: 'حالة الشعبة والقبول * (f_sec_status)', type: 'select', options: ['نشطة ومتاحة للقبول 🟢 (Active & Open)', 'مكتملة العدد والطاقة 🔒 (Full Capacity)', 'موقفة ومجمدة مؤقتاً 🔴 (Inactive)'], required: true },
            { id: 'f_sec_notes', key: 'notes', label: 'الملاحظات والتجهيزات الخاصة (f_sec_notes)', type: 'textarea', placeholder: 'اكتب مواصفات تجهيز القاعة (شاشة ذكية، تكييف، مقاعد تفاعلية)...', required: false, fullWidth: true }
        ];
    }

    if (entity === 'stages' || entity === 'stage' || entity === 'grades' || entity === 'grade') {
        return [
            { id: 'f_stg_code', key: 'code', label: 'كود المرحلة / الصف المرجعي * (f_stg_code)', type: 'text', placeholder: 'مثال: STG-01', required: true },
            { id: 'f_stg_name', key: 'name', label: 'اسم المرحلة الدراسية بالعربية * (f_stg_name)', type: 'text', placeholder: 'مثال: المرحلة الأساسية - الصفوف العليا (7-9)', required: true, fullWidth: true },
            { id: 'f_stg_name_en', key: 'nameEn', label: 'اسم المرحلة بالإنجليزية (f_stg_name_en)', type: 'text', placeholder: 'Upper Basic Stage (Grades 7-9)', required: false },
            { id: 'f_stg_grades', key: 'grades', label: 'الصفوف التابعة والمدرجة بالمرحلة * (f_stg_grades)', type: 'text', placeholder: 'مثال: الصف السابع، الصف الثامن، الصف التاسع', required: true, fullWidth: true },
            { id: 'f_stg_type', key: 'type', label: 'نوع وطبيعة المرحلة التعليمية * (f_stg_type)', type: 'select', options: ['مرحلة رياض الأطفال والتمهيدي (Kindergarten KG) 🟣', 'المرحلة الأساسية الابتدائية (Primary Stage 1-6) 🔵', 'المرحلة الأساسية المتوسطة (Middle Basic Stage 7-9) 🟢', 'المرحلة الثانوية العامة (Secondary Stage 10-12) 🔴', 'مسار علمي / أدبي تخصصي 🟡'], required: true },
            { id: 'f_stg_pass_mark', key: 'passMark', label: 'درجة النجاح الدنيا (المعيار) * (f_stg_pass_mark)', type: 'text', placeholder: '50% كحد أدنى', required: true },
            { id: 'f_stg_grading_system', key: 'gradingSystem', label: 'نظام التقييم ورصد الدرجات * (f_stg_grading_system)', type: 'select', options: ['نظام فصلي تراكمي بالأرقام (100 درجة) 📊', 'نظام التقييم الوصفي والمستمر (A-F) 📝', 'نظام الساعات المعتمدة والمعدل التراكمي GPA 🎓'], required: true },
            { id: 'f_stg_order', key: 'order', label: 'ترتيب وتسلسل المرحلة في الهيكل * (f_stg_order)', type: 'number', placeholder: '1', required: true },
            { id: 'f_stg_capacity', key: 'capacity', label: 'السعة الطلابية القصوى المقدرة * (f_stg_capacity)', type: 'number', placeholder: '350', required: true },
            { id: 'f_stg_max_per_section', key: 'maxPerSection', label: 'الحد الأقصى لطلاب الشعبة الواحدة * (f_stg_max_per_section)', type: 'number', placeholder: '35', required: true },
            { id: 'f_stg_supervisor', key: 'supervisor', label: 'المشرف الأكاديمي ورئيس المرحلة * (f_stg_supervisor)', type: 'text', placeholder: 'مثال: أ. سالم الحميري', required: true },
            { id: 'f_stg_building', key: 'building', label: 'مبنى المرحلة وموقع القاعات (f_stg_building)', type: 'select', options: ['المبنى الرئيسي - الجناح الأيمن', 'المبنى الرئيسي - الجناح الأيسر', 'مبنى الثانوية والمعامل المستقلة', 'مبنى الروضة المستقل'], required: false },
            { id: 'f_stg_status', key: 'status', label: 'حالة المرحلة الدراسية * (f_stg_status)', type: 'select', options: ['نشطة ومفعلة تقبل القبول 🟢', 'مكتملة الطاقة الاستيعابية 🟡', 'موقفة مؤقتاً 🔴'], required: true },
            { id: 'f_stg_notes', key: 'notes', label: 'الملاحظات والتعليمات الأكاديمية (f_stg_notes)', type: 'textarea', placeholder: 'اكتب تفاصيل الخطة الدراسية للمرحلة ولوائح الانتقال والرسوم المعتمدة...', required: false, fullWidth: true }
        ];
    }

    if (entity === 'academic_calendar' || entity === 'academicCalendar' || entity === 'academic-calendar' || entity === 'calendar' || entity === 'events') {
        return [
            { id: 'f_cal_code', key: 'code', label: 'كود الفعالية المرجعي * (f_cal_code)', type: 'text', placeholder: 'مثال: EVT-2026-001', required: true },
            { id: 'f_cal_title', key: 'title', label: 'عنوان واسم الفعالية بالعربية * (f_cal_title)', type: 'text', placeholder: 'مثال: المعرض العلمي السنوي والابتكار الروبوتي', required: true, fullWidth: true },
            { id: 'f_cal_title_en', key: 'titleEn', label: 'عنوان الفعالية بالإنجليزية (f_cal_title_en)', type: 'text', placeholder: 'Annual Science & Robotics Fair', required: false },
            { id: 'f_cal_category', key: 'category', label: 'نوع وتصنيف الفعالية * (f_cal_category)', type: 'select', options: ['إجازة وعطلة رسمية (Official Holiday) 🟢', 'فترة اختبارات وتقييم (Exams & Assessments Period) 🔴', 'بداية / نهاية فصل دراسي (Term Milestone) 🟣', 'نشاط لاصفي ورحلات مدرسية (Extracurricular Activity & Trips) 🟡', 'ورش عمل وتطوير كادر (Professional Development) 🔵', 'اجتماع أولياء أمور (Parent-Teacher Meeting) 🟤'], required: true },
            { id: 'f_cal_academic_year', key: 'academicYear', label: 'العام الدراسي المرتبط * (f_cal_academic_year)', type: 'select', options: ['العام الدراسي 2026 / 2027 م', 'العام الدراسي 2027 / 2028 م'], required: true },
            { id: 'f_cal_term', key: 'term', label: 'الفصل الدراسي المحدد * (f_cal_term)', type: 'select', options: ['الفصل الدراسي الأول', 'الفصل الدراسي الثاني', 'العام بالكامل'], required: true },
            { id: 'f_cal_start_date', key: 'startDate', label: 'تاريخ بداية الفعالية * (f_cal_start_date)', type: 'date', default: '2026-09-01', required: true },
            { id: 'f_cal_end_date', key: 'endDate', label: 'تاريخ نهاية الفعالية * (f_cal_end_date)', type: 'date', default: '2026-09-01', required: true },
            { id: 'f_cal_audience', key: 'audience', label: 'الفئة والجمهور المستهدف * (f_cal_audience)', type: 'select', options: ['جميع الطلاب وكافة المراحل 👨‍🎓', 'المرحلة الثانوية فقط', 'المرحلة الأساسية فقط', 'الكادر التعليمي والإداري 👨‍🏫', 'أولياء الأمور 👨‍👩‍👧‍👦'], required: true },
            { id: 'f_cal_organizer', key: 'organizer', label: 'الجهة والمشرف المسؤول * (f_cal_organizer)', type: 'text', placeholder: 'مثال: قسم الأنشطة ورعاية الموهوبين', required: true },
            { id: 'f_cal_location', key: 'location', label: 'مكان التنفيذ وموقع الفعالية * (f_cal_location)', type: 'text', placeholder: 'مثال: الصالة الرياضية والمعامل الكبرى', required: true },
            { id: 'f_cal_notify', key: 'notify', label: 'إرسال تنبيه وتذكير آلي (f_cal_notify)', type: 'select', options: ['إشعار عبر تطبيق ولي الأمر + SMS 📲', 'إشعار داخلي للكادر التعليمي', 'بدون إشعار عام'], required: false },
            { id: 'f_cal_status', key: 'status', label: 'حالة الفعالية والاعتماد * (f_cal_status)', type: 'select', options: ['مجدولة ومؤكدة 🟢', 'جارية اليوم ⏱️', 'مكتملة ومنتهية 🔒', 'مؤجلة مؤقتاً 🟡'], required: true },
            { id: 'f_cal_notes', key: 'notes', label: 'التفاصيل وشرح برنامج الفعالية (f_cal_notes)', type: 'textarea', placeholder: 'اكتب تفاصيل جدول الفعالية والفقرات الإرشادية والترتيبات اللوجستية...', required: false, fullWidth: true }
        ];
    }

    if (entity === 'academic_years' || entity === 'academicYears' || entity === 'academic-years' || entity === 'school_years') {
        return [
            { id: 'f_ay_code', key: 'code', label: 'كود العام الدراسي * (f_ay_code)', type: 'text', placeholder: 'مثال: AY-2026-2027', required: true },
            { id: 'f_ay_name', key: 'name', label: 'مسمى العام الدراسي بالعربية * (f_ay_name)', type: 'text', placeholder: 'مثال: العام الدراسي 2026 / 2027 م', required: true, fullWidth: true },
            { id: 'f_ay_name_en', key: 'nameEn', label: 'مسمى العام الدراسي بالإنجليزية (f_ay_name_en)', type: 'text', placeholder: 'Academic Year 2026-2027', required: false },
            { id: 'f_ay_start_date', key: 'startDate', label: 'تاريخ بدء العام الدراسي * (f_ay_start_date)', type: 'date', default: '2026-09-01', required: true },
            { id: 'f_ay_end_date', key: 'endDate', label: 'تاريخ انتهاء العام الدراسي * (f_ay_end_date)', type: 'date', default: '2027-06-30', required: true },
            { id: 'f_ay_terms_count', key: 'termsCount', label: 'نظام الفصول الدراسية * (f_ay_terms_count)', type: 'select', options: ['فصلان دراسيان (Two Semesters System) 🟣', 'نظام الثلاثة فصول الدراسية (Trimester System) 🔵', 'نظام الأربعة أرباع السنوية (Quarterly System) 🟡'], required: true },
            { id: 'f_ay_t1_start', key: 't1Start', label: 'تاريخ بدء الفصل الأول * (f_ay_t1_start)', type: 'date', default: '2026-09-01', required: true },
            { id: 'f_ay_t1_end', key: 't1End', label: 'تاريخ نهاية الفصل الأول * (f_ay_t1_end)', type: 'date', default: '2027-01-15', required: true },
            { id: 'f_ay_t2_start', key: 't2Start', label: 'تاريخ بدء الفصل الثاني * (f_ay_t2_start)', type: 'date', default: '2027-02-01', required: true },
            { id: 'f_ay_t2_end', key: 't2End', label: 'تاريخ نهاية الفصل الثاني * (f_ay_t2_end)', type: 'date', default: '2027-06-30', required: true },
            { id: 'f_ay_study_days', key: 'studyDays', label: 'إجمالي عدد أيام الدراسة الفعلية * (f_ay_study_days)', type: 'number', placeholder: '185', required: true },
            { id: 'f_ay_fee_plan', key: 'feePlan', label: 'ربط هيكل الرسوم واللائحة المالية * (f_ay_fee_plan)', type: 'select', options: ['لائحة الرسوم القياسية 2026/2027 🟢', 'لائحة رسوم مخفضة للفروع', 'استيراد هيكل الرسوم من العام السابق'], required: true },
            { id: 'f_ay_status', key: 'status', label: 'حالة العام الدراسي والتشغيل * (f_ay_status)', type: 'select', options: ['نشط وفعال حالياً 🟢 (Active Current Year)', 'مخطط ومجدول مستقبلاً 🟡 (Planned Upcoming Year)', 'مغلق ومؤرشف نهائياً 🔒 (Closed & Archived)'], required: true },
            { id: 'f_ay_notes', key: 'notes', label: 'الملاحظات والتعليمات الوزارية (f_ay_notes)', type: 'textarea', placeholder: 'اكتب القرارات الوزارية المنظمة للعام الدراسي وتواريخ الإجازات المعتمدة...', required: false, fullWidth: true }
        ];
    }

        if (entity === 'finance_reports' || entity === 'financeReports' || entity === 'finance_report' || entity === 'financial_reports') {
        return [
            { id: 'f_frp_code', key: 'code', label: 'كود التقرير المالي * (f_frp_code)', type: 'text', placeholder: 'مثال: FIN-REP-01', required: true },
            { id: 'f_frp_title', key: 'title', label: 'اسم وعنوان التقرير المالي بالعربية * (f_frp_title)', type: 'text', placeholder: 'مثال: قائمة الدخل والأرباح والخسائر المقارنة', required: true, fullWidth: true },
            { id: 'f_frp_title_en', key: 'titleEn', label: 'اسم التقرير بالإنجليزية (f_frp_title_en)', type: 'text', placeholder: 'Income Statement & Profit/Loss Report', required: false },
            { id: 'f_frp_category', key: 'category', label: 'التصنيف المالي للتقرير * (f_frp_category)', type: 'select', options: ['القوائم المالية الختامية (Financial Statements) 🟣', 'موازين المراجعة والأستاذ العام (Trial Balance & Ledger) 🔵', 'تقارير الإيرادات والتحصيل والرسوم (Revenues & Collections) 🟢', 'تقارير المصروفات والرواتب والنفقات (Expenses & Payroll) 🔴', 'التدفقات النقدية والسيولة (Cash Flow & Liquidity) 🟡', 'تقارير مراكز التكلفة والموازنات (Cost Centers & Budgets) 🟤'], required: true },
            { id: 'f_frp_period_type', key: 'periodType', label: 'الفترة المالية والمدى الزمني * (f_frp_period_type)', type: 'select', options: ['فترة مخصصة محددة (Custom Date Range)', 'شهر أغسطس 2026 الحالي', 'الفصل الدراسي الأول 2026', 'الربع السنوي Q3', 'العام المالي 2026 كامل'], required: true },
            { id: 'f_frp_start_date', key: 'startDate', label: 'تاريخ بداية الفترة * (f_frp_start_date)', type: 'date', default: '2026-08-01', required: true },
            { id: 'f_frp_end_date', key: 'endDate', label: 'تاريخ نهاية الفترة * (f_frp_end_date)', type: 'date', default: '2026-08-31', required: true },
            { id: 'f_frp_currency', key: 'currency', label: 'العملة المعتمدة للتقرير * (f_frp_currency)', type: 'select', options: ['YER - ريال يمني', 'USD - دولار أمريكي', 'SAR - ريال سعودي', 'جميع العملات موحدة بالريال'], required: true },
            { id: 'f_frp_cost_center', key: 'costCenter', label: 'مركز التكلفة المالي المحدد (f_frp_cost_center)', type: 'select', options: ['جميع المراكز الموحدة', 'الإدارة العامة', 'فرع البنين', 'فرع البنات'], required: false },
            { id: 'f_frp_detail_level', key: 'detailLevel', label: 'مستوى التفصيل والتبويب * (f_frp_detail_level)', type: 'select', options: ['مستوى الحسابات الرئيسي 1 (Summary Level)', 'المستوى التجميعي 2 (Aggregated Level)', 'المستوى التحليلي التفصيلي 4 (Detailed Analytical)'], required: true },
            { id: 'f_frp_display_options', key: 'displayOptions', label: 'خيارات العرض والإظهار * (f_frp_display_options)', type: 'select', options: ['إظهار الحسابات الصفرية', 'إخفاء الحسابات الصفرية', 'مقارنة مع الموازنة التقديرية', 'مقارنة مع العام السابق'], required: true },
            { id: 'f_frp_format', key: 'formats', label: 'صيغة التصدير الافتراضية * (f_frp_format)', type: 'select', options: ['PDF رسمي معتمد 📄', 'Excel جداول بيانات 📊', 'عرض تفاعلي مباشر 💻'], required: true },
            { id: 'f_frp_status', key: 'status', label: 'حالة اعتماد وتفعيل التقرير * (f_frp_status)', type: 'select', options: ['جاهز ومحدث لحظياً 🟢', 'مسودة قيد التطوير 🟡', 'معطل 🔴'], required: true },
            { id: 'f_frp_notes', key: 'notes', label: 'الملاحظات والتعليمات المحاسبية (f_frp_notes)', type: 'textarea', placeholder: 'اكتب معايير إعداد القوائم المالية والملاحظات الإيضاحية...', required: false, fullWidth: true }
        ];
    }

        if (entity === 'demand_letters' || entity === 'demandLetters' || entity === 'demand_letter') {
        return [
            { id: 'f_dmn_code', key: 'code', label: 'كود إشعار المطالبة * (f_dmn_code)', type: 'text', placeholder: 'مثال: DMN-2026-001', required: true },
            { id: 'f_dmn_parent', key: 'parent', label: 'اسم ولي الأمر / الملتزم سداداً * (f_dmn_parent)', type: 'text', placeholder: 'مثال: أ. عادل ناصر العولقي', required: true, fullWidth: true },
            { id: 'f_dmn_student', key: 'student', label: 'اسم الطالب والمرحلة الدراسية * (f_dmn_student)', type: 'text', placeholder: 'مثال: حمزة عادل العولقي - الصف التاسع (أ)', required: true, fullWidth: true },
            { id: 'f_dmn_phone', key: 'phone', label: 'رقم هاتف ولي الأمر / واتساب * (f_dmn_phone)', type: 'text', placeholder: 'مثال: +967 771234567', required: true },
            { id: 'f_dmn_level', key: 'level', label: 'مستوى المطالبة والتصعيد * (f_dmn_level)', type: 'select', options: ['تذكير أولي لطيف بموعد القسط 🔵 (Level 1: Friendly Reminder)', 'مطالبة مالية رسمية ثانية 🟡 (Level 2: Official Demand)', 'إنذار نهائي قبل إيقاف الخدمات 🔴 (Level 3: Final Escalation)', 'إشعار جدولة وتسوية استثنائية 🟣 (Settlement Notice)'], required: true },
            { id: 'f_dmn_amount', key: 'amount', label: 'إجمالي المبلغ المتأخر والمستحق * (f_dmn_amount)', type: 'number', placeholder: 'مثال: 150000', required: true },
            { id: 'f_dmn_currency', key: 'currency', label: 'العملة المعتمدة للمطالبة * (f_dmn_currency)', type: 'select', options: ['YER - ريال يمني', 'USD - دولار أمريكي', 'SAR - ريال سعودي'], required: true },
            { id: 'f_dmn_delay_days', key: 'delayDays', label: 'عدد أيام التأخير المسجلة * (f_dmn_delay_days)', type: 'number', placeholder: 'مثال: 15', required: true },
            { id: 'f_dmn_send_date', key: 'sendDate', label: 'تاريخ إصدار وإرسال المطالبة * (f_dmn_send_date)', type: 'date', default: new Date().toISOString().split('T')[0], required: true },
            { id: 'f_dmn_due_date', key: 'dueDate', label: 'تاريخ المهلة النهائية للسداد * (f_dmn_due_date)', type: 'date', default: '2026-08-25', required: true },
            { id: 'f_dmn_channel', key: 'channel', label: 'قناة التوصيل والإرسال المعتمدة * (f_dmn_channel)', type: 'select', options: ['رسائل واتساب تفاعلية (WhatsApp API Gateway) 🟢', 'رسائل نصية قصيرة (SMS Direct) 🔵', 'إشعار عبر تطبيق ولي الأمر الذكي (Push Notification) 🟣', 'تسليم يدوي مع التوقيع بالاستلام 📄'], required: true },
            { id: 'f_dmn_pay_link', key: 'payLink', label: 'رابط الدفع المباشر السريع (f_dmn_pay_link)', type: 'text', placeholder: 'https://pay.school.edu/d/DMN-001', required: false },
            { id: 'f_dmn_status', key: 'status', label: 'حالة الاستجابة والتفاعل * (f_dmn_status)', type: 'select', options: ['بانتظار السداد والمتابعة ⏳ (Pending Payment)', 'تم الاستلام والقراءة عبر الواتساب 👁️ (Delivered & Read)', 'تم السداد بنجاح وإصدار سند 🟢 (Paid & Settled)', 'تعهد خطي بمهلة إضافية 🟡 (Extension Promised)', 'تم التصعيد للشؤون القانونية 🔴 (Escalated to Legal)'], required: true },
            { id: 'f_dmn_message', key: 'message', label: 'نص رسالة المطالبة والتنبيه (f_dmn_message)', type: 'textarea', placeholder: 'اكتب نص رسالة التنبيه الموجهة لولي الأمر مع تفاصيل الحساب البنكي للسداد...', required: false, fullWidth: true }
        ];
    }

        if (entity === 'checks' || entity === 'check' || entity === 'bank_checks') {
        return [
            { id: 'f_chk_number', key: 'checkNumber', label: 'رقم ورقة الشيك البنكي * (f_chk_number)', type: 'text', placeholder: 'مثال: CHK-88901', required: true },
            { id: 'f_chk_type', key: 'type', label: 'نوع حركة الشيك * (f_chk_type)', type: 'select', options: ['شيك وارد (سند قبض وتحصيل) 🟢 (Incoming Receipt Check)', 'شيك صادر (سند صرف ومدفوعات) 🔴 (Outgoing Payment Check)', 'شيك ضمان تأميني (Guaranty Check) 🟡'], required: true },
            { id: 'f_chk_bank', key: 'bank', label: 'اسم البنك المسحوب عليه * (f_chk_bank)', type: 'select', options: ['بنك اليمن والكويت', 'بنك الكريمي الإسلامي للتمويل الأصغر', 'بنك التضامن الإسلامي الدولي', 'بنك القطيبي الإسلامي للتمويل', 'البنك الأهلي اليمني', 'مصرف آخر'], required: true, fullWidth: true },
            { id: 'f_chk_party', key: 'party', label: 'اسم الساحب / المستفيد من الشيك * (f_chk_party)', type: 'text', placeholder: 'مثال: ولي أمر الطالب أحمد علي باعباد أو شركة الأمل', required: true, fullWidth: true },
            { id: 'f_chk_amount', key: 'amount', label: 'مبلغ الشيك بالأرقام * (f_chk_amount)', type: 'number', placeholder: 'مثال: 500000', required: true },
            { id: 'f_chk_currency', key: 'currency', label: 'العملة المعتمدة للشيك * (f_chk_currency)', type: 'select', options: ['YER - ريال يمني', 'USD - دولار أمريكي', 'SAR - ريال سعودي'], required: true },
            { id: 'f_chk_issue_date', key: 'issueDate', label: 'تاريخ تحرير وكتابة الشيك * (f_chk_issue_date)', type: 'date', default: new Date().toISOString().split('T')[0], required: true },
            { id: 'f_chk_due_date', key: 'dueDate', label: 'تاريخ استحقاق صرف الشيك * (f_chk_due_date)', type: 'date', default: '2026-08-30', required: true },
            { id: 'f_chk_drawer_acc', key: 'drawerAcc', label: 'رقم الحساب البنكي / الآيبان للساحب (f_chk_drawer_acc)', type: 'text', placeholder: 'مثال: YE99YKC0001234567890', required: false },
            { id: 'f_chk_voucher_no', key: 'voucherNo', label: 'رقم السند المالي المرتبط بالشيك (f_chk_voucher_no)', type: 'text', placeholder: 'مثال: VCH-REC-0012', required: false },
            { id: 'f_chk_gl_account', key: 'glAccount', label: 'الحساب الوسيط للأستاذ العام * (f_chk_gl_account)', type: 'select', options: ['110106 - شيكات برسم التحصيل', '210103 - شيكات صادرة تحت الصرف'], required: true },
            { id: 'f_chk_attachment', key: 'attachment', label: 'صورة الشيك / المرفق الضوئي (f_chk_attachment)', type: 'text', placeholder: 'صورة_الشيك_88901.jpg', required: false },
            { id: 'f_chk_status', key: 'status', label: 'حالة الشيك وموقعه * (f_chk_status)', type: 'select', options: ['تحت التحصيل بالخزينة / البنك 🟡 (Under Collection)', 'تم التحصيل والإيداع بالحساب 🟢 (Cleared & Deposited)', 'تم الصرف والخصم من الحساب 🔵 (Deducted / Paid)', 'شيك مرتد ومرفوض 🔴 (Bounced / Returned)', 'ملغى ⚪ (Cancelled)'], required: true },
            { id: 'f_chk_notes', key: 'notes', label: 'الملاحظات وسبب التحرير / الارتجاع (f_chk_notes)', type: 'textarea', placeholder: 'اكتب تفاصيل إضافية عن سبب إصدار الشيك أو أسباب الارتجاع إن وجدت...', required: false, fullWidth: true }
        ];
    }

    if (entity === 'banks' || entity === 'bank' || entity === 'bank_account' || entity === 'bankAccount') {
        return [
            { id: 'f_bnk_code', key: 'code', label: 'كود الحساب المصرفي * (f_bnk_code)', type: 'text', placeholder: 'مثال: BNK-01', required: true },
            { id: 'f_bnk_name', key: 'name', label: 'اسم البنك / المصرف بالعربية * (f_bnk_name)', type: 'text', placeholder: 'مثال: بنك اليمن والكويت', required: true, fullWidth: true },
            { id: 'f_bnk_name_en', key: 'nameEn', label: 'اسم البنك بالإنجليزية (f_bnk_name_en)', type: 'text', placeholder: 'Yemen Kuwait Bank (YKB)', required: false },
            { id: 'f_bnk_account_no', key: 'accountNo', label: 'رقم الحساب البنكي / رقم الآيبان IBAN * (f_bnk_account_no)', type: 'text', placeholder: 'مثال: YE99YKC0001234567890', required: true, fullWidth: true },
            { id: 'f_bnk_type', key: 'type', label: 'نوع وطبيعة الحساب المصرفي * (f_bnk_type)', type: 'select', options: ['حساب جاري (Current Account) 🔵', 'حساب توفير واستثمار (Savings Account) 🟢', 'محفظة دفع إلكترونية (E-Wallet / Payment Gateway) 🟣', 'حساب ودائع واعتمادات (Deposit Account) 🟡'], required: true },
            { id: 'f_bnk_branch', key: 'branch', label: 'الفرع والمدينة * (f_bnk_branch)', type: 'text', placeholder: 'مثال: الفرع الرئيسي - صنعاء', required: true },
            { id: 'f_bnk_currency', key: 'currency', label: 'العملة المعتمدة للحساب * (f_bnk_currency)', type: 'select', options: ['YER - ريال يمني', 'USD - دولار أمريكي', 'SAR - ريال سعودي'], required: true },
            { id: 'f_bnk_balance', key: 'balance', label: 'الرصيد الافتتاحي / الحالي * (f_bnk_balance)', type: 'number', placeholder: 'مثال: 45200000', required: true },
            { id: 'f_bnk_gl_account', key: 'glAccount', label: 'كود ورقم حساب الأستاذ العام المرتبط * (f_bnk_gl_account)', type: 'select', options: ['110102 - بنك اليمن والكويت', '110103 - بنك الكريمي الإسلامي', '110104 - بنك التضامن الإسلامي', '110105 - بنك القطيبي الإسلامي'], required: true },
            { id: 'f_bnk_cost_center', key: 'costCenter', label: 'مركز التكلفة المالي المرتبط (f_bnk_cost_center)', type: 'select', options: ['عام', 'الإدارة العامة', 'فرع البنين', 'فرع البنات'], required: false },
            { id: 'f_bnk_signatories', key: 'signatories', label: 'المخولون بالتوقيع والسحب * (f_bnk_signatories)', type: 'text', placeholder: 'مثال: المدير العام التنفيذي + المدير المالي العام', required: true, fullWidth: true },
            { id: 'f_bnk_attachment', key: 'attachment', label: 'رابط مستند شهادة فتح الحساب (f_bnk_attachment)', type: 'text', placeholder: 'شهادة_بنكية_رسمية.pdf', required: false },
            { id: 'f_bnk_status', key: 'status', label: 'حالة الحساب المصرفي * (f_bnk_status)', type: 'select', options: ['نشط ومفعل 🟢', 'مجمد وموقف 🔴', 'قيد الفتح والاعتماد 🟡'], required: true },
            { id: 'f_bnk_notes', key: 'notes', label: 'الملاحظات والتعليمات البنكية (f_bnk_notes)', type: 'textarea', placeholder: 'اكتب تفاصيل السويفت كود SWIFT وعمولات التحويل والخدمات المصرفية...', required: false, fullWidth: true }
        ];
    }

    if (entity === 'system_settings' || entity === 'systemSettingsData' || entity === 'settings') {
        return [
            { id: 'f_setting_key', key: 'key', label: 'كود الإعداد البرمجي / المفتاح * (Setting Key)', type: 'text', placeholder: 'مثال: SYS_SESSION_TIMEOUT', required: true },
            { id: 'f_setting_name', key: 'name', label: 'اسم الإعداد * (Setting Name)', type: 'text', placeholder: 'مثال: مدة إغلاق الجلسة التلقائي (Session Timeout)', required: true },
            { id: 'f_setting_category', key: 'category', label: 'التصنيف / الموديول * (Module Category)', type: 'select', options: ['الأمان والحماية والسيادة', 'النسخ الاحتياطي والأرشيف', 'إعدادات التشغيل والخدمات', 'الهوية البصرية والواجهات', 'الشؤون المالية والحسابات', 'شؤون الطلاب والقبول'], required: true },
            { id: 'f_setting_value', key: 'value', label: 'القيمة المعتمدة للإعداد * (Setting Value)', type: 'text', placeholder: 'مثال: 15 أو 0 2 * * * أو enabled', required: true },
            { id: 'f_setting_type', key: 'valueType', label: 'نوع خيار التحكم والقيمة * (Value Type)', type: 'select', options: ['مفتاح Boolean Switch', 'نص Text', 'رقم Number', 'خيارات Dropdown'], required: true },
            { id: 'f_setting_status', key: 'status', label: 'حالة التفعيل * (Status)', type: 'select', options: ['نشط ومفعل 🟢', 'معطل 🔴'], required: true },
            { id: 'f_setting_notes', key: 'notes', label: 'الملاحظات وشرح وظيفة الإعداد (Notes)', type: 'textarea', placeholder: 'اكتب الوصف التفصيلي لوظيفة التكوين البرمجي والهدف منه...', required: false, fullWidth: true }
        ];
    }

    
        if (entity === 'alerts' || entity === 'alertsData' || entity === 'alert') {
        return [
            { id: 'f_alert_title', key: 'title', label: 'اسم القاعدة / التنبيه * (f_alert_title)', type: 'text', placeholder: 'مثال: تنبيه الغياب الصباحي التلقائي', required: true, fullWidth: true },
            { id: 'f_alert_trigger', key: 'trigger', label: 'الحدث المحفز (Trigger Event) * (f_alert_trigger)', type: 'select', options: ['تسجيل غياب طالب بدون عذر مقبول', 'باقي 5 أيام على موعد استحقاق القسط', 'اعتماد نتائج الفصل الدراسي بالكنترول', 'تسجيل مخالفة سلوكية جديدة', 'إيداع سند قبض مالي جديد'], required: true },
            { id: 'f_alert_channel', key: 'channel', label: 'قناة الإرسال المعتمدة * (f_alert_channel)', type: 'select', options: ['إشعار تطبيق (Push) + SMS', 'SMS + WhatsApp API 🟢', 'رسائل نصية SMS فقط', 'رسائل واتساب WhatsApp فقط', 'إشعار نظام داخلي فقط'], required: true },
            { id: 'f_alert_audience', key: 'targetAudience', label: 'الجمهور المستهدف * (f_alert_audience)', type: 'select', options: ['أولياء الأمور', 'الطلاب', 'الكادر التعليمي', 'الإدارة'], required: true },
            { id: 'f_alert_execution', key: 'executionTime', label: 'زمن التنفيذ والتكرار * (f_alert_execution)', type: 'select', options: ['فوري لحظة وقوع الحدث ⏱️', 'يومياً 08:30 ص', 'يومياً 09:00 ص', 'أسبوعياً'], required: true },
            { id: 'f_alert_cost', key: 'gatewayCost', label: 'تكلفة بوابة الرسائل المقدرة * (f_alert_cost)', type: 'text', placeholder: '0.02 YER', required: true },
            { id: 'f_alert_status', key: 'status', label: 'حالة تفعيل القاعدة * (f_alert_status)', type: 'select', options: ['نشط ومفعل 🟢', 'معطل 🔴'], required: true },
            { id: 'f_alert_template', key: 'template', label: 'قالب نص الرسالة مع المتغيرات * (f_alert_template)', type: 'textarea', placeholder: 'عزيزي ولي الأمر، تم تسجيل غياب ابنكم {اسم_الطالب} اليوم {التاريخ}...', required: true, fullWidth: true }
        ];
    }

                                                                                        if (entity === 'closing' || entity === 'closings') {
        return [
            { id: 'f_cls_code', key: 'code', label: 'رقم أمر الإقفال * (f_cls_code)', type: 'text', placeholder: 'مثال: CLS-2026-M08', required: true },
            { id: 'f_cls_type', key: 'type', label: 'نوع ومستوى الإقفال المحاسبي * (f_cls_type)', type: 'select', options: ['إقفال شهري عام للأستاذ (Monthly Closing) 🔵', 'إقفال يومي للصناديق والخزائن (Daily Cashbox Closing) 🟢', 'إقفال الفصل الدراسي (Semester Closing) 🟣', 'إقفال سنوي ختامي وترحيل الأرباح (Year-End Closing) 🟡'], required: true },
            { id: 'f_cls_title', key: 'title', label: 'اسم وتسمية الفترة المالية * (f_cls_title)', type: 'text', placeholder: 'مثال: إقفال حسابات شهر أغسطس 2026', required: true, fullWidth: true },
            { id: 'f_cls_start_date', key: 'startDate', label: 'تاريخ بداية الفترة المقفلة * (f_cls_start_date)', type: 'date', default: '2026-08-01', required: true },
            { id: 'f_cls_end_date', key: 'endDate', label: 'تاريخ نهاية الفترة المقفلة * (f_cls_end_date)', type: 'date', default: '2026-08-31', required: true },
            { id: 'f_cls_currency', key: 'currency', label: 'العملة المعتمدة للإقفال * (f_cls_currency)', type: 'select', options: ['YER - ريال يمني', 'USD - دولار أمريكي', 'SAR - ريال سعودي'], required: true },
            { id: 'f_cls_total_revenue', key: 'totalRevenue', label: 'إجمالي المقبوضات والإيرادات المحققة * (f_cls_total_revenue)', type: 'number', placeholder: 'مثال: 4850000', required: true },
            { id: 'f_cls_total_expense', key: 'totalExpense', label: 'إجمالي المصروفات والنفقات الفعلية * (f_cls_total_expense)', type: 'number', placeholder: 'مثال: 3100000', required: true },
            { id: 'f_cls_net_surplus', key: 'netSurplus', label: 'صافي الفائض / العجز الدوري * (f_cls_net_surplus)', type: 'number', placeholder: 'مثال: 1750000', required: true },
            { id: 'f_cls_accountant', key: 'accountant', label: 'المحاسب المسؤول عن الإقفال * (f_cls_accountant)', type: 'text', placeholder: 'مثال: أ. محمد عبدالباقي', required: true },
            { id: 'f_cls_approved_by', key: 'approvedBy', label: 'المدير المالي المعتمد * (f_cls_approved_by)', type: 'text', placeholder: 'مثال: المدير المالي العام', required: true },
            { id: 'f_cls_attachment', key: 'attachment', label: 'مرفق ميزان المراجعة والقوائم المالية (f_cls_attachment)', type: 'text', placeholder: 'ميزان_مراجعة_أغسطس.pdf', required: false },
            { id: 'f_cls_status', key: 'status', label: 'حالة الإقفال وترحيل القيود * (f_cls_status)', type: 'select', options: ['مقفل ومرحل نهائياً 🔒🟢', 'مسودة قيد المراجعة 🟡', 'إقفال مؤقت 🔵'], required: true },
            { id: 'f_cls_notes', key: 'notes', label: 'ملاحظات وقرارات تسوية الفترة (f_cls_notes)', type: 'textarea', placeholder: 'اكتب تفاصيل المعالجات المحاسبية وفروق التسوية والترحيل...', required: false, fullWidth: true }
        ];
    }
    if (entity === 'cashbox_inventory' || entity === 'cashboxInventory' || entity === 'cashbox-inventory') {
        return [
            { id: 'f_cinv_code', key: 'code', label: 'رقم محضر الجرد * (f_cinv_code)', type: 'text', placeholder: 'مثال: INV-CB-2026-001', required: true },
            { id: 'f_cinv_cashbox', key: 'cashbox', label: 'الصندوق / الخزينة المراد جردها * (f_cinv_cashbox)', type: 'select', options: ['صندوق تحصيل الرسوم الدراسية (CB-101)', 'خزينة الإدارة العامة الرئيسية (CB-102)', 'صندوق مبيعات المقصف المدرسي (CB-103)', 'صندوق العهدة النقدية للصيانة والتشغيل (CB-104)'], required: true, fullWidth: true },
            { id: 'f_cinv_date', key: 'date', label: 'تاريخ وتوقيت الجرد * (f_cinv_date)', type: 'datetime-local', default: new Date().toISOString().slice(0,16), required: true },
            { id: 'f_cinv_type', key: 'type', label: 'نوع وطبيعة الجرد * (f_cinv_type)', type: 'select', options: ['جرد دوري شهري 🔵 (Monthly Audit)', 'جرد مفاجئ رقابي ⚡ (Surprise Audit)', 'جرد سنوي ختامي 🟣 (Year-End Audit)', 'جرد تسليم واستلام عهدة 🤝 (Custody Handover)'], required: true },
            { id: 'f_cinv_currency', key: 'currency', label: 'العملة المجرودة * (f_cinv_currency)', type: 'select', options: ['YER - ريال يمني', 'USD - دولار أمريكي', 'SAR - ريال سعودي'], required: true },
            { id: 'f_cinv_book_balance', key: 'bookBalance', label: 'الرصيد الدفتري المسجل بالنظام * (f_cinv_book_balance)', type: 'number', placeholder: 'مثال: 1250000', required: true },
            { id: 'f_cinv_physical_balance', key: 'physicalBalance', label: 'الرصيد النقدي الفعلي المعدود * (f_cinv_physical_balance)', type: 'number', placeholder: 'مثال: 1250000', required: true },
            { id: 'f_cinv_difference', key: 'difference', label: 'الفارق المحتسب آلياً (عجز / زيادة) (f_cinv_difference)', type: 'number', placeholder: '0 (مطابق)', required: false },
            { id: 'f_cinv_keeper', key: 'keeper', label: 'أمين الخزينة المسؤول * (f_cinv_keeper)', type: 'text', placeholder: 'مثال: أ. سالم باحارثة', required: true },
            { id: 'f_cinv_committee', key: 'committee', label: 'رئيس وأعضاء لجنة الجرد * (f_cinv_committee)', type: 'text', placeholder: 'مثال: أ. محمد عبدالباقي (المراجع المالي)', required: true },
            { id: 'f_cinv_settlement_action', key: 'settlementAction', label: 'الإجراء المحاسبي للتسوية * (f_cinv_settlement_action)', type: 'select', options: ['مطابق - إقفال وترحيل فوري 🟢', 'تحميل العجز على أمين الصندوق 🔴', 'ترحيل الفائض لحساب إيرادات متنوعة 🟡', 'إعادة العد والتدقيق 🔍'], required: true },
            { id: 'f_cinv_attachment', key: 'attachment', label: 'المرفق والمستند المؤيد (f_cinv_attachment)', type: 'text', placeholder: 'محضر_جرد_معتمد.pdf', required: false },
            { id: 'f_cinv_status', key: 'status', label: 'حالة اعتماد المحضر * (f_cinv_status)', type: 'select', options: ['معتمد ومقفل 🟢', 'مسودة قيد التدقيق 🟡', 'مرفوض 🔴'], required: true },
            { id: 'f_cinv_notes', key: 'notes', label: 'الملاحظات وتوصيات لجنة الجرد (f_cinv_notes)', type: 'textarea', placeholder: 'اكتب التوصيات الرقابية والملاحظات على سلامة الخزينة...', required: false, fullWidth: true }
        ];
    }
    if (entity === 'currency' || entity === 'currencies') {
        return [
            { id: 'f_cur_code', key: 'code', label: 'كود العملة الدولي (ISO Code) * (f_cur_code)', type: 'text', placeholder: 'مثال: USD أو SAR', required: true },
            { id: 'f_cur_name', key: 'name', label: 'اسم العملة بالعربية * (f_cur_name)', type: 'text', placeholder: 'مثال: دولار أمريكي', required: true, fullWidth: true },
            { id: 'f_cur_name_en', key: 'nameEn', label: 'اسم العملة بالإنجليزية (f_cur_name_en)', type: 'text', placeholder: 'US Dollar', required: false },
            { id: 'f_cur_symbol', key: 'symbol', label: 'رمز العملة المختصر * (f_cur_symbol)', type: 'text', placeholder: 'مثال: $ أو ر.س', required: true },
            { id: 'f_cur_is_base', key: 'isBase', label: 'طبيعة العملة * (f_cur_is_base)', type: 'select', options: ['عملة أجنبية (Foreign Currency) 🟢', 'العملة الأساسية للنظام (Base Currency) 🔵'], required: true },
            { id: 'f_cur_rate', key: 'rate', label: 'سعر الصرف الرسمي المعتمد * (f_cur_rate)', type: 'number', placeholder: 'مثال: 530.00', required: true },
            { id: 'f_cur_buy_rate', key: 'buyRate', label: 'سعر صرف الشراء (Buy Rate) * (f_cur_buy_rate)', type: 'number', placeholder: 'مثال: 528.00', required: true },
            { id: 'f_cur_sell_rate', key: 'sellRate', label: 'سعر صرف البيع (Sell Rate) * (f_cur_sell_rate)', type: 'number', placeholder: 'مثال: 532.00', required: true },
            { id: 'f_cur_decimals', key: 'decimals', label: 'عدد الخانات العشرية * (f_cur_decimals)', type: 'select', options: ['2 خانات عشرية (0.00)', '3 خانات عشرية (0.000)', '0 بدون كسور'], required: true },
            { id: 'f_cur_diff_acc', key: 'diffAcc', label: 'حساب فروق أسعار الصرف * (f_cur_diff_acc)', type: 'select', options: ['4105 - أرباح وخسائر فروق أسعار الصرف', '5109 - مصاريف وعمولات فروق العملة'], required: true },
            { id: 'f_cur_rate_date', key: 'rateDate', label: 'تاريخ سريان وتحديث السعر * (f_cur_rate_date)', type: 'date', default: new Date().toISOString().split('T')[0], required: true },
            { id: 'f_cur_status', key: 'status', label: 'حالة العملة والتداول * (f_cur_status)', type: 'select', options: ['نشطة ومتداولة 🟢', 'موقفة ومجمدة 🔴'], required: true }
        ];
    }
    if (entity === 'account-ceiling' || entity === 'accountCeiling' || entity === 'account_ceiling') {
        return [
            { id: 'f_ceil_account_code', key: 'accountCode', label: 'كود الحساب المالي * (f_ceil_account_code)', type: 'text', placeholder: 'مثال: 110201-01', required: true },
            { id: 'f_ceil_account_name', key: 'accountName', label: 'اسم الحساب / العميل / الجهة * (f_ceil_account_name)', type: 'text', placeholder: 'مثال: ولي أمر الطالب أحمد علي باعباد', required: true, fullWidth: true },
            { id: 'f_ceil_type', key: 'type', label: 'نوع السقف والحد المالي * (f_ceil_type)', type: 'select', options: ['سقف مديونية مدين (Debit Limit)', 'سقف مورد دائن (Credit Limit)', 'سقف عهدة نقدية (Petty Cash Limit)', 'سقف صرف يومي من الصندوق (Daily Cash Limit)'], required: true },
            { id: 'f_ceil_max_limit', key: 'maxLimit', label: 'مبلغ السقف الأقصى المعتمد * (f_ceil_max_limit)', type: 'number', placeholder: 'مثال: 500000', required: true },
            { id: 'f_ceil_currency', key: 'currency', label: 'العملة المعتمدة للسقف * (f_ceil_currency)', type: 'select', options: ['YER - ريال يمني', 'USD - دولار أمريكي', 'SAR - ريال سعودي'], required: true },
            { id: 'f_ceil_credit_days', key: 'creditDays', label: 'فترة الائتمان المسموحة (بالأيام) * (f_ceil_credit_days)', type: 'number', placeholder: 'مثال: 30', required: true },
            { id: 'f_ceil_margin_pct', key: 'marginPct', label: 'نسبة هامش التجاوز المسموح % * (f_ceil_margin_pct)', type: 'number', placeholder: 'مثال: 5', required: true },
            { id: 'f_ceil_current_balance', key: 'utilized', label: 'الرصيد المستغل الحالي * (f_ceil_current_balance)', type: 'number', placeholder: 'مثال: 150000', required: true },
            { id: 'f_ceil_action_on_breach', key: 'actionOnBreach', label: 'الإجراء التلقائي عند بلوغ السقف * (f_ceil_action_on_breach)', type: 'select', options: ['منع وحظر العملية آلياً 🔒 (Block Transaction)', 'تعليق العملية وطلب موافقة المدير المالي ⚠️ (Require Financial Approval)', 'إصدار تنبيه وتحذير فقط دون إيقاف 🔔 (Warning Alert Only)'], required: true },
            { id: 'f_ceil_approval_authority', key: 'authority', label: 'المسؤول المخول بمنح الاستثناء * (f_ceil_approval_authority)', type: 'select', options: ['المدير العام التنفيذي', 'المدير المالي العام', 'مدير الحسابات'], required: true },
            { id: 'f_ceil_start_date', key: 'startDate', label: 'تاريخ بدء سريان السقف * (f_ceil_start_date)', type: 'date', default: new Date().toISOString().split('T')[0], required: true },
            { id: 'f_ceil_end_date', key: 'endDate', label: 'تاريخ انتهاء / تجديد السقف * (f_ceil_end_date)', type: 'date', default: '2026-12-31', required: true },
            { id: 'f_ceil_status', key: 'status', label: 'حالة السقف والائتمان * (f_ceil_status)', type: 'select', options: ['آمن ومفعل 🟢', 'موقف ومجمد 🔴', 'قيد المراجعة 🟡'], required: true },
            { id: 'f_ceil_notes', key: 'notes', label: 'الملاحظات وشروط الضمان الائتماني (f_ceil_notes)', type: 'textarea', placeholder: 'اكتب تفاصيل الضمانات البنكية أو السندات لأمر المعتمدة...', required: false, fullWidth: true }
        ];
    }
    if (entity === 'cost_center' || entity === 'cost_centers' || entity === 'costCenters' || entity === 'cost-centers') {
        return [
            { id: 'f_cc_code', key: 'code', label: 'كود مركز التكلفة * (f_cc_code)', type: 'text', placeholder: 'مثال: CC-105', required: true },
            { id: 'f_cc_name', key: 'name', label: 'اسم مركز التكلفة بالعربية * (f_cc_name)', type: 'text', placeholder: 'مثال: مشروع تجهيز معامل الذكاء الاصطناعي', required: true, fullWidth: true },
            { id: 'f_cc_name_en', key: 'nameEn', label: 'اسم المركز بالإنجليزية (f_cc_name_en)', type: 'text', placeholder: 'AI Labs Development Project', required: false },
            { id: 'f_cc_parent', key: 'parent', label: 'المركز الأب / التابع له (f_cc_parent)', type: 'text', placeholder: 'كود المركز الأب (مثال: CC-101)', required: false },
            { id: 'f_cc_type', key: 'type', label: 'المستوى والنوع * (f_cc_type)', type: 'select', options: ['رئيسي (Main)', 'فرعي (Sub)'], required: true },
            { id: 'f_cc_category', key: 'category', label: 'التصنيف / الموديول * (f_cc_category)', type: 'select', options: ['فرع', 'قسم', 'مشروع', 'نشاط'], required: true },
            { id: 'f_cc_manager', key: 'manager', label: 'مدير / مسؤول المركز * (f_cc_manager)', type: 'text', placeholder: 'مثال: م. خالد عبدالكريم', required: true },
            { id: 'f_cc_budget', key: 'budget', label: 'الموازنة المالية المعتمدة * (f_cc_budget)', type: 'number', placeholder: 'مثال: 2500000', required: true },
            { id: 'f_cc_actual', key: 'actualExpenses', label: 'المصروف الفعلي المحقق * (f_cc_actual)', type: 'number', placeholder: 'مثال: 950000', required: true },
            { id: 'f_cc_currency', key: 'currency', label: 'العملة المعتمدة للموازنة * (f_cc_currency)', type: 'select', options: ['YER - ريال يمني', 'USD - دولار أمريكي', 'SAR - ريال سعودي'], required: true },
            { id: 'f_cc_start_date', key: 'startDate', label: 'تاريخ بداية الموازنة * (f_cc_start_date)', type: 'date', default: new Date().toISOString().split('T')[0], required: true },
            { id: 'f_cc_end_date', key: 'endDate', label: 'تاريخ نهاية الموازنة * (f_cc_end_date)', type: 'date', default: '2026-12-31', required: true },
            { id: 'f_cc_restriction', key: 'restriction', label: 'نطاق تقييد المصروفات والحسابات * (f_cc_restriction)', type: 'select', options: ['جميع الحسابات', 'مصروفات التشغيل والصيانة فقط', 'بنود الرواتب والأجور فقط', 'المشتريات الرأسمالية فقط'], required: true },
            { id: 'f_cc_status', key: 'status', label: 'حالة مركز التكلفة * (f_cc_status)', type: 'select', options: ['نشط ومفعل 🟢', 'موقف ومجمد 🔴'], required: true }
        ];
    }
    if (entity === 'cashbox' || entity === 'cashboxes') {
        return [
            { id: 'f_cb_code', key: 'code', label: 'كود الصندوق المالي * (f_cb_code)', type: 'text', placeholder: 'مثال: CB-105', required: true },
            { id: 'f_cb_name', key: 'name', label: 'اسم الصندوق والخزينة بالعربية * (f_cb_name)', type: 'text', placeholder: 'مثال: صندوق تحصيل الرسوم الدراسية', required: true, fullWidth: true },
            { id: 'f_cb_name_en', key: 'nameEn', label: 'اسم الصندوق بالإنجليزية (f_cb_name_en)', type: 'text', placeholder: 'Tuition Fees Cash Box', required: false },
            { id: 'f_cb_account', key: 'accountCode', label: 'الحساب المحاسبي المرتبط * (f_cb_account)', type: 'select', options: ['110101 - صندوق النقدية الرئيسي', '110102 - بنك اليمن والكويت', '1101 - النقدية وما في حكمها'], required: true },
            { id: 'f_cb_branch', key: 'branch', label: 'الفرع / القسم التابع له * (f_cb_branch)', type: 'select', options: ['الفرع الرئيسي - صنعاء', 'فرع البنين - حدة', 'فرع البنات', 'الإدارة العامة والمكتب التنفيذي', 'قسم الأنشطة المدرسية'], required: true },
            { id: 'f_cb_cashier', key: 'cashier', label: 'أمين الصندوق (المسؤول) * (f_cb_cashier)', type: 'text', placeholder: 'مثال: أحمد محمد (أمين صندوق)', required: true },
            { id: 'f_cb_currency', key: 'currency', label: 'العملة المعتمدة للصندوق * (f_cb_currency)', type: 'select', options: ['YER - ريال يمني', 'USD - دولار أمريكي', 'SAR - ريال سعودي'], required: true },
            { id: 'f_cb_type', key: 'type', label: 'نوع وطبيعة الصندوق * (f_cb_type)', type: 'select', options: ['مبيعات يومية', 'عهدة مستديمة', 'تحصيل رسوم دراسية', 'مصروفات نثرية'], required: true },
            { id: 'f_cb_max_limit', key: 'maxLimit', label: 'سقف الصندوق (الحد الأقصى) * (f_cb_max_limit)', type: 'number', placeholder: 'مثال: 5000000', required: true },
            { id: 'f_cb_min_limit', key: 'minLimit', label: 'الحد الأدنى للنقدية * (f_cb_min_limit)', type: 'number', placeholder: 'مثال: 100000', required: true },
            { id: 'f_cb_balance', key: 'balance', label: 'الرصيد النقدي الفعلي * (f_cb_balance)', type: 'number', placeholder: 'مثال: 3500000', required: true },
            { id: 'f_cb_allow_negative', key: 'allowNegative', label: 'سياسة السماح بالرصيد السالب * (f_cb_allow_negative)', type: 'select', options: ['غير مسموح 🔒', 'مسموح بتجاوز استثنائي ⚠️'], required: true },
            { id: 'f_cb_status', key: 'status', label: 'حالة الصندوق * (f_cb_status)', type: 'select', options: ['نشط ومفعل 🟢', 'موقف ومجمد 🔴'], required: true }
        ];
    }
    if (entity === 'journal' || entity === 'journal_entry' || entity === 'journalEntries') {
        return [
            { id: 'f_jv_no', key: 'code', label: 'رقم القيد المالي * (f_jv_no)', type: 'text', placeholder: 'مثال: JV-2026-0005', required: true },
            { id: 'f_jv_date', key: 'date', label: 'تاريخ القيد * (f_jv_date)', type: 'date', default: new Date().toISOString().split('T')[0], required: true },
            { id: 'f_jv_ref', key: 'refNo', label: 'رقم المرجع / المستند المؤيد (f_jv_ref)', type: 'text', placeholder: 'مثال: INV-9988', required: false },
            { id: 'f_jv_type', key: 'type', label: 'نوع القيد المحاسبي * (f_jv_type)', type: 'select', options: ['قيد يومية عام (General Journal)', 'قيد افتتاحي (Opening Entry)', 'قيد تسوية وتعديل (Adjustment Entry)', 'قيد إقفال ختامي (Closing Entry)'], required: true },
            { id: 'f_jv_debit_acc', key: 'debitAcc', label: 'الحساب المالي المدين (Debit) * (f_jv_debit_acc)', type: 'select', options: ['5101 - رواتب وأجور الكادر التعليمي والإداري', '5102 - مصاريف الصيانة والتشغيل والأنشطة', '110101 - صندوق النقدية الرئيسي', '110102 - بنك اليمن والكويت', '110201 - رسوم الطلاب المستحقة المدينة', '2101 - الموردون والدائنون'], required: true },
            { id: 'f_jv_credit_acc', key: 'creditAcc', label: 'الحساب المالي الدائن (Credit) * (f_jv_credit_acc)', type: 'select', options: ['110101 - صندوق النقدية الرئيسي', '110102 - بنك اليمن والكويت', '4101 - إيرادات الرسوم الدراسية والتسجيل', '2101 - الموردون والدائنون', '3 - حقوق الملكية ورأس المال'], required: true },
            { id: 'f_jv_amount', key: 'amount', label: 'مبلغ القيد المتوازن * (f_jv_amount)', type: 'number', placeholder: 'مثال: 1800000', required: true },
            { id: 'f_jv_currency', key: 'currency', label: 'العملة المعتمدة * (f_jv_currency)', type: 'select', options: ['YER - ريال يمني', 'USD - دولار أمريكي', 'SAR - ريال سعودي'], required: true },
            { id: 'f_jv_cost_center', key: 'costCenter', label: 'مركز التكلفة المالي (f_jv_cost_center)', type: 'select', options: ['إدارة المدرسة والمبنى الرئيسي', 'إيرادات الرسوم الدراسية', 'صيانة ومرافق المدرسة', 'عام'], required: false },
            { id: 'f_jv_attachment', key: 'attachment', label: 'المرفق والمستند المؤيد (f_jv_attachment)', type: 'text', placeholder: 'مسير_الرواتب.pdf أو كشف_الحساب.jpg', required: false },
            { id: 'f_jv_status', key: 'status', label: 'حالة القيد والترحيل * (f_jv_status)', type: 'select', options: ['مرحّل للأستاذ العام 🟢', 'مسودة بانتظار المراجعة 🟡'], required: true },
            { id: 'f_jv_desc', key: 'mainDesc', label: 'البيان والتفاصيل الشاملة * (f_jv_desc)', type: 'textarea', placeholder: 'اكتب الشرح والبيان المحاسبي لموجب هذا القيد...', required: true, fullWidth: true }
        ];
    }
    if (entity === 'voucher' || entity === 'vouchers' || entity === 'voucher_receipt' || entity === 'voucher_payment') {
        const isPayment = entity === 'voucher_payment';
        return [
            { id: 'f_vch_code', key: 'code', label: 'رقم السند المالي * (f_vch_code)', type: 'text', placeholder: isPayment ? 'مثال: VCH-PAY-2026-004' : 'مثال: VCH-REC-2026-004', required: true },
            { id: 'f_vch_type', key: 'type', label: 'نوع السند * (f_vch_type)', type: 'select', options: isPayment ? ['سند صرف 🔴 (Payment Voucher)', 'سند قبض 🟢 (Receipt Voucher)'] : ['سند قبض 🟢 (Receipt Voucher)', 'سند صرف 🔴 (Payment Voucher)'], required: true },
            { id: 'f_vch_date', key: 'date', label: 'تاريخ السند * (f_vch_date)', type: 'date', default: new Date().toISOString().split('T')[0], required: true },
            { id: 'f_vch_amount', key: 'amount', label: 'مبلغ السند * (f_vch_amount)', type: 'number', placeholder: 'مثال: 150000', required: true },
            { id: 'f_vch_currency', key: 'currency', label: 'العملة المعتمدة * (f_vch_currency)', type: 'select', options: ['YER - ريال يمني', 'USD - دولار أمريكي', 'SAR - ريال سعودي'], required: true },
            { id: 'f_vch_party', key: 'party', label: 'اسم المسدد / المستفيد * (f_vch_party)', type: 'text', placeholder: isPayment ? 'مثال: أ. محمد الأحمدي (معلم رياضيات)' : 'مثال: الشيخ علي باعباد (ولي أمر)', required: true, fullWidth: true },
            { id: 'f_vch_method', key: 'paymentMethod', label: 'طريقة الدفع والتسوية * (f_vch_method)', type: 'select', options: ['نقداً من الخزينة (Cash)', 'تحويل بنكي / إيداع (Bank Transfer)', 'شيك بنكي معتمد (Check)', 'نقاط بيع / شبكة (POS)'], required: true },
            { id: 'f_vch_ref', key: 'refNo', label: 'رقم المرجع / التحويل / الشيك (f_vch_ref)', type: 'text', placeholder: 'REC-99881 أو CHK-889021', required: false },
            { id: 'f_vch_cost_center', key: 'costCenter', label: 'مركز التكلفة المالي * (f_vch_cost_center)', type: 'select', options: ['إيرادات الرسوم الدراسية', 'المصروفات الإدارية والتشغيلية', 'رواتب وأجور المعلمين', 'عهد الأنشطة المدرسية', 'صيانة ومرافق المدرسة'], required: true },
            { id: 'f_vch_account', key: 'account', label: 'حساب الخزينة / البنك المالي * (f_vch_account)', type: 'select', options: ['الصندوق الرئيسي (خزينة الإدارة)', 'بنك اليمن والكويت (حساب رئيسي)', 'بنك الكريمي الإسلامي', 'عهدة المصروفات النثرية'], required: true },
            { id: 'f_vch_attachment', key: 'attachment', label: 'مرفق السند / إشعار الدفع (f_vch_attachment)', type: 'text', placeholder: 'إشعار_تحويل_بنكي.pdf أو صورة_الشيك.jpg', required: false },
            { id: 'f_vch_status', key: 'status', label: 'حالة السند والترحيل * (f_vch_status)', type: 'select', options: ['معتمد ومرحل للأستاذ العام 🟢', 'مسودة بانتظار الاعتماد 🟡'], required: true },
            { id: 'f_vch_desc', key: 'description', label: 'البيان والتفاصيل الشاملة * (f_vch_desc)', type: 'textarea', placeholder: 'سداد القسط الأول من الرسوم الدراسية للعام الجديد / صرف مستحقات...', required: true, fullWidth: true }
        ];
    }
        if (entity === 'chart-accounts' || entity === 'accounts' || entity === 'chart_accounts') {
        return [
            { id: 'f_acc_code', key: 'code', label: 'كود الحساب المالي * (f_acc_code)', type: 'text', placeholder: 'مثال: 110101', required: true },
            { id: 'f_acc_name', key: 'name', label: 'اسم الحساب بالعربية * (f_acc_name)', type: 'text', placeholder: 'مثال: صندوق النقدية الرئيسي', required: true, fullWidth: true },
            { id: 'f_acc_name_en', key: 'nameEn', label: 'اسم الحساب بالإنجليزية (f_acc_name_en)', type: 'text', placeholder: 'Main Cash Box Account', required: false },
            { id: 'f_acc_parent', key: 'parent', label: 'كود ورقم الحساب الأب * (f_acc_parent)', type: 'text', placeholder: 'كود الحساب الأب (مثال: 1101)', required: false },
            { id: 'f_acc_level', key: 'level', label: 'المستوى المحاسبي في الشجرة * (f_acc_level)', type: 'select', options: ['1 (مستوى رئيسي عام)', '2 (مستوى تجميعي)', '3 (مستوى فرعي)', '4 (مستوى تحليلي للقيود)'], required: true },
            { id: 'f_acc_category', key: 'category', label: 'تصنيف الحساب المالي * (f_acc_category)', type: 'select', options: ['أصول متداولة', 'أصول ثابتة', 'خصوم متداولة', 'حقوق ملكية ورأس المال', 'إيرادات نشاط تعليمي', 'مصروفات تشغيلية', 'مصروفات عمومية وإدارية'], required: true },
            { id: 'f_acc_nature', key: 'nature', label: 'طبيعة الحساب المحاسبية * (f_acc_nature)', type: 'select', options: ['مدين (Debit) 🔵', 'دائن (Credit) 🟢'], required: true },
            { id: 'f_acc_type', key: 'postingType', label: 'نوع حركة الحساب والتقييد * (f_acc_type)', type: 'select', options: ['حساب رئيسي للعرض والتجميع فقط', 'حساب تحليلي يقبل القيود والترحيل 🟢'], required: true },
            { id: 'f_acc_currency', key: 'currency', label: 'العملة المعتمدة للحساب * (f_acc_currency)', type: 'select', options: ['YER - ريال يمني', 'USD - دولار أمريكي', 'SAR - ريال سعودي'], required: true },
            { id: 'f_acc_balance', key: 'balance', label: 'الرصيد الافتتاحي للحساب (f_acc_balance)', type: 'number', placeholder: 'مثال: 1500000', required: false },
            { id: 'f_acc_report', key: 'reportLink', label: 'الربط المالي بالقوائم الختامية * (f_acc_report)', type: 'select', options: ['الميزانية العمومية (Balance Sheet)', 'قائمة الدخل والأرباح والخسائر (Income Statement)'], required: true },
            { id: 'f_acc_cost_center', key: 'costCenter', label: 'مركز التكلفة الافتراضي (f_acc_cost_center)', type: 'select', options: ['عام', 'الإدارة العامة', 'فرع البنين', 'فرع البنات'], required: false },
            { id: 'f_acc_status', key: 'status', label: 'حالة تفعيل الحساب * (f_acc_status)', type: 'select', options: ['نشط ومفعل يقبل الحركات 🟢 (Active)', 'موقف ومجمد مؤقتاً 🔴 (Inactive)'], required: true },
            { id: 'f_acc_notes', key: 'notes', label: 'الملاحظات والتعليمات المحاسبية (f_acc_notes)', type: 'textarea', placeholder: 'اكتب تفاصيل وضوابط التقييد واستخدام الحساب المحاسبي...', required: false, fullWidth: true }
        ];
    }
    if (entity === 'posting' || entity === 'postingBatches') {
        return [
            { id: 'f_batch_id', key: 'id', label: 'رقم الدفعة * (f_batch_id)', type: 'text', placeholder: 'مثال: BATCH-2026-085', required: true },
            { id: 'f_batch_module', key: 'module', label: 'الموديول والنوع * (f_batch_module)', type: 'select', options: ['سندات القبض المالية (Receipt Vouchers)', 'سندات الصرف والعهد (Payment Vouchers)', 'قيود اليومية العامة (Journal Entries)', 'شيتات درجات الكنترول (Grading Sheets)', 'مسير ومعالجة الرواتب (Payroll)'], required: true },
            { id: 'f_batch_desc', key: 'description', label: 'البيان وتفاصيل المعاملة * (f_batch_desc)', type: 'text', placeholder: 'مثال: ترحيل سندات تحصيل الرسوم للفترة...', required: true, fullWidth: true },
            { id: 'f_batch_date', key: 'date', label: 'تاريخ المعاملة * (f_batch_date)', type: 'date', default: new Date().toISOString().split('T')[0], required: true },
            { id: 'f_batch_amount', key: 'amount', label: 'إجمالي المبلغ / القيمة * (f_batch_amount)', type: 'text', placeholder: 'مثال: 1,850,000 YER', required: true },
            { id: 'f_batch_count', key: 'count', label: 'عدد السجلات والعمليات * (f_batch_count)', type: 'text', placeholder: 'مثال: 14 سند مالي', required: true },
            { id: 'f_batch_author', key: 'author', label: 'المسؤول والمنشئ * (f_batch_author)', type: 'text', placeholder: 'أ. سارة المحاسبة', required: true },
            { id: 'f_batch_status', key: 'status', label: 'حالة الترحيل * (f_batch_status)', type: 'select', options: ['بانتظار الترحيل ⏳', 'مرحل ومعتمد للأستاذ العام 🟢'], required: true }
        ];
    }

    if (entity === 'archive' || entity === 'archiveDocs') {
        return [
            { id: 'f_arc_title', key: 'title', label: 'عنوان الوثيقة الأصلي * (f_arc_title)', type: 'text', placeholder: 'مثال: الترخيص الوزاري الرسمي 2026...', required: true, fullWidth: true },
            { id: 'f_arc_code', key: 'id', label: 'كود الوثيقة * (f_arc_code)', type: 'text', placeholder: 'DOC-2026-005', required: true },
            { id: 'f_arc_category', key: 'category', label: 'التصنيف / المجلد * (f_arc_category)', type: 'select', options: ['الوثائق السيادية والترخيص', 'الشؤون القانونية والعقارات', 'اللوائح التنظيمية والأكاديميا', 'سجلات الطلاب والشهادات', 'الشؤون المالية والإقفالات', 'الموارد البشرية والعقود', 'التقارير والإحصائيات'], required: true },
            { id: 'f_arc_ref', key: 'refNo', label: 'الرقم الإشاري الأصلي * (f_arc_ref)', type: 'text', placeholder: 'LIC-MOE-2026-8941', required: true },
            { id: 'f_arc_format', key: 'format', label: 'نوع ومعاينة الملف * (f_arc_format)', type: 'select', options: ['PDF 📄', 'XLSX / PDF 📊', 'PNG 🖼️', 'DOCX 📝'], required: true },
            { id: 'f_arc_conf', key: 'confidentiality', label: 'مستوى السرية * (f_arc_conf)', type: 'select', options: ['سري للغاية 🔴', 'سري جداً 🔴', 'خاص بالإدارة 🟡', 'خاص بالسجلات 🟡', 'عام ومتاح 🟢'], required: true },
            { id: 'f_arc_tags', key: 'tags', label: 'الكلمات المفتاحية (OCR Tags) * (f_arc_tags)', type: 'text', placeholder: '#ترخيص #وزارة #اعتماد #سيادي', required: true },
            { id: 'f_arc_archivist', key: 'archivist', label: 'اسم الموظف المؤرِشف * (f_arc_archivist)', type: 'text', placeholder: 'د. عبد الرحمن باعباد', required: true },
            { id: 'f_arc_retention', key: 'retention', label: 'سياسة الحفظ والوضع * (f_arc_retention)', type: 'select', options: ['حفظ دائم 🔒', 'حفظ 15 سنة 🟢', 'حفظ 10 سنوات 🟢', 'حفظ 5 سنوات 🟡'], required: true }
        ];
    }

    if (entity === 'user' || entity === 'users') {
        return [
            { id: 'f_user_fullname', key: 'name', label: 'الاسم الكامل والوظيفي *', type: 'text', placeholder: 'مثال: أ. سالم محمد الحميري', required: true, fullWidth: true },
            { id: 'f_user_username', key: 'username', label: 'اسم تسجيل الدخول (Username) *', type: 'text', placeholder: 'اسم المستخدم أو الرقم الوظيفي/الوطني...', required: true },
            { id: 'f_user_password', key: 'password', label: 'كلمة المرور الابتدائية *', type: 'password', placeholder: 'كلمة المرور للدخول...', required: true },
            { id: 'f_user_role', key: 'role', label: 'نوع الحساب والدور *', type: 'select', options: ['مدير المدرسة (School Admin)', 'وكيل / مشرف تربوي (Supervisor)', 'معلم (Teacher)', 'محاسب مالي رئيسي (Accountant)', 'أمين مخزن ومشتريات (Inventory Manager)', 'مسؤول شؤون طلاب وقبول (Registrar)', 'مشرف حافلات ومواصلات (Transport Officer)', 'رائد نشاط مدرسي (Activities Leader)', 'ولي أمر طالب (Parent)', 'طالب (Student)'], required: true },
            { id: 'f_user_dept', key: 'dept', label: 'القسم / الإدارة التابع لها *', type: 'select', options: ['الإدارة العامة والمكتب التنفيذي', 'قسم الشؤون المالية والحسابات', 'قسم شؤون الطلاب والقبول', 'قسم المرحلة الثانوية', 'قسم المرحلة الأساسية', 'قسم رياض الأطفال والتمهيدي', 'الكنترول وإدارة الامتحانات', 'قسم الخدمات والأنشطة المدرسية والمستودعات', 'قسم الحركة والمواصلات', 'أولياء الأمور والطلاب'], required: true },
            { id: 'f_user_phone', key: 'phone', label: 'رقم الهاتف / الجوال *', type: 'tel', placeholder: '771234567', required: true, hint: 'مخصص لإشعارات الدخول والتحقق الثنائي 2FA' },
            { id: 'f_user_email', key: 'email', label: 'البريد الإلكتروني المهني', type: 'email', placeholder: 'user@school.edu.ye', required: false },
            { id: 'f_user_status', key: 'status', label: 'حالة الحساب *', type: 'select', options: ['نشط 🟢', 'موقوف 🔴', 'قيد التدقيق 🟡'], required: true }
        ];
    }

    if (entity === 'student' || entity === 'students') {
        return [
            { id: 'st_name', key: 'name', label: 'اسم الطالب الرباعي', type: 'text', placeholder: 'مثال: أحمد علي محمد باعباد', required: true, fullWidth: true },
            { id: 'st_national_id', key: 'nationalId', label: 'الرقم الوطني / رقم الهوية الوطنية', type: 'text', placeholder: 'مثال: 10892019920', required: true, hint: '🔑 سيكون اسم/رقم المستخدم لحساب ولي الأمر في البوابة' },
            { id: 'st_parent_name', key: 'parentName', label: 'اسم ولي الأمر الكامل', type: 'text', placeholder: 'مثال: الشيخ علي محمد باعباد', required: true },
            { id: 'st_parent_phone', key: 'parentPhone', label: 'رقم هاتف ولي الأمر (الجوال)', type: 'tel', placeholder: 'مثال: 771234567', required: true, hint: '🔒 ستكون كلمة المرور المعتمدة لتسجيل دخول ولي الأمر' },
            { id: 'st_grade', key: 'grade', label: 'المرحلة والصف والشعبة', type: 'select', options: ['الثالث الثانوي - علمي 1', 'الثالث الثانوي - أدبي', 'الثاني الثانوي - علمي', 'الأول الثانوي - عام', 'التاسع أساسي', 'الثامن أساسي', 'السابع أساسي', 'السادس أساسي', 'الخامس أساسي', 'الرابع أساسي', 'الثالث أساسي', 'الثاني أساسي', 'الأول أساسي', 'تمهيدي وروضة'], required: true },
            { id: 'st_dob', key: 'dob', label: 'تاريخ الميلاد', type: 'date', default: '2010-05-15', required: false },
            { id: 'st_nationality', key: 'nationality', label: 'الجنسية', type: 'select', options: ['يمني 🇾🇪', 'سعودي 🇸🇦', 'مصري 🇪🇬', 'سوري 🇸🇾', 'أردني 🇯🇴', 'أخرى'], required: true },
            { id: 'st_address', key: 'address', label: 'عنوان السكن والتفاصيل', type: 'text', placeholder: 'صنعاء - شارع حدة - حي الرويشان', required: false },
            { id: 'st_date', key: 'date', label: 'تاريخ التسجيل والقبول', type: 'date', default: new Date().toISOString().split('T')[0], required: true },
            { id: 'st_status', key: 'status', label: 'حالة الرسوم والقبول', type: 'select', options: ['مسدد بالكامل 🟢', 'قيد السداد / أقساط 🟡', 'غير مسدد 🔴', 'منحة دراسية وتفوق 🔵'], required: true }
        ];
    }

    return [
        { id: 'f_title', key: 'name', label: 'الاسم / العنوان *', type: 'text', placeholder: 'أدخل الاسم...', required: true },
        { id: 'f_code', key: 'code', label: 'الكود / المعرف *', type: 'text', placeholder: 'الكود المرجعي...', required: true },
        { id: 'f_category', key: 'category', label: 'التصنيف / الموديول', type: 'text', placeholder: 'التصنيف...', required: true },
        { id: 'f_status', key: 'status', label: 'الحالة *', type: 'select', options: ['نشط ومفعل 🟢', 'معطل 🔴', 'قيد الانتظار 🟡'], required: true },
        { id: 'f_notes', key: 'notes', label: 'الملاحظات والبيان', type: 'textarea', placeholder: 'اكتب الملاحظات...', required: false }
    ];
}
window.getFormFields = getFormFields;

function saveForm(type) {
    type = type || window.currentEditingType || 'student';
    const collKey = getCollectionKey(type);
    
    if (!window.DB) window.DB = {};
    if (!window.DB[collKey]) window.DB[collKey] = [];

    const editId = window.currentEditingId;
    const fields = getFormFields(type);

    const newRec = {};
    for (const f of fields) {
        const el = document.getElementById(f.id);
        if (el) {
            const val = el.value ? String(el.value).trim() : '';
            if (f.required && !val) {
                el.classList.add('is-invalid');
                el.style.border = '2px solid #ef4444';
                el.style.boxShadow = '0 0 0 3px rgba(239, 68, 68, 0.25)';
                el.focus();
                const fieldLabel = (f.label || f.key || '').replace('*', '').trim() || 'هذا الحقل';
                if (typeof toast === 'function') toast(`⚠️ يرجى تعبئة الحقل الإلزامي: (${fieldLabel})`, 1);
                return false;
            } else {
                el.classList.remove('is-invalid');
                el.style.border = '';
                el.style.boxShadow = '';
            }
            newRec[f.key] = val;
        }
    }

    if (type === 'user' || type === 'users') {
        const checkedBoxes = document.querySelectorAll('.rbac-chk:checked');
        const perms = Array.from(checkedBoxes).map(c => c.value);
        newRec.permissions = perms;
        newRec.allowedPagesCount = perms.length + ' واجهة مصرح بها 🟢';
        if (newRec.name) newRec.roleName = newRec.role;

        newRec.actions = {
            create: document.getElementById('perm_act_create')?.checked ?? true,
            edit: document.getElementById('perm_act_edit')?.checked ?? true,
            delete: document.getElementById('perm_act_delete')?.checked ?? true,
            search: document.getElementById('perm_act_search')?.checked ?? true,
            print: document.getElementById('perm_act_print')?.checked ?? true
        };
    }

    if (editId) {
        let item = window.DB[collKey].find(x =>
            x.id == editId || x.code == editId || x.nationalId == editId || x.username == editId || x.key == editId
        );
        if (item) {
            Object.assign(item, newRec);
            if (typeof toast === 'function') toast('✅ تم تحديث بيانات السجل بنجاح!');
        } else {
            if (typeof toast === 'function') toast('⚠️ تم حفظ التعديلات في النظام!');
        }
    } else {
        const prefix = {
            'student':'STD','students':'STD','employee':'EMP','employees':'EMP','user':'USR',
            'users':'USR','system_settings':'SET','systemSettingsData':'SET','archive':'DOC'
        };
        const pfx = prefix[type] || (type.toUpperCase().slice(0,3));
        newRec.id = pfx + '-' + Date.now().toString().slice(-5);
        newRec.schoolId = window.currentSchoolId || 1;
        if (!newRec.date) newRec.date = new Date().toISOString().split('T')[0];

        window.DB[collKey].unshift(newRec);
    }

    closeForm();

    if (type === 'user' || type === 'users') {
        if (typeof renderUsersGrid === 'function') renderUsersGrid();
    } else if (type === 'system_settings' || type === 'systemSettingsData') {
        if (typeof renderSystemSettingsGrid === 'function') renderSystemSettingsGrid();
    } else if (type === 'posting' || type === 'postingBatches') {
        if (typeof renderPostingGrid === 'function') renderPostingGrid();
    } else if (type === 'currency' || type === 'currencies') {
        if (typeof renderCurrenciesGrid === 'function') renderCurrenciesGrid();
    } else if (type === 'cashbox_inventory' || type === 'cashboxInventory') {
        if (typeof renderCashboxInventoryGrid === 'function') renderCashboxInventoryGrid();
    } else if (type === 'closing' || type === 'closings') {
        if (typeof renderClosingsGrid === 'function') renderClosingsGrid();
    } else if (type === 'banks' || type === 'bank') {
        if (typeof renderBanksGrid === 'function') renderBanksGrid();
    } else if (type === 'checks' || type === 'check') {
        if (typeof renderChecksGrid === 'function') renderChecksGrid();
    } else if (type === 'demand_letters' || type === 'demandLetters') {
        if (typeof renderDemandLettersGrid === 'function') renderDemandLettersGrid();
    } else if (type === 'finance_reports' || type === 'financeReports') {
        if (typeof renderFinanceReportsGrid === 'function') renderFinanceReportsGrid();
    } else if (type === 'academic_years' || type === 'academicYears' || type === 'academic-years') {
        if (typeof renderAcademicYearsGrid === 'function') renderAcademicYearsGrid();
    } else if (type === 'academic_calendar' || type === 'academicCalendar' || type === 'academic-calendar') {
        if (typeof renderAcademicCalendarGrid === 'function') renderAcademicCalendarGrid();
    } else if (type === 'stages' || type === 'stage' || type === 'grades') {
        if (typeof renderStagesGrid === 'function') renderStagesGrid();
    } else if (type === 'sections' || type === 'section') {
        if (typeof renderSectionsGrid === 'function') renderSectionsGrid();
    } else if (type === 'subjects' || type === 'subject') {
        if (typeof renderSubjectsGrid === 'function') renderSubjectsGrid();
    } else if (type === 'subject_distribution' || type === 'subject-distribution' || type === 'subjectDistribution') {
        if (typeof renderSubjectDistributionGrid === 'function') renderSubjectDistributionGrid();
    } else if (type === 'classrooms' || type === 'classroom' || type === 'labs') {
        if (typeof renderClassroomsGrid === 'function') renderClassroomsGrid();
    } else if (type === 'class_times' || type === 'class-times' || type === 'classTimes') {
        if (typeof renderClassTimesGrid === 'function') renderClassTimesGrid();
    } else if (type === 'timetable_builder' || type === 'timetable-builder' || type === 'timetableBuilder') {
        if (typeof renderTimetableBuilderGrid === 'function') renderTimetableBuilderGrid();
    } else if (type === 'required_docs' || type === 'required-docs' || type === 'requiredDocs') {
        if (typeof renderRequiredDocsGrid === 'function') renderRequiredDocsGrid();
    } else if (type === 'fee_categories' || type === 'fee-categories' || type === 'feeCategories') {
        if (typeof renderFeeCategoriesGrid === 'function') renderFeeCategoriesGrid();
    } else if (type === 'discount_categories' || type === 'discount-categories' || type === 'discountCategories' || type === 'discounts') {
        if (typeof renderDiscountCategoriesGrid === 'function') renderDiscountCategoriesGrid();
    } else if (type === 'installment_plans' || type === 'installment-plans' || type === 'installmentPlans') {
        if (typeof renderInstallmentPlansGrid === 'function') renderInstallmentPlansGrid();
    } else if (type === 'grade_fees' || type === 'grade-fees' || type === 'gradeFees') {
        if (typeof renderGradeFeesGrid === 'function') renderGradeFeesGrid();
    } else if (type === 'account-ceiling' || type === 'accountCeiling' || type === 'account_ceiling') {
        if (typeof renderAccountCeilingGrid === 'function') renderAccountCeilingGrid();
    } else if (type === 'cost_center' || type === 'cost_centers' || type === 'costCenters' || type === 'cost-centers') {
        if (typeof renderCostCentersGrid === 'function') renderCostCentersGrid();
    } else if (type === 'cashbox' || type === 'cashboxes') {
        if (typeof renderCashboxesGrid === 'function') renderCashboxesGrid();
    } else if (type === 'journal' || type === 'journal_entry' || type === 'journalEntries') {
        if (typeof renderJournalGrid === 'function') renderJournalGrid();
    } else if (type === 'voucher' || type === 'vouchers' || type === 'voucher_receipt' || type === 'voucher_payment') {
        if (typeof renderVouchersGrid === 'function') renderVouchersGrid();
    } else if (type === 'chart-accounts' || type === 'accounts') {
        if (typeof renderChartAccountsTree === 'function') renderChartAccountsTree();
    } else if (type === 'alerts' || type === 'alertsData') {
        if (typeof renderAlertsGrid === 'function') renderAlertsGrid();
    } else if (type === 'archive' || type === 'archiveDocs') {
        if (typeof renderArchiveGrid === 'function') renderArchiveGrid();
    } else if (typeof hydrateAndMountAllGrids === 'function') {
        hydrateAndMountAllGrids();
    }

    if (typeof toast === 'function') toast('🎉 تم حفظ السجل بنجاح ومزامنة البيانات لحظياً!');
    return true;
}
window.saveForm = saveForm;
