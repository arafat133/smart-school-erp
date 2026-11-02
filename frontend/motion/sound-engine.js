/**
 * SMART SCHOOL MOTION GRAPHICS — SOUND & VOICEOVER ENGINE
 * Features:
 * - HTML5 Web Audio API & Native WAV Fallback
 * - Dynamic Background Music (BGM) with Auto-Ducking
 * - Synchronized SFX (Whoosh, Sub-Bass, Ticks, Chimes, Flash)
 * - Arabic Neural/Browser Voiceover Narrator (SpeechSynthesis)
 * - Real-Time Audio Visualizer Equalizer
 */

class SoundEngine {
    constructor() {
        this.ctx = null;
        this.masterGain = null;
        this.sfxGain = null;
        this.bgmGain = null;
        this.isMuted = false;
        this.isVoiceoverEnabled = true;
        this.isInitialized = false;

        // Audio buffers cache
        this.buffers = {};
        this.bgmSource = null;
        this.bgmAudioElement = null;

        // Voiceover state
        this.synth = window.speechSynthesis;
        this.arabicVoice = null;
        this.lastSpokenMarker = null;

        // Equalizer canvas / elements
        this.analyser = null;
        this.dataArray = null;

        this.initVoice();
    }

    init() {
        if (this.isInitialized) return;

        try {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            this.ctx = new AudioContext();

            // Master Gain
            this.masterGain = this.ctx.createGain();
            this.masterGain.gain.setValueAtTime(0.85, this.ctx.currentTime);

            // Sub Gains
            this.sfxGain = this.ctx.createGain();
            this.sfxGain.gain.setValueAtTime(0.9, this.ctx.currentTime);
            this.sfxGain.connect(this.masterGain);

            this.bgmGain = this.ctx.createGain();
            this.bgmGain.gain.setValueAtTime(0.35, this.ctx.currentTime);
            this.bgmGain.connect(this.masterGain);

            // Analyser for UI visualizer
            this.analyser = this.ctx.createAnalyser();
            this.analyser.fftSize = 64;
            this.masterGain.connect(this.analyser);
            this.analyser.connect(this.ctx.destination);
            this.dataArray = new Uint8Array(this.analyser.frequencyBinCount);

            this.isInitialized = true;
            console.log('Audio Context initialized successfully.');

            // Load WAV files or prepare synthesized fallbacks
            this.loadSound('whoosh', 'audio/sfx_whoosh.wav');
            this.loadSound('sub_bass', 'audio/sfx_sub_bass.wav');
            this.loadSound('chime', 'audio/sfx_chime.wav');
            this.loadSound('tick', 'audio/sfx_tick.wav');
            this.loadSound('flash', 'audio/sfx_flash.wav');
            this.loadSound('cascade', 'audio/sfx_cascade.wav');

            this.startBGM();
        } catch (e) {
            console.warn('Web Audio API not supported or blocked:', e);
        }
    }

    initVoice() {
        if (!this.synth) return;

        const updateVoices = () => {
            const voices = this.synth.getVoices();
            // Find best Arabic voice available (Saudi Arabia, Egypt, or generic Arabic)
            this.arabicVoice = voices.find(v => v.lang.startsWith('ar-SA')) ||
                               voices.find(v => v.lang.startsWith('ar')) ||
                               voices[0];
            if (this.arabicVoice) {
                console.log('Selected Voiceover Voice:', this.arabicVoice.name, this.arabicVoice.lang);
            }
        };

        updateVoices();
        if (this.synth.onvoiceschanged !== undefined) {
            this.synth.onvoiceschanged = updateVoices;
        }
    }

    async loadSound(name, url) {
        try {
            const resp = await fetch(url);
            const arrayBuffer = await resp.arrayBuffer();
            this.buffers[name] = await this.ctx.decodeAudioData(arrayBuffer);
        } catch (err) {
            // Fallback to purely procedural Web Audio synthesizer
            console.log(`Using procedural audio for: ${name}`);
        }
    }

    // Play named sound with fallback to synthesizer
    playSFX(name) {
        if (this.isMuted || !this.isInitialized) return;

        if (this.ctx && this.ctx.state === 'suspended') {
            this.ctx.resume();
        }

        if (this.buffers[name]) {
            const source = this.ctx.createBufferSource();
            source.buffer = this.buffers[name];
            source.connect(this.sfxGain);
            source.start(0);
        } else {
            // Procedural synthesizers
            switch (name) {
                case 'sub_bass':
                    this.synthSubBass();
                    break;
                case 'chime':
                    this.synthChime();
                    break;
                case 'tick':
                    this.synthTick();
                    break;
                case 'flash':
                    this.synthFlash();
                    break;
                case 'whoosh':
                    this.synthWhoosh();
                    break;
                case 'cascade':
                    this.synthCascade();
                    break;
            }
        }
    }

    // --- Procedural Web Audio Synthesizers ---
    synthSubBass() {
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(110, this.ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(35, this.ctx.currentTime + 1.2);
        gain.gain.setValueAtTime(1, this.ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 1.2);
        osc.connect(gain);
        gain.connect(this.sfxGain);
        osc.start();
        osc.stop(this.ctx.currentTime + 1.2);
    }

    synthChime() {
        [1046.5, 1318.5, 1567.98, 2093.0].forEach((freq, idx) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(freq, this.ctx.currentTime + idx * 0.06);
            gain.gain.setValueAtTime(0.2, this.ctx.currentTime + idx * 0.06);
            gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + idx * 0.06 + 1.0);
            osc.connect(gain);
            gain.connect(this.sfxGain);
            osc.start(this.ctx.currentTime + idx * 0.06);
            osc.stop(this.ctx.currentTime + idx * 0.06 + 1.0);
        });
    }

    synthTick() {
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(1800, this.ctx.currentTime);
        gain.gain.setValueAtTime(0.3, this.ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.05);
        osc.connect(gain);
        gain.connect(this.sfxGain);
        osc.start();
        osc.stop(this.ctx.currentTime + 0.05);
    }

    synthFlash() {
        const node = this.ctx.createBufferSource();
        const buffer = this.ctx.createBuffer(1, this.ctx.sampleRate * 0.4, this.ctx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < buffer.length; i++) {
            data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (this.ctx.sampleRate * 0.1));
        }
        node.buffer = buffer;
        const filter = this.ctx.createBiquadFilter();
        filter.type = 'lowpass';
        filter.frequency.setValueAtTime(3000, this.ctx.currentTime);
        node.connect(filter);
        filter.connect(this.sfxGain);
        node.start();
    }

    synthWhoosh() {
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(120, this.ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(800, this.ctx.currentTime + 0.5);
        gain.gain.setValueAtTime(0.01, this.ctx.currentTime);
        gain.gain.linearRampToValueAtTime(0.35, this.ctx.currentTime + 0.25);
        gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.6);
        osc.connect(gain);
        gain.connect(this.sfxGain);
        osc.start();
        osc.stop(this.ctx.currentTime + 0.6);
    }

    synthCascade() {
        const notes = [523.25, 659.25, 783.99, 1046.5, 1318.51, 1567.98];
        notes.forEach((freq, idx) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'sine';
            const startTime = this.ctx.currentTime + idx * 0.08;
            osc.frequency.setValueAtTime(freq, startTime);
            gain.gain.setValueAtTime(0.2, startTime);
            gain.gain.exponentialRampToValueAtTime(0.001, startTime + 0.4);
            osc.connect(gain);
            gain.connect(this.sfxGain);
            osc.start(startTime);
            osc.stop(startTime + 0.4);
        });
    }

    // --- Background Music ---
    startBGM() {
        if (!this.bgmAudioElement) {
            this.bgmAudioElement = new Audio('audio/bgm_ambient_loop.wav');
            this.bgmAudioElement.loop = true;
            this.bgmAudioElement.volume = 0.35;
        }

        if (!this.isMuted) {
            this.bgmAudioElement.play().catch(() => {
                // Browser policy may require click
            });
        }
    }

    pauseBGM() {
        if (this.bgmAudioElement) {
            this.bgmAudioElement.pause();
        }
    }

    resumeBGM() {
        if (this.bgmAudioElement && !this.isMuted) {
            this.bgmAudioElement.play().catch(() => {});
        }
    }

    restartBGM() {
        if (this.bgmAudioElement) {
            this.bgmAudioElement.currentTime = 0;
            this.resumeBGM();
        }
    }

    // --- Voiceover Integration (SpeechSynthesis) ---
    speakArabic(text, markerId) {
        if (!this.isVoiceoverEnabled || this.isMuted || !this.synth) return;
        if (this.lastSpokenMarker === markerId) return;

        this.lastSpokenMarker = markerId;
        this.synth.cancel(); // Stop prior speech

        // Auto-duck BGM while talking
        if (this.bgmAudioElement) {
            this.bgmAudioElement.volume = 0.12;
        }

        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'ar-SA';
        if (this.arabicVoice) {
            utterance.voice = this.arabicVoice;
        }
        utterance.rate = 1.05; // natural commercial pacing
        utterance.pitch = 0.95; // professional deep tone

        utterance.onend = () => {
            // Restore BGM volume
            if (this.bgmAudioElement && !this.isMuted) {
                this.bgmAudioElement.volume = 0.35;
            }
        };

        this.synth.speak(utterance);
    }

    stopVoice() {
        if (this.synth) {
            this.synth.cancel();
        }
        if (this.bgmAudioElement && !this.isMuted) {
            this.bgmAudioElement.volume = 0.35;
        }
    }

    // --- Master Controls ---
    toggleMute() {
        this.isMuted = !this.isMuted;
        if (this.masterGain) {
            this.masterGain.gain.setValueAtTime(this.isMuted ? 0 : 0.85, this.ctx.currentTime);
        }
        if (this.bgmAudioElement) {
            this.bgmAudioElement.muted = this.isMuted;
        }
        if (this.isMuted) {
            this.stopVoice();
        }
        return this.isMuted;
    }

    toggleVoiceover() {
        this.isVoiceoverEnabled = !this.isVoiceoverEnabled;
        if (!this.isVoiceoverEnabled) {
            this.stopVoice();
        }
        return this.isVoiceoverEnabled;
    }
}

// Global Sound Engine Singleton
window.soundEngine = new SoundEngine();
