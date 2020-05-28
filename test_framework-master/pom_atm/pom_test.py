#!/usr/bin/env python
# @Time : 2020/4/3 10:27 
# @Author : lifei
#@desc:
import time

from pom_atm.pom_login import LoginPOM
from pom_atm.pom_sell import SellPOM
from selenium import webdriver
class WoniuSalesTest:
    def __init__(self):
        #保证只有一个实例（单例）
        # self.driver = webdriver.Firefox()
        # self.driver.implicitly_wait(5)
        # self.driver.maximize_window()
        # self.driver.get("http://127.0.0.1:8080/WoniuSales-20180508-V1.4-bin/")
        # self.login = LoginPOM(self.driver)
        # self.sell = SellPOM(self.driver)
        self.login = LoginPOM()
        self.sell = SellPOM()


    def test_login(self):
        self.login.do_login('admin','admin123')
        time.sleep(3)
        try:
            self.login.driver.find_element_by_link_text('注销')
            print('登录成功')
        except:
            print('登录失败')

    def test_sell(self):
        self.sell.do_buy_goods('6955203659750','78')
        self.sell.do_sell('15981218050','1.8')

if __name__ == '__main__':
   wst =  WoniuSalesTest()
   wst.test_login()
   wst.test_sell()