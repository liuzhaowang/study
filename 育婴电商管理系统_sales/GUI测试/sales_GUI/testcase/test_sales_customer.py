import unittest
import time
from parameterized import parameterized
from selenium.webdriver.common.by import By
from guitest.woniusales_test03.util.service import Service
from guitest.woniusales_test03.util.utility import Utility
test_config_info=Utility.get_json('..\\config\\testdata.conf')
customer_info=Utility.get_excel_to_tuple(test_config_info[6])

class SalesCustomerTest(unittest.TestCase):

    def setUp(self):
        self.driver = Service.get_driver('..\\config\\base.conf')
        from guitest.woniusales_test03.common.sales import Sales
        self.sales=Sales(self.driver,'..\\config\\base.conf')

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    @parameterized.expand(customer_info)
    def test_query_customer(self,customerphone,expect):
        self.sales.query_customer_info(customerphone)
        sql = 'SELECT credittotal FROM customer WHERE customerphone="%s"' % customerphone
        credittotal = Utility.query_one('..\\config\\base.conf', sql)[0]
        ele_credittotal_v = self.driver.find_element_by_id('oldcredit').get_attribute('value')
        if credittotal == int(ele_credittotal_v):
            actual = 'query_success'

        else:
            actual = 'query_fail'

            print('credittotal', credittotal)
        self.assertEqual(actual, expect)