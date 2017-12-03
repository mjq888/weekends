import os
import unittest
#html.TestRunner是基于unitest框架的扩展可以从网上下载.但要区分P2,P3
import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText
from lib.HTMLTestRunner import HTMLTestRunner


def send_email(path):
    f = open(path,'rb')
    mail_body = f.read() #读取报告的内容作为正文
    f.close()
    #要发邮件,要把二进制的内容转成mime格式,
    #MIME 多用途多multipurse ,internet mail extension扩展,多用途互联网邮件,邮件协议的扩展,使邮件
    #不仅支持文本格式,还支持多媒体多种格式,比如图片音频二进制文件.
    msg = MIMEText(mail_body,'html','utf-8') #转换格式
    #对于一个邮件来讲,上面是邮件正文,还有要发件人,还有主题,收件人
    msg['Subject']= Header("自动化测试报告",'utf-8')
    msg['From'] = "bwftest126@126.com"
    msg['To']="mujiaqin161@sohu.com"
    #开始发送邮件,连接邮箱服务器,才能登录邮箱
    #登录登录页面
    #要想连接服务器,首先必须搞清楚网络传说协议
    #发邮件的协议有三种,要先查看邮箱支持那种协议,pop3 smtp,imap,126邮箱支持这三种协议
    #输入用户名和密码登录邮箱
    #发送邮件
    #退出邮箱
    #smtp simple mail tran  protocol, smtp协议
    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login("bwftest126@126.com","abc123asd654")
    smtp.sendmail("bwftest126@126.com","mujiaqin161@sohu.com",msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    suit = unittest.defaultTestLoader.discover('./day5',pattern='*Test.py')
    #生成HTML格式的测试报告,
    # 指定报告的路径
    base_path=os.path.dirname(__file__)
    path = base_path + "/result/result"+now+".html"
    file =open(path,'wb')
    HTMLTestRunner(stream=file, title="海盗商城测试报告", description="测试环境 window Server2008+chrome+").run(suit)
    #这是生成的测试报告只能给专业人员开,我们应该把相关的手动测试用例的标题加到我们测试
    #手工测试用例的标题
    print("当前用户名:mjq6")
    file.close()    #把html报告的正文发送给老板
    send_email(path)

