from threading import Thread

import xlrd

from alive import UrlCheck

from queue import  Queue
class YinTu(Thread):
    YT_DOMAIN=Queue()
    def __init__(self,file_name):
        YT_DATA=xlrd.open_workbook(file_name)
        YT_TABLE=YT_DATA.sheet_by_index(0)
        YT_TABLE_col=YT_TABLE.ncols
        YT_TABLE_row=YT_TABLE.nrows
        self.YT_INFORMATION_MAP={}
        self.YT_INFOMATION_LIST=[]
        for c in range(0,YT_TABLE_col):
            YT_INFORMATION_TMP=[]
            for r in range(0,YT_TABLE_row):
                YT_INFORMATION_TMP.append([str(YT_TABLE.cell_value(i,c) ) for i in range(1,r)])
            self.YT_INFOMATION_LIST.append(YT_INFORMATION_TMP)
        for domain in self.YT_INFORMATION_MAP[6]:
            self.YT_DOMAIN.put(domain)
    def run(self):
        for i in range(50):
            bdm = UrlCheck(self.YT_, self.ARL_ALIVE_URL)
            bdm.daemon = True
            bdm.start()
        self.ARL_URL_QUENE.join()
        self.Clean()

    def Clean(self):

if __name__=='__main__':
    YinTu('../assets_20221122.xls')

