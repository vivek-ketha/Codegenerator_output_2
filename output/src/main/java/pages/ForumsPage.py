
from playwright.sync_import import sync_playwright

class ForumsPage:
    def __init__(self, page):
        self.page = page

    forums_header = page.locator(".c_Header-logoLink")
    pagination_bar = page.locator("#PagerBefore")
    numbered_pages = page.locator("a")
    new_results = page.locator(".DataList.Discussions")
    forums_search_bar = page.locator("#Form_Search")
    forums_search_results = page.locator("#search-results")

    def is_forums_header_present(self):
        return self.page.wait_for_selector(self.forums_header).is_visible()

    def get_pagination(self):
        return self.pagination_bar.query_selector_all(self.numbered_pages)

    def is_next_page_successful(self):
        return self.page.wait_for_selector(self.new_results).is_visible()

    def search_forum(self, text):
        self.forums_search_bar.fill(text)

    def press_enter(self):
        self.page.mouse.click(self.forums_search_bar)

    def is_search_successful(self):
        return self.page.wait_for_selector(self.forums_search_results).is_visible()