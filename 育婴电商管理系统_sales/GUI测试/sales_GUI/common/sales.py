# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         sales
# Description:  
# Author:       Administrator
# Date:         2020/2/11
#-------------------------------------------------------------------------------
import time

from guitest.woniusales_test03.util.service import Service


class Sales:

	def __init__(self,driver,base_config_path):
		self.driver = driver
		Service.miss_login(self.driver, base_config_path)
		self.driver.find_element_by_link_text('销售出库').click()

	# 扫描或输入条码
	def input_barcode(self,barcode):
		barcode_ele = self.driver.find_element_by_id('barcode')
		Service.send_input(barcode_ele,barcode)

	# 点击条码的确定按钮
	def click_barcode_button(self):
		self.driver.find_element_by_css_selector('.glyphicon-ok').click()

	# 执行条码扫描或输入并确定
	def scan_barcode(self,barcode):
		time.sleep(2)
		self.input_barcode(barcode)
		self.click_barcode_button()

	# 移除操作
	def remove_goods(self,barcode):
		self.scan_barcode(barcode)
		time.sleep(2)
		self.driver.find_element_by_link_text('移除').click()

	# 输入电话号码
	def  input_phone(self,customerphone):
		phone_ele = self.driver.find_element_by_id('customerphone')
		Service.send_input(phone_ele,customerphone)

	# 点击查询电话号码
	def click_phone_button(self):
		self.driver.find_element_by_css_selector('button.form-control:nth-child(4)').click()

	# 查询会员信息操作
	def query_customer_info(self,customerphone):
		self.input_phone(customerphone)
		self.click_phone_button()






