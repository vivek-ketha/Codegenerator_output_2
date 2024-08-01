```
import os
from playwright.sync_api import Playwright, sync_playwright

def get_web_driver(browser):
    if browser == "chrome":
        return "Chrome"
    elif browser == "firefox":
        return "Firefox"
    elif browser == "seleniumGrid":
        return "Selenium Grid"
    else:
        raise RuntimeError(f"Browser type {browser} not found")

def get_web_driver_with_existing_driver(existing_driver):
    return existing_driver
with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    print(page.title())
    browser.close()
```