import time

from selenium.webdriver.common.by import By

from common.train_source import TrainSource
from util.service import Service


class TrainTrack:
    def __init__(self,driver):
        self.driver=driver
        self.ts=TrainSource(self.driver)
        self.ts.click_train_source()

    def click_tracking(self):
        time.sleep(1)
        self.driver.find_element_by_xpath('//table[@id="personal-table"]/tbody/tr[1]/td[15]/button[1]').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('跟踪资源').click()
    def select_status(self,status_name):
        status=self.driver.find_element_by_id('newStatus')
        Service.select_by_name(status,status_name)
    def select_priority(self,priority_name):
        priority=self.driver.find_element_by_xpath('//form[@id="formFollow"]/div/div[2]/select')
        Service.select_by_name(priority,priority_name)
    def track_time(self,time_data):
        # time=self.driver.find_element_by_xpath('//form[@id="formFollow"]/div/div[3]/div/input')
        time=self.driver.find_element_by_id('next_time')
        # js ="document.getElementById('next_time').setAttribute('readOnly','true')"
        # self.driver.execute_script(js)
        jsValue = 'document.getElementById("next_time").value="2019-11-12"'

        driver.execute_script(jsValue)
    def remark(self,value):
        remark=self.driver.find_element_by_xpath("//form[@id='formFollow']/div[2]/div/textarea")
        Service.send_input(remark,value)

    def save(self):
        self.driver.find_element_by_id('saveTrackingBtn').click()

    def get_track_times(self):
        track_times=self.driver.find_element_by_xpath('//table[@id="personal-table"]/tbody/tr[1]/td[8]').text
        return track_times

    def close_track(self):
        self.driver.find_element_by_xpath('//div[@id="follow"]/div/div/div/div/button/span').click()

    def do_tracking(self,keyw,cus_status,cus_pri,cus_next_tracking,cus_remark):
        self.ts.send_keywords(keyw)
        self.ts.click_search()
        self.click_tracking()
        self.select_status(cus_status)
        self.select_priority(cus_pri)
        self.track_time(cus_next_tracking)
        self.remark(cus_remark)
        self.save()
        self.close_track()


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    a=TrainTrack(driver)
    a.get_track_times()
    a.click_tracking()
    a.close_track()
    # a.track_time('2020-04-25')
    # a.remark('remark test')
