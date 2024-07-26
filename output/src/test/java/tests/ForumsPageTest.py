
from playwright.sync_api import Page, expect

def navigate_to_forums_page(page: Page):
    page.goto("https://www.tutorialspoint.com/index.htm")
    page.hover("//span[text()='Community']")
    page.click("//a[text()='Forums']")
    page.switch_to_frame(page.frame_locator("iframe[id='google_osd_static_frame']"))

def verify_forums_header_present(page: Page):
    forums_header = page.locator("h1[class='page-title']")
    expect(forums_header).to_be_visible()

def click_next_page(page: Page):
    pagination = page.locator("ul[class='pagination']")
    for i in range(1, len(pagination)):
        pagination.get_by_text(str(i)).click()
        if i == 6:
            break

def verify_forum_search(page: Page):
    search_bar = page.locator("input[id='search-input']")
    search_bar.fill("error")
    search_bar.press("Enter")
    search_results = page.locator("div[class='search-results']")
    expect(search_results).to_be_visible()