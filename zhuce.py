#打开浏览器
from selenium import webdriver
#操作浏览器 用代码来操作浏览器
driver = webdriver.Chrome()
driver.get("http://localhost/")
driver.find_element_by_link_text("注册").click()
cwh=driver.current_window_handle
cws=driver.window_handles
for item in cws:
    if item==cwh:
        #pass
       driver.close() #关闭当前标签
    else:
        driver.switch_to_window(item)
driver.find_element_by_name("username").send_keys("mjqxyziihh")
driver.find_element_by_name("password").send_keys("1234567")
driver.find_element_by_name("userpassword2").send_keys("1234567")
driver.find_element_by_name("mobile_phone").send_keys("13811918085")
driver.find_element_by_name("email").send_keys("4481330@qq.com")
driver.find_element_by_class_name("reg_btn").click()
js='document.getElementsByClassName("site-nav-right fr")[0].childNodes[3].removeAttribute("target") '
driver.execute_script(js)
