from selenium import webdriver
import time

class WoniuBoss:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:8080/WoniuBoss4.0/login')
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
    def test_login(self,username,password,verifycode):
        uname = self.driver.find_element_by_name('userName')
        uname.clear()
        uname.send_keys(username)

        upass = self.driver.find_element_by_name('userPass')
        upass.clear()
        upass.send_keys(password)

        vcode = self.driver.find_element_by_name('checkcode')
        vcode.clear()
        vcode.send_keys(verifycode)

        self.driver.find_element_by_css_selector('.btn').click()
        time.sleep(2)
        try:
            login_name = self.driver.find_element_by_class_name('welcome').text
            if login_name == '成都 . 研发部 . 超级管理员':
                print('登录成功')
            else:
                print('登录失败')
            time.sleep(2)
            self.driver.find_element_by_link_text('[注销]').click()
            time.sleep(2)
            self.driver.close()
        except:
            print('登录失败')
            self.driver.close()



if __name__ == '__main__':
    W= WoniuBoss()
    W.test_login('WNCD000', 'woniu123', '0000')

    W = WoniuBoss()
    W.test_login('WNCD110', 'woniu123', '0000')

    W = WoniuBoss()
    W.test_login('WNCD000', 'woniu1234', '0000')

    W = WoniuBoss()
    W.test_login('WNCD000', 'woniu123', 'ABCD')