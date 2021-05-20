collge_id = '6010'
collge_id_list = ['6001','6002', '6003', '6004', '6005', '6006']
college_list_url = "https://www.sqatools.in/2021/05/pune-college-list.html"


from automation_framework.data.session_data import test_data_excel_file_path
from automation_framework.utilities.excel_reader import ExcelReader
sheet_name = 'dummy_ticket'
excel_obj = ExcelReader(test_data_excel_file_path)