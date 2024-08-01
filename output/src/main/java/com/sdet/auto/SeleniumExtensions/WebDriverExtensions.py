```
from playwright.sync_api import Page, expect

def get_element_by_selector(page: Page, css_selector: str, wait_seconds: int = 10) -> Page:
    return page.wait_for_selector(css_selector, timeout=wait_seconds * 1000)

def selenium_exception_handler(page: Page, exception: Exception) -> None:
    exception_name = exception.__class__.__name__
    print(f"WebDriver Exception Handler Caught Exception: [{exception_name}]")
    screenshot(page)
    print("End")

def screenshot(page: Page) -> None:
    test_name = f"{page.context.options['name']}_{page.context.options['unique_identifier']}.png"
    screenshot_dir = "screenshots/"
    try:
        print("Attempting Selenium Screenshot ...")
        screenshot = page.screenshot()
        with open(screenshot_dir + test_name, "wb") as f:
            f.write(screenshot)
        print(f"Browser Screenshot Save Location: {screenshot_dir + test_name}")
    except Exception as e:
        print(f"Failed to take screenshot: {e}")
```