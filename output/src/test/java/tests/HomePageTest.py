from playwright.sync_api import Page, expect

def test_verify_title(page: Page) -> None:
    page.goto("https://www.oculus.com/")
    expect(page).to_have_title("Oculus | VR Headsets & Equipment")

def test_verify_logo(page: Page) -> None:
    page.goto("https://www.oculus.com/")
    expect(page.locator(".oculus-logo")).to_be_visible()

def test_verify_headsets_dropdown(page: Page) -> None:
    page.goto("https://www.oculus.com/")
    page.hover(".oculus-header-nav-item-headsets")
    expected = [
        "Oculus Rift S\nPC-Powered VR Gaming",
        "Oculus Quest\nAll-In-One VR Gaming",
        "Oculus Go\nAll-In-One VR Viewing",
        "Compare All Headsets",
    ]
    actual = [link.text_content() for link in page.query_selector_all(".oculus-header-nav-item-headsets-dropdown a")]
    assert actual == expected