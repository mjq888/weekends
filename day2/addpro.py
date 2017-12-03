from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_name("userpass").submit()
driver.find_element_by_link_text("商品管理").click()
driver.find_element_by_link_text("添加商品").click()
driver.switch_to.frame("mainFrame")
driver.find_element_by_name("name").send_keys("iphonex")
#在一个页面中嵌套多个页面,看起来是一个面.
driver.find_element_by_xpath("//*[@id='1']").click()
driver.find_element_by_id("2").click()
driver.find_element_by_id("6").click()
a=driver.find_element_by_id("7")

#driver.find_element_by_css_selector('//*[@id="jiafen"]').click()
ActionChains(driver).double_click(a).perform()
#driver.find_element_by_id("jiafen").click()
brand = driver.find_element_by_name("brand_id")
Select(brand).select_by_index(1)
brand.submit()

driver.find_elements_by_link_text("商品列表").click()
