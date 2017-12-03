import os
import  unittest

import time
from selenium import webdriver

class DengluTest(unittest.TestCase):
    '''登录模块测试用例'''
    def setUp(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        #驱动和浏览器版本匹配才能窗口最大化
        #driver.
    def tearDown(self):
        time.sleep(10)
        self.driver.quit()

    def test_denglu(self):
        """登录测试正常情况"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").send_keys("mjq6")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_class_name("login_btn").click()
        basepath = os.path.dirname(__file__)
        path = basepath.replace("day5", "result/image/")
        driver.get_screenshot_as_file(path + "denglu.png")
        print("用户名:mjq6")


