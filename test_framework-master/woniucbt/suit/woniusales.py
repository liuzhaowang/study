#!/usr/bin/env python
# @Time : 2020/4/4 20:23 
# @Author : lifei
# @desc:
from woniucbt.case.login import LoginTest
from woniucbt.case.sell import SellTest
from woniucbt.case.customer import CustomerTest
from woniucbt.common.utility import Utility
from woniucbt.common.reporter import Reporter
class WOniuSalesSuit:
    def start_test(self):
        # login_test = LoginTest()
        # login_test.test_login_gui()
        # login_test.test_login_http()
        #
        # SellTest().test_sell()
        # customer_test = CustomerTest()
        # customer_test.test_add_customer()
        # customer_test.test_edit_customer()

        # 在不同的模块的case里边实现高内聚,在suit层调用模块级用例实现低耦合
        Utility.version = Utility.get_config_value('ci','version')
        LoginTest().main_test()
        SellTest().main_test()
        CustomerTest().main_test()
        Reporter().generate_report(Utility.version)

if __name__ == '__main__':
    WOniuSalesSuit().start_test()
