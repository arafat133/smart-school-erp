/**
 * ============================================================================
 * MODULE: DASHBOARD.JS - School ERP Dashboard Controller & Statistics Engine
 * ============================================================================
 */

(function() {
    'use strict';

    function initDashboard() {
        if (typeof window.renderDashboard === 'function') {
            window.renderDashboard();
        }
    }

    // Auto-run if DOM is already ready and on dashboard
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            const activePage = document.querySelector('.page.active');
            if (!activePage || activePage.id === 'pg-dashboard') {
                initDashboard();
            }
        });
    } else {
        const activePage = document.querySelector('.page.active');
        if (!activePage || activePage.id === 'pg-dashboard') {
            initDashboard();
        }
    }

    window.initDashboardModule = initDashboard;
    console.log('✅ Dashboard Module initialized and ready.');
})();
