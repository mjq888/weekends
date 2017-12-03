import unittest
from selenium import webdriver
import time

class MemberTest(unittest.TestCase):
    #self. 变量是类的属性，可以被所有的方法访问
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
      #  self.driver.maximize_window()
    def tearDown(self):
        #close,是关闭一个浏览器标签，quit是关闭浏览器
        #代码编写和调试的时候需要quit方法前加一个时间等待
        #正式运行是去掉时间功能，因为编写代码的时候需要看清楚执行过程。运行时为了提供程序执行速度。
       time.sleep(20)
       self.driver.quit()
    def test_addmerber(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("userpass").send_keys("password")
        driver.find_element_by_name("userverify").send_keys("1234")
        driver.find_element_by_name("userverify").submit()
        time.sleep(5)
        driver.find_element_by_link_text("会员管理").click()
        time.sleep(5)
        driver.find_element_by_link_text("添加会员").click()
        driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("username").send_keys("abddddfd")
        driver.find_element_by_name("mobile_phone").send_keys("13711141231")
        driver.find_element_by_css_selector('#xb[value="1"]').click()
        date = driver.find_element_by_id("date")
        driver.execute_script('arguments[0].removeAttribute("readonly")',date)
        date.clear()
        date.send_keys("1980-10-21")
        driver.find_element_by_name("email").send_keys("4481000@qq.com")
        driver.find_element_by_name("email").submit()









