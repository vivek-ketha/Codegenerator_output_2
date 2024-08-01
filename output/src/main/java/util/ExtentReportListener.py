from playwright.sync_api import Page
from playwright.sync_api import Reporter

class ExtentReportListener(Reporter):
    def __init__(self, page: Page):
        self.page = page

    def on_start(self, suite: str):
        self.report = ExtentReports(f"./report/{suite}_Results.html")

    def on_test_start(self, test: str):
        self.logger = self.report.start_test(test)
        self.logger.log(LogStatus.INFO, f"Executing test: {test}")

    def on_test_end(self, test: str):
        self.logger.log(LogStatus.INFO, "Finished executing test")

    def on_test_fail(self, test: str):
        file_name = f"Screenshot-{int(time.time())}.jpg"
        self.page.screenshot(path=f"./screenshots/{file_name}")
        self.logger.log(LogStatus.FAIL, "Test failed, attaching screenshot in screenshots folder")

    def on_test_skip(self, test: str):
        self.logger.log(LogStatus.SKIP, "Test skipped")

    def on_end(self, suite: str):
        self.report.flush()