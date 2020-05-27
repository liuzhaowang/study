# -*- coding: utf-8 -*-#

import unittest


class Driven:

    def start(self):
        from HTMLTestRunner import HTMLTestRunner
        ts = unittest.TestSuite()
        loader = unittest.TestLoader()

        from woniuboss4_API.tools.utility import Utility
        testcase_names = Utility.trans_str('..\\conf\\test.conf')
        print(testcase_names)
        tests = loader.loadTestsFromNames(testcase_names)
        ts.addTests(tests)
        # 测试报告文件名称的格式为：xxxx-xx-xx_xx_xx_xx_report.html
        import time
        ctime = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
        with open('..\\logs\\%s_report.html' % (ctime), 'w') as file:
            runner = HTMLTestRunner(stream=file, verbosity=2)
            runner.run(ts)


if __name__ == '__main__':
    Driven().start()

