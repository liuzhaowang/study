# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         test_customer
# Description:  
# Author:       Administrator
# Date:         2020/2/20
#-------------------------------------------------------------------------------
from interfacetest.woniusales_test01.common.customer import Customer
from interfacetest.woniusales_test01.util.utility import Utility


class CustomerTest:

	def __init__(self,data_config_path):
		self.customer = Customer()
		self.data_config_info = Utility.get_json(data_config_path)

	def test_add_customer(self):
		add_customer_info = Utility.get_excel_to_dict(self.data_config_info[1])
		for add_info in add_customer_info:
			add_customer_url = add_info['URL']
			add_customer_data = add_info['DATA']

			add_customer_resp = self.customer.add_customer(add_customer_url,add_customer_data)

			# 断言
			flag = Utility.assert_equals(add_customer_resp.text,add_info['CONTENT'])
			if flag:
				print('add customer test pass')
			else:
				print('add customer test fail')

	# 测试查询会员的接口：查询1条，查询0条，查询所有，查询部分
	def test_query_customer(self):
		query_customer_info = Utility.get_excel_to_dict(self.data_config_info[2])
		for query_info in query_customer_info:
			query_customer_url = query_info['URL']
			query_customer_data = query_info['DATA']
			query_customer_content = self.customer.query_customer(query_customer_url,query_customer_data)
			sql_all = 'select count(customerid) from customer'
			all_customer_number = Utility.query_one('..\\config\\base.conf',sql_all)[0]
			phone = query_customer_data['customerphone']
			# sql_part = 'select count(customerid) from customer where customerphone like "%'+phone+'%"'
			sql_part = 'select count(customerid) from customer where customerphone like "%s"'%(phone)
			part_cusomer_number = Utility.query_one('..\\config\\base.conf',sql_part)[0]
			if len(query_customer_content) == 0:
				actual = 'query zero'
			elif len(query_customer_content) == 1:
				actual = 'query one'
			elif len(query_customer_content) == all_customer_number:
				actual = 'query all'
			elif len(query_customer_content) == part_cusomer_number:
				actual = 'query part'
			else:
				actual = 'query error'

			flag = Utility.assert_equals(actual,query_info['CONTENT'])
			if flag:
				print('query customer test pass')
			else:
				print('query customer test fail')


	def test_edit_customer(self):
		pass

if __name__ == '__main__':
	CustomerTest('..\\config\\testdata.conf').test_query_customer()
