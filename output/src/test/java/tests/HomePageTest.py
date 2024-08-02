  Here is the converted code:

from playwright.sync_api import Page, expect
from tests.base_test import BaseTestClass

class HomePageTest(BaseTestClass):
    def test_verify_title(self):
        page = self.page
        logger = self.logger
        logger.info("Checking title matches string")
        expect(page).to_have_title("Oculus | VR Headsets & Equipment")
        logger.info("Title matches with title from DOM")

    def test_verify_logo(self):
        page = self.page
        logger = self.logger
        logger.info("Checking if logo is present")
        expect(page.get_by_role("img", name="Oculus")).to_be_visible()
        logger.info("Logo is present")

    def test_verify_headsets_dropdown(self):
        page = self.page
        logger = self.logger
        page.locator(".//a[@data-nav-item='headsets']").hover()
        logger.info("Hovering over Headsets tab")
        expected = [
            "Oculus Rift S\n" + "PC-Powered VR Gaming",
            "Oculus Quest\n" + "All-In-One VR Gaming",
            "Oculus Go\n" + "All-In-One VR Viewing",
            "Compare All Headsets",
        ]
        for i, link in enumerate(page.locator(".//a[@data-nav-item='headsets']//a").all()):
            logger.info(f"Checking if {link.inner_text()} link is present")
            expect(link).to_have_text(expected[i])

The converted code uses the Playwright Python library to automate the tests. The tests verify the title, the presence of the logo, and the contents of the headsets dropdown menu.

The tests use the expect() function from the Playwright Python library to make assertions. For example, the test_verify_title() test uses expect(page).to_have_title("Oculus | VR Headsets & Equipment") to verify that the page title matches the expected string.

The test_verify_logo() test uses expect(page.get_by_role("img", name="Oculus")).to_be_visible() to verify that the Oculus logo is present on the page.

The test_verify_headsets_dropdown() test uses expect(link).to_have_text(expected[i]) to verify that each link in the headsets dropdown menu has the expected text.

The tests use the logger from the BaseTestClass to log information and status messages. For example, the test_verify_title() test uses logger.info("Checking title matches string") and logger.info("Title matches with title from DOM") to log information about the test process.