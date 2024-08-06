  Here is the converted code to Playwright:

```python
from playwright.sync_api import Playwright, sync_playwright

def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.goto("https://playwright.dev")
        page.screenshot(path="example.png")
        browser.close()

if __name__ == "__main__":
    main()
```