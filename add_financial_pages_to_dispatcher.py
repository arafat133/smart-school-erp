"""
Explicitly add all 5 financial page handlers to Master Central Dispatcher goTo(id) in app.js
"""
import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

dispatcher_addition = """
    // Financial Pages Dispatcher Routing
    if (id === 'pg-currencies') renderCurrenciesGrid();
    if (id === 'pg-cashbox-inventory') renderCashboxInventoryGrid();
    if (id === 'pg-closings') renderClosingsGrid();
    if (id === 'pg-banks') renderBanksGrid();
    if (id === 'pg-demand-letters') renderDemandLettersGrid();
"""

if "if (id === 'pg-currencies') renderCurrenciesGrid();" not in js:
    js = js.replace("function goTo(id) {", "function goTo(id) {\n" + dispatcher_addition)
    print("  ✓ Added explicit financial pages dispatcher routing inside goTo(id)")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js successfully!")
