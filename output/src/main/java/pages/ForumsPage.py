  Here is the converted code:

```python
from playwright.sync_api import Page, expect

class ForumsPage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def forums_header(self):
        return self.page.locator(".c_Header-logoLink")

    @property
    def pagination_bar(self):
        return self.page.locator("#PagerBefore")

    @property
    def numbered_pages(self):
        return self.pagination_bar.locators("a")

    @property
    def new_results(self):
        return self.page.locator(".DataList.Discussions")

    @property
    def forums_search_bar(self):
        return self.page.locator("#Form_Search")

    @property
    def forums_search_results(self):
        return self.page.locator("#search-results")

    def is_forums_header_present(self):
        return self.forums_header.is_visible()

    def get_pagination(self):
        return self.numbered_pages.all()

    def is_next_page_successful(self):
        return self.new_results.is_visible()

    def search_forum(self, text):
        self.forums_search_bar.fill(text)

    def press_enter(self):
        self.page.keyboard.press("Enter")

    def is_search_successful(self):
        return self.forums_search_results.is_visible()
```