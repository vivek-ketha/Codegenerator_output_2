
from playwright.sync_api import Playwright, Page
from datetime import datetime
import os

def on_test_start(result):
    logger = report.start_test(result.method_name)
    logger.log("Executing test: " + result.method_name)

def on_test_success(result):
    logger.log("Finished executing test")

def on_test_failure(result):
    file_name = "Screenshot-{}.jpg".format(datetime.now().strftime("%Y%m%d_%H%M%S"))
    driver = result.test_context.attributes["WebDriver"] # use string from setAttribute from BasePage
    src_file = driver.take_screenshot()
    dest_file = os.path.join("./screenshots", file_name)
    with open(dest_file, "wb") as f:
        f.write(src_file)
    logger.log("Test failed, attaching screenshot in screenshots folder")

def on_test_skipped(result):
    logger.log("Test skipped")