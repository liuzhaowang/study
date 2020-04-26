# -*- coding: UTF-8 -*-
from woniuboss2.interface_test.tools.utility import Utility


class LoginTest:

    def __init__(self,data_config_path):
        self.data_config_info=Utility.get_json(data_config_path)

    def test_login(self):
        login_info=Utility.get_excel_to_dict(self.data_config_info[0])
        for info in login_info:
            login_url=info['URL']
            login_data=info['DATA']

            from woniuboss2.interface_test.lib.login import Login
            login_resp=Login().do_login(login_url,login_data)
            login_resp_content=login_resp.text
            flag=Utility.assert_equals(login_resp_content,info['CONTENT'])
            if flag:
                print("login test ok")
            else:
                print('login test fail')


if __name__ == '__main__':

    LoginTest('../conf/testdata.conf').test_login()
