#!/usr/bin/env python
# @Time : 2020/4/3 10:19
# @Author : lifei
#@desc:
import time
from woniucbt.common.utility import Utility
class LoginObject:
    def __init__(self):
        self.driver = Utility.get_webdriver()

    def get_username(self):
        self.driver.find_element_by_id('username')
        return self.driver.find_element_by_id('username')

    def get_password(self):
        self.driver.find_element_by_id('password')
        return self.driver.find_element_by_id('password')

    def get_verifycode(self):
        self.driver.find_element_by_id('verifycode')
        return self.driver.find_element_by_id('verifycode')

    def get_login_button(self):
        return self.driver.find_element_by_xpath('/html/body/div[4]/div/form/div[6]/button')

    # ATM:Action
    def do_login(self,username,password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_verifycode().send_keys('0000')
        self.get_login_button().click()
