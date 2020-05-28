# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/4 22:02 
# @Author : lifei
# @desc:
import random

from woniucbt.common.utility import Utility
class CustomerTest:
    def __init__(self):
        pass

    def main_test(self):
        self.test_add_customer()
        self.test_edit_customer()

    def test_add_customer(self):
        list = self.read_customer_data()
        for item in list:
            data = {'customername':item['customername'],'customerphone':item['customerphone'],
                    'childsex':item['childsex'],'childdate':item['childdate'],
                    'creditkids':item['creditkids'],'creditcloth':item['creditcloth']}
            resp = Utility.get_session().post('http://127.0.0.1:8080/WoniuSales-20180508-V1.4-bin/customer/add', data=data)
            # print('test_add_customer 参数',data)
            self.write_result('新增会员',item['expectresult'],resp.text)

    def test_edit_customer(self):
        rand_phone = random.randrange(10000000,99999999)
        data = Utility.build_dict('customerid=1&customerphone=18%d&customername='
                                  '某人&childsex=男&childdate=2015-12-31'
                                  '&creditkids=500&creditcloth=516750' % rand_phone)
        resp = Utility.get_session().\
            post('http://127.0.0.1:8080/WoniuSales-20180508-V1.4-bin/customer/edit',data)
        self.write_result('修改会员','edit-successful',resp.text)

    def write_result(self,case,expect,actual):
        Utility.assert_result('会员管理','接口测试',case,expect,actual)


    def read_customer_data(self):
        path = '../data/customer.csv'
        with open(path, encoding='utf-8') as f:
            temp_list = f.readlines()
        column = temp_list[0].strip().split(',')
        list = []
        for i in range(1, len(temp_list)):
            dict = {}
            temp = temp_list[i].strip().split(',')
            for j in range(len(column)):
                dict[column[j]] = temp[j]
                # print()
            list.append(dict)
        return list


