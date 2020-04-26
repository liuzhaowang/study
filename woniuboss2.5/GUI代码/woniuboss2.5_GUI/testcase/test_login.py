from common.login import Login
from util.service import Service
import unittest
from  parameterized import parameterized
import time

from util.utility import Utility

test_config_info=Utility.get_json('..\\config\\testdata.conf')
login_info =Utility.get_excel_to_tuple(test_config_info[0])

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=Service.get_driver('..\\config\\base.conf')
        cls.login=Login(cls.driver)

    @parameterized.expand(login_info)
    def test_login(self,uname,upass,vfcode,expect):
        data={'username':uname,'password':upass,'verfifycode':vfcode}
        self.login.do_login('..\\config\\base.conf',data)
        from selenium.webdriver.common.by import By
        if Service.is_element_present(self.driver,By.LINK_TEXT,'注销'):
            actual='pass'
            self.driver.find_element_by_link_text('注销').click()
        else:
            actual = 'fail'
            self.driver.refresh()
        self.assertEqual(actual,expect)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    test_config_info = Utility.get_json('..\\config\\testdata.conf')
    login_info = Utility.get_excel_to_tuple(test_config_info[0])
    print(login_info)
    unittest.main(verbosity=2)