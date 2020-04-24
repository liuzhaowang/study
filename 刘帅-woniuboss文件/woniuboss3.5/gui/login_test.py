from selenium import webdriver
import time

class Login:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:8080/WoniuBoss/login')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def read_data(self):
        with open('./login_data','r') as file:
            results = file.readlines()
            for result in results:
                result = result.strip().split(',')
                self.username = result[0]
                self.password = result[1]
                self.verifycode = result[2]
                # print(username,password,verifycode)
        return username, password, verifycode

    def do_login(self):
        uname = self.driver.find_element_by_name('userName')
        uname.clear()
        uname.send_keys('WNCD056')

        pword = self.driver.find_element_by_name('userPass')
        pword.clear()
        pword.send_keys('woniu123')

        vcode = self.driver.find_element_by_name('checkcode')
        vcode.clear()
        vcode.send_keys('0000')

        click_button = self.driver.find_element_by_css_selector('.btn').click()
        time.sleep(3)
        #
        self.driver.find_element_by_css_selector('ul.nav:nth-child(1) > li:nth-child(2) > a:nth-child(1)').click()
        print('测试成功')

if __name__ == '__main__':

    Login().do_login()
