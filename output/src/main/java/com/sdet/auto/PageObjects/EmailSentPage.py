
from playwright.sync_api import Page

class EmailSentPage:
    def __init__(self, page: Page):
        self.page = page

    @staticmethod
    def verify_email_sent(test_assert, expected_msg):
        txt_message = "#content"
        test_assert.set_pass(LoggingLibrary.compare_result(self.page.get_by_selector(txt_message).text_content(), expected_msg))