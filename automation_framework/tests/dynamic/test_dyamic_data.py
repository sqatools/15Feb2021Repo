import pytest
from automation_framework.modules.dynamic.dynamic import Dynamic
from automation_framework.base.selenium_code import selenium_driver
from pytest_html_reporter import attach
from automation_framework.data.session_data import test_data_excel_file_path
from automation_framework.utilities.excel_reader import ExcelReader
from automation_framework.data.dynamic_data import *
import logging
from time import sleep

log = logging.getLogger(__name__)

@pytest.mark.usefixtures("class_setup")
class TestDynamic:

    def test_select_dynamic(self):
        self.driver.get(college_list_url)
        global obj
        obj = Dynamic(self.driver)
        obj.select_dynamic_checkbox(collge_id)
        sleep(5)

    def test_select_multiple_checkbox(self):
        for id in collge_id_list:
            obj = Dynamic(self.driver)
            obj.select_dynamic_checkbox(id)
        sleep(5)

    def test_select_multiple_checkbox_from_excel(self):
        sheet_name = 'dynamic'
        excel_obj = ExcelReader(test_data_excel_file_path)
        for i in range(1, 9):
           id = excel_obj.read_excel_data(i, 1, sheetname=sheet_name)
           log.info(f"institute id from excel {id}")
           obj.select_dynamic_checkbox(id)

        sleep(5)

