
from playwright.sync_api import Page, expect
from tests.base_test import BaseTestClass
from pages.home_page import HomePage


class HomePageTest(BaseTestClass):
    def test_verify_title(self):
        home_page = HomePage(self.page)
        expect(self.page).to_have_title("Oculus | VR Headsets & Equipment")
        self.logger.info("Title matches with title from DOM")

    def test_verify_logo(self):
        home_page = HomePage(self.page)
        expect(home_page.get_logo()).to_be_visible()
        self.logger.info("Logo is present")

    def test_verify_headsets_dropdown(self):
        home_page = HomePage(self.page)
        home_page.hover_over_headsets_tab()
        self.logger.info("Hovering over Headsets tab")
        expected = [
            "Oculus Rift S\n" + "PC-Powered VR Gaming",
            "Oculus Quest\n" + "All-In-One VR Gaming",
            "Oculus Go\n" + "All-In-One VR Viewing",
            "Compare All Headsets",
        ]
        for i, link in enumerate(home_page.headsets_dropdown_results()):
            expect(link).to_have_text(expected[i])
            self.logger.info(f"Checking if {link.text_content()} link is present")

HomePageTest().main()