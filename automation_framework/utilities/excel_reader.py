import openpyxl

class ExcelReader:
    def __init__(self, file_path):
        self.filepath = file_path

    def read_excel_data(self, row, col, sheetname='Sheet1'):
        wb = openpyxl.load_workbook(self.filepath)
        sheet = wb[sheetname]
        data = sheet.cell(row, col).value
        return data

# if __name__ == '__main__':
#     file_path = "E:\\15feb2021\\automation_framework\\data\\excel_files\\dummy_ticket.xlsx"
#     obj = ExcelReader(file_path)
#     print(obj.read_excel_data(1, 1))
#     print(obj.read_excel_data(1, 1, sheetname='Sheet2'))
