import  unittest

from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase

class ZhuceTest(MyTestCase)
    def test_zhu_ce(self):
        driver =self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element_by_name("username").send_keys("mjq8")
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("userpassword2").send_keys("123456")
        driver.find_element_by_name("")

