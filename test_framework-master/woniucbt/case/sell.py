#!/usr/bin/env python
# @Time : 2020/4/4 17:36 
# @Author : lifei
# @desc:
from woniucbt.common.utility import Utility
from woniucbt.object.sell import SellObject
import random
from woniucbt.common.database import DataBase
class SellTest:
    def __init__(self):
        self.sell_object = SellObject()
        self.database = DataBase()
        
    def main_test(self):
        self.test_sell()

    def test_sell(self):
        # 从csv文件中随机读取一个条码
        barcode_list = self.read_sell_barcode()
        barcode = random.choice(barcode_list)
        self.sell_object.do_buy_goods(barcode, '78')
        # 从数据库中随机读取一个电话号码
        phone = self.database.querry_one('SELECT customerphone FROM customer ORDER BY RAND() LIMIT 0,1')
        self.sell_object.do_sell(phone['customerphone'], '1.8')
        #销售完后进行断言,直接从数据库中取值
        sql = "SELECT barcode FROM sell WHERE barcode = '{}' ORDER BY sellid DESC LIMIT 0,1".format(barcode)
        if self.database.querry_one(sql) is None:
            Utility.assert_result_2('销售出库模块','GUI测试','扫码功能测试','失败')
        else:
            Utility.assert_result_2('销售出库模块','GUI测试','扫码功能测试','成功')

    def read_sell_barcode(self):
        barcode_list = []
        with open('../data/barcode.csv') as file:
            line_list = file.readlines()
        for i in range(1,len(line_list)):
            barcode_list.append(line_list[i].strip())

        # print(random.sample(barcode_list,1))#随机取
        return barcode_list



