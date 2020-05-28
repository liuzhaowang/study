import unittest
import time
from parameterized import parameterized
from selenium.webdriver.common.by import By
from guitest.woniusales_test03.util.service import Service
from guitest.woniusales_test03.util.utility import Utility
test_config_info=Utility.get_json('..\\config\\testdata.conf')
scan_barcode_info=Utility.get_excel_to_tuple(test_config_info[4])

class SalesTest(unittest.TestCase):

    def setUp(self):
        self.driver = Service.get_driver('..\\config\\base.conf')
        from guitest.woniusales_test03.common.sales import Sales
        self.sales=Sales(self.driver,'..\\config\\base.conf')

    def tearDown(self):
        self.driver.quit()

    @parameterized.expand(scan_barcode_info)
    def test_scan_barcode(self,barcode,expect):

        self.sales.scan_barcode(barcode)
        time.sleep(2)
        if Service.is_element_present(self.driver, By.LINK_TEXT, '移除'):
            actual = 'scan_successful'
        else:
            actual = 'scan_fail'
        self.assertEqual(actual,expect)

