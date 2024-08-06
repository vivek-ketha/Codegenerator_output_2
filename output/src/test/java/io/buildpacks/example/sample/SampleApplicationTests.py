  Here's how we can convert this code to Playwright:

```python
from playwright.sync_api import Playwright, sync_playwright

def test_context_loads(playwright: Playwright) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8080")
        assert page.title() == "Sample Application"
        browser.close()
```