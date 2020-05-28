# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/8 21:14 
# @Author : lifei
# @desc: KDT简单操作
from selenium import webdriver
import time,random,os
class KDT:
    def __init__(self):
        self.driver = None

    def start(self):
        with open('keyword.txt') as file:
            line_list = file.readlines()
        for line in line_list:
            key_list = line.strip().split(',')
            operation = key_list[0]
            operation = operation.replace(' ','_')
            # if len(key_list) == 2:
            #     getattr(self,operation)(key_list[1])
            # elif len(key_list) == 3:
            #     getattr(self,operation)(key_list[1],key_list[2])

            args = []
            for i in range(1,len(key_list)):
                args.append(key_list[i])
            getattr(self,operation)(*args)



    def open(self,url,browser):
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
    # *args 避免多穿报错
    def wait(self,timeout,*args):
        time.sleep(int(timeout))

    def input(self,identify,value):
        self.find_element(identify).clear()
        self.find_element(identify).send_keys(value)

    def click(self,identify):
        self.find_element(identify).click()

    def check_exist(self,identify,expect):
        try:
            self.find_element(identify)
            print('测试成功 %s'%identify)
        except:
            print('测试失败 %s'%identify)

    def check_value(self,identify,expect):
        actual = self.find_element(identify).text
        print(actual)
        if actual == expect:
            print('测试成功')
        else:
            print('测试失败 期望结果%s 实际结果:%s'%(expect,actual))



    def find_element(self,identify):
        how = identify.split('=',1)[0]
        what = identify.split('=',1)[1]
        if how == 'id':
            return self.driver.find_element_by_id(what)
        elif how == 'xpath':
            return self.driver.find_element_by_xpath(what)
        elif how == 'link':
            return self.driver.find_element_by_link_text(what)
        elif how == 'class':
            return self.driver.find_elements_by_css_selector(what)

if __name__ == '__main__':
    kdt = KDT()
    kdt.start()