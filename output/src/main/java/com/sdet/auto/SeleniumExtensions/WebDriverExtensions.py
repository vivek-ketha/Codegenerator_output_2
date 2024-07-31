
from playwright.sync_api import Page

def get_element_by_selector(page: Page, css_selector: str) -> Page:
    return page.wait_for_selector(css_selector)

def get_element_by_selector(page: Page, css_selector: str, wait_seconds: int) -> Page:
    return page.wait_for_selector(css_selector, timeout=wait_seconds * 1000)

def selenium_exception_handler(exception: Exception) -> None:
    exception_name = type(exception).__name__
    print(f"Selenium Exception Handler Caught Exception: [{exception_name}]")
    screenshot(page)
    print("Screenshot taken")

def screenshot(page: Page) -> None:
    test_name = "test_name"
    screenshot_dir = "/path/to/screenshots"
    test_screenshot_path = f"{screenshot_dir}/{test_name}.png"
    page.screenshot(path=test_screenshot_path)
    print(f"Browser Screenshot Save Location: {test_screenshot_path}")