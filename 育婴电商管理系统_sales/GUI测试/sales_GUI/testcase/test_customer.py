import time
import unittest
from guitest.woniusales_test03.util.utility import Utility
from guitest.woniusales_test03.util.service import Service
from parameterized import parameterized
from selenium.webdriver.common.by import By

test_config_info=Utility.get_json('..\\config\\testdata.conf')
add_customer_info=Utility.get_excel_to_tuple(test_config_info[1])

class CustomerTest(unittest.TestCase):

    def setUp(self):
        self.driver = Service.get_driver('..\\config\\base.conf')
        from guitest.woniusales_test03.common.customer import Customer
        self.customer=Customer(self.driver)


    def tearDown(self):
        self.driver.quit()

    @parameterized.expand(add_customer_info)
    def test_add_customer(self,cname,cphone,cdata,ckids,ccloth,expect):
        add_customer_data={'customername':cname,'customerphone':cphone,
                           'childdate':cdata,'creditkids':ckids,
                           'creditcloth':ccloth}

        sql='select count(customerid) from customer'
        old_customer_count=Utility.query_one('..\\config\\base.conf',sql)
        self.customer.add_customer('..\\config\\base.conf',add_customer_data)

        if Service.is_element_present(self.driver, By.CSS_SELECTOR,
                                      '.modal-sm > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)'):
            time.sleep(2)
            # 用于获取弹出页面的文本内容
            content = self.driver.find_element_by_css_selector('.bootbox-body').text
            if '请勿重复添加' in content:
                actual = 'already-added'
            else:
                actual = 'add-failed'
        else:
            # 判断customer表中的记录数是否增加
            new_customer_count = Utility.query_one('..\\config\\base.conf', sql)
            if new_customer_count[0] - old_customer_count[0] == 1:
                actual = 'add-successful'
            else:
                actual = 'add-failed'

        self.assertEqual(actual,expect)






