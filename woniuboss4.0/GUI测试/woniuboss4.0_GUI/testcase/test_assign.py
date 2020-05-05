import unittest
from common.train_assign import TrainAssign
from util.service import Service
from parameterized import parameterized

from util.utility import Utility

test_config_info=Utility.get_json('..\\config\\testdata.conf')
assign_random=Utility.get_excel_to_tuple(test_config_info[14])
assign_all=Utility.get_excel_to_tuple(test_config_info[15])
class AssignTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=Service.get_driver('..\\config\\base.conf')
        self.assign=TrainAssign(self.driver)
    @parameterized.expand(assign_random)
    def test_assign_to_counselor(self,cus_channel,cus_curriculum,expect):
        result=self.assign.do_assign_to_counselor(cus_channel,cus_curriculum)
        if result==1:
            actual='pass'
        else:
            actual='fail'
        self.assertEqual(actual,expect)
    @parameterized.expand(assign_all)
    def test_assign_all_to_counselor(self,cus_channel,cus_curriculum,expect):
        if self.assign.do_assign_all_to_counselor(cus_channel,cus_curriculum):
            actual='pass'
        else:
            actual='fail'
        self.assertEqual(actual,expect)



    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
