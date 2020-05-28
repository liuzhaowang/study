#!/usr/bin/env python
# @Time : 2020/4/4 18:17 
# @Author : lifei
# @desc: 数据库的操作
import pymysql
from pymysql.cursors import SSDictCursor
from woniucbt.common.utility import Utility as util
class DataBase:
    def __init__(self):
        self.conn = pymysql.connect(util.get_config_value('db','host'),util.get_config_value('db','user'),util.get_config_value('db','pass'),util.get_config_value('db','dbname'),charset='utf8')
        self.cursor = self.conn.cursor(cursor=SSDictCursor)

    def querry_all(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def querry_one(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result


