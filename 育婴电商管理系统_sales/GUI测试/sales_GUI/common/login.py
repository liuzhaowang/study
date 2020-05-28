# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         login
# Description:  
# Author:       Administrator
# Date:         2020/2/10
#-------------------------------------------------------------------------------
from guitest.woniusales_test03.util.service import Service

class Login:

	def __init__(self,driver):
		self.driver = driver

	# 向用户名输入框输入内容
	def input_uname(self,username):
		uname = self.driver.find_element_by_id('username')
		Service.send_input(uname,username)

	# 向密码框输入密码
	def input_upass(self,password):
		upass = self.driver.find_element_by_id('password')
		Service.send_input(upass,password)

	# 向验证码框输入验证码
	def input_vfcode(self,verifycode):
		vfcode = self.driver.find_element_by_id('verifycode')
		Service.send_input(vfcode,verifycode)

	# 点击登录按钮
	def click_button(self):
		self.driver.find_element_by_css_selector('button.form-control').click()

	# 将以上的动作进行组织，形成整体的登录操作,参数login_data是字典
	def do_login(self,base_config_path,login_data):

		Service.open_page(self.driver,base_config_path)
		self.input_uname(login_data['username'])
		self.input_upass(login_data['password'])
		self.input_vfcode(login_data['verifycode'])
		self.click_button()
