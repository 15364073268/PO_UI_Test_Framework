#coding=gbk
import xlrd
import os

now_path = os.path.dirname(__file__)
execl_path = os.path.join(now_path, '../element_info_datas/element_infos.xlsx')


class ExeclRead:
    def __init__(self,which_page,lement_path=execl_path):
        self.wrokbook = xlrd.open_workbook(filename=execl_path)
        self.table = self.wrokbook.sheet_by_name(sheet_name=which_page)
        self.row = self.table.nrows

    def execl_element_read(self):

        element_infos = {}
        for i in range(1, self.row):

            element_info = {}
            element_info['element_name'] = self.table.cell_value(i, 1)
            element_info['locator_type'] = self.table.cell_value(i, 2)
            element_info['locator_value'] = self.table.cell_value(i, 3)
            element_info['timeout'] = self.table.cell_value(i, 4)
            element_infos[self.table.cell_value(i, 0)] = element_info

        return element_infos

if __name__ =="__main__":
    element = ExeclRead('login_page').execl_element_read()
    print(element)
