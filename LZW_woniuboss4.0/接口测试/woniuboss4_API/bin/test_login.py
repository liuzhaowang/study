# -*- coding: UTF-8 -*-
from woniuboss4_API.tools.utility import Utility
import unittest

class LoginTest:

    def __init__(self,path):
        self.data_config_info=Utility.get_json(path)

    def test_login(self):
        login_info=Utility.get_excel_to_dict(self.data_config_info[0])
        #print(login_info)
        for info in login_info:
            login_url=info['URL']
            login_data=info['DATA']

            from woniuboss4_API.lib.login import Login
            login_resp=Login().do_login(login_url,login_data)
            print(login_resp)
            #print(login_resp.text)
            login_resp_content=login_resp.text
            #print(login_resp_content)
            flag=Utility.assert_equals(login_resp_content,info['CONTENT'])
            if flag:
                print("login test ok")
            else:
                print('login test fail')


if __name__ == '__main__':

    LoginTest('../conf/testdata.conf').test_login()
