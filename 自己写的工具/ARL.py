import xlrd
from threading import Thread
from queue import Queue
from alive import UrlCheck


class ARL(Thread):
    ARL_URL_QUENE = Queue()
    ARL_ALIVE_URL = []
    ARL_ALIVE_URL_INDEFITY=[]
    ARL_ALIVE_IP=[]
    def __init__(self, file_name):
        super().__init__()
        ARL_DATA = xlrd.open_workbook(file_name)
        self.ARL_INFORMATION_MAP={}
        ARL_INFORMATION_LIST=[]
        for i in range(0,4):
            ARL_TABLE=ARL_DATA.sheet_by_index(i)
            for col in range(0,ARL_TABLE.ncols):
                for row in range(0,ARL_TABLE.nrows):
                    ARL_INFORMATION_LIST.append([str(ARL_TABLE.cell_value(j,col)) for j in range(1,row)])





    def run(self):
        for i in range(50):
            bdm = UrlCheck(self.ARL_URL_QUENE, self.ARL_ALIVE_URL)
            bdm.daemon = True
            bdm.start()
        self.ARL_URL_QUENE.join()
        self.Clean()


    def Clean(self):
    ##获取IP
        for url in self.ARL_ALIVE_URL:
               self.ARL_ALIVE_IP.append()
        print(self.ARL_ALIVE_URL_INDEFITY)
    ##获取对应ip




