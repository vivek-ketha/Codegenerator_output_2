from playwright.sync_api import Page, expect

def test_verify_title(page: Page) -> None:
    home_page = page.goto("https://www.oculus.com/")
    expect(home_page).to_have_title("Oculus | VR Headsets & Equipment")

def test_verify_logo(page: Page) -> None:
    home_page = page.goto("https://www.oculus.com/")
    logo = page.locator("css=div.oculus-logo")
    expect(logo).to_be_visible()

def test_verify_headsets_dropdown(page: Page) -> None:
    home_page = page.goto("https://www.oculus.com/")
    headsets_tab = page.locator("css=li.nav-item-headsets")
    headsets_tab.hover()
    headsets_dropdown_results = page.locator("css=div.oculus-megamenu-content a")
    expected = [
        "Oculus Rift S\n" + "PC-Powered VR Gaming",
        "Oculus Quest\n" + "All-In-One VR Gaming",
        "Oculus Go\n" + "All-In-One VR Viewing",
        "Compare All Headsets",
    ]
    for i, result in enumerate(headsets_dropdown_results):
        displayed_name = result.inner_text()
        expect(displayed_name).to_equal(expected[i])