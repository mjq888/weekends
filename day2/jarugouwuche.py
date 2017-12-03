import time
from select import select

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://localhost/")
#在登录点击按钮之前,需要删除target属性
login_link = driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()
driver.find_element_by_id("username").send_keys("mmmm")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("username").submit()
driver.find_element_by_link_text("进入商城购物").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
#iphone_img = "body > div.w1170.catalogue > div > div.catalogue-pro > div > a > img"
iphone_link = " div.shop_01-imgbox > a "
iphone = driver.find_element_by_css_selector(iphone_link)
print(iphone)
driver.execute_script("arguments[0].removeAttribute('target')",iphone)
iphone.click()
driver.find_element_by_id("joinCarButton").click()
pay = "div.shopCar_T > span.shopCar_T_span3"
payjs = driver.find_element_by_css_selector(pay)
payjs.click()
js = " div:nth-child(3) > a"
driver.find_element_by_css_selector(js).click()
driver.find_element_by_class_name("add-address").click()
driver.find_element_by_name("address[address_name]").send_keys("mujiaqin")
driver.find_element_by_name("address[mobile]").send_keys("13718995421")
#driver.find_element_by_css_selector("[value='230000']").click()
#driver.find_element_by_css_selector("[value='230100']").click()
#driver.find_element_by_css_selector("[value='230103']").click()
#driver.find_element_by_name("address[address]").send_keys("丽都饭")
#driver.find_element_by_name("address[zipcode]").send_keys("100000")
sheng = driver.find_elements_by_tag_name("select")[0]
Select(sheng).select_by_visible_text("黑龙江")
shi = driver.find_elements_by_tag_name("select")[1]
Select(shi).select_by_value("230600")
qu = driver.find_elements_by_tag_name("select")[2]
Select(qu).select_by_index(3)
driver.find_element_by_name("address[address]").send_keys("丽都饭")
driver.find_element_by_name("address[zipcode]").send_keys("100000")
driver.find_element_by_class_name("aui_state_highlight").click()








