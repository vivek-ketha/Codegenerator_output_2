
from playwright.sync_api import Page, Playwright

class ForumsPage:
    def __init__(self, page: Page):
        self.page = page

    def is_forums_header_present(self) -> bool:
        forums_header = self.page.locator(".c_Header-logoLink")
        return forums_header.is_visible()

    def get_pagination(self) -> list:
        pagination_bar = self.page.locator("#PagerBefore")
        numbered_pages = pagination_bar.query_selector_all("a")
        return numbered_pages

    def is_next_page_successful(self) -> bool:
        new_results = self.page.locator(".DataList.Discussions")
        return new_results.is_visible()

    def search_forum(self, text: str) -> None:
        self.page.locator("#Form_Search").fill(text)

    def press_enter(self) -> None:
        self.page.keyboard.press("Enter")

    def is_search_successful(self) -> bool:
        forums_search_results = self.page.locator("#search-results")
        return forums_search_results.is_visible()