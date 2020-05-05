from common.login import Login
from util.service import Service
from util.utility import Utility
import time

class TrainSource:
    def __init__(self,driver):
        self.driver=driver
        self.login=Login(self.driver).do_login_zixun_manager('..\\config\\base.conf')

    def click_train_source(self):
        self.driver.find_element_by_link_text('资源管理').click()
        self.driver.find_element_by_link_text('培训资源').click()

    def click_allot_source(self):
        self.driver.find_element_by_link_text('资源管理').click()
        self.driver.find_element_by_link_text('分配资源').click()

    def click_public_source(self):
        self.driver.find_element_by_link_text('资源管理').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('公共资源').click()

    def click_transform_source(self):
        self.driver.find_element_by_link_text('资源管理').click()
        self.driver.find_element_by_link_text('转交资源').click()


    def send_sencpass(self,secp):
        self.driver.find_element_by_id('btn-decrypt').click()
        time.sleep(2)
        sec=self.driver.find_element_by_xpath('//div[@id="secondPass-modal"]/div/div/div[2]/input')


        Service.send_input(sec,secp)
        self.driver.find_element_by_xpath('//div[@id="secondPass-modal"]/div/div/div[3]/button').click()

    def select_pooltype(self,pool_name):

        # Service.miss_login(self.driver,'..\\config\\base.conf')
        select = self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div/select[1]')
        Service.select_by_name(select,pool_name)
    def select_worker(self,work_name):
        select = self.driver.find_element_by_css_selector('div.col-lg-12:nth-child(8) > select:nth-child(1)')

        select.click()
        Service.select_by_name(select, work_name)

    def select_status(self, status_name):
        select = self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div/select[2]')
        Service.select_by_name(select, status_name)

    def select_source(self, source_name):
        select = self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div/select[3]')
        Service.select_by_name(select, source_name)


    def send_start_time(self,stime):
        date=self.driver.find_element_by_id('date1')
        Service.send_input(date,stime)

    def send_end_time(self, etime):
        date = self.driver.find_element_by_id('date2')
        Service.send_input(date, etime)
    def send_keywords(self,keywords):
        input_cusinfo=self.driver.find_element_by_xpath\
            ('//div[@id="content"]/div[2]/div/input[3]')
        Service.send_input(input_cusinfo,keywords)

    def click_search(self):
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div/button').click()
        #self.driver.find_element_by_xpath('//div[@class="modal-body"]/div[1]/input')
    def total_info(self):
        total_str=self.driver.find_element_by_xpath('//div[@class="pull-left pagination-detail"]/span').text
        total_number=Utility.get_number(total_str,'总共')
        return total_number



if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()

    import time

    time.sleep(2)

    a=TrainSource(driver)
    time.sleep(2)
    a.send_sencpass('ccc')
    # a.select_pooltype('临时池')
    # a.send_keywords('18323587888')
    # a.click_search()
    # total_info = driver.find_element_by_xpath('//div[@class="pull-left pagination-detail"]/span')
    # g=total_info.text
    # print(g)
    # num=Utility.get_number(g,'总共')
    # print(num)
    # print(type(num))

    # import time
    # time.sleep(2)
    # Service.miss_login(driver,'..\\config\\base.conf')
    # time.sleep(1)
    #






