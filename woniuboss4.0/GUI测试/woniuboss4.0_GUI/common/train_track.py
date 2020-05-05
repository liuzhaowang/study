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
        jsValue = 'document.getElementById("next_time").value="%s"'%time_data
        self.driver.execute_script(jsValue)

    def remark(self,value):
        remark=self.driver.find_element_by_xpath("//form[@id='formFollow']/div[2]/div/textarea")
        Service.send_input(remark,value)

    def save(self):
        self.driver.find_element_by_id('saveTrackingBtn').click()

    def get_track_times(self):
        track_times=self.driver.find_element_by_xpath('//table[@id="personal-table"]/tbody/tr[1]/td[8]').text
        return track_times

    def close_track(self):
        self.driver.find_element_by_xpath('/html/body/div[13]/div/div/div/div[1]/button/span[1]').click()



    def public_info_query(self):
        abandon_time=self.driver.find_element_by_xpath('//table[@id="public-pool-table"]/tbody/tr[1]/td[14]').text
        return abandon_time

    def student_source_query(self,pool,keyw):
        self.ts.select_pooltype(pool)
        self.ts.send_keywords(keyw)
        self.ts.click_search()
    def present_student(self):
        pst=Service.is_element_present(self.driver,By.XPATH,'/html/body/div[8]/div[3]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]')
        return pst
    def send_public_keywords(self,keyw):
        key=self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/input')
        Service.send_input(key,keyw)


    def click_public_search(self):
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/button').click()

    def do_tracking(self,cus_status,cus_pri,cus_next_tracking,cus_remark):
        self.click_tracking()
        self.select_status(cus_status)
        self.select_priority(cus_pri)
        self.track_time(cus_next_tracking)
        self.remark(cus_remark)
        self.save()
        self.close_track()
    def public_source_query(self,keyw):
        self.driver.find_element_by_link_text('公共资源').click()
        time.sleep(2)
        self.send_public_keywords(keyw)
        self.click_public_search()

    def do_tracking_public(self,keyw,cus_status,cus_pri,cus_next_tracking,cus_remark):
        self.do_tracking(cus_status,cus_pri,cus_next_tracking,cus_remark)
        self.public_source_query(keyw)


    def study_class(self,keyw,cus_status,cus_pri,cus_next_tracking,cus_remark,cus_class_no,cus_payable,cus_deposit,cus_payment,cus_account,time_data):
        self.ts.send_keywords(keyw)
        self.ts.click_search()
        self.click_tracking()
        self.select_status(cus_status)
        self.select_priority(cus_pri)
        self.track_time(cus_next_tracking)
        self.remark(cus_remark)

        if Service.wait_present(self.driver,By.ID,'panel-element-enroll'):

            class_no =self.driver.find_element_by_xpath('//div[@id="panel-element-enroll"]/div/div/div[1]/div[1]/select')
            payable = self.driver.find_element_by_xpath('//div[@id="panel-element-enroll"]/div/div/div[1]/div[2]/select')
            deposit = self.driver.find_element_by_xpath('//div[@id="panel-element-enroll"]/div/div/div[1]/div[3]/select')
            payment = self.driver.find_element_by_xpath('//div[@id="panel-element-enroll"]/div/div/div[2]/div[1]/select')
            account = self.driver.find_element_by_xpath('//div[@id="panel-element-enroll"]/div/div/div[2]/div[2]/select')
            payment_time='document.getElementsByName("trade_time")[0].value="%s"'%time_data

            # jsValue = 'document.getElementById("next_time").value="%s"' % time_data
            self.driver.execute_script(payment_time)
            Service.select_by_name(class_no,cus_class_no)
            Service.select_by_name(payable,cus_payable)
            Service.select_by_name(deposit,cus_deposit)
            Service.select_by_name(payment,cus_payment)
            Service.select_by_name(account,cus_account)
            self.save()
            self.driver.refresh()




if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    a=TrainTrack(driver)
