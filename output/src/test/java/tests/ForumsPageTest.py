
from playwright.sync_api import Page, expect

def navigate_to_forums_page(page: Page):
    page.hover(selector='.community-tab')
    page.click(selector='.forums-tab')
    page.switch_to_next_tab()

def verify_forums_header_present(page: Page):
    forums_header = page.get_by_text('Forums')
    expect(forums_header).to_be_visible()

def click_next_page(page: Page):
    pagination = page.get_by_role('link', name='Page')
    for i in range(1, len(pagination)):
        pagination.nth(i).click()
        if i == 6:
            break
        expect(page).to_have_url(lambda url: url.startswith('https://www.google.com/forums?p='))

def verify_forum_search(page: Page):
    page.fill(selector='.searchbar', value='error')
    page.press(selector='.searchbar', key='Enter')
    search_results = page.get_by_role('listitem', name='Search results')
    expect(search_results).to_be_visible()

def forums_page_test(page: Page):
    navigate_to_forums_page(page)
    verify_forums_header_present(page)
    click_next_page(page)
    verify_forum_search(page)