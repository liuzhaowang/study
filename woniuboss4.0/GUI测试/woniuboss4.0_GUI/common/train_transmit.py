import time

import selenium
from selenium.webdriver.common.by import By

from common.login import Login
from util.service import Service
from util.utility import Utility


class TrainTransmit:
    def __init__(self,driver):
        self.driver=driver
        self.login=Login(self.driver).do_login_manager('..\\config\\base.conf')

    def click_transmit(self):
        self.driver.find_element_by_link_text('资源管理').click()
        self.driver.find_element_by_link_text('转交资源').click()

    def select_origin_region(self,cus_region):
        region=self.driver.find_element_by_id('regionSelect1')
        Service.select_by_name(region,cus_region)

    def select_origin_dept(self, user_dept):
        dept = self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[1]/select[2]')
        Service.select_by_name(dept, user_dept)

    def select_origin_emp(self, user_name):
        emp = self.driver.find_element_by_id('empNameSelect1')
        Service.select_by_name(emp, user_name)

    def select_status(self, cus_status):
        status = self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[1]/select[4]')
        Service.select_by_name(status, cus_status)

    def select_source(self, cus_source):
        source = self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[1]/select[5]')
        Service.select_by_name(source, cus_source)
    def input_keywords(self,cus_keyw):
        keyword=self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[1]/input')
        Service.send_input(keyword,cus_keyw)

    def click_search(self):
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[1]/button').click()

    def click_option(self):
        self.driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[1]/div[2]/div[2]/table/tbody/tr/td[1]/input').click()

    def select_transmit_region(self,region_name):
        transmit_region=self.driver.find_element_by_id('regionSelect2')
        Service.select_by_name(transmit_region,region_name)

    def select_transmit_dept(self,dept_name):
        transmit_dept=self.driver.find_element_by_id('deptSelect2')
        Service.select_by_name(transmit_dept,dept_name)

    def select_transmit_worker(self,worker_name):
        transmit_worker=self.driver.find_element_by_id('empNameSelect2')
        Service.select_by_name(transmit_worker,worker_name)
    def click_submit(self):
        submit=self.driver.find_element_by_id('Submit').click()
    def click_confirm(self):
        self.driver.find_element_by_xpath('/html/body/div[10]/div/div/div[3]/button[2]').click()


    def get_total(self):
        total_info=self.driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]').text
        total=Utility.get_number(total_info,'总共')
        return total

    def do_query(self,cus_region,user_dept,user_name,cus_status,cus_source):
        self.click_transmit()
        self.select_origin_region(cus_region)
        self.select_origin_dept(user_dept)
        self.select_origin_emp(user_name)
        self.select_status(cus_status)
        self.select_source(cus_source)
        total=int(self.get_total())
        return total

    def do_submit(self,cus_region,user_dept,user_name,cus_status,cus_source,region_name,dept_name,worker_name):
        self.click_transmit()
        self.select_origin_region(cus_region)
        self.select_origin_dept(user_dept)
        self.select_origin_emp(user_name)
        self.select_status(cus_status)
        self.select_source(cus_source)
        time.sleep(1)
        total_before = int(self.get_total())
        self.select_transmit_region(region_name)
        self.select_transmit_dept(dept_name)
        self.select_transmit_worker(worker_name)
        time.sleep(2)
        self.click_option()
        self.click_submit()
        time.sleep(2)
        self.click_confirm()
        time.sleep(2)
        if Service.is_element_present(self.driver,By.XPATH,'/html/body/div[7]/div[3]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[1]/input'):
            total_after = int(self.get_total())
            print(total_after)
        else:
            total_after=0
        total = total_before - total_after
        print(total)
        return total

if __name__ == '__main__':

    from selenium import webdriver
    driver=webdriver.Firefox()
    ts=TrainTransmit(driver)
    ts.do_submit("上海","咨询部","包芸","新入库","专属简历","西安","咨询部","阿吉")



