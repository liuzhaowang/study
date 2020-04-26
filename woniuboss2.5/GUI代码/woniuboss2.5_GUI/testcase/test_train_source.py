from common.train_source import TrainSource
import unittest,time
from parameterized import parameterized
from util.service import Service
from util.utility import Utility


test_config_info = Utility.get_json('..\\config\\testdata.conf')
train_info=Utility.get_excel_to_tuple(test_config_info[1])
train_worker=Utility.get_excel_to_tuple(test_config_info[2])
train_status=Utility.get_excel_to_tuple(test_config_info[3])
train_source=Utility.get_excel_to_tuple(test_config_info[4])
train_time=Utility.get_excel_to_tuple(test_config_info[5])
train_keywords=Utility.get_excel_to_tuple(test_config_info[6])
train_whole=Utility.get_excel_to_tuple(test_config_info[7])

class TrainsourceTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver=Service.get_driver('..\\config\\base.conf')
        self.train=TrainSource(self.driver)

    @parameterized.expand(train_info)
    @unittest.skip
    def test_train_query_pool(self,pool,expect):
        self.train.select_pooltype(pool)
        total_number=self.train.total_info()
        if pool=='临时池':
            db_pool='temp'
        elif pool=='公共池':
            db_pool='public'
        elif pool=='个人池':
            db_pool = 'private'
        elif pool=='学生池':
            db_pool = 'student'
        elif pool=='全部':
            db_pool='""or 1=1'
        else:
            db_pool=0
        sql='select count(*)as total from customer where pool_type="%s"'%(db_pool)
        result=Utility().db_query_dict('..\\config\\base.conf',sql)[0]['total']
        if int(total_number)==result:
            actual='pass'
        else:
            actual='fail'

        self.assertEqual(actual,expect)


    @parameterized.expand(train_worker)
    @unittest.skip
    def test_train_query_worker(self,worker_name,expect):
        self.driver.refresh()
        time.sleep(3)
        self.train.select_worker(worker_name)
        total_number = self.train.total_info()
        sql = 'SELECT COUNT(*)AS total FROM customer a,employee b WHERE a.work_id=b.work_id AND b.employee_name="%s" AND pool_type NOT IN ("public")'% worker_name
        result = Utility().db_query_dict('..\\config\\base.conf', sql)[0]['total']
        if int(total_number) == result:
            actual = 'pass'
        else:
            actual = 'fail'

        self.assertEqual(actual, expect)

    @parameterized.expand(train_status)
    @unittest.skip
    def test_train_query_status(self,status, expect):
        self.driver.refresh()
        time.sleep(3)
        self.train.select_status(status)
        total_number = self.train.total_info()
        sql = 'SELECT COUNT(*)AS total FROM customer WHERE last_status="%s"AND pool_type NOT IN ("public")' % status
        result = Utility().db_query_dict('..\\config\\base.conf', sql)[0]['total']
        if int(total_number) == result:
            actual = 'pass'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)
    @parameterized.expand(train_source)
    @unittest.skip
    def test_train_query_source(self,source_name,expect):

        self.train.select_source(source_name)
        total_number=self.train.total_info()
        sql='SELECT COUNT(*)total FROM customer WHERE source="%s" AND pool_type NOT IN ("public")'%source_name
        result=Utility.db_query_dict('..\\config\\base.conf',sql)[0]['total']
        if result==int(total_number):
            actual='pass'
        else:
            actual='fail'
        self.assertEqual(actual,expect)
    @parameterized.expand(train_time)
    @unittest.skip
    def test_train_query_time(self,stime,etime,expect):
        self.train.send_start_time(stime)
        self.train.send_end_time(etime)
        self.train.click_search()
        try:
            total_number=self.train.total_info()

            if int(total_number)>=1:
                actual='pass'
            else:
                actual='fail'
                self.driver.refresh()
        except:
            actual='fail'
        self.assertEqual(actual,expect)
    @parameterized.expand(train_keywords)
    @unittest.skip
    def test_train_query_keywords(self,keywords,expect):
        self.train.send_keywords(keywords)
        self.train.click_search()
        try:
            total_number=self.train.total_info()
            if int(total_number) >= 1:
                actual = 'pass'
            else:
                actual = 'fail'
                self.driver.refresh()
        except:
            actual = 'fail'
        self.assertEqual(actual, expect)
    @parameterized.expand(train_whole)
    def test_train_query_whole(self,pool,worker,status,source,expect):
        self.train.select_pooltype(pool)
        self.train.select_worker(worker)
        self.train.select_status(status)
        self.train.select_source(source)

        try:
            total_number = self.train.total_info()
            if int(total_number) >= 1:
                actual = 'pass'
            else:
                actual = 'fail'
                self.driver.refresh()
        except:
            actual = 'fail'
        self.assertEqual(actual, expect)



    def tearDown(self) -> None:
        self.driver.close()



if __name__ == '__main__':
   unittest.main(verbosity=2)



