

class PersonalCenterPage:
    #网页是基于浏览器打开,所有把浏览器传进来
    #不能把浏览器在页面中创建
    def __init__(self,driver):
        self.driver = driver

    title = "我的会员中心 - 道e坊商城 - Powered by Haidao"
    url = "http://localhost/index.php?m=user&c=index&a=index"
