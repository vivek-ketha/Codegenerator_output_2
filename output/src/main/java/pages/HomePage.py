from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    async def get_title(self) -> str:
        return await self.page.title()

    async def get_logo(self) -> bool:
        return await self.page.locator("._2v0_").is_visible()

    async def click_log_in_link(self):
        await self.page.locator("a:has-text('Log In or Sign Up')").click()

    async def click_sign_in_link(self):
        await self.page.locator("a#u_0_1v:has-text('Sign in')").click()

    async def hover_over_community_tab(self):
        await self.page.locator("#u_0_15").hover()

    async def click_forums_tab(self):
        await self.page.locator("#u_0_17").click()

    async def switch_tabs(self):
        tabs = await self.page.context.pages()
        await tabs[1].set_default_navigation_timeout(0)
        await tabs[1].goto("", wait_until="domcontentloaded")

    async def hover_over_headsets_tab(self):
        await self.page.locator("#u_0_x").hover()

    async def headsets_dropdown_results(self):
        return await self.page.locator("div#u_0_x span a[data-testid^='navlink-']").all_text_contents()

    async def click_oculus_quest(self):
        await self.page.locator("#u_0_10").click()

    async def add_to_cart(self):
        await self.page.locator("button._8166._4pg_._3hmq._4phk._4ph1:has-text('Buy Now')").click()
        await self.page.locator("div>.modal__button-wrapper-128").click()

    async def is_cart_page_loaded(self) -> bool:
        return await self.page.locator("._4ju3._4pg_._3hmq._4phk").is_visible()