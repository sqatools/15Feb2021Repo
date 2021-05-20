#test data
import os
from automation_framework.data.session_data import test_data_excel_file_path
from automation_framework.utilities.excel_reader import ExcelReader

sheet_name = 'Google'
excel_obj = ExcelReader(test_data_excel_file_path)
#search_data = "Python"

search_data = excel_obj.read_excel_data(1, 1, sheetname=sheet_name)





#locators
search_field = ("q", "name")
search_button = ("btnK", "name")
