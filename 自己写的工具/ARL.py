import xlrd
from threading import Thread
from queue import Queue
from alive import UrlCheck


class ARL(Thread):
    ARL_URL_QUENE = Queue()
    ARL_ALIVE_URL = []
    ARL_ALIVE_URL_INDEFITY = []
    ARL_ALIVE_IP = []
    ARL_ALIVE_PORT=[]
    ARL_ALIVE_MAP = {}

    def __init__(self, file_name):
        super().__init__()
        ARL_DATA = xlrd.open_workbook(file_name)
        self.ARL_INFORMATION_MAP = {}

        for i in range(0, 4):
            ARL_INFORMATION_LIST = []
            ARL_TABLE = ARL_DATA.sheet_by_index(i)
            for col in range(0, ARL_TABLE.ncols):
                row = ARL_TABLE.nrows
                ARL_INFORMATION_LIST.append([str(ARL_TABLE.cell_value(j, col)) for j in range(1, row)])
            self.ARL_INFORMATION_MAP[i] = ARL_INFORMATION_LIST

    def run(self):
        self.GetAlive()
        self.Clean()
        # for i in range(50):
        #     bdm = UrlCheck(self.ARL_URL_QUENE, self.ARL_ALIVE_URL)
        #     bdm.daemon = True
        #     bdm.start()
        # self.ARL_URL_QUENE.join()
        # self.Clean()

    def GetAlive(self):
        for url in self.ARL_INFORMATION_MAP.get(3)[0]:
            self.ARL_URL_QUENE.put(url)
        for i in range(50):
            Check = UrlCheck(self.ARL_URL_QUENE, self.ARL_ALIVE_URL)
            Check.daemon = True
            Check.start()
        self.ARL_URL_QUENE.join()

    def Clean(self):
        ##获取对应IP
        IP_LIST = self.ARL_INFORMATION_MAP.get(3)[3]
        URL_LIST = self.ARL_INFORMATION_MAP.get(3)[0]
        PORT_LIST = self.ARL_INFORMATION_MAP.get(1)[1]
        for url in self.ARL_ALIVE_URL:
            self.ARL_ALIVE_IP.append(IP_LIST[URL_LIST.index(url)].split())
        print(self.ARL_ALIVE_IP)
    ##获取ip对应的端口
        for list in self.ARL_ALIVE_IP:
            for ip in list:
                self.ARL_ALIVE_PORT.append(PORT_LIST[IP_LIST.index(ip)].split())
        print(self.ARL_ALIVE_PORT)