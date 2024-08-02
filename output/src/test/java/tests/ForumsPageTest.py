async def navigate_to_forums_page(self):
    await self.page.hover("text=Community")
    await self.page.click("text=Forums")
    await self.page.wait_for_url("https://www.tutorialspoint.com/forums")