
from playwright.sync_api import Page, expect

class ForumsPage:
    def __init__(self, page: Page):
        self.page = page

    def is_forums_header_present(self) -> bool:
        forums_header = self.page.locator(".c_Header-logoLink")
        return expect(forums_header).to_be_visible().is_ok()

    def get_pagination(self) -> list:
        pagination_bar = self.page.locator("#PagerBefore")
        numbered_pages = pagination_bar.locators("a")
        return numbered_pages

    def is_next_page_successful(self) -> bool:
        new_results = self.page.locator(".DataList.Discussions")
        return expect(new_results).to_be_visible().is_ok()

    def search_forum(self, text: str) -> None:
        forums_search_bar = self.page.locator("#Form_Search")
        forums_search_bar.type(text)

    def press_enter(self) -> None:
        self.page.keyboard.press("Enter")

    def is_search_successful(self) -> bool:
        forums_search_results = self.page.locator("#search-results")
        return expect(forums_search_results).to_be_visible().is_ok()