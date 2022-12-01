import xlrd
from threading import Thread
from queue import Queue
from alive import UrlCheck


class ARL(Thread):
    ##存储URL的队列，用于进行存活探测
    ARL_DOMAIN = Queue()
    ##存储URL的列表，用于进行提取
    ARL_DOMAIN_LIST=[]
    ARL_IP_LIST={}
    ARL_PORT_LIST=[]
    ARL_INDEFITY_LIST=[]
    ##存储已进行存活探测的DOMAIN
    ARL_ALIVE_DOMAIN = []
    ##存储已经进行存活探测的DOMAIN的组件信息
    ARL_ALIVE_DOMAIN_INDEFITY = []
    ##存储已经进行存活探测的DOMAIN的IP信息
    ARL_ALIVE_DOAMIN_IP = []
    ##存储已经进行存活探测的DOMAIN的IP的端口信息
    ARL_ALIVE_IP_PORT=[]
    ARL_ALIVE_INFORMATION_MAP={}


    def __init__(self, file_name):
        super().__init__()
        ARL_DATA = xlrd.open_workbook(file_name)
        self.ARL_INFORMATION_MAP = {}

        for i in range(0, 4):
            ARL_INFORMATION_LIST_TMP = []
            ARL_TABLE = ARL_DATA.sheet_by_index(i)
            for col in range(0, ARL_TABLE.ncols):
                row = ARL_TABLE.nrows
                ARL_INFORMATION_LIST_TMP.append([str(ARL_TABLE.cell_value(j, col)) for j in range(1, row)])
            self.ARL_INFORMATION_MAP[i] = ARL_INFORMATION_LIST_TMP
        ##取出IP



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
            self.ARL_DOMAIN.put(url)
        for i in range(50):
            Check = UrlCheck(self.ARL_DOMAIN, self.ARL_ALIVE_DOMAIN)
            Check.daemon = True
            Check.start()
        self.ARL_DOMAIN.join()

    def Clean(self):

        IP_LIST_TMP = self.ARL_INFORMATION_MAP.get(3)[3]
        self.DOMAIN_LIST = self.ARL_INFORMATION_MAP.get(3)[0]
        for domain in self.ARL_ALIVE_DOMAIN:
            self.ARL_ALIVE_DOAMIN_IP.append(IP_LIST_TMP[self.DOMAIN_LIST.index(domain)].split())

    ##获取ip对应的端口
        IP_LIST_TMP = self.ARL_INFORMATION_MAP.get(2)[0]
        PORT_LIST_TMP = self.ARL_INFORMATION_MAP.get(1)[1]
        for list in self.ARL_ALIVE_DOAMIN_IP:
            for ip in list:
                self.ARL_ALIVE_IP_PORT.append(PORT_LIST_TMP[IP_LIST_TMP.index(ip)].split())
        for i in range(0,len(IP_LIST_TMP)):
            for list in self.ARL_ALIVE_DOAMIN_IP:
                    if IP_LIST_TMP[i] in list:


    ##获取
