
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select


class WoniuBoss:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:8080/WoniuBoss4.0/login')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        uname = self.driver.find_element_by_name('userName')
        uname.clear()
        uname.send_keys('WNCD000')

        upass = self.driver.find_element_by_name('userPass')
        upass.clear()
        upass.send_keys('woniu123')

        self.driver.find_element_by_css_selector('.btn').click()
        time.sleep(2)
        login_name = self.driver.find_element_by_class_name('welcome').text
        if login_name == '成都 . 研发部 . 超级管理员':
            print('登录成功')
        else:
            print('登录失败')
        time.sleep(2)
    def addStaff(self):
        self.driver.find_element_by_link_text('人事管理').click()
        self.driver.find_element_by_link_text('员工信息').click()
        self.driver.find_element_by_css_selector('button.btn-padding:nth-child(1)').click()
        self.driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > select:nth-child(2)').send_keys('上海')
        self.driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > select:nth-child(2)').send_keys('就业部')
        self.driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > input:nth-child(2)').send_keys('测试工程师')
        self.driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(2)').send_keys('王若愚')
        self.driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > select:nth-child(2)').send_keys('男')
        self.driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > input:nth-child(2)').send_keys('13877779999')
        self.driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > input:nth-child(2)').send_keys('952724861')
        self.driver.find_element_by_css_selector('#addEmp-form > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > select:nth-child(2)').send_keys('大专')
        self.driver.find_element_by_css_selector('#addEmpBtn').click()
        time.sleep(3)
        result = self.driver.find_element_by_xpath('/html/body/div[16]/div/div/div[2]/div').text
        time.sleep(3)
        if result == '新增员工成功':
            print('添加员工信息成功')
        else:
            print('添加员工信息失败')
        print(result)
        self.driver.find_element_by_css_selector('.bootbox > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)').click()






if __name__ == '__main__':
    W= WoniuBoss()
    W.addStaff()