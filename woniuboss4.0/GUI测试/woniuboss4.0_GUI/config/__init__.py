# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         __init__.py
# Description:  
# Author:       Administrator
# Date:         2020/2/11
#-------------------------------------------------------------------------------
from selenium.webdriver.support.select import Select

from util.service import Service
import time
driver=Service.get_driver('..\\config\\base.conf')
time.sleep(4)
Service.miss_login(driver,'..\\config\\base.conf')
from util.utility import Utility
a=Utility.get_json('..\\config\\testdata.conf')[1]
print(a)
b=Utility.get_excel_to_dict(a)
print(b)
t=driver.find_element_by_id('poolSelect')
Select(t).select_by_index(b['select'])
# seleter_length = len(Select(selecter).options)
# import random
# random_index = random.randint(0, seleter_length - 1)
# Select(selecter).select_by_index(random_index)