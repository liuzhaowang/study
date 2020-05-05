import time
import unittest

from parameterized import parameterized

from common.train_abandon import TrainAbadon
from util.service import Service
from util.utility import Utility

test_config_info=Utility.get_json('..\\config\\testdata.conf')
abandon_test_info=Utility.get_excel_to_tuple(test_config_info[13])

class AbandonTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=Service.get_driver('..\\config\\base.conf')
        self.abandon=TrainAbadon(self.driver)
    @parameterized.expand(abandon_test_info)
    def test_abandon(self,cus_keyw,expect):

        self.abandon.ts.send_keywords(cus_keyw)
        self.abandon.ts.click_search()
        self.abandon.do_abandon(cus_keyw)
        self.abandon.click_public()
        time.sleep(2)
        try:
            abandon_time=self.abandon.query_abandon_time()
            if len(abandon_time)>3:
                actual='pass'
            else:
                actual='fail'
        except:
            actual='fail'
        self.assertEqual(actual,expect)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)