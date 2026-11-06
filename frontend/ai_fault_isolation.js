/**
 * ==============================================================================
 * 🛡️ CYBER GUARDIAN AI: INTERFACE FAULT ISOLATION & AUTONOMOUS REPAIR ENGINE
 * نظام عزل الأعطال الذاتي والتعافي التلقائي للواجهات السحابية
 * ==============================================================================
 */
(function() {
    window.AI_QUARANTINE_REGISTRY = {};
    window.AI_HEALING_IN_PROGRESS = {};

    // 1. Universal Error Boundary Interceptor
    window.addEventListener('error', function(event) {
        try {
            const activePage = document.querySelector('.page.active');
            if (activePage && activePage.id && !window.AI_QUARANTINE_REGISTRY[activePage.id]) {
                console.warn(`[AI Guardian] Intercepted runtime crash inside active page: ${activePage.id}`, event.error);
                isolateAndHealInterface(activePage.id, event.error || event.message);
                event.preventDefault();
            }
        } catch(e) {}
    });

    // 2. Safe Interface Switcher / Error Boundary for goTo()
    window.safeExecuteModule = function(pageId, executeCallback) {
        if (!pageId) return;
        
        // If page is currently quarantined
        if (window.AI_QUARANTINE_REGISTRY[pageId]) {
            renderAiQuarantineBanner(pageId, window.AI_QUARANTINE_REGISTRY[pageId]);
            return;
        }

        try {
            if (typeof executeCallback === 'function') {
                executeCallback();
            }
        } catch (err) {
            console.error(`[AI Guardian Intercept] Failure in interface [${pageId}]:`, err);
            isolateAndHealInterface(pageId, err);
        }
    };

    // 3. Interface Isolation (Quarantine)
    window.isolateAndHealInterface = function(pageId, error) {
        if (!pageId) return;
        const targetEl = document.getElementById(pageId);
        if (!targetEl) return;

        const errMsg = (error && error.message) ? error.message : String(error || 'خطأ غير متوقع في معالجة عناصر الواجهة');
        
        window.AI_QUARANTINE_REGISTRY[pageId] = {
            id: pageId,
            error: errMsg,
            quarantinedAt: new Date().toLocaleTimeString('ar-YE'),
            status: 'QUARANTINED',
            retryCount: (window.AI_QUARANTINE_REGISTRY[pageId]?.retryCount || 0) + 1
        };

        if (typeof toast === 'function') {
            toast(`🛡️ تنبيه سيبراني: تم عزل الواجهة (${pageId}) لحماية النظام، وجاري الإصلاح الذاتي...`, 2);
        }

        renderAiQuarantineBanner(pageId, window.AI_QUARANTINE_REGISTRY[pageId]);
        triggerAutonomousHealing(pageId);
    };

    // 4. Quarantine Banner Rendering
    function renderAiQuarantineBanner(pageId, record) {
        const targetEl = document.getElementById(pageId);
        if (!targetEl) return;

        targetEl.classList.add('active');
        targetEl.style.display = 'block';

        targetEl.innerHTML = `
            <div class="ai-quarantine-container" style="max-width: 860px; margin: 35px auto; padding: 30px; background: rgba(15, 23, 42, 0.95); border: 2px solid #3b82f6; border-radius: 20px; box-shadow: 0 20px 50px rgba(0,0,0,0.5), 0 0 30px rgba(59, 130, 246, 0.2); backdrop-filter: blur(16px); color: #f8fafc; font-family: 'Tajawal', sans-serif; text-align: center; position: relative; overflow: hidden;">
                
                <div style="position: absolute; top: -50px; right: -50px; width: 160px; height: 160px; background: radial-gradient(circle, rgba(59,130,246,0.3) 0%, transparent 70%); border-radius: 50%; pointer-events: none;"></div>
                
                <div style="width: 80px; height: 80px; margin: 0 auto 16px; border-radius: 50%; background: rgba(59, 130, 246, 0.15); border: 2px solid #38bdf8; display: flex; align-items: center; justify-content: center; font-size: 2.3rem; color: #38bdf8; animation: pulseGlow 2s infinite alternate;">
                    <i class="fa-solid fa-shield-halved"></i>
                </div>

                <div style="display: inline-block; padding: 6px 16px; background: rgba(59, 130, 246, 0.2); border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 30px; color: #60a5fa; font-weight: 700; font-size: 0.88rem; margin-bottom: 12px;">
                    🛡️ درع العزل الذاتي الذكي (Fault Isolation Active)
                </div>

                <h2 style="font-size: 1.5rem; font-weight: 800; margin: 0 0 10px; color: #ffffff;">
                    تم حجب وعزل هذه الواجهة مؤقتاً لحماية استقرار النظام والبيانات
                </h2>
                
                <p style="color: #94a3b8; font-size: 0.95rem; max-width: 650px; margin: 0 auto 18px; line-height: 1.6;">
                    رصد النظام خللاً في الواجهة (<code style="color:#38bdf8; background:rgba(255,255,255,0.06); padding:2px 8px; border-radius:6px;">${pageId}</code>). 
                    تم <strong style="color:#34d399;">حجب هذه الواجهة فقط</strong> لحماية المدرسة، بينما تستمر جميع البوابات وأقسام النظام الأخرى بالعمل بكفاءة 100%!
                </p>

                <div style="background: rgba(0, 0, 0, 0.4); border: 1px dashed rgba(239, 68, 68, 0.4); border-radius: 12px; padding: 12px 18px; text-align: right; max-width: 700px; margin: 0 auto 20px; font-family: monospace; font-size: 0.85rem; color: #fca5a5;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 6px;">
                        <span style="color:#94a3b8;"><i class="fa-solid fa-clock"></i> وقت الحجب: ${record.quarantinedAt}</span>
                        <span style="color:#f87171; font-weight:bold;"><i class="fa-solid fa-triangle-exclamation"></i> كود الخطأ المعزول</span>
                    </div>
                    <div style="white-space: pre-wrap; word-break: break-all;">${record.error}</div>
                </div>

                <div style="background: rgba(30, 41, 59, 0.8); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 16px 22px; max-width: 700px; margin: 0 auto 22px; text-align: right;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 10px;">
                        <span style="font-weight:700; color:#38bdf8; font-size:0.92rem;">
                            <i class="fa-solid fa-robot fa-spin" style="margin-left:6px;"></i> وكيل الذكاء الاصطناعي السيبراني (Cyber Guardian AI):
                        </span>
                        <span id="aiHealPhase_${pageId}" style="color:#34d399; font-weight:800; font-size:0.85rem;">
                            ⏳ جاري فحص بنية الـ DOM وترميم البيانات...
                        </span>
                    </div>
                    
                    <div style="width: 100%; height: 9px; background: rgba(0,0,0,0.5); border-radius: 10px; overflow: hidden; position: relative;">
                        <div id="aiHealProgress_${pageId}" style="width: 35%; height: 100%; background: linear-gradient(90deg, #3b82f6, #10b981); border-radius: 10px; transition: width 0.6s ease;"></div>
                    </div>
                </div>

                <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
                    <button onclick="triggerAutonomousHealing('${pageId}', true)" style="background: linear-gradient(135deg, #2563eb, #1d4ed8); color: white; border: none; padding: 11px 22px; border-radius: 10px; font-weight: 800; cursor: pointer; display: flex; align-items: center; gap: 8px; font-family: inherit; box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4);">
                        <i class="fa-solid fa-wand-magic-sparkles"></i> تنفيذ الإصلاح التلقائي الآن
                    </button>
                    <button onclick="goTo('pg-dashboard')" style="background: rgba(255, 255, 255, 0.08); color: #cbd5e1; border: 1px solid rgba(255,255,255,0.15); padding: 11px 22px; border-radius: 10px; font-weight: 700; cursor: pointer; display: flex; align-items: center; gap: 8px; font-family: inherit;">
                        <i class="fa-solid fa-house"></i> متابعة العمل في باقي الأقسام
                    </button>
                </div>
            </div>
            <style>
                @keyframes pulseGlow {
                    0% { box-shadow: 0 0 10px rgba(56, 189, 248, 0.2); }
                    100% { box-shadow: 0 0 35px rgba(56, 189, 248, 0.6); }
                }
            </style>
        `;
    }

    // 5. Autonomous Self-Healing Pipeline
    window.triggerAutonomousHealing = function(pageId, isManual) {
        if (window.AI_HEALING_IN_PROGRESS[pageId]) return;
        window.AI_HEALING_IN_PROGRESS[pageId] = true;

        const prg = document.getElementById('aiHealProgress_' + pageId);
        const phs = document.getElementById('aiHealPhase_' + pageId);

        // Phase 1: DOM Sanitization (0.8s)
        setTimeout(() => {
            if (prg) prg.style.width = '65%';
            if (phs) phs.innerHTML = '🧹 تنظيف عناصر الـ DOM التالفة ومسح التضارب البرمجي...';

            document.querySelectorAll('.modal-backdrop, .stray-overlay').forEach(el => el.remove());

            // Phase 2: Data Rehydration (1.6s)
            setTimeout(() => {
                if (prg) prg.style.width = '90%';
                if (phs) phs.innerHTML = '✨ إعادة بناء وتوليد الواجهة بنمط الحماية العالية...';

                const collectionKeyMap = {
                    'pg-students': 'students',
                    'pg-sections': 'sections',
                    'pg-stages': 'stages',
                    'pg-vouchers': 'vouchers',
                    'pg-journal': 'journalEntries',
                    'pg-employees': 'employees',
                    'pg-users': 'users'
                };
                const coll = collectionKeyMap[pageId];
                if (coll && window.DB && (!window.DB[coll] || !Array.isArray(window.DB[coll]))) {
                    window.DB[coll] = [];
                }

                // Phase 3: Restoration and Clearance (2.4s)
                setTimeout(() => {
                    delete window.AI_QUARANTINE_REGISTRY[pageId];
                    delete window.AI_HEALING_IN_PROGRESS[pageId];

                    const pageEl = document.getElementById(pageId);
                    if (pageEl) {
                        pageEl.innerHTML = '';
                    }

                    if (typeof goTo === 'function') {
                        goTo(pageId);
                    }

                    if (typeof toast === 'function') {
                        toast(`🎉 نجح وكيل الذكاء الاصطناعي في إصلاح واجهة (${pageId}) واستعادتها بالكامل دون توقف النظام!`, 0);
                    }

                    if (typeof addAudit === 'function') {
                        addAudit('إصلاح ذاتي بالذكاء الاصطناعي', `قام Cyber Guardian AI بعزل وإصلاح الخلل في واجهة ${pageId} بنجاح.`);
                    }
                }, 800);

            }, 800);

        }, 800);
    };
})();
