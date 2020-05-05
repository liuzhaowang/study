import unittest
from parameterized import parameterized
from util.utility import Utility
from common.train_public import TrainPublic
from util.service import Service
test_config_data=Utility.get_json('..\\config\\testdata.conf')
test_claim_one=Utility.get_excel_to_tuple(test_config_data[16])

test_claim_all=Utility.get_excel_to_tuple(test_config_data[17])

class PublicTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=Service.get_driver('..\\config\\base.conf')
        self.public=TrainPublic(self.driver)

    @parameterized.expand(test_claim_one)
    def test_do_claim_one(self,worker,expect):
        self.public.do_claim_one(worker)
        message=self.public.get_result()
        if '成功'in message:
            actual='pass'
        else:
            actual='fail'
        self.assertEqual(actual,expect)

    @parameterized.expand(test_claim_all)
    def test_do_claim_all(self, worker, expect):
        self.public.do_claim_all(worker)
        message = self.public.get_result()
        if '成功' in message:
            actual = 'pass'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)