from playwright.sync_api import Page, expect

class TestForumsPage:
    def test_forums_header_present(self, page: Page) -> None:
        page.goto("https://discuss.flarum.org/")
        expect(page).to_have_selector(".c_Header-logoLink")

    def test_pagination_next_page_successful(self, page: Page) -> None:
        page.goto("https://discuss.flarum.org/")
        pagination_bar = page.locator("#PagerBefore")
        numbered_pages = pagination_bar.locators("a")
        next_page_button = numbered_pages[-1]
        next_page_button.click()
        expect(page).to_have_selector(".DataList.Discussions")

    def test_forums_search_successful(self, page: Page) -> None:
        page.goto("https://discuss.flarum.org/")
        forums_search_bar = page.locator("#Form_Search")
        forums_search_bar.fill("playwright")
        forums_search_bar.press("Enter")
        expect(page).to_have_selector("#search-results")