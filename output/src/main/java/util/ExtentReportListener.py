from playwright.sync_api import Page

def on_test_failure(page: Page, result: dict) -> None:
    file_name = f"Screenshot-{calendar.timegm(time.gmtime())}.jpg"
    page.screenshot(path=f"./screenshots/{file_name}")
    logger.log(LogStatus.FAIL, "Test failed, attaching screenshot in screenshots folder")