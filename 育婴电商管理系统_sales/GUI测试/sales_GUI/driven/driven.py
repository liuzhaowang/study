import unittest

class Driven:

    def start(self):
        from HTMLTestRunner import HTMLTestRunner
        ts=unittest.TestSuite()
        loader=unittest.TestLoader()
        from guitest.woniusales_test03.util.utility import Utility
        testcases_names=Utility.trans_str('..\\config\\test.conf')
        tests=loader.loadTestsFromNames(testcases_names)
        ts.addTests(tests)
        import time
        ctime = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
        with open('..\\report\\%s_report.html'%(ctime),'w') as file:
            runner=HTMLTestRunner(stream=file,verbosity=2)
            runner.run(ts)


if __name__ == '__main__':
    Driven().start()