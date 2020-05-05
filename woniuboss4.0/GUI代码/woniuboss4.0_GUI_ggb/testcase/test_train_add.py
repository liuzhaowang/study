from common.login import Login
from common.train_add import Trainadd
import time,unittest
from parameterized import parameterized

from util.service import Service
from util.utility import Utility
test_config_info=Utility.get_json('..\\config\\testdata.conf')
train_add_info=Utility.get_excel_to_tuple(test_config_info[8])

class TrainAddTest(unittest.TestCase):
    def setUp(self) -> None:
        test_base_info=Utility.get_json('..\\config\\base.conf')
        self.driver=Service.get_driver('..\\config\\base.conf')
        self.train=Trainadd(self.driver)
        self.train.click_train_source()

    #测试手机号为空
    @parameterized.expand(train_add_info)
    def test_add_cus(self,cus_phone,cus_name,cus_sex,cus_status,cus_grade,cus_source,experience,expect):

        self.train.add_tel_verify(cus_phone,cus_name,cus_sex,cus_status,cus_grade,cus_source,experience)
        time.sleep(3)
        try:
            add_message=self.train.message()
            if add_message == '新增成功.':
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