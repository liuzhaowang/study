# -*- coding: UTF-8 -*-
'''=================================================
@FileName：market
@Author：Administrator
@Date  ：2020/4/16
@Desc  ：
=================================================='''

import  requests

from woniuboss4_API.tools.service import Service


class Market:

    def __init__(self):
        self.session=Service.get_session()

    def market_query(self,query_url,query_data):
        return self.session.post(query_url,query_data)

    def market_addnet(self,add_url,add_data):
        return self.session.post(add_url,add_data)

    def market_upload(self):
        pass
