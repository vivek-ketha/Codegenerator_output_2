
from playwright.sync_api import Page
from axe_playwright import AxePlaywright

def basic_accessibility_check(page: Page):
    axe = AxePlaywright(page)
    results = axe.analyze()
    if results["violations"]:
        print("FAIL: basic_accessibility_check | Violations found.")
        print(results["violations"])
    else:
        print("PASS: basic_accessibility_check | No violations found.")