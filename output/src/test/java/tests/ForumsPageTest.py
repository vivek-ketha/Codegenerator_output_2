
from playwright.sync_api import Playwright, expect

def test_forums_page(playwright: Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.selenium.dev/documentation/en/")
    page.hover(".community-tab")
    page.click(".forums-tab")
    page.switch_to_frame(page.frame_locator("iframe"))
    assert page.locator(".forums-header").is_visible()
    for i in range(1, len(page.locator(".pagination-list").locators(".pagination-item"))):
        page.locator(f".pagination-item:nth-child({i})").click()
        assert page.locator(".next-page-success").is_visible()
        if i == 6:
            break
    page.fill(".searchbar", "error")
    page.press(".searchbar", "Enter")
    assert page.locator(".search-success").is_visible()
    context.close()
    browser.close()