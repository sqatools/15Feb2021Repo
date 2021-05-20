import os
from datetime import datetime
browser = 'chrome'
url = "https://www.google.co.in/"
dummy_url = "https://www.dummyticket.com/dummy-ticket-for-visa-application/"
rebbus_url = "https://www.redbus.in/bus-tickets/"

chrome_driver_path = os.environ['CHROME_PATH']

cure_dir = os.getcwd()

log_path  = os.path.join(cure_dir, 'logs')

#E:\15feb2021\automation_framework\logs

excel_path = os.path.join(os.path.join(cure_dir, 'data'), 'excel_files')

#E:\15feb2021\automation_framework\data\excel_files

log_file = datetime.now().strftime("%d_%m_%y_%H_%M_%S")

log_file_path = os.path.join(log_path, f"debug_{log_file}.log")

headless = False

test_data_excel_file = 'test_data.xlsx'

test_data_excel_file_path  = os.path.join(excel_path, test_data_excel_file)