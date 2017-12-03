from selenium import  webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/")
js='document.getElementsByClassName("site-nav-right fr")[0].childNodes[3].removeAttribute("target") '
driver.find_element_by_link_text("登录").click()
#从浏览器中所有窗口排查第一个窗口.
#把selenium 切换到第c二个窗口
cwh=driver.current_window_handle
whs=driver.window_handles
for item in whs:
    if item==cwh:
        driver.close()
    else:
        driver.switch_to_window(item)
driver.find_element_by_id("username").send_keys("mjq")
driver.find_element_by_id("password").send_keys("1234567")
driver.find_element_by_class_name("login_btn").click()

