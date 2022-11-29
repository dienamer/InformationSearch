import xlrd
data=xlrd.open_workbook('assets_20221122.xls')
table=data.sheet_by_index(0)

row=table.nrows
print(row)

city_list = [str(table.cell_value(i, 11)) for i in range(1, row)]
domain_list=[str(table.cell_value(i, 0)) for i in range(1, row)]
domain=[]
print(domain_list)
with open('url.txt','r') as f:
    domain=f.read().splitlines()
for d in domain:
    str1="http://"+d
    str2="https://"+d
    if  str1 in domain_list:
        print("域名:{0}---->指纹:{1}".format(d,city_list[domain_list.index(str1)]))
    if  str2 in domain_list:
        print("域名:{0}---->指纹:{1}".format(d,city_list[domain_list.index(str2)]))