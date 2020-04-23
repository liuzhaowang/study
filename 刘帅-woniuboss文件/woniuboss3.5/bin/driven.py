
import unittest

from scripts.login import Login
from tools.utility import Utility

import time

class LoginTest:

	def __init__(self,driver):
		self.driver = driver

	# 参数中的path指测试数据所在的配置文件和路径
	def test_login(self,base_config_path,data_config_path):
		# 思路：1.获取测试数据；2.遍历执行每一条测试数据得到运行结果；
		# 3.实际结果actual与预期结果进行对比，如果一直证明测试通过，否则测试不通过提交缺陷
		# 获取所有的登录用到的测试数据及预期结果
		data_config_info = Utility.get_json(data_config_path)
		login_info = Utility.get_excel(data_config_info[0])

		for login_data in login_info:


			Login(self.driver).do_login(base_config_path,login_data)
			# 判断登录是否成功,同时得到实际结果actual
			from selenium.webdriver.common.by import By
			from tools.service import Service
			if Service.is_element_present(self.driver, By.LINK_TEXT, '注销'):
				actual = 'login-pass'
				self.driver.find_element_by_link_text('注销').click()
				time.sleep(2)
			else:
				actual = 'login-fail'
				time.sleep(2)
				self.driver.refresh()

			# 对结果进行断言
			flag = Utility.assert_equals(actual,login_data['expect'])
			if flag:
				print('test pass')
			else:
				print('test fail')

if __name__ == '__main__':

	from selenium import webdriver
	driver = webdriver.Firefox()
	driver.get('http://localhost:8080/WoniuBoss/login')
	LoginTest().test_login(driver,'..\\conf\\testdata.conf')
