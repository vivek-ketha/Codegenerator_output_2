from playwright.sync_api import Page, expect

def test_login_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.click("text=Login")
    page.click("text=Sign in")
    page.fill("css=input[id=user-name]", "InvalidEmail@gmail.com")
    page.fill("css=input[id=password]", "")
    page.click("css=input[type=submit]")
    expect(page).to_have_css("css=div[class*=error-message-container]", visible=True)
    page.fill("css=input[id=user-name]", "testuser@yahoo.com")
    page.fill("css=input[id=password]", "")
    page.click("css=input[type=submit]")
    expect(page).to_have_css("css=div[class*=error-message-container]", visible=True)
    page.fill("css=input[id=user-name]", "standard_user")
    page.fill("css=input[id=password]", "")
    page.click("css=input[type=submit]")
    expect(page).to_have_css("css=div[class*=product_label]", visible=True)