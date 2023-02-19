
from openpyxl import load_workbook

class HandleExcel:

    def __init__(self,file_name,sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name

    # 获取 excel 测试用例数据
    def get_test_case(self):
        wb = load_workbook(filename=self.file_name)              # 实例化
        sh = wb[self.sheet_name]                                 # 获取 sheetname
        all_excel_data = list(sh.iter_rows(values_only=True))    # 获取表格所有数据
        excel_title = all_excel_data[0]                          # 获取表头
        case_data_list = all_excel_data[1:]                      # 获取所有的用例数据
        test_case_list = []                                      # 测试用例数据
        for case in case_data_list:
            test_case = dict(zip(excel_title,case))              # 数据拼接，用表头与测试用例数据进行组装拼成 dict
            test_case_list.append(test_case)                     # 将每次拼接好的测试添加到test_case_list
        wb.close()
        return test_case_list
