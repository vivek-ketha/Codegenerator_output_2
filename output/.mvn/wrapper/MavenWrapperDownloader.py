
from playwright.sync_api import Playwright, sync_playwright

def download_file_from_url(url: str, destination: str):
    with sync_playwright() as playwright:
        with playwright.chromium.launch() as browser:
            page = browser.new_page()
            page.goto(url)
            page.download(destination)

if __name__ == "__main__":
    download_file_from_url("https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/0.4.0/maven-wrapper-0.4.0.jar", ".mvn/wrapper/maven-wrapper.jar")