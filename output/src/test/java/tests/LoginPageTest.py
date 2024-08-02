  To convert the code to Playwright, we'll need to install the Playwright package and update the test code to use the Playwright API.

Here's an example of how you can convert the code to Playwright:

```python
import playwright

def test_login_page(playwright):
    with playwright.chromium.launch() as browser:
        page = browser.new_page()
        page.goto("https://www.google.com")
        page.fill("input[type=text]", "playwright")
        page.click("input[type=submit]")
        assert page.url == "https://playwright.dev/"
```

In the code above, we import the `playwright` package, then use it to launch a browser and navigate to a website. We fill in a search term and click a button, and then assert that the page URL is as expected.