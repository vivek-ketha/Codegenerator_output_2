  Here's how you can rewrite the code to use Playwright:
  
```python
import playwright

class BasePage:
    def __init__(self, browser, url="https://www.oculus.com/"):
        self.browser = browser
        self.url = url

    async def setup(self):
        self.page = await self.browser.newPage()
        await self.page.goto(self.url)

    async def teardown(self):
        await self.browser.close()
```

The `setup` method initializes the browser and navigates to the specified URL, while the `teardown` method closes the browser.