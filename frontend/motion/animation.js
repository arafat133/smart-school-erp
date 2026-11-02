/**
 * SMART SCHOOL ERP — MOTION GRAPHICS AD TIMELINE (GSAP 3)
 * Full 60-Second Interactive Ad Timeline with Audio & Arabic Voiceover Integration
 */

document.addEventListener('DOMContentLoaded', () => {
    gsap.registerPlugin(TextPlugin);

    // Audio Engine Reference
    const snd = window.soundEngine;

    // Cache DOM Elements
    const progressFill = document.getElementById('progressFill');
    const progressBar = document.getElementById('progressBar');
    const timeDisplay = document.getElementById('timeDisplay');
    const btnPlay = document.getElementById('btnPlay');
    const btnPause = document.getElementById('btnPause');
    const btnRestart = document.getElementById('btnRestart');
    const btnSound = document.getElementById('btnSound');
    const btnVoice = document.getElementById('btnVoice');
    const audioEqualizer = document.getElementById('audioEqualizer');
    const audioPromptOverlay = document.getElementById('audioPromptOverlay');
    const btnEnableAudio = document.getElementById('btnEnableAudio');
    const btnMuteAudio = document.getElementById('btnMuteAudio');

    // --- Master Timeline Setup ---
    const masterTL = gsap.timeline({
        paused: true, // initially paused until prompt is resolved
        onUpdate: updatePlaybackUI,
        onComplete: () => {
            console.log('Motion Graphics Ad Completed.');
            if (audioEqualizer) audioEqualizer.classList.remove('playing');
        }
    });

    // Create background particles for scenes 3 & 10
    createParticles('particles3', 35);
    createParticles('particles10', 40);

    // ========================================================================
    // SCENE 1: THE PAIN QUESTION (0.0s – 5.0s)
    // ========================================================================
    const scene1TL = gsap.timeline();
    scene1TL
        .set('#scene1', { autoAlpha: 1 })
        // Arabic Voiceover Trigger
        .add(() => {
            snd.speakArabic('كم ساعة تضيع كل أسبوع في محاولة ضبط الجداول المدرسية يدوياً وحل التعارضات؟', 'vo_scene1');
        }, 0.2)
        .fromTo('#questionMark', 
            { scale: 0.5, opacity: 0 }, 
            { scale: 1, opacity: 0.06, duration: 2, ease: "power2.out" }, 0)
        // Subtle clock ticks during question typing
        .add(() => snd.playSFX('tick'), 0.5)
        .add(() => snd.playSFX('tick'), 1.2)
        .add(() => snd.playSFX('tick'), 2.0)
        .add(() => snd.playSFX('tick'), 2.8)
        .to('#questionText', {
            duration: 3.2,
            text: {
                value: 'كم ساعة تضيع كل أسبوع في محاولة ضبط الجداول المدرسية يدوياً وحل التعارضات؟',
                delimiter: ""
            },
            ease: "none"
        }, 0.3)
        .to('#scene1', { autoAlpha: 0, duration: 0.5, ease: "power2.in" }, 4.5);

    // ========================================================================
    // SCENE 2: THE CHAOS (5.0s – 12.0s)
    // ========================================================================
    const scene2TL = gsap.timeline();
    const chaosCards = gsap.utils.toArray('.chaos-card');
    
    scene2TL
        .set('#scene2', { autoAlpha: 1 })
        // Voiceover for Scene 2
        .add(() => {
            snd.speakArabic('تعارض مستمر في الجداول، تشتت مالي، ومخاطر أمنية مهددة.', 'vo_scene2');
        }, 0.2)
        // Card 1 Slam
        .add(() => snd.playSFX('tick'), 0.2)
        // Card 2 Slam
        .add(() => snd.playSFX('tick'), 0.55)
        // Card 3 Slam
        .add(() => snd.playSFX('tick'), 0.9)
        // Card 4 Slam
        .add(() => snd.playSFX('sub_bass'), 1.25)
        .fromTo(chaosCards, 
            { scale: 0.7, opacity: 0, y: 40, rotation: () => gsap.utils.random(-8, 8) },
            { 
                scale: 1, 
                opacity: 1, 
                y: 0, 
                rotation: () => gsap.utils.random(-3, 3), 
                stagger: 0.35, 
                duration: 0.8, 
                ease: "back.out(1.7)" 
            }, 0.2)
        // Light subtle camera shake effect on chaos container
        .to('.chaos-cards', {
            x: () => gsap.utils.random(-4, 4),
            y: () => gsap.utils.random(-3, 3),
            repeat: 5,
            yoyo: true,
            duration: 0.1,
            ease: "none"
        }, 2.5)
        .to('#scene2', { autoAlpha: 0, duration: 0.3 }, 6.7);

    // ========================================================================
    // FLASH TRANSITION (12.0s – 12.4s)
    // ========================================================================
    const flashTL = gsap.timeline();
    flashTL
        .add(() => snd.playSFX('flash'), 0)
        .fromTo('#flashOverlay', 
            { opacity: 0 }, 
            { opacity: 1, duration: 0.15, ease: "power2.in" })
        .to('#flashOverlay', 
            { opacity: 0, duration: 0.25, ease: "power2.out" });

    // ========================================================================
    // SCENE 3: LOGO REVEAL (12.4s – 18.0s)
    // ========================================================================
    const scene3TL = gsap.timeline();
    scene3TL
        .set('#scene3', { autoAlpha: 1 })
        .add(() => {
            snd.playSFX('sub_bass');
            snd.playSFX('chime');
        }, 0.1)
        .add(() => {
            snd.speakArabic('منظومة إدارة المدرسة الذكية، السحابية الآمنة.', 'vo_scene3');
        }, 0.6)
        .fromTo('#logoIcon', 
            { opacity: 0, scale: 0.6 }, 
            { opacity: 1, scale: 1, duration: 0.8, ease: "back.out(1.5)" }, 0.1)
        .to('.logo-path', {
            strokeDashoffset: 0,
            duration: 1.5,
            stagger: 0.2,
            ease: "power2.inOut"
        }, 0.2)
        .fromTo('#logoGlow', 
            { opacity: 0, scale: 0.5 }, 
            { opacity: 0.8, scale: 1.3, duration: 1.2, ease: "power2.out" }, 0.5)
        .fromTo('#brandName', 
            { opacity: 0, y: 30, scale: 0.85 }, 
            { opacity: 1, y: 0, scale: 1, duration: 0.8, ease: "power3.out" }, 1.2)
        .fromTo('#brandSubtitle', 
            { opacity: 0, y: 15 }, 
            { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, 1.6)
        .fromTo('#brandLine', 
            { width: 0 }, 
            { width: '280px', duration: 0.8, ease: "power3.inOut" }, 1.8)
        .to('#scene3', { autoAlpha: 0, duration: 0.5, ease: "power2.in" }, 5.1);

    // ========================================================================
    // SCENE 4: EXECUTIVE DASHBOARD (18.0s – 24.0s)
    // ========================================================================
    const scene4TL = gsap.timeline();
    const statCards = gsap.utils.toArray('.mock-stat-card');
    const chartBars = gsap.utils.toArray('.mock-bar');

    scene4TL
        .set('#scene4', { autoAlpha: 1 })
        .add(() => snd.playSFX('whoosh'), 0.1)
        .add(() => {
            snd.speakArabic('لوحة قيادة تنفيذية ذكية بمؤشرات أداء رقمية لحظية.', 'vo_scene4');
        }, 0.3)
        .fromTo('#scene4Title', 
            { opacity: 0, y: -20 }, 
            { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, 0)
        .fromTo('#dashboardMockup', 
            { opacity: 0, rotationY: -10, scale: 0.9, y: 30 },
            { opacity: 1, rotationY: 0, scale: 1, y: 0, duration: 1.1, ease: "power3.out" }, 0.2)
        .fromTo(statCards, 
            { opacity: 0, y: 20 },
            { opacity: 1, y: 0, stagger: 0.15, duration: 0.6, ease: "back.out(1.4)" }, 0.6)
        // Animate counter numbers + clicks
        .add(() => {
            snd.playSFX('tick');
            animateNumber('1248', '[data-target="1248"]', 0, 1248, 1.2, '');
            animateNumber('96.8', '[data-target="96.8"]', 0, 96.8, 1.2, '%');
            animateNumber('482500', '[data-target="482500"]', 0, 482500, 1.4, 'SAR ', true);
        }, 0.8)
        // Grow chart bars
        .to(chartBars, {
            height: (i, el) => el.getAttribute('data-height') + '%',
            stagger: 0.1,
            duration: 0.9,
            ease: "power2.out"
        }, 1.2)
        .to('#scene4', { autoAlpha: 0, duration: 0.5, ease: "power2.in" }, 5.5);

    // ========================================================================
    // SCENE 5: CSP TIMETABLE ENGINE (24.0s – 32.0s)
    // ========================================================================
    const scene5TL = gsap.timeline();
    const ttCells = gsap.utils.toArray('.tt-cell');
    const consoleLines = gsap.utils.toArray('.console-line');

    scene5TL
        .set('#scene5', { autoAlpha: 1 })
        .add(() => {
            snd.speakArabic('محرك جدولة ذكي بالذكاء الاصطناعي، يولد الجدول في ثانية وثمانية أجزاء، بصفر تعارضات.', 'vo_scene5');
        }, 0.2)
        .fromTo('#scene5Title', 
            { opacity: 0, y: -20 }, 
            { opacity: 1, y: 0, duration: 0.5, ease: "power2.out" }, 0)
        .fromTo('#timetableGrid', 
            { opacity: 0, scale: 0.95 }, 
            { opacity: 1, scale: 1, duration: 0.6, ease: "power2.out" }, 0.2)
        // Sound cascade as timetable fills up
        .add(() => snd.playSFX('cascade'), 0.4)
        .to(ttCells, {
            opacity: 1,
            scale: 1,
            backgroundColor: (i, el) => el.getAttribute('data-color'),
            stagger: {
                grid: [3, 5],
                from: "random",
                amount: 1.2
            },
            duration: 0.4,
            ease: "back.out(1.6)"
        }, 0.4)
        // Zero Conflict Badge pop + Chime
        .add(() => snd.playSFX('chime'), 1.8)
        .fromTo('#zeroConflict', 
            { opacity: 0, scale: 0.5, y: 10 }, 
            { opacity: 1, scale: 1, y: 0, duration: 0.6, ease: "back.out(2)" }, 1.8)
        // Transition timetable to console log
        .to(['#timetableGrid', '#zeroConflict'], { opacity: 0, scale: 0.95, duration: 0.4, display: 'none' }, 2.7)
        .fromTo('#cspConsole', 
            { opacity: 0, y: 20 }, 
            { opacity: 1, y: 0, duration: 0.5, ease: "power2.out" }, 2.9)
        .add(() => snd.playSFX('tick'), 3.1)
        .to(consoleLines, {
            opacity: 1,
            x: 0,
            stagger: 0.25,
            duration: 0.3,
            ease: "power1.out"
        }, 3.1)
        // Reveal Big Number "1.8s" + Sub Bass Impact
        .to('#cspConsole', { opacity: 0, duration: 0.4, display: 'none' }, 5.2)
        .add(() => snd.playSFX('sub_bass'), 5.4)
        .fromTo('#bigNumber', 
            { opacity: 0, scale: 0.7, y: 30 }, 
            { opacity: 1, scale: 1, y: 0, duration: 0.8, ease: "back.out(1.8)" }, 5.4)
        .to('#scene5', { autoAlpha: 0, duration: 0.5, ease: "power2.in" }, 7.5);

    // ========================================================================
    // SCENE 6: 10 OPERATIONAL MODULES (32.0s – 40.0s)
    // ========================================================================
    const scene6TL = gsap.timeline();
    const moduleCards = gsap.utils.toArray('.module-card');

    scene6TL
        .set('#scene6', { autoAlpha: 1 })
        .add(() => {
            snd.speakArabic('عشرة قطاعات تشغيلية متكاملة، وأكثر من ستين واجهة عمل ذكية.', 'vo_scene6');
        }, 0.2)
        .fromTo('#scene6Title', 
            { opacity: 0, y: -20 }, 
            { opacity: 1, y: 0, duration: 0.5, ease: "power2.out" }, 0)
        .add(() => snd.playSFX('whoosh'), 0.2)
        .fromTo(moduleCards, 
            { opacity: 0, scale: 0.6, y: 30 }, 
            { 
                opacity: 1, 
                scale: 1, 
                y: 0, 
                stagger: 0.08, 
                duration: 0.5, 
                ease: "back.out(1.7)" 
            }, 0.2)
        .fromTo('.module-counter', 
            { opacity: 0, scale: 0.8 }, 
            { opacity: 1, scale: 1, duration: 0.6, ease: "power2.out" }, 1.5)
        .add(() => {
            snd.playSFX('tick');
            const counterObj = { val: 0 };
            const el = document.getElementById('interfaceCounter');
            gsap.to(counterObj, {
                val: 64,
                duration: 1.8,
                ease: "power2.out",
                onUpdate: () => {
                    if (el) el.textContent = Math.round(counterObj.val) + '+';
                }
            });
        }, 1.7)
        .to(moduleCards, {
            y: (i) => (i % 2 === 0 ? -6 : 6),
            repeat: 2,
            yoyo: true,
            stagger: 0.05,
            duration: 0.8,
            ease: "sine.inOut"
        }, 2.5)
        .to('#scene6', { autoAlpha: 0, duration: 0.5, ease: "power2.in" }, 7.5);

    // ========================================================================
    // SCENE 7: 3D CAROUSEL LIVE SCREENS (40.0s – 47.0s)
    // ========================================================================
    const scene7TL = gsap.timeline();
    const carouselItems = gsap.utils.toArray('.carousel-item');
    const labelEl = document.getElementById('carouselLabel');

    scene7TL
        .set('#scene7', { autoAlpha: 1 })
        .add(() => {
            snd.speakArabic('تجربة استخدام سلسة، وأمان سيبراني معتمد بأعلى المعايير.', 'vo_scene7');
        }, 0.2)
        .fromTo('#scene7Title', 
            { opacity: 0, y: -20 }, 
            { opacity: 1, y: 0, duration: 0.5, ease: "power2.out" }, 0);

    // Sequence each item through the carousel focus with whoosh sounds
    carouselItems.forEach((item, index) => {
        const itemTL = gsap.timeline();
        const labelText = item.getAttribute('data-label') || '';
        
        itemTL
            .set(item, { zIndex: 10 })
            .add(() => snd.playSFX('whoosh'), 0)
            .fromTo(item, 
                { opacity: 0, scale: 0.75, rotationY: 25, z: -150 }, 
                { opacity: 1, scale: 1, rotationY: 0, z: 0, duration: 0.5, ease: "power3.out" })
            .add(() => { if (labelEl) labelEl.textContent = labelText; }, 0.1)
            .to(item, { duration: 0.7 })
            .to(item, {
                opacity: 0,
                scale: 0.8,
                rotationY: -25,
                z: -150,
                duration: 0.4,
                ease: "power2.in"
            });
        
        scene7TL.add(itemTL, 0.4 + (index * 1.25));
    });

    scene7TL.to('#scene7', { autoAlpha: 0, duration: 0.4, ease: "power2.in" }, 6.6);

    // ========================================================================
    // SCENE 8: IMPACT NUMBERS (47.0s – 52.0s)
    // ========================================================================
    const scene8TL = gsap.timeline();
    const impactCards = gsap.utils.toArray('.impact-card');

    scene8TL
        .set('#scene8', { autoAlpha: 1 })
        .add(() => {
            snd.speakArabic('أرقام قياسية وكفاءة استجابة فائقة.', 'vo_scene8');
        }, 0.2)
        .fromTo('#scene8Title', 
            { opacity: 0, y: -20 }, 
            { opacity: 1, y: 0, duration: 0.5, ease: "power2.out" }, 0)
        .add(() => snd.playSFX('chime'), 0.2)
        .fromTo(impactCards, 
            { opacity: 0, y: 40, scale: 0.9 }, 
            { opacity: 1, y: 0, scale: 1, stagger: 0.2, duration: 0.7, ease: "back.out(1.5)" }, 0.2)
        .add(() => {
            // Animate SVG circular progress rings
            document.querySelectorAll('.impact-card').forEach((card) => {
                const ring = card.querySelector('.ring-fill');
                const strokeColor = card.querySelector('.impact-ring').getAttribute('data-color');
                if (ring) {
                    ring.style.stroke = strokeColor;
                    ring.style.strokeDashoffset = '0';
                }
            });
        }, 0.5)
        .to('#scene8', { autoAlpha: 0, duration: 0.5, ease: "power2.in" }, 4.5);

    // ========================================================================
    // SCENE 9: CALL TO ACTION (52.0s – 56.0s)
    // ========================================================================
    const scene9TL = gsap.timeline();
    scene9TL
        .set('#scene9', { autoAlpha: 1 })
        .add(() => {
            snd.speakArabic('حوّل مدرستك إلى منظومة ذكية، وابدأ الآن مجاناً.', 'vo_scene9');
        }, 0.2)
        .fromTo('.cta-heading', 
            { opacity: 0, scale: 0.85, y: 20 }, 
            { opacity: 1, scale: 1, y: 0, duration: 0.7, ease: "back.out(1.5)" }, 0.1)
        .fromTo('.cta-sub', 
            { opacity: 0, y: 15 }, 
            { opacity: 1, y: 0, duration: 0.5, ease: "power2.out" }, 0.4)
        .add(() => snd.playSFX('whoosh'), 0.7)
        .fromTo('#ctaButton', 
            { opacity: 0, scale: 0.7 }, 
            { opacity: 1, scale: 1, duration: 0.6, ease: "back.out(2)" }, 0.7)
        .fromTo('.cta-pulse-ring', 
            { opacity: 0.8, scale: 1 }, 
            { opacity: 0, scale: 1.4, repeat: 3, duration: 0.8, ease: "power1.out" }, 1.0)
        .to('#scene9', { autoAlpha: 0, duration: 0.4, ease: "power2.in" }, 3.6);

    // ========================================================================
    // SCENE 10: CLOSING LOGO & TAGLINE (56.0s – 60.0s)
    // ========================================================================
    const scene10TL = gsap.timeline();
    scene10TL
        .set('#scene10', { autoAlpha: 1 })
        .add(() => {
            snd.playSFX('chime');
            snd.playSFX('sub_bass');
        }, 0.1)
        .add(() => {
            snd.speakArabic('المدرسة الذكية، مستقبل التعليم يبدأ الآن.', 'vo_scene10');
        }, 0.4)
        .fromTo('.closing-icon', 
            { opacity: 0, scale: 0.5, rotation: -20 }, 
            { opacity: 1, scale: 1, rotation: 0, duration: 0.8, ease: "back.out(1.8)" }, 0.1)
        .fromTo('.closing-brand', 
            { opacity: 0, y: 20 }, 
            { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, 0.5)
        .fromTo('.closing-tagline', 
            { opacity: 0, y: 15 }, 
            { opacity: 1, y: 0, duration: 0.5, ease: "power2.out" }, 0.8)
        .fromTo('.closing-line', 
            { width: 0 }, 
            { width: '240px', duration: 0.7, ease: "power3.inOut" }, 1.0)
        .fromTo('.closing-contacts', 
            { opacity: 0, y: 10 }, 
            { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, 1.3)
        .to('#scene10', { opacity: 0, duration: 1.2, ease: "power2.inOut" }, 3.0);

    // ========================================================================
    // ASSEMBLE MASTER TIMELINE (Exactly 60s total)
    // ========================================================================
    masterTL
        .add(scene1TL, 0)       // 0.0 - 5.0s
        .add(scene2TL, 5.0)     // 5.0 - 12.0s
        .add(flashTL, 12.0)     // 12.0 - 12.4s
        .add(scene3TL, 12.4)    // 12.4 - 18.0s
        .add(scene4TL, 18.0)    // 18.0 - 24.0s
        .add(scene5TL, 24.0)    // 24.0 - 32.0s
        .add(scene6TL, 32.0)    // 32.0 - 40.0s
        .add(scene7TL, 40.0)    // 40.0 - 47.0s
        .add(scene8TL, 47.0)    // 47.0 - 52.0s
        .add(scene9TL, 52.0)    // 52.0 - 56.0s
        .add(scene10TL, 56.0);  // 56.0 - 60.0s

    // ========================================================================
    // AUDIO PROMPT OVERLAY HANDLERS
    // ========================================================================
    function startExperience(withAudio = true) {
        if (audioPromptOverlay) {
            audioPromptOverlay.classList.add('hidden');
        }
        snd.init();
        if (!withAudio) {
            snd.toggleMute();
            updateAudioButtonsUI();
        }
        masterTL.play();
        if (audioEqualizer && withAudio) audioEqualizer.classList.add('playing');
    }

    if (btnEnableAudio) {
        btnEnableAudio.addEventListener('click', () => startExperience(true));
    }
    if (btnMuteAudio) {
        btnMuteAudio.addEventListener('click', () => startExperience(false));
    }

    // ========================================================================
    // PLAYBACK CONTROLS & EVENT LISTENERS
    // ========================================================================
    if (btnPlay) {
        btnPlay.addEventListener('click', () => {
            snd.init();
            snd.resumeBGM();
            masterTL.play();
            if (audioEqualizer && !snd.isMuted) audioEqualizer.classList.add('playing');
        });
    }

    if (btnPause) {
        btnPause.addEventListener('click', () => {
            masterTL.pause();
            snd.pauseBGM();
            snd.stopVoice();
            if (audioEqualizer) audioEqualizer.classList.remove('playing');
        });
    }

    if (btnRestart) {
        btnRestart.addEventListener('click', () => {
            snd.init();
            snd.restartBGM();
            snd.lastSpokenMarker = null;
            masterTL.restart();
            // Reset custom visual states
            document.querySelectorAll('.ring-fill').forEach(r => r.style.strokeDashoffset = '326.7');
            const counter = document.getElementById('interfaceCounter');
            if (counter) counter.textContent = '0';
            if (audioEqualizer && !snd.isMuted) audioEqualizer.classList.add('playing');
        });
    }

    if (btnSound) {
        btnSound.addEventListener('click', () => {
            snd.init();
            const muted = snd.toggleMute();
            updateAudioButtonsUI();
        });
    }

    if (btnVoice) {
        btnVoice.addEventListener('click', () => {
            const enabled = snd.toggleVoiceover();
            updateAudioButtonsUI();
        });
    }

    function updateAudioButtonsUI() {
        if (btnSound) {
            btnSound.innerHTML = snd.isMuted ? '<i class="fas fa-volume-xmark"></i>' : '<i class="fas fa-volume-high"></i>';
            btnSound.classList.toggle('muted', snd.isMuted);
            btnSound.classList.toggle('active', !snd.isMuted);
        }
        if (btnVoice) {
            btnVoice.innerHTML = snd.isVoiceoverEnabled ? '<i class="fas fa-microphone"></i>' : '<i class="fas fa-microphone-slash"></i>';
            btnVoice.classList.toggle('muted', !snd.isVoiceoverEnabled);
            btnVoice.classList.toggle('active', snd.isVoiceoverEnabled);
        }
        if (audioEqualizer) {
            if (snd.isMuted || masterTL.paused()) {
                audioEqualizer.classList.remove('playing');
            } else {
                audioEqualizer.classList.add('playing');
            }
        }
    }

    // Scrubber click on progress bar
    if (progressBar) {
        progressBar.addEventListener('click', (e) => {
            const rect = progressBar.getBoundingClientRect();
            const clickX = e.clientX - rect.left;
            const progressRatio = Math.max(0, Math.min(1, clickX / rect.width));
            masterTL.progress(progressRatio);
            snd.stopVoice();
            snd.lastSpokenMarker = null;
        });
    }

    // Keyboard shortcuts
    window.addEventListener('keydown', (e) => {
        if (e.code === 'Space') {
            e.preventDefault();
            if (masterTL.paused()) {
                snd.init();
                snd.resumeBGM();
                masterTL.play();
                if (audioEqualizer && !snd.isMuted) audioEqualizer.classList.add('playing');
            } else {
                masterTL.pause();
                snd.pauseBGM();
                snd.stopVoice();
                if (audioEqualizer) audioEqualizer.classList.remove('playing');
            }
        } else if (e.code === 'KeyR') {
            masterTL.restart();
            snd.restartBGM();
            snd.lastSpokenMarker = null;
        } else if (e.code === 'KeyM') {
            snd.toggleMute();
            updateAudioButtonsUI();
        } else if (e.code === 'ArrowRight') {
            masterTL.seek(Math.min(masterTL.duration(), masterTL.time() + 2));
            snd.stopVoice();
        } else if (e.code === 'ArrowLeft') {
            masterTL.seek(Math.max(0, masterTL.time() - 2));
            snd.stopVoice();
        }
    });

    // ========================================================================
    // HELPER FUNCTIONS
    // ========================================================================
    function updatePlaybackUI() {
        const time = masterTL.time();
        const duration = masterTL.duration() || 60;
        const progress = (time / duration) * 100;

        if (progressFill) progressFill.style.width = progress + '%';

        if (timeDisplay) {
            const currentMin = String(Math.floor(time / 60)).padStart(2, '0');
            const currentSec = String(Math.floor(time % 60)).padStart(2, '0');
            const totalMin = String(Math.floor(duration / 60)).padStart(2, '0');
            const totalSec = String(Math.floor(duration % 60)).padStart(2, '0');
            timeDisplay.textContent = `${currentMin}:${currentSec} / ${totalMin}:${totalSec}`;
        }
    }

    function animateNumber(targetId, selector, start, end, duration, prefix = '', formatComma = false) {
        const el = document.querySelector(selector);
        if (!el) return;
        const obj = { val: start };
        gsap.to(obj, {
            val: end,
            duration: duration,
            ease: "power2.out",
            onUpdate: () => {
                let formatted = end % 1 === 0 ? Math.round(obj.val) : obj.val.toFixed(1);
                if (formatComma) formatted = Number(formatted).toLocaleString();
                el.textContent = prefix + formatted + (el.getAttribute('data-suffix') || '');
            }
        });
    }

    function createParticles(containerId, count) {
        const container = document.getElementById(containerId);
        if (!container) return;
        container.innerHTML = '';
        for (let i = 0; i < count; i++) {
            const p = document.createElement('div');
            p.className = 'particle';
            p.style.left = gsap.utils.random(5, 95) + '%';
            p.style.top = gsap.utils.random(5, 95) + '%';
            p.style.width = gsap.utils.random(2, 5) + 'px';
            p.style.height = p.style.width;
            p.style.backgroundColor = gsap.utils.random(['#3B82F6', '#6366F1', '#10B981', '#ffffff']);
            container.appendChild(p);

            gsap.to(p, {
                y: gsap.utils.random(-30, 30),
                x: gsap.utils.random(-30, 30),
                opacity: gsap.utils.random(0.2, 0.7),
                repeat: -1,
                yoyo: true,
                duration: gsap.utils.random(2, 4),
                ease: "sine.inOut",
                delay: gsap.utils.random(0, 2)
            });
        }
    }
});
