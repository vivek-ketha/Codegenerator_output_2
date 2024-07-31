
import asyncio

async def nav_to_web_page_under_test(page, config):
    await page.goto(config.web_url)
    print("Navigated to the web page under test.")