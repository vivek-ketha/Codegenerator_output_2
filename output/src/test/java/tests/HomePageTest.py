
from playwright.sync_api import Page, expect

def test_verify_title(page: Page):
    page.goto("https://www.oculus.com/")
    expect(page).to_have_title("Oculus | VR Headsets & Equipment")

def test_verify_logo(page: Page):
    page.goto("https://www.oculus.com/")
    logo = page.locator("img[alt='Oculus Logo']")
    expect(logo).to_be_visible()

def test_verify_headsets_dropdown(page: Page):
    page.goto("https://www.oculus.com/")
    headsets_tab = page.locator("a[href='/headsets/']")
    headsets_tab.hover()
    headsets_dropdown_results = page.locator("ul[class='nav__sub-nav'] a")
    expected = [
        "Oculus Rift S\nPC-Powered VR Gaming",
        "Oculus Quest\nAll-In-One VR Gaming",
        "Oculus Go\nAll-In-One VR Viewing",
        "Compare All Headsets",
    ]
    for i, result in enumerate(headsets_dropdown_results.all()):
        expect(result).to_have_text(expected[i])