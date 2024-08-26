from selenium.webdriver.common.by import By

from utils.base import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.div_greetings = (By.XPATH, "//span[@class='home-header__info__name']")
        self.btn_close = (By.XPATH, "//*[@class='wm-close-button walkme-x-button']")
        self.link_hf_academy = (By.XPATH, "//*[contains(@class,'walkme-launcher-image')]")
        self.div_walkme_overlay = (By.ID, "walkme-menu")
        self.txt_walkme_search = (By.XPATH, "//input[contains(@class, 'walkme-search-box')]")
        self.div_walkme_close = (By.XPATH, "//*[contains(@class, 'walkme-minimize')]")
        self.btn_logout = (By.ID, "MenuFooter_Logout")

    def launch_hf_academy(self):
        self.click_element(self.link_hf_academy)

    def close_hf_academy(self):
        self.click_element(self.div_walkme_close)

    def hf_academy_search_for(self, text: str):
        self.input_text(self.txt_walkme_search, text)

    def verify_name_in_greetings(self, name: str):
        assert (self.get_text(self.div_greetings) == f"Hello {name}")
        self.save_page_screenshot()

    def dismiss_dialog_box(self):
        self.wait_until_visible(self.btn_close, 60)
        self.click_element(self.btn_close)

    def click_logout(self):
        self.click_element(self.btn_logout)

    def verify_hf_academy_result(self, article):
        element = (By.XPATH, f"//*[@title='{article}']")
        self.scroll_into_view(element)
        assert(self.is_element_visible(element))
        self.save_page_screenshot()
