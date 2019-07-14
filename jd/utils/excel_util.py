import xlrd
class ExcelUtil:
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            excel_path = '/Users/mengtingting/PycharmProjects/review/jd/config/data.xls'
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]
        self.rows = self.table.nrows

    def get_data(self):
        result = []
        for i in range(self.rows):
            col = self.table.row_values(i)
            print(col)
            result.append(col)
        return result

if __name__ == '__main__':
    excel_u = ExcelUtil()
    excel_u.get_data()
