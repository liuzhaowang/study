#coding=gbk
from tools.service import Service
from selenium import webdriver

class Login:
    #初始化driver
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:8080/WoniuBoss/login')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)


    # 向用户名输入框输入内容
    def input_uname(self, username):
        uname = self.driver.find_element_by_name('userName')
        uname.clear()
        uname.send_keys(username)

    # 向密码框输入密码
    def input_upass(self, password):
        upass = self.driver.find_element_by_name('userPass')
        upass.clear()
        upass.send_keys(password)

    # 向验证码框输入验证码
    def input_vfcode(self, verifycode):
        vfcode = self.driver.find_element_by_name('checkcode')
        vfcode.clear()
        vfcode.send_keys(verifycode)

    # 点击登录按钮
    def click_button(self):
        self.driver.find_element_by_css_selector('.btn').click()

    # 将以上的动作进行组织，形成整体的登录操作,参数login_data是字典
    def do_login(self):
        self.input_uname('WNCD056')
        self.input_upass('woniu123')
        self.input_vfcode('0000')
        self.click_button()
if __name__ == '__main__':
    L=Login()
    L.do_login()