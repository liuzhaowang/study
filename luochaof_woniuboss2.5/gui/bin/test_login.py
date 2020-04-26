
# -*- coding: utf-8 -*-#

# 该模块封装与登录相关的测试
import unittest
from parameterized import parameterized

# 获取登录用的测试信息
from woniuboss2.gui.lib.login import Login
from woniuboss2.gui.tools.service import Service
from woniuboss2.gui.tools.utility import Utility

test_config_info = Utility.get_json('..\\conf\\testdata.conf')
login_info = Utility.get_excel_to_tuple(test_config_info[0])

# 思路：1.获取测试数据；2.执行每条数据；
# 3.实际结果actual与预期结果进行对比，如果一直证明测试通过，否则测试不通过提交缺陷
# 获取所有的登录用到的测试数据及预期结果
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Service.get_driver('..\\conf\\base.conf')
        cls.login = Login(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @parameterized.expand(login_info)
    def test_login(self, uname, upass, expect):
        # 将参数重新组织成字典
        login_data = {'username': uname, 'password': upass}
        self.login.do_login('..\\conf\\base.conf', login_data)
        from selenium.webdriver.common.by import By
        if Service.is_element_present(self.driver, By.LINK_TEXT, '注销'):
            actual = 'successful'
            self.driver.find_element_by_link_text('注销').click()
        else:
            err_UNmsg=self.login.get_UNfail_info()
            if '找不到该用户名' in err_msg:
                actual='user_invalid'
            elif '密码输入错误' in err_msg:
                actual='password_invalid'
            elif '用户名不能为空' in err_msg:
                actual='user_invalid'
            else:
                actual='fail'

            self.driver.refresh()
        self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)
