#!/usr/bin/env python
# @Time : 2020/4/4 17:36 
# @Author : lifei
# @desc:
from woniucbt.object.login import LoginObject
from woniucbt.common.utility import Utility as util
class LoginTest:
    def __init__(self):
        self.login_object = LoginObject()

    def main_test(self):
        self.test_login_http()
        self.test_login_gui()

    def test_login_gui(self):
        login_list = self.read_login_data()
        for login in login_list:
            self.login_object.do_login(login['username'], login['password'])
            try:
                self.login_object.driver.find_element_by_link_text('注销')
                # print('登录成功')
                util.assert_result_2('登录模块','GUI','测试基本登录功能','成功')
            except:
                util.assert_result_2('登录模块','GUI','测试基本登录功能','失败')

    def test_login_http(self):
        login = self.read_login_data()[0]
        data = {'username':login['username'],'password':login['password'],'verifycode':'0000'}
        resp = util.get_session().post('http://127.0.0.1:8080/WoniuSales-20180508-V1.4-bin/user/login',data)
        util.assert_result('登录测试','接口测试','基本登录功能测试','login-pass',resp.text)


    def read_login_data(self):
        login_list =[]
        with open('../data/login.csv') as file:
            line_list = file.readlines()
        for i in  range(1,len(line_list)):
            username = line_list[i].strip().split(',')[0]
            password = line_list[i].strip().split(',')[1]
            dict = {}
            dict['username'] = username
            dict['password'] = password
            login_list.append(dict)
        return login_list

