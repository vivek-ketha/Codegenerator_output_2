
from playwright.sync_api import Playwright, sync_playwright

def get_web_url():
    return web_url

def set_web_url(url):
    global web_url
    web_url = url

def get_web_browser():
    return web_browser

def set_web_browser(browser):
    global web_browser
    web_browser = browser

web_url = None
web_browser = None

def get_config_settings():
    global web_url
    global web_browser

    property = {}
    prop_file_name = "config.properties"
    with open(prop_file_name, "r") as file:
        for line in file:
            key, value = line.split("=")
            property[key] = value

    set_web_url(property["webUrl"])
    set_web_browser(property["webBrowser"])

    print("Test Config Settings")
    print(f"WebUrl: {get_web_url()}")
    print(f"WebBrowser: {get_web_browser()}")

with sync_playwright() as playwright:
    get_config_settings()