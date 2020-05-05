import random
from common.login import Login
from util.service import Service
from util.utility import Utility
import time
class TrainAssign:
    def __init__(self,driver):
        self.driver=driver
        self.login=Login(self.driver).do_login_zixun_manager('..\\config\\base.conf')

    def click_assign(self):
        self.driver.find_element_by_link_text('资源管理').click()
        self.driver.find_element_by_link_text('分配资源').click()

    def select_channel(self,cus_channel):
        channel=self.driver.find_element_by_name('source')

        Service.select_by_name(channel,cus_channel)

    def input_keyward(self,cus_keyw):
        keyward=self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[2]/input')
        Service.send_input(keyward,cus_keyw)

    def click_query(self):
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[2]/button').click()

    def assign_curriculum(self,cus_curriculum):
        curriculum=self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[3]/select')
        Service.select_by_name(curriculum,cus_curriculum)


    def submit(self):
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[3]/button[1]').click()

    def select_assign_random(self):
        total_info=int(self.total_info())
        if total_info>10:
            total_info=10
        self.driver.find_element_by_xpath('//table[@id="allot-table"]/tbody/tr[%d]/td[1]'%(random.randint(1,total_info))).click()

    def select_assign_all(self):
        self.driver.find_element_by_xpath('//table[@id="allot-table"]/thead/tr/th/div/input').click()

    def click_confirm(self):
        self.driver.find_element_by_xpath('//div[@class="modal-dialog modal-sm"]/div/div[3]/button[2]').click()
    def close_tip(self):
        self.driver.find_element_by_xpath('//div[@class="bootbox modal fade mydialog in"]/div/div/div[1]/button').click()

    def do_proportion(self):
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[3]/button[2]').click()


    def total_info(self):
        total_str=self.driver.find_element_by_xpath('//div[@class="pull-left pagination-detail"]/span').text
        total_number=Utility.get_number(total_str,'总共')
        return total_number
    #渠道搜索,选在任意一个学员，按咨询师进行简历分配
    def do_assign_to_counselor(self,cus_channel,cus_curriculum):
        self.click_assign()
        self.select_channel(cus_channel)
        time.sleep(1)
        total_before=self.total_info()
        self.select_assign_random()
        self.assign_curriculum(cus_curriculum)
        self.submit()
        time.sleep(2)
        self.click_confirm()
        time.sleep(1)
        self.close_tip()
        total_after=self.total_info()
        total=int(total_before)-int(total_after)
        return total

    def do_assign_all_to_counselor(self, cus_channel, cus_curriculum):
        self.click_assign()
        self.select_channel(cus_channel)
        total_before = self.total_info()
        self.select_assign_all()
        self.assign_curriculum(cus_curriculum)
        self.submit()
        time.sleep(2)
        self.click_confirm()
        time.sleep(1)
        self.close_tip()
        try:
            total_after = self.total_info()
            if total_after<total_before:
                return True
            else:
                return False
        except:
            return True




if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    ts=TrainAssign(driver)
    import time
    time.sleep(2)
    ts.click_assign()
    total=ts.do_assign_to_counselor('自然流量','安琪')
    print(total)

