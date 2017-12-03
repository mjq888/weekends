import unittest
import ddt
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from day4.readCsv2 import read

@ddt.ddt
class MemberManageTest(unittest.TestCase):
    #调用之前的read方法,获取配置文件中数据,memberinfo
    member=read("member.csv")

    # 在当前类只执行一次
    @classmethod
    def setUpClass(cls):
        print("所有方法之前,执行一次")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
      #  cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(20)
        cls.driver.quit()

    def testa_log_in(self):
        print("登录测试 ")
        driver = self.driver
        driver.get("http://localhost/admin.php")
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB).send_keys("1234").send_keys(Keys.ENTER).perform()
    @ddt.data(*member)
    def testb_add_member(self,row):
        #每组测试用例都是独立,不应该用for循环,上个执行失败,导致下一个不能执行,用DDT装饰器,修饰这个方法.
        #for row in read("member.csv"): 4.注释FOR循环
        print("添加会员")
        driver = self.driver
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        # driver.switch_to.frame("mainFrame")
        # 如果frame没有name属性时, 我们可以通过其他方式定位iframe标签, 把定位好的页面元素传给driver.switch_to.frame(iframe_html)方法也可以实现frame切换
        iframe_css = "#mainFrame"
        iframe_html =driver.find_element_by_css_selector(iframe_css)
        driver.switch_to.frame(iframe_html)
        driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("mobile_phone").send_keys(row[1])
        driver.find_element_by_css_selector('[value="{0}"]'.format(row[2])).click()
        driver.find_element_by_id("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        driver.find_element_by_class_name("button_search").submit()
        sj = driver.find_element_by_css_selector("#datagrid-row-r1-2-0 > td:nth-child(1) > div").text
        ex = row[0]
        driver.switch_to.default_content()
        time.sleep(10)
        self.assertEquals(sj, ex)



if __name__ == '__main__':
    unittest.main()







