from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def type_username(self, username):
        self.driver.find_element(By.ID, "email").clear()
        self.driver.find_element(By.ID, "email").send_keys(username)

    def type_password(self, password):
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_sign_in(self):
        self.driver.find_element(By.ID, "sign_in").click()

    def error_container_displayed(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bxInputControl.bxInputControl--error"))).is_displayed()

    def verify_new_page(self):
        self.wait.until(EC.url_to_be("https://www.oculus.com/"))
        return self.driver.title == "Oculus | VR Headsets & Equipment"