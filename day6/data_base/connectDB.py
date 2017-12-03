
# 导入pymysql代码库
import pymysql

def connDb():
    #要想连接数据,需要值得数据库的哪些信息
    #ip ,端口号,用户名密码
    conn = pymysql.Connect(host="127.0.0.1", user="root", password="root",
                 database="pirate", port=3306,charset="utf8")
    sql ="select * from hd_user order by id desc"

    #通过连接执行sql语句首先要获得数据库的游标cursor
    curs = conn.cursor()
    #通过游标来执行sql数据
    curs.execute(sql)
    #获取最新的一条记录
    #把数据库结果倒叙排列,然后用fecthone()方法获取第一天记录
    result = curs.fetchone()

    return result

if __name__ == '__main__':
     print(connDb())


