  To convert the code to Playwright, you can use the playwright-java library. This library provides a Java API for writing end-to-end tests using Playwright.

Here's how you can convert the code to Playwright using the playwright-java library:

```java
import io.playwright.Browser;
import io.playwright.BrowserType;
import io.playwright.Playwright;

public class SampleApplication {
    public static void main(String[] args) {
        Playwright playwright = Playwright.create();
        Browser browser = playwright.chromium().launch();
        BrowserPage page = browser.newPage();
        page.navigate("https://www.google.com");
        page.screenshot(new Page.ScreenshotOptions().setPath("screenshot.png"));
        browser.close();
        playwright.close();
    }
}
```

The code above uses the playwright-java library to launch a Chromium browser, navigate to Google, take a screenshot, and close the browser. You can modify the code to match your specific testing requirements.