import os
from automation_framework.data.session_data import excel_path
from automation_framework.utilities.excel_reader import ExcelReader
sheet_name = 'Redbus'
dummy_ticket_excel_file = os.path.join(excel_path, 'dummy_ticket.xlsx')
excel_obj = ExcelReader(dummy_ticket_excel_file)

# Test data


travel_date = 20
source_location = "Pune"
source_area = "Swargate"

# Locators
source_element = ("txtSource", "id")
source_dropdown_option = (f"//li[contains(text(), '{source_area}, ')]/strong[text()='{source_location}']", "xpath")
destination_element = ("txtDestination", "id")
depart_date_element = (f"//span[text()='{travel_date}']", "xpath")
search_button = ("//button[@class='D120_search_btn searchBuses']", "xpath")
