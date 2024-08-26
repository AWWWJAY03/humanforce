from selenium.webdriver.common.by import By
from utils.base import BasePage
import os

class HumanforcePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.btn_accept_cookies = (By.ID, "cookiescript_accept")
        self.link_time_and_attendance = (By.ID, "//*[@href='/product/workforce-management/time-and-attendance/']")

    def launch_humanforce(self):
        self.driver.get(os.getenv("HUMANFORCE_URL"))

    def accept_cookies(self):
        self.wait_until_visible(self.btn_accept_cookies, 60)
        self.click_element(self.btn_accept_cookies)

    def verify_article_is_loaded_successfully(self, article: str):
        element = (By.XPATH, "//span[.='7 benefits of workforce analytics for business']")
        assert self.is_element_visible(element), f"{article} not loaded"
        self.save_page_screenshot()

