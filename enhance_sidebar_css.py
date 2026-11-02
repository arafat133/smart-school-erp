"""
Enhance sidebar styling in style.css for glassmorphism, responsive accordion, and luxury theme.
"""
import re, time

print("=" * 60)
print("Enhancing sidebar CSS in style.css...")
print("=" * 60)

with open('frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

sidebar_css_boost = """
/* ========== LUXURY GLASSMORPHIC SIDEBAR STYLING ========== */
.sidebar {
    width: var(--sidebar-w, 280px);
    position: fixed;
    right: 0;
    top: 0;
    height: 100vh;
    display: flex;
    flex-direction: column;
    z-index: 100;
    transition: transform .3s cubic-bezier(0.4, 0, 0.2, 1);
    background: rgba(15, 23, 42, 0.92) !important;
    backdrop-filter: blur(25px) !important;
    -webkit-backdrop-filter: blur(25px) !important;
    border-left: 1px solid rgba(255, 255, 255, 0.1) !important;
    box-shadow: -10px 0 40px rgba(0, 0, 0, 0.6) !important;
    overflow: hidden;
}

.sidebar-header {
    height: 70px;
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 0 20px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    background: rgba(255, 255, 255, 0.02);
}

.sidebar-logo {
    font-size: 1.6rem;
    color: #38bdf8;
    filter: drop-shadow(0 0 10px rgba(56, 189, 248, 0.5));
}

.sidebar-header h2 {
    font-size: 1.1rem;
    font-weight: 800;
    flex: 1;
    background: linear-gradient(135deg, #ffffff, #94a3b8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.sidebar-nav {
    flex: 1;
    padding: 16px 14px;
    overflow-y: auto;
    scrollbar-width: thin;
    scrollbar-color: rgba(255, 255, 255, 0.15) transparent;
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.nav-section {
    background: rgba(30, 41, 59, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    overflow: hidden;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    transition: all 0.3s ease;
}

.nav-section:hover {
    border-color: rgba(255, 255, 255, 0.18);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}

.nav-item.has-sub {
    user-select: none;
    cursor: pointer;
    background: rgba(255, 255, 255, 0.03);
    padding: 13px 15px;
    font-size: 0.92rem;
    font-weight: 700;
    color: #f8fafc;
    transition: all 0.25s ease;
    display: flex;
    align-items: center;
    gap: 10px;
    border-bottom: 1px solid transparent;
}

.nav-section.open .nav-item.has-sub {
    background: rgba(59, 130, 246, 0.12);
    color: #60a5fa;
    border-bottom-color: rgba(255, 255, 255, 0.08);
}

.nav-item.has-sub:hover {
    background: rgba(255, 255, 255, 0.08);
    color: #ffffff;
}

.nav-item.has-sub i:not(.fa-chevron-down) {
    color: #38bdf8;
    font-size: 1.15rem;
    width: 22px;
    text-align: center;
    filter: drop-shadow(0 0 6px rgba(56, 189, 248, 0.3));
}

.nav-item.has-sub .fa-chevron-down {
    transition: transform 0.3s ease;
    color: #94a3b8;
}

.nav-section.open .nav-item.has-sub .fa-chevron-down {
    transform: rotate(180deg);
    color: #60a5fa;
}

.sub-menu {
    display: none;
    padding: 8px 10px 10px;
    flex-direction: column;
    gap: 4px;
    background: rgba(15, 23, 42, 0.6);
}

.nav-section.open .sub-menu {
    display: flex;
    animation: slideDown 0.3s ease-out;
}

@keyframes slideDown {
    from { opacity: 0; transform: translateY(-8px); }
    to { opacity: 1; transform: translateY(0); }
}

.sub-menu a {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 9px 14px;
    border-radius: 9px;
    color: #cbd5e1;
    text-decoration: none !important;
    font-size: 0.85rem;
    font-weight: 500;
    transition: all 0.25s ease;
    border: 1px solid transparent;
}

.sub-menu a i {
    width: 18px;
    text-align: center;
    font-size: 0.95rem;
    color: #38bdf8;
    transition: transform 0.2s ease;
}

.sub-menu a:hover {
    background: rgba(255, 255, 255, 0.08);
    color: #ffffff;
    transform: translateX(-4px);
    border-color: rgba(255, 255, 255, 0.15);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
}

.sub-menu a:hover i {
    transform: scale(1.18);
    color: #38bdf8;
}

.sub-menu a.active {
    background: linear-gradient(135deg, rgba(79, 70, 229, 0.35), rgba(14, 165, 233, 0.35)) !important;
    color: #ffffff !important;
    border-color: rgba(56, 189, 248, 0.5) !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 15px rgba(14, 165, 233, 0.25) !important;
}

.sub-menu a.active i {
    color: #38bdf8 !important;
}
"""

if 'LUXURY GLASSMORPHIC SIDEBAR STYLING' not in css:
    css += "\n" + sidebar_css_boost.strip() + "\n"

with open('frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Enhanced sidebar CSS successfully!")
