#!/usr/bin/python3
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------------------------
# @Author  : WANG
# @FileName: driven.py
# @Software: PyCharm
# @Time    : 2020/4/26
#---------------------------------------------------------------------------------------
import time

from selenium.webdriver.common.by import By

from woniuboss4_GUI.common.login import Login
from woniuboss4_GUI.util.service import Service


class Staffadd:
    def __init__(self,driver):
        self.driver=driver
        self.login=Login(self.driver).do_login_admin('..\\config\\base.conf')

    def click_train_source(self):
        self.driver.find_element_by_link_text('人事管理').click()
        self.driver.find_element_by_link_text('员工信息').click()

    #点击新增按钮
    def click_add(self):  #
        ele_add=self.driver.find_element_by_xpath('/html/body/div[9]/div[2]/div[1]/div/button')
        ele_add.click()

    #选择区域
    def select_area(self,cus_zone):
        sex=self.driver.find_element_by_xpath('/html/body/div[15]/div/div/form/div/div[1]/div[1]/select')
        Service.select_by_name(sex,cus_zone)

    #选择部门
    def select_branch(self,cus_section):
        sex=self.driver.find_element_by_xpath('/html/body/div[15]/div/div/form/div/div[1]/div[2]/select')
        Service.select_by_name(sex,cus_section)

    #填写职位
    def input_job(self,cus_job):#/html/body/div[15]/div/div/form/div/div[1]/div[3]/input
        phone=self.driver.find_element_by_xpath('/html/body/div[15]/div/div/form/div/div[1]/div[3]/input')
        Service.send_input(phone,cus_job)
    #填写姓名
    def input_name(self,cus_name):
        name = self.driver.find_element_by_xpath('/html/body/div[15]/div/div/form/div/div[2]/div[1]/input')
        Service.send_input(name,cus_name)

    #填写电话
    def input_phone(self,cus_phone):
        name = self.driver.find_element_by_xpath('/html/body/div[15]/div/div/form/div/div[3]/div[1]/input')
        Service.send_input(name,cus_phone)

    #填写工号
    def input_jobnumber(self,cus_jobnum):
        name = self.driver.find_element_by_xpath('/html/body/div[15]/div/div/form/div/div[8]/div/input')
        Service.send_input(name,cus_jobnum)

    #点击保存
    def click_save(self):
        addc=self.driver.find_element_by_xpath('//*[@id="addEmpBtn"]')
        addc.click()
    def message(self):
        add_message=self.driver.find_elements(By.CLASS_NAME,'bootbox-body')[0].text
        return add_message
    def close_add(self):
        close_button=self.driver.find_element_by_xpath('html/body/div[8]/div/div/div/button/span[1]')
        close_button.click()

    def add_tel_verify(self,cus_zone,cus_section,cus_job,cus_name,cus_phone,cus_jobnum):
        self.click_add()
        self.select_area(cus_zone)
        self.select_branch(cus_section)
        self.input_job(cus_job)
        self.input_name(cus_name)
        self.input_jobnumber(cus_jobnum)
        self.input_phone(cus_phone)
        self.click_save()








if __name__ == '__main__':
    from selenium import  webdriver
    driver=webdriver.Firefox()
    a=Staffadd(driver)
    a.click_train_source()
    a.click_add()
    time.sleep(1)

    a.select_area('成都')
    a.select_branch('咨询部')
    a.input_job('咨询师')
    a.input_name('大大怪')
    a.input_jobnumber('WNCD090')
    a.input_phone('13945676543')
    a.click_save()
    time.sleep(3)
    b=a.message()
    print(b)




