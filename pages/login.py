import os
from selenium.webdriver.common.by import By
from utils.base import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.txt_username = (By.ID, "UserName")
        self.txt_password = (By.ID, "Password")
        self.btn_login = (By.ID, "btnSubmit")
        self.div_login_form = (By.ID, "LoginForm")

    def launch_humanforce_login_page(self):
        self.driver.get(os.getenv("HUMANFORCE_LOGIN_PAGE"))

    def enter_username(self, username: str):
        self.input_text(self.txt_username, username)

    def enter_password(self, password: str):
        self.input_text(self.txt_password, password)

    def click_login(self):
        self.click_element(self.btn_login)

    def login(self, user):
        self.launch_humanforce_login_page()
        username = os.getenv(f"{user}_USER".upper())
        password = os.getenv(f"{user}_PASSWORD".upper())
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def verify_login_error_is_displayed(self, message):
        element = (By.XPATH, f"//*[contains(@class,'error')]//*[.='{message}']")
        self.is_element_visible(element)
        self.save_page_screenshot()

    def verify_successful_logout(self):
        self.is_element_visible(self.div_login_form)
        self.save_page_screenshot()



