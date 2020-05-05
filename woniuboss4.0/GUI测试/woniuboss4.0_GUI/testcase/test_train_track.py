import unittest

from parameterized import parameterized
from common.train_track import TrainTrack
from util.service import Service
from util.utility import Utility
import time
test_config_info=Utility.get_json('..\\config\\testdata.conf')
track_info=Utility.get_excel_to_tuple(test_config_info[10])
track_info_public=Utility.get_excel_to_tuple(test_config_info[11])
track_info_student=Utility.get_excel_to_tuple(test_config_info[12])

class TraintrackTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=Service.get_driver('..\\config\\base.conf')
        self.track=TrainTrack(self.driver)

    @parameterized.expand(track_info)
    @unittest.skip
    def test_track(self,keyw,cus_status,cus_pri,cus_time,cus_remark,expect):
        self.track.ts.send_keywords(keyw)
        self.track.ts.click_search()
        time1=self.track.get_track_times()
        self.track.do_tracking(cus_status,cus_pri,cus_time,cus_remark)
        self.driver.refresh()
        try:
            self.track.ts.select_pooltype('个人池')
            self.track.ts.send_keywords(keyw)
            time.sleep(2)
            self.track.ts.click_search()

            time.sleep(2)
            time2=self.track.get_track_times()
            times=int(time2)-int(time1)

            if times==1:
                actual='pass'
            else:
                actual='fail'
        except:
            actual='fail'

        self.assertEqual(actual,expect)

    @parameterized.expand(track_info_public)
    def test_track_public(self, keyw, cus_status, cus_pri, cus_time, cus_remark, expect):
        self.track.ts.send_keywords(keyw)
        self.track.ts.click_search()
        self.track.do_tracking_public(keyw,cus_status,cus_pri,cus_time,cus_remark)
        try:
            if self.track.present_student():

               actual = 'pass'
            else:
                actual = 'fail'
        except:
                actual = 'fail'

        self.assertEqual(actual, expect)

    @parameterized.expand(track_info_student)
    def test_track_student(self,keywards,status,priority,next_tracking,
                           tracking_content,cus_class_no,cus_payable,cus_deposit,cus_payment,cus_account,time_data,pool,expect):
        self.track.study_class(keywards,status,priority,next_tracking,
                           tracking_content,cus_class_no,cus_payable,cus_deposit,cus_payment,cus_account,time_data)
        time.sleep(1)
        self.track.student_source_query(pool,keywards)
        time.sleep(2)
        try:
            if self.track.present_student():
                actual='pass'
            else:
                actual='fail'
                time.sleep(1)
                self.driver.refresh()
        except:
            actual='fail'
        self.assertEqual(actual,expect)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)