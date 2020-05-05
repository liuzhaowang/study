import random
import time

from common.login import Login
from util.service import Service


class TrainPublic:
    def __init__(self,driver):
        self.driver=driver
        self.login=Login(self.driver).do_login_zixun_manager('..\\config\\base.conf')

    def click_public_source(self):
        self.driver.find_element_by_link_text('资源管理').click()
        self.driver.find_element_by_link_text('公共资源').click()


    def click_claim(self):
        self.driver.find_element_by_id('ownCusBtn').click()
        self.driver.find_element_by_xpath('//div[@class="bootbox modal fade mydialog in"]/div/div/div[3]/button[2]').click()
    def abandon_person(self,worker):
        person=self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/select[3]')
        Service.select_by_name(person,worker)

    def select_option(self):
        self.driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[1]/input').click()
    def select_all_option(self):
        self.driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[1]/div[2]/div[2]/table/thead/tr/th[1]/div[1]/input').click()

    def get_result(self):
        message=self.driver.find_element_by_xpath('//div[@class="bootbox modal fade mydialog in"]/div/div/div[2]/div').text
        return message
    def click_confirm(self):
        self.driver.find_element_by_xpath('//div[@class="bootbox modal fade mydialog in"]/div/div/div[3]/button').click()

    def do_claim_one(self,worker):
        self.click_public_source()
        time.sleep(1)
        self.abandon_person(worker)
        self.select_option()
        self.click_claim()

    def do_claim_all(self,worker):
        self.click_public_source()
        self.abandon_person(worker)
        self.select_all_option()
        self.click_claim()




