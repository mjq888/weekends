import os

from selenium import webdriver
from day5 import myTestCase

from day5.myTestCase import MyTestCase
class ZhuCeTest(MyTestCase):
    '''注册模块测试用例'''
    def test_zhu_ce(self):
        #3个单引号表示文档字符串,会显示在文档中
        """注册模块正常测试用例"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        actual = driver.title
        expect = "用户注册 - 道e坊商城 - Powered by Haidao"

        basepath = os.path.dirname(__file__)
        path= basepath.replace("day5","result/image/")
        driver.get_screenshot_as_file(path+"zhuce.png")
        self.assertEquals(actual, expect)
        print("用户名:mjq6")