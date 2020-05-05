from common.login import Login
from common.train_source import TrainSource
from util.service import Service

class TrainAbadon:
    def __init__(self,driver):
        self.driver=driver
        self.ts = TrainSource(self.driver)
        self.ts.click_train_source()

    def click_option(self):
        self.driver.find_element_by_xpath('//table[@id="personal-table"]/tbody/tr[1]/td[1]/input').click()

    def click_abandon(self):
        self.driver.find_element_by_id('abandon').click()

    def click_confirm_abandon(self):
        self.driver.find_element_by_xpath('//div[@class="modal-dialog modal-sm"]/div/div[3]/button[2]').click()

    def click_public(self):
        self.driver.find_element_by_link_text('公共资源').click()

    def publick_keyward_query(self,value):
        key=self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div/input').click()
        Service.send_input(key,value)
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div/button').click()

    def query_abandon_time(self):
        abandon_time=self.driver.find_element_by_xpath('//table[@id="public-pool-table"]/tbody/tr[1]/td[14]').text
        return abandon_time

    def do_abandon(self,cus_kwys):
        self.click_option()
        self.click_abandon()
        self.click_confirm_abandon()
        self.click_public()



if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    a=TrainAbadon(driver)
    a.click_option()
    a.click_abandon()


