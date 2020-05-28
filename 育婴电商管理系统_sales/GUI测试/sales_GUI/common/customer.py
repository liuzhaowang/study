# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         customer
# Description:  
# Author:       Administrator
# Date:         2020/2/10
#-------------------------------------------------------------------------------
from guitest.woniusales_test03.util.service import Service
from selenium import webdriver

class Customer:

	def __init__(self,driver):
		self.driver = driver
	# 输入电话号码
	def input_phone(self,customerphone):
		phone = self.driver.find_element_by_id('customerphone')
		Service.send_input(phone,customerphone)

	# 输入会员昵称
	def input_name(self,customername):
		cname = self.driver.find_element_by_id('customername')
		Service.send_input(cname,customername)

	# 随机选择孩子的性别
	def select_sex(self):
		sex_select = self.driver.find_element_by_id('childsex')
		Service.select_random(sex_select)

	# 向出生日期输入框输入出生日期
	def input_date(self,childdate):
		Service.remove_readonly(self.driver,'childdate')
		childdate_ele = self.driver.find_element_by_id('childdate')
		Service.send_input(childdate_ele,childdate)

	# 输入母婴积分
	def input_creditkids(self,creditkids):
		kids = self.driver.find_element_by_id('creditkids')
		Service.send_input(kids,creditkids)

	# 输入童装积分
	def input_creditcloth(self,creditcloth):
		cloth = self.driver.find_element_by_id('creditcloth')
		Service.send_input(cloth,creditcloth)

	# 点击添加按钮
	def click_add_button(self):
		self.driver.find_element_by_css_selector('button.form-control:nth-child(1)').click()

	# 添加会员动作的组合
	def add_customer(self,base_config_path, add_customer_data):
		driver = self.driver
		Service.miss_login(driver, base_config_path)
		driver.find_element_by_link_text('会员管理').click()
		self.input_phone(add_customer_data['customerphone'])
		self.input_name(add_customer_data['customername'])
		self.select_sex()
		self.input_date( add_customer_data['childdate'])
		self.input_creditkids(add_customer_data['creditkids'])
		self.input_creditcloth(add_customer_data['creditcloth'])
		self.click_add_button()

	# 仅只点击查询按钮
	def click_query_button(self):
		self.driver.find_element_by_css_selector('button.form-control:nth-child(3)').click()

	# 点击查询按钮:由于只有电话号码是查询条件，所以需要输入电话号码后再点击查询按钮
	def query_customer(self,base_config_path,query_customer_data):
		driver = self.driver
		Service.miss_login(driver, base_config_path)
		driver.find_element_by_link_text('会员管理').click()
		self.input_phone(query_customer_data['customerphone'])
		driver.find_element_by_css_selector('button.form-control:nth-child(3)').click()

	# 随机获取列表中的修改链接元素
	def get_random_edit_ele(self,customer_count):
		import random
		self.driver.find_element_by_xpath('//tbody[@id="customerlist"]/tr[%d]/td[11]/a'%(random.randint(1,customer_count))).click()

	# 点击最后的编辑保存按钮
	def click_edit(self):
		self.driver.find_element_by_id('editBtn').click()

	# 随机编辑一条记录
	def edit_customer(self,base_config_path,edit_customer_data):
		# 1.登录；2.打开会员管理页面；3.输入电话号码（为空）,点击查询；4.找到刚才定义的元素
		Service.miss_login(self.driver,base_config_path)
		self.driver.find_element_by_link_text('会员管理').click()
		self.click_query_button()
		# 编写sql，查询符合条件的记录数
		sql = 'select count(customerid) from customer'
		from guitest.woniusales_test02.util.utility import Utility
		customer_count = Utility.query_one(base_config_path,sql)[0]
		self.get_random_edit_ele(customer_count)
		# 将要修改的数据重新填入
		self.input_phone(edit_customer_data['customerphone'])
		self.input_name(edit_customer_data['customername'])
		self.select_sex()
		self.input_date(edit_customer_data['childdate'])
		self.input_creditkids(edit_customer_data['creditkids'])
		self.input_creditcloth(edit_customer_data['creditcloth'])
		self.click_edit()

if __name__ == '__main__':

    driver = webdriver.Firefox()

