
from playwright.sync_api import Page
from datetime import datetime
import os
from playwright.sync_api import Browser

class ExtentReportListener:
    def __init__(self, browser: Browser):
        self.browser = browser

    def on_test_start(self, test):
        self.logger = self.report.start_test(test.method_name)
        self.logger.log("Executing test: " + test.method_name)

    def on_test_success(self, test):
        self.logger.log("Finished executing test")

    def on_test_failure(self, test):
        screenshot_file_name = f"Screenshot-{datetime.now().strftime('%Y%m%d-%H%M%S')}.png"
        page: Page = test.context.attribute("page")  # use string from setAttribute from BasePage
        page.screenshot(path=os.path.join("./screenshots", screenshot_file_name))
        self.logger.log("Test failed, attaching screenshot in screenshots folder")

    def on_test_skipped(self, test):
        self.logger.log("Test skipped")

    def on_suite_start(self, suite):
        self.report = ExtentReports(f"./report/{suite.name}_Results.html")

    def on_suite_end(self, suite):
        self.report.flush()