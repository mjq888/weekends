import  unittest

import time
from selenium import webdriver

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        #驱动和浏览器版本匹配才能窗口最大化

    def tearDown(self):
        time.sleep(20)
        self.driver.quit()