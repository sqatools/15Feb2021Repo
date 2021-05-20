from automation_framework.base.selenium_code import selenium_driver
from automation_framework.data.bus.bus_booking_page_data import *


class BusBooking(selenium_driver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_source(self):
        self.input_text(source_element, source_location)
        self.click_element(source_dropdown_option)