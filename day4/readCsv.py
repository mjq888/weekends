#首先准备一个CvsWWENJ
#导入csv包,python语言内置的包,说明常用selenium
import csv
#存放路径
#前面加r,表示没有转义字号的存在,\ 不看作转义符( /  \\_
path = r"C:\Users\51Testing\PycharmProjects\weekend8\data\member.csv"
#通过路径打开问文件
file= open(path,'r')
#通过csv的代码库,读取csv文件
data_table = csv.reader(file)
print(data_table)
#通过data_table分别打印每一行
#for row in data_table:
#    print(row)



