#!/usr/bin/env python
# @Time : 2020/4/4 16:51 
# @Author : lifei
#@desc: 实现实例化
from selenium import webdriver
import time
class Common:
    driver = None #将driver定义为类级变量,不随实例化而被重新赋值

    def __init__(self):
        pass
    @classmethod
    def get_webdriver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Firefox()
            cls.driver.implicitly_wait(10)
            cls.driver.maximize_window()
            cls.driver.get("http://127.0.0.1:8080/WoniuSales-20180508-V1.4-bin/")
            time.sleep(5)
        return cls.driver