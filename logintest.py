#打开浏览器
from selenium import webdriver
#操作浏览器 用代码来操作浏览器
driver = webdriver.Chrome()
driver.get("http://localhost/")
js = 'document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")'
#username
driver.execute_script(js)
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id("username").send_keys("mmmm")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_class_name("login_btn").click()
driver.find_element_by_link_text("进入商城购物")
