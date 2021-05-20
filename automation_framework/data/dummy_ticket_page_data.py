import os
from automation_framework.data.session_data import test_data_excel_file_path
from automation_framework.utilities.excel_reader import ExcelReader
sheet_name = 'dummy_ticket'
excel_obj = ExcelReader(test_data_excel_file_path)
# data

# user_name = "John"
# last_name = "Harry"
# date_of_birth = "28"
# dob_month = 'Aug'
# dob_year = '1990'
# extra_passenger = 'add 2 more passengers (200%)'


user_name = excel_obj.read_excel_data(1, 2, sheetname=sheet_name)
last_name = excel_obj.read_excel_data(2, 2, sheetname=sheet_name)
date_of_birth = excel_obj.read_excel_data(3, 2, sheetname=sheet_name)
dob_month = excel_obj.read_excel_data(4, 2, sheetname=sheet_name)
dob_year = excel_obj.read_excel_data(5, 2, sheetname=sheet_name)
extra_passenger = excel_obj.read_excel_data(6, 2, sheetname=sheet_name)



#Locator
first_name_field = ("travname", "id")
last_name_field = ("travlastname", "id")
dob_calender = ("dob", "id")
month_dropdown = ("//select[@data-handler='selectMonth']", "xpath")
year_dropdown = ("//select[@data-handler='selectYear']", "xpath")
date_link= (str(date_of_birth), "link")
gender_button = ("sex_1", "id")

add_more_passenger_checkbox = ('addmorepax', 'id')
add_more_pass_dropdown = ('addpaxno', 'id')


