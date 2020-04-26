from common.train_add import Trainadd

import time,unittest
from parameterized import parameterized

from util.service import Service
from util.utility import Utility
test_config_info=Utility.get_json('..\\config\\testdata.conf')
train_tel_blank=Utility.get_excel_to_tuple(test_config_info[8])
train_tel_verify=Utility.get_excel_to_tuple(test_config_info[9])

class TrainAddTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=Service.get_driver('..\\config\\base.conf')
        self.train=Trainadd(self.driver)
    #测试手机号为空
    @parameterized.expand(train_tel_blank)
    @unittest.skip
    def test_add_blank(self,cus_name,cus_status,cus_grade,cus_source,expect):
        self.train.add_tel_blank(cus_name,cus_status,cus_grade,cus_source)
        time.sleep(3)
        try:
            add_message=self.train.message()
            if add_message=='新增成功.':
                actual='pass'
            else:
                actual='fail'
        except:
            actual='fail'
        finally:
            time.sleep(2)
            self.train.close_add()
        self.assertEqual(actual,expect)
    @parameterized.expand(train_tel_verify)
    def test_add_cus(self,cus_phone,cus_name,cus_status,cus_grade,cus_source,expect):

        self.train.add_tel_verify(cus_phone,cus_name,cus_status,cus_grade,cus_source)
        time.sleep(3)
        try:
            add_message=self.train.message()
            if add_message == '新增成功.':
                actual = 'pass'
            else:
                actual = 'fail'
        except:
            actual = 'fail'
        finally:
            time.sleep(2)
            self.train.close_add()
        self.assertEqual(actual, expect)


    def tearDown(self) -> None:
        self.driver.close()
if __name__ == '__main__':
    unittest.main(verbosity=2)