import time
from selenium import  webdriver
from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase
from day6.loginPage import LoginPage
from day6.personalCentPage import PersonalCenterPage


class LoginTest(MyTestCase):
    #测试用例维护性比较差,
    def test_login(self):
        #self.driver.get("http://localhost/index.php?m=user&c=public&a=login")
        lp = LoginPage(self.driver) #实例化一个登录页面
    #self.driver.find_element(By.ID,"username").send_keys("mjq6")
    #self.driver.find_element(By.ID,"password").send_keys("123456")
    #self.driver.find_element(By.CLASS_NAME,"login_btn").click()
    #time.sleep(5)
    #self.assertIn("我的会员中心",self.driver.title)
        lp.open()
        lp.input_username("mjq6")
        lp.input_password("123456")
        lp.login()

        pcp = PersonalCenterPage(self.driver)
        time.sleep(5)
        self.assertEqual(pcp.title,pcp.driver.title)
