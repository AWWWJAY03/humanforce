from selenium.webdriver.common.by import By

from utils.base import BasePage

class AdminPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.btn_add_new_record = (By.XPATH, '//*[.="Add new record"]')
        self.txt_name = (By.ID, "Name")
        self.txt_short_name = (By.ID, "ShortName")
        self.txt_export_code = (By.ID, "ExportCode")
        self.btn_save = (By.XPATH, '//*[.="Save"]')
        self.btn_delete_confirm = (By.ID, 'yesButton')

    def add_new_record(self, data):
        self.click_element(self.btn_add_new_record)
        self.input_text(self.txt_name, data["name"])
        self.input_text(self.txt_short_name, data["short_name"])
        self.input_text(self.txt_export_code, data["export_code"])
        self.click_element(self.btn_save)

    def delete_record(self, data):
        name = data["name"]
        element = (By.XPATH, f"//tr[td[.='{name}']]//a[.='Delete']")
        if self.is_element_visible(element):
            self.click_element(element)
            self.click_element(self.btn_delete_confirm)

    def verify_newly_added_record(self, data):
        name = data["name"]
        element = (By.XPATH, f"//*[@id='GridAreas']//td[.='{name}']")
        assert self.is_element_visible(element)
        export_code = data["export_code"]
        element = (By.XPATH, f"//*[@id='GridAreas']//td[.='{export_code}']")
        assert self.is_element_visible(element)
        self.save_page_screenshot()

    def verify_deleted_record(self, data):
        name = data["name"]
        element = (By.XPATH, f"//*[@id='GridAreas']//td[.='{name}']")
        assert not self.is_element_visible(element)
        self.save_page_screenshot()





