# -*- coding: UTF-8 -*-
'''=================================================
@FileName：test_market
@Author：Administrator
@Date  ：2020/4/20 
@Desc  ：
=================================================='''
from woniuboss2.interface_test.lib.market import Market
from woniuboss2.interface_test.tools.utility import Utility


class MarketTest:

    def __init__(self,data_config_path):
        self.data_config_info=Utility.get_json(data_config_path)

    def test_market_query(self):
        query_info=Utility.get_excel_to_dict(self.data_config_info[1])
        for info in query_info:
            query_url=info['URL']
            query_data=info['DATA']

            query_resp=Market().market_query(query_url,query_data)
            query_resp_content=query_resp.text

            flag=Utility.assert_equals(query_resp_content,info['CONTENT'])
            if flag:
                print("market_query test ok")
            else:
                print('market_query test fail')

    def test_market_addnet(self):
        add_info=Utility.get_excel_to_dict(self.data_config_info[2])
        for info in add_info:
            add_url=info['URL']
            add_data=info['DATA']

            add_resp=Market().market_query(add_url,add_data)
            add_resp_content=add_resp.text

            flag=Utility.assert_equals(add_resp_content,info['CONTENT'])
            if flag:
                print("market_addnet test ok")
            else:
                print('market_addnet test fail')




if __name__ == '__main__':

    # MarketTest('../conf/testdata.conf').test_market_query()
    MarketTest('../conf/testdata.conf').test_market_addnet()