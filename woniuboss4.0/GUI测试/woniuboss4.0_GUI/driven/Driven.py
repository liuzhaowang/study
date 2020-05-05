import unittest

from util.utility import Utility


class Driven_woniuboss:
    def start(self):
        from HTMLTestRunner import HTMLTestRunner
        ts=unittest.TestSuite()
        loader=unittest.TestLoader()
        testcases_name=Utility.trans_str('..\\config\\test.conf')
        tests=loader.loadTestsFromNames(testcases_name)
        ts.addTests(tests)
        import time
        ctime=time.strftime('%Y%m%d_%H%M%S',time.localtime())
        with open('..\\report\\%s_report.html'%(ctime),'w')as file:
            runner=HTMLTestRunner(stream=file,verbosity=2)
            runner.run(ts)



if __name__ == '__main__':
    Driven_woniuboss().start()
