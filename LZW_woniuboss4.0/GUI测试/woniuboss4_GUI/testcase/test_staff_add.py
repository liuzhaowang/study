#!/usr/bin/python3
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------------------------
# @Author  : WANG
# @FileName: test_staff_add.py
# @Software: PyCharm
# @Time    : 2020/4/26
#---------------------------------------------------------------------------------------

from woniuboss4_GUI.common.login import Login
from woniuboss4_GUI.common.staff_add import Staffadd
import time,unittest
from parameterized import parameterized

from woniuboss4_GUI.util.service import Service
from woniuboss4_GUI.util.utility import Utility
test_config_info=Utility.get_json('..\\config\\testdata.conf')
train_add_info=Utility.get_excel_to_tuple(test_config_info[10])

class TrainAddTest(unittest.TestCase):
    def setUp(self) -> None:
        test_base_info=Utility.get_json('..\\config\\base.conf')
        self.driver=Service.get_driver('..\\config\\base.conf')
        self.staff=Staffadd(self.driver)
        self.staff.click_train_source()


    @parameterized.expand(train_add_info)
    def test_add_cus(self,cus_zone,cus_section,cus_job,cus_name,cus_phone,cus_jobnum,expect):

        self.staff.add_tel_verify(cus_zone,cus_section,cus_job,cus_name,cus_phone,cus_jobnum)
        time.sleep(3)
        try:
            add_message=self.staff.message()
            if add_message == '新增员工成功.':
                actual = 'pass'
            else:
                actual = 'fail'
        except:
            actual = 'fail'
        self.assertEqual(actual, expect)

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)