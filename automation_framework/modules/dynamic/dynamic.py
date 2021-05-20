from automation_framework.base.selenium_code import selenium_driver
from automation_framework.data.dynamic_data import *


class Dynamic(selenium_driver):
    def __init__(self, driver):
        super().__init__(driver)


    def select_dynamic_checkbox(self, institude_id):
        dynamic_xpath = f"//td[text()='{institude_id}']//parent::tr//input"
        self.click_element((dynamic_xpath, "xpath"))