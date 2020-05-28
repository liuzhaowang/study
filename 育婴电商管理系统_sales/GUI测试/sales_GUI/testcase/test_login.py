# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         test_login
# Description:  
# Author:       Administrator
# Date:         2020/2/10
#-------------------------------------------------------------------------------

# 该模块封装与登录相关的测试
from guitest.woniusales_test03.common.login import Login
from guitest.woniusales_test03.util.service import Service
from guitest.woniusales_test03.util.utility import Utility
import time,unittest
from parameterized import parameterized

test_config_info=Utility.get_json('..\\config\\testdata.conf')
login_info=Utility.get_excel_to_tuple(test_config_info[0])

class LoginTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = Service.get_driver('..\\config\\base.conf')
		cls.login = Login(cls.driver)

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	def setUp(self):
		pass
		#self.driver=Service.get_driver('..\\config\\base.conf')
		#self.login=Login(self.driver)

	def tearDown(self):
		pass
		#self.driver.quit()

	@parameterized.expand(login_info)
	def test_login(self,uname,upass,vfcode,expect):

		login_data={'username':uname,'password':upass,'verifycode':vfcode}
		self.login.do_login('..\\config\\base.conf',login_data)
		from selenium.webdriver.common.by import By
		if Service.is_element_present(self.driver,By.LINK_TEXT,'注销'):
			actual='login-pass'
			self.driver.find_element_by_link_text('注销').click()
		else:
			actual='login-fail'
			self.driver.refresh()
		self.assertEqual(actual,expect)


if __name__ == '__main__':
	unittest.main(verbosity=2)

