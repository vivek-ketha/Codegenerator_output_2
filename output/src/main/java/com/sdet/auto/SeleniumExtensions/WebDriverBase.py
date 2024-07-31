
from playwright.sync_api import sync_playwright

def get_web_driver(browser):
    if browser == "chrome":
        print("Launching Chrome Browser.")
        options = {"args": ["--start-maximized", "--disable-extensions", "disable-infobars"]}
        with sync_playwright() as p:
            driver = p.chromium.launch(headless=False, channel="chrome", executable_path="src/main/resources/chromedriver", options=options)
            driver.context.clear_cookies()

    elif browser == "firefox":
        print("Launching Firefox Browser.")
        with sync_playwright() as p:
            driver = p.firefox.launch(headless=False, channel="firefox", executable_path="src/main/resources/geckodriver")
            driver.context.clear_cookies()

    elif browser == "seleniumGrid":
        print("Launching Browser Using Selenium Grid - Chrome Browser.")
        grid_url = "http://y75EbcWLcnPNI0p8sZBQTcTUGj5PCOl0:LhvNjhomu4Z3Ue2d3tTMwDx3MtJe7V5I@SESYNPZ6.gridlastic.com:80/wd/hub"
        options = {"args": ["--start-maximized", "--disable-extensions", "disable-infobars"]}
        capabilities = {"browserName": "chrome", "platform": "WINDOWS", "version": "latest"}
        with sync_playwright() as p:
            driver = p.chromium.connect(grid_url, options=options, capabilities=capabilities)
            driver.context.clear_cookies()

    else:
        raise RuntimeError(f"Browser Type {browser}, not Found, please add additional code for this desired WebDriver Type.")

    return driver