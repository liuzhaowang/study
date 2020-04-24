#!/usr/bin/python3
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------------------------
# @Author  : WANG
# @FileName: test_training.py
# @Software: PyCharm
# @Time    : 2020/4/5
#---------------------------------------------------------------------------------------

import unittest
from parameterized import parameterized
from woniuboss.tools.util import Utility
from woniuboss.lib.training import Tran
train_data=Utility.get_json('..\\config\\testAPI.conf')
query_message_info=Utility.get_excel_to_tuple(train_data[0])
query_resume_info=Utility.get_excel_to_tuple(train_data[1])
Track_resources_info=Utility.get_excel_to_tuple(train_data[2])
Modify_information_info=Utility.get_excel_to_tuple(train_data[3])
add_information_info=Utility.get_excel_to_tuple(train_data[4])
Waste_resources_info=Utility.get_excel_to_tuple(train_data[5])
transfer_query_info=Utility.get_excel_to_tuple(train_data[6])
transfer_view_info=Utility.get_excel_to_tuple(train_data[7])
transfer_commit_info=Utility.get_excel_to_tuple(train_data[8])
distribution_query_info=Utility.get_excel_to_tuple(train_data[9])
Proportionate_distribution_info=Utility.get_excel_to_tuple(train_data[10])
Public_query_info=Utility.get_excel_to_tuple(train_data[11])
Public_claim_info=Utility.get_excel_to_tuple(train_data[12])
class test_train(unittest.TestCase):
    def setUp(self):
        self.train = Tran(0)
    #搜索功能
    @parameterized.expand(query_message_info)
    def test_query_message(self,URL,DATA,CONTENT):
        query_message_url=URL
        query_message_data=DATA
        resp=self.train.query_message(query_message_url,query_message_data)
        #断言
        self.assertEqual(resp.json(),CONTENT)

    @parameterized.expand(query_resume_info)
    def test_query_resume(self, URL, DATA, CONTENT):
        query_resume_url=URL
        query_resume_data=DATA
        resp=self.train.query_resume(query_resume_url,query_resume_data)
        #断言
        self.assertEqual(resp.json(),CONTENT)

    @parameterized.expand(Track_resources_info)
    def test_Track_resources(self, URL, DATA, CONTENT):
        Track_resources_url=URL
        Track_resources_data=DATA
        resp=self.train.Track_resources(Track_resources_url,Track_resources_data)
        #断言
        self.assertEqual(resp.text,CONTENT)

    @parameterized.expand(Modify_information_info)
    def test_Modify_information(self, URL, DATA, CONTENT):
        Modify_information_url=URL
        Modify_information_data=DATA
        resp=self.train.Modify_information(Modify_information_url,Modify_information_data)
        #断言
        self.assertEqual(resp.text,CONTENT)

    @parameterized.expand(add_information_info)
    def test_add_information(self, URL, DATA, CONTENT):
        add_information_url=URL
        add_information_data=DATA
        resp=self.train.add_information(add_information_url,add_information_data)
        #断言
        self.assertEqual(resp.text,CONTENT)

    @parameterized.expand(Waste_resources_info)
    def test_Waste_resources(self, URL, DATA, CONTENT):
        Waste_resources_url=URL
        Waste_resources_data=DATA
        resp=self.train.Waste_resources(Waste_resources_url,Waste_resources_data)
        #断言
        self.assertEqual(resp.text,CONTENT)

    @parameterized.expand(transfer_query_info)
    def test_transfer_query(self, URL, DATA, CONTENT):
        transfer_query_url=URL
        transfer_query_data=DATA
        resp=self.train.transfer_query(transfer_query_url,transfer_query_data)
        #断言
        self.assertEqual(resp.json(),CONTENT)

    @parameterized.expand(transfer_view_info)
    def test_transfer_view(self, URL, DATA, CONTENT):
        transfer_view_url=URL
        transfer_view_data=DATA
        resp=self.train.transfer_view(transfer_view_url,transfer_view_data)
        #断言
        self.assertEqual(resp.json(),CONTENT)

    @parameterized.expand(transfer_commit_info)
    def test_transfer_commit(self, URL, DATA, CONTENT):
        transfer_commit_url=URL
        transfer_commit_data=DATA
        resp=self.train.transfer_commit(transfer_commit_url,transfer_commit_data)
        #断言
        self.assertEqual(resp.text,CONTENT)

    @parameterized.expand(distribution_query_info)
    def test_distribution_query(self, URL, DATA, CONTENT):
        distribution_query_url = URL
        distribution_query_data = DATA
        resp = self.train.distribution_query(distribution_query_url, distribution_query_data)
        # 断言
        self.assertEqual(resp.json(), CONTENT)

    @parameterized.expand(Proportionate_distribution_info)
    def test_Proportionate_distribution(self, URL, DATA, CONTENT):
        Proportionate_distribution_url = URL
        Proportionate_distribution_data = DATA
        resp = self.train.Proportionate_distribution(Proportionate_distribution_url, Proportionate_distribution_data)
        # 断言
        self.assertEqual(resp.json(), CONTENT)

    @parameterized.expand(Public_query_info)
    def test_Public_query(self, URL, DATA, CONTENT):
        Public_query_url=URL
        Public_query_data=DATA
        resp=self.train.Public_query(Public_query_url,Public_query_data)
        #断言
        self.assertEqual(resp.json(),CONTENT)

    @parameterized.expand(Public_claim_info)
    def test_Public_claim(self, URL, DATA, CONTENT):
        Public_claim_url=URL
        Public_claim_data=DATA
        resp=self.train.Public_claim(Public_claim_url,Public_claim_data)
        #断言
        self.assertEqual(resp.text,CONTENT)


if __name__ == '__main__':
    unittest.main(verbosity=2)