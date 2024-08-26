import os
from datetime import datetime
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click_element(self, element):
        # locator = ec.visibility_of_element_located(element)
        self.wait.until(ec.element_to_be_clickable(element)).click()
        # self.scroll_into_view(locator)

    def input_text(self, element, text: str):
        element = self.wait.until(ec.visibility_of_element_located(element))
        element.clear()
        element.send_keys(text)

    def get_text(self, element):
        element = self.wait.until(ec.visibility_of_element_located(element))
        text = element.text
        return element.text

    def select_dropdown(self, element, options: str):
        element = Select(self.wait.until(ec.visibility_of_element_located(element)))
        element.select_by_value(options)

    def click_link_by_visible_text(self, link_text: str):
        element = (By.XPATH, f"//*[.='{link_text}']/a")
        self.scroll_into_view(element)
        self.click_element(element)

    def scroll_into_view(self, element):
        locator = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", locator)

    def is_element_visible(self, element):
        element = self.wait.until(ec.visibility_of_element_located(element))
        return element.is_displayed()

    def wait_until_visible(self, element, timeout=30):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(element))

    def save_page_screenshot(self,prefix = "screenshot"):
        filename = f"{prefix}_{datetime.now().strftime('%Y%m%d%H%M%S%f')}.png"
        filepath = os.path.join('reports', 'screenshots', filename)
        self.driver.save_screenshot(filepath)

    def go_to_link(self, link):
        self.driver.get(f"{os.getenv('HUMANFORCE_LOGIN_PAGE')}/{link}")

