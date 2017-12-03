from selenium.webdriver.common.by import By

class LoginPage:
    #构造方法的作用
    #实例化LoginPage对象的时候,drvie
    def __init__(self,driver):
        self.driver = driver

    title ="用户登录 - 道e坊商城 - Powered by Haidao"
    url= "http://localhost/index.php?m=user&c=public&a=login"
    #小括号表示元组,元组中有两个值,第一个元素是控件的定位方式,第二个是元素的值
    username_input_loc = (By.ID,"username")
    password_input_loc = (By.ID, "password")
    loginbtn = (By.CLASS_NAME,"login_btn")

    def open(self):
        self.driver.get(self.url)
    def input_username(self,username):
        self.driver.find_element(*self.username_input_loc).send_keys(username)
    def input_password(self,password):
        self.driver.find_element(*self.password_input_loc).send_keys(password)
    def login(self):
        self.driver.find_element(*self.loginbtn).click()

