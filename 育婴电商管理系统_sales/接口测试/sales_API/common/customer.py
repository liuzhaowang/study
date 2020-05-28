# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         customer
# Description:  
# Author:       Administrator
# Date:         2020/2/20
#-------------------------------------------------------------------------------

import requests
class Customer:

	def __init__(self):
		from interfacetest.woniusales_test01.util.service import Service
		self.session = Service.get_session()


	def add_customer(self,add_customer_url,add_customer_data):
		return self.session.post(add_customer_url,add_customer_data)

	# 对于带有分页功能的查询，返回的是json格式
	def query_customer(self,query_customer_url,query_customer_data):
		query_customer_result = []
		page_num = 1
		while 1:
			result = self.session.post(query_customer_url, {'customerphone':query_customer_data['customerphone'],'page':str(page_num)})
			result_json = result.json()
			if len(result_json) == 0:
				break
			else:
				for r in result_json:
					query_customer_result.append(r)
				page_num += 1
		return query_customer_result

	def edit_customer(self,edit_customer_url,edit_customer_data):
		return self.session.post(edit_customer_url,edit_customer_data)

if __name__ == '__main__':
	c = Customer()
	result = c.query_customer('http://192.168.1.4:8080/WoniuSales/customer/search',{'customerphone':'34','page':'1'})
	print(len(result))
