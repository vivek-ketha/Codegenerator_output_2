
from playwright.sync_api import Playwright, Page
from datetime import datetime
import os

def on_test_start(result):
    logger = report.start_test(result.method_name)
    logger.log("info", "Executing test: " + result.method_name)

def on_test_success(result):
    logger.log("info", "Finished executing test")

def on_test_failure(result):
    file_name = f"Screenshot-{datetime.now().timestamp()}.jpg"
    driver = result.test_context.attributes["WebDriver"]
    src_file = driver.get_screenshot_as(OutputType.FILE)
    dest_file = os.path.join("./screenshots", file_name)
    try:
        shutil.copyfile(src_file, dest_file)
        print("Screenshot taken, saved in screenshots folder")
    except IOError:
        print("Failed to take screenshot")
    logger.log("fail", "Test failed, attaching screenshot in screenshots folder")

def on_test_skipped(result):
    logger.log("skip", "Test skipped")