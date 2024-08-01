from playwright.sync_api import Page

class ForumsPage:
    def __init__(self, page: Page):
        self.page = page

    async def is_forums_header_present(self) -> bool:
        header = await self.page.locator(".c_Header-logoLink").is_visible()
        return header

    async def get_pagination(self) -> list:
        pagination = await self.page.locator("#PagerBefore a").all_text_contents()
        return pagination

    async def is_next_page_successful(self) -> bool:
        results = await self.page.locator(".DataList.Discussions").is_visible()
        return results

    async def search_forum(self, text: str) -> None:
        await self.page.locator("#Form_Search").fill(text)

    async def press_enter(self) -> None:
        await self.page.locator("#Form_Search").press("Enter")

    async def is_search_successful(self) -> bool:
        results = await self.page.locator("#search-results").is_visible()
        return results