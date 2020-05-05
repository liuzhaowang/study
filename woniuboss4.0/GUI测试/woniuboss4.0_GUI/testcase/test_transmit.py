import unittest
from parameterized import parameterized
from common.train_transmit import TrainTransmit
from util.service import Service
from util.utility import Utility
test_config_info=Utility.get_json('..\\config\\testdata.conf')
query_data=Utility.get_excel_to_tuple(test_config_info[19])
submit_data=Utility.get_excel_to_tuple(test_config_info[20])

class TransmitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=Service.get_driver('..\\config\\base.conf')
        self.transmit=TrainTransmit(self.driver)
    @parameterized.expand(query_data)
    def test_query(self,origion_region,dept,worker,status,source,expect):
        total=self.transmit.do_query(origion_region,dept,worker,status,source)
        if total>0:
            actual='pass'
        else:
            actual='fail'
        self.assertEqual(actual,expect)
    @parameterized.expand(submit_data)
    def test_do_submit(self,cus_region,user_dept,user_name,cus_status,cus_source,region_name,dept_name,worker_name,expect):
        total=self.transmit.do_submit(cus_region,user_dept,user_name,cus_status,cus_source,region_name,dept_name,worker_name)
        if total==1:
            actual='pass'
        else:
            actual='fail'

        self.assertEqual(actual,expect)


    def tearDown(self) -> None:
        self.driver.quit()



if __name__ == '__main__':
    unittest.main(verbosity=2)

