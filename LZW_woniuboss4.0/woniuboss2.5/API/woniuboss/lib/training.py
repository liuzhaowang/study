#!/usr/bin/python3
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------------------------
# @Author  : WANG
# @FileName: training.py
# @Software: PyCharm
# @Time    : 2020/4/5
#---------------------------------------------------------------------------------------


import requests
from woniuboss.tools.server import Service
class Tran:
    def __init__(self,sum):
        self.session = Service.get_session(sum)
    #搜索功能
    def query_message(self,query_message_url,query_message_data):
        return self.session.post(query_message_url,query_message_data)

    #查看简历
    def query_resume(self,query_resume_url,query_resume_data):
        return self.session.post(query_resume_url,query_resume_data)

    #跟踪资源
    def Track_resources(self,Track_resources_url,Track_resources_data):
        return self.session.post(Track_resources_url,Track_resources_data)

    #修改信息
    def Modify_information(self,Modify_information_url,Modify_information_data):
        return self.session.post(Modify_information_url,Modify_information_data)

    #新增信息
    def add_information(self,add_information_url,add_information_data):
        return self.session.post(add_information_url,add_information_data)

    #废弃资源
    def Waste_resources(self,Waste_resources_url,Waste_resources_data):
        return self.session.post(Waste_resources_url,Waste_resources_data)

    #转交责任人查询
    def transfer_query(self,transfer_query_url,transfer_query_data):
        return self.session.post(transfer_query_url,transfer_query_data)

    #转交查看
    def transfer_view(self,transfer_view_url,transfer_view_data):
        return self.session.post(transfer_view_url,transfer_view_data)

    #转交提交
    def transfer_commit(self,transfer_commit_url,transfer_commit_data):
        return self.session.post(transfer_commit_url,transfer_commit_data)

    #分配查询
    def distribution_query(self,distribution_query_url,distribution_query_data):
        return self.session.post(distribution_query_url,distribution_query_data)

    #按比例分配
    def Proportionate_distribution(self,Proportionate_distribution_url,Proportionate_distribution_data):
        return self.session.post(Proportionate_distribution_url,Proportionate_distribution_data)

    #公共查询
    def Public_query(self,Public_query_url,Public_query_data):
        return self.session.post(Public_query_url,Public_query_data)

    #公共认领
    def Public_claim(self,Public_claim_url,Public_claim_data):
        return self.session.post(Public_claim_url,Public_claim_data)
