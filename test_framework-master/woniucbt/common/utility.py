#!/usr/bin/env python
# @Time : 2020/4/4 18:57 
# @Author : lifei
# @desc:
from selenium import webdriver
import time, requests, os
from woniucbt.common.reporter import Reporter
from configparser import ConfigParser

class Utility:
    driver = None
    session = None
    version = ''

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

    @classmethod
    def get_session(cls):
        if cls.session is None:
            cls.session = requests.session()
        return cls.session

    @classmethod
    def write_result_file(cls, case, result):
        path = os.path.abspath('..') + '/result/mytest.txt'
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        line = now + ',' + case + ',' + result + '\n'
        with open(path, 'a+', encoding='utf-8') as f:
            f.write(line)

    @classmethod
    def write_result(cls,module,testtype,casetitle,result):
        reporter = Reporter()
        if result == '失败':
            screenshot = reporter.capture_screen()
        else:
            screenshot = '无'
        testtime = time.strftime('%Y-%m-%d %H:%M:%S')
        reporter.write_report(version=cls.version,module=module,
                              testtype=testtype,casetitle=casetitle,
                              result = result,screenshot=screenshot)


    @classmethod
    def assert_result(cls,module,testtype, case, expect, actual):
        if expect == actual:
            cls.write_result(module,testtype,case, '成功')
        else:
            cls.write_result(module, testtype, case, '失败')

    # GUI
    @classmethod
    def assert_result_2(cls, module, testtype, case,result):
        cls.write_result(module,testtype,case,result)

    # 把一个post请求上下文的key=value&key=value的普通字符串转换为一个字典对象,供request发请求用
    @classmethod
    def build_dict(self, string):
        dict = {}
        list = string.split('&')
        for item in list:
            key = item.split('=')[0]
            value = item.split('=')[1]
            dict[key] = value
        return dict

    @classmethod
    def get_config_value(cls,section,key):
        conf = ConfigParser()
        conf.read('../data/woniusales.conf') #读取当前目录下的配置文件
        return  conf.get(section,key)


if __name__ == '__main__':
    Utility.assert_result('登录','GUI','成功登录','1','2')