import pytest
from automation_framework.modules.google_search_page import GoogleSearch
from automation_framework.base.selenium_code import selenium_driver
from pytest_html_reporter import attach
import logging

log = logging.getLogger(__name__)

@pytest.mark.usefixtures("class_setup")
class TestGoogleSearch:
    log.info("_____TestGoogleSearch______")

    def test_search_data_google(self):
        log.info("test cases : test_search_data_google : start")
        gc = GoogleSearch(self.driver)
        gc.search_content()
        log.info("test cases : test_search_data_google : finish")

    def test_click_on_link(self):
         log.info("test cases : test_click_on_link : start")
         try:
             dr = selenium_driver(self.driver)
             dr.click_element(("Welcome to Python.org", "link1"))
         except Exception as e:
             attach(data=self.driver.get_screenshot_as_png())
             raise e
         log.info("test cases : test_click_on_link : finish")
