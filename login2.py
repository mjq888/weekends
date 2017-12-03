from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost")
driver.find_element_by_link_text("登录").click()
cwh=driver.current_window_handle
cws=driver.window_handles
for item in cws:
    if item==cwh:
        #pass
       driver.close() #关闭当前标签
    else:
        driver.switch_to_window(item)

driver.find_element_by_id("username").send_keys("mjq")
driver.find_element_by_id("password").send_keys("1234567")
driver.find_element_by_class_name("login_btn").click()
#打开浏览器
#点击登录连接
#输入用户名
#点击登录按钮

