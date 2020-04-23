from selenium import webdriver
import time,unittest,HTMLTestRunner,os


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:8080/WoniuBoss/login')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def test_login1(self):
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
        self.driver.find_element_by_link_text('领用登记').click()
        time.sleep(3)
        print('测试成功')

    def test_login2(self):
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
        #获取登录成功的截图
    def get_png(self):
        png_path = os.path.join(os.getcwd(),'report/screenshot')
        self.driver.get_screenshot_as_file(login_pass)
        self.driver.find_element_by_link_text('领用登记').click()
        time.sleep(3)
        print('测试成功')


    def tearDown(self):
        self.driver.close()

# def suite():
#     suite = unittest.TestSuite()
#     tset1=Login.test_login1()
#     tset2=Login.test_login2()
#     suiteTest.addTests([tset1,test2])
#     with open('D:\\report.html','wb') as file:
#         runner = HTMLTestRunner.HTMLTestRunner(stream=file,verbosity=2)
#         runner.run(suite)
if __name__ == '__main__':
    unittest.main(verbosity=2)