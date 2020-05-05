import time

from selenium.webdriver.common.by import By

from woniuboss4_GUI.common.login import Login
from woniuboss4_GUI.util.service import Service


class Trainadd:
    def __init__(self,driver):
        self.driver=driver
        self.login=Login(self.driver).do_login_zixun_manager('..\\config\\base.conf')

    def click_train_source(self):
        self.driver.find_element_by_link_text('资源管理').click()
        self.driver.find_element_by_link_text('培训资源').click()

    def click_add(self):
        ele_add=self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div/div/div/button')
        ele_add.click()
    def input_phone(self,cus_phone):
        phone=self.driver.find_element_by_xpath('//form[@id="addCus"]/div/div/div/input')
        Service.send_input(phone,cus_phone)

    def input_name(self,cus_name):
        name = self.driver.find_element_by_xpath('//form[@id="addCus"]/div/div/div[2]/input')
        Service.send_input(name,cus_name)

    def select_sex(self,cus_sex):
        sex=self.driver.find_element_by_xpath('//form[@id="addCus"]/div/div/div[3]/select')
        Service.select_by_name(sex,cus_sex)

    def select_status(self,cus_status):
        status=self.driver.find_element_by_xpath('//div[@class="modal-body"]/div[2]/div/select')
        Service.select_by_name(status,cus_status)
    def select_grade(self,cus_grade):
        grade=self.driver.find_element_by_xpath('//form[@id="addCus"]/div/div[3]/div[2]/select')
        Service.select_by_name(grade,cus_grade)
    def select_experience(self,experience_name):
        experience=self.driver.find_element_by_xpath('//form[@id="addCus"]/div/div[4]/div[2]/select')
        Service.select_by_name(experience,experience_name)
    def select_source(self,cus_source):
        source=self.driver.find_element_by_xpath('//form[@id="addCus"]/div/div[5]/div/select')
        Service.select_by_name(source,cus_source)

    def click_save(self):
        addc=self.driver.find_element_by_xpath('// *[ @ id = "addCusBtn"]')
        addc.click()
    def message(self):#
        add_message=self.driver.find_elements(By.CLASS_NAME,'bootbox-body')[0].text
        return add_message
    def close_add(self):
        close_button=self.driver.find_element_by_xpath('html/body/div[8]/div/div/div/button/span[1]')
        close_button.click()

    def add_tel_verify(self,cus_phone,cus_name,cus_sex,cus_status,cus_grade,cus_experience,cus_source):
        self.click_add()
        self.input_phone(cus_phone)
        self.input_name(cus_name)
        self.select_sex(cus_sex)
        self.select_status(cus_status)
        self.select_grade(cus_grade)
        self.select_experience(cus_experience)
        self.select_source(cus_source)
        self.click_save()




# /html/body/div[14]/div/div/div[3]/button





if __name__ == '__main__':
    from selenium import  webdriver
    driver=webdriver.Firefox()
    a=Trainadd(driver)
    a.click_train_source()
    a.click_add()
    time.sleep(1)
    a.select_sex('女')
    a.select_status('新入库')
    a.select_grade('本科')
    a.select_experience('2年')
    a.select_source('学员介绍')




