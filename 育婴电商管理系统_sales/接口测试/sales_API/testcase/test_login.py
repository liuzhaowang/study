# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         logintest
# Description:  
# Author:       Administrator
# Date:         2020/2/20
#-------------------------------------------------------------------------------
from interfacetest.woniusales_test01.util.utility import Utility


class LoginTest:

	# 获取测试数据,从测试数据配置文件中读取json
	def __init__(self,data_config_path):

		self.data_config_info = Utility.get_json(data_config_path)

	def test_login(self):
		# 准备数据
		login_info = Utility.get_excel_to_dict(self.data_config_info[0])
		for info in  login_info:
			login_url = info['URL']
			login_data = info['DATA']
			from interfacetest.woniusales_test01.common.login import Login
			login_resp = Login().do_login(login_url,login_data)
			# 获取响应码和响应正文
			# login_resp_code = login_resp.status_code
			#将返回的正文当做预期结果
			login_resp_content = login_resp.text

			# 断言
			flag = Utility.assert_equals(login_resp_content,info['CONTENT'])
			if flag:
				print('login test pass')
			else:
				print('login test fail')


if __name__ == '__main__':
	LoginTest('..\\config\\testdata.conf').test_login()