from playwright.sync_api import Page, expect

def test_navigate_to_forums_page(page: Page):
    page.goto("https://www.selenium.dev/")
    page.hover(".community-tab")
    page.click("text=Forums")
    page.switch_to_next_tab()

def test_verify_forums_header_present(page: Page):
    page.goto("https://www.selenium.dev/forums/")
    forums_header = page.locator(".forum-header")
    expect(forums_header).to_be_visible()

def test_click_next_page(page: Page):
    page.goto("https://www.selenium.dev/forums/")
    pagination = page.locator(".pagination a")
    for i in range(1, len(pagination)):
        pagination.nth(i).click()
        if i == 6:
            break
        expect(page).to_have_url(lambda url: url.startswith("https://www.selenium.dev/forums/"))

def test_verify_forum_search(page: Page):
    page.goto("https://www.selenium.dev/forums/")
    search_input = page.locator("#search-input")
    search_input.fill("error")
    search_input.press("Enter")
    expect(page).to_have_url(lambda url: url.startswith("https://www.selenium.dev/forums/search?q=error"))