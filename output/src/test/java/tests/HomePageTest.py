
from playwright.sync_api import Page, expect

def test_verify_title(page: Page):
    page.goto("https://www.oculus.com/")
    actual_title = page.title()
    expected_title = "Oculus | VR Headsets & Equipment"
    expect(actual_title).to_be(expected_title)
    print("Title matches the expected title.")

def test_verify_logo(page: Page):
    page.goto("https://www.oculus.com/")
    logo_element = page.locator(".header__logo")
    expect(logo_element).to_be_visible()
    print("Logo is present.")

def test_verify_headsets_dropdown(page: Page):
    page.goto("https://www.oculus.com/")
    headsets_tab = page.locator(".header__nav-link:has-text('Headsets')")
    headsets_tab.hover()
    headsets_dropdown_results = page.locator(".header__nav-sub-list a")
    expected_results = [
        "Oculus Rift S\nPC-Powered VR Gaming",
        "Oculus Quest\nAll-In-One VR Gaming",
        "Oculus Go\nAll-In-One VR Viewing",
        "Compare All Headsets"
    ]
    for i, result in enumerate(headsets_dropdown_results):
        actual_result = result.inner_text()
        expect(actual_result).to_be(expected_results[i])
        print(f"Result {i+1} matches the expected result.")