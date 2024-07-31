
from playwright.sync_api import Page

def test_forget_password(page: Page):
    page.goto("https://example.com/forget_password")
    page.fill(txtEmail, "")
    page.click(btnRetrievePassword)
    print("Email entered and retrieve button clicked.")
    assert page.url == "https://example.com/password_sent"
    print("Password sent page loaded.")