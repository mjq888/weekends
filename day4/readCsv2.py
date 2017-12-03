#刚才readCsv不能被其他测试用例调用,应该封装在到一个方法里
#每个测试用例的路径,不同,所以path应该作为参数传入进来
#打开文件,没有关闭,可能会造成内存泄露
import csv
import os

def read(file_name):

    #重复的代码,是设计不合理,应该封装在同一个方法里
    current_file_path = os.path.dirname(__file__)
    path = current_file_path.replace("day4", "data/")+file_name
    #file = open(path,'r')
    #with语句是一个代码库,代码块中的内容都要缩进4个控制
    #with语句可以自动关闭with中的声明的变量file
    #因为一旦文件被关闭,所以单独声明一个列表来保存里面的数据
    result = []
    with open(path,"r") as file:
        data_table =csv.reader(file)
        for row in data_table:
            result.append(row)
    return result


    #如果在打卡和关闭程序的中间发生了异常,导致后面的代码不能正常运行
    #应该用with as语句实现文件的关闭

if __name__ == '__main__':
    member_info = read("member.csv")
    for row in member_info:
     print(member_info)
    #path=r"C:\Users\51Testing\PycharmProjects\weekend8\data\member.csv"
    #这个路径是绝对路径,一个项目不是一个人
    #没有统一要求大家都把项目代码放在一个路径下,
    #通过当前代码位置,找到csv的相对位置,
    #操作系统,path路径,dir是目录direction
    #__ 是python内置变量,指的是当前文件
    #print(current_file_path )
    #csv文件路径
    #print(path)
   # read(path)
     #如何通过使用多出来的数据,驱动测试.应该把数据作为方法的返回值,方便进入一步调用.