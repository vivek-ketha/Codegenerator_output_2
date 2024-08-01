from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    async def get_title(self) -> str:
        return await self.page.title()

    async def get_logo(self) -> bool:
        oculus_logo = await self.page.query_selector("._2v0_")
        return await oculus_logo.is_visible()

    async def click_log_in_link(self) -> None:
        log_in_link = await self.page.query_selector("//a[contains(text(), 'Log In or Sign Up')]")
        await log_in_link.click()

    async def click_signin_link(self) -> None:
        signin_button = await self.page.query_selector("//a[@id='u_0_1v'][contains(text(), 'Sign in')]")
        await signin_button.click()

    async def hover_over_community_tab(self) -> None:
        community_tab = await self.page.query_selector("#u_0_17")
        await self.page.mouse.move(100, 200)

    async def click_forums_tab(self) -> None:
        forums_tab = await self.page.query_selector("#u_0_17")
        await forums_tab.click()

    async def switch_tabs(self) -> None:
        tabs = await self.page.context.pages()
        await tabs[1].goto("")

    async def hover_over_headsets_tab(self) -> None:
        headsets_tab = await self.page.query_selector("#u_0_x")
        await self.page.mouse.move(100, 200)

    async def click_oculus_quest(self) -> None:
        oculus_quest = await self.page.query_selector("#u_0_10")
        await oculus_quest.click()

    async def add_to_cart(self) -> None:
        buy_now_button = await self.page.query_selector("//button[@class='_8166 _4pg_ _3hmq _4phk _4ph1']//span[contains(text(), 'Buy Now')]")
        await buy_now_button.click()
        one_twenty_eight_gb = await self.page.query_selector("div>.modal__button-wrapper-128")
        await one_twenty_eight_gb.click()

    async def is_cart_page_loaded(self) -> bool:
        checkout_button = await self.page.query_selector("._4ju3._4pg_._3hmq._4phk")
        return await checkout_button.is_visible()