from playwright.sync_api import Page, expect

class ForumsPage:
    def __init__(self, page: Page):
        self.page = page

    forums_header = "#Header-logoLink"
    pagination_bar = "#PagerBefore"
    numbered_pages = "#PagerBefore a"
    new_results = ".DataList.Discussions"
    forums_search_bar = "#Form_Search"
    forums_search_results = "#search-results"

    def is_forums_header_present(self):
        header = self.page.locator(self.forums_header)
        return expect(header).to_be_visible().is_visible()

    def get_pagination(self):
        pagination = self.page.locator(self.pagination_bar)
        return pagination.locator(self.numbered_pages).all()

    def is_next_page_successful(self):
        results = self.page.locator(self.new_results)
        return expect(results).to_be_visible().is_visible()

    def search_forum(self, text):
        self.page.locator(self.forums_search_bar).fill(text)

    def press_enter(self):
        self.page.keyboard.press("Enter")

    def is_search_successful(self):
        results = self.page.locator(self.forums_search_results)
        return expect(results).to_be_visible().is_visible()