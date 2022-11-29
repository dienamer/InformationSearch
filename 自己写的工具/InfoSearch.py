import threading
import time

import xlrd
from alive import UrlCheck
from queue import Queue
from collections import  deque

from 自己写的工具.ARL import ARL


class Information(object):
    _URL_=''
    _IP_=''
    _ADDR_=''
    _PORT_=[]
    _SERVICE_=[]
    _SYSTEM_=[]
    _ASSEMBLY_=[]
    _IDENTFI_=''

    @property
    def IP(self):
        return self._IP_

    @property
    def URL(self):
        return self._URL_
    @property
    def ADDR(self):
        return self._ADDR_

    @property
    def PORT(self):
        return self._PORT_

    @property
    def SERVICE(self):
        return self._SERVICE_
    @property
    def SYSTEM(self):
        return self._SYSTEM_
    @property
    def ASSEMBLY(self):
        return self._ASSEMBLY_
    @IP.setter
    def IP(self,value):
        
            if isinstance(value, str):
                self._IP_ = value
            else:
                print("The value to IP is not str!!!!")
    @ADDR.setter
    def ADDR(self, value):
        
            if isinstance(value,str):
                self._ADDR_ = value
            else:
                print("The value to ADDR is not str!!!!")

    @PORT.setter
    def PORT(self, value):
        
            if isinstance(value, list):
                self._PORT_ = value.copy()
            else:
                print("The value to PORT is not list!!!!")

    @SERVICE.setter
    def SERVICE(self, value):
        
            if isinstance(value, list):
                self._SERVICE_ = value.copy()
            else:
                print("The value to SERVICE is not list!!!!")

    @SYSTEM.setter
    def SYSTEM(self, value):
        
            if isinstance(value, list):
                self._SYSTEM_ = value.copy()
            else:
                print("The value to SYSTEM is not list!!!!")

    @ASSEMBLY.setter
    def ASSEMBLY(self, value):
        
            if isinstance(value, list):
                self._ASSEMBLY_ = value.copy()
            else:
                print("The value to ASSEMBLY is not list!!!!")

    @URL.setter
    def URL(self, value):

        if isinstance(value, list   ):
            self._ASSEMBLY_ = value.copy()
        else:
            print("The value to ASSEMBLY is not list!!!!")
# def ARL(file_place):
#     ARL_DATA=xlrd.open_workbook(file_place)
#     ARL_TABLE=ARL_DATA.sheet_by_index(0)
#     ARL_TABLE_ROW=ARL_TABLE.nrows
#     ARL_TABLE_COL=ARL_TABLE.ncols
#     #print(ARL_TABLE_COL)
#     Alive_Url=[]
#     ARL_URL=[str(ARL_TABLE.cell_value(i,0)) for i in range(1,ARL_TABLE_ROW)]
#     ARL_URL_Quene=Queue()
#     for url in ARL_URL:
#         ARL_URL_Quene.put(url)
#     Alive_URL= UrlCheck(ARL_URL_Quene,Alive_Url)
#     Alive_URL.start()
#     ARL_IP=[str(ARL_TABLE.cell_value(i,1)) for i in range(1,ARL_TABLE_ROW)]
#
#     print(ARL_URL)
def PR():
    while(True):
        print('success')
        time.sleep(2)
if __name__=='__main__':
    A=ARL('../arl.xls')
    A.start()