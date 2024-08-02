  Here's an example of how you can implement this using Playwright:

```python
from playwright.sync_api import Page, expect

def test_login(page: Page):
    page.goto("https://example.com/login")
    page.fill("input[name=username]", "username")
    page.fill("input[name=password]", "")
    page.click("button[type=submit]")
    expect(page).to_have_url("https://example.com/home")
```