#!/usr/bin/env python
# @Time : 2020/4/3 10:19
# @Author : lifei
#@desc:
import time

from woniucbt.common.utility import Utility


class SellObject:
    def __init__(self):
        self.driver = Utility.get_webdriver()

    def get_barcode(self):

        return self.driver.find_element_by_id('barcode')

    def get_barcode_button(self):
        return self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[1]/form/button')

    def get_discount_ratio(self):
        return self.driver.find_element_by_css_selector('.discountratio > input')

    def get_buy_count_plus(self):
        return self.driver.find_element_by_css_selector('.buycountInput > button:nth-child(3)')

    def get_customer_phone(self):
        return self.driver.find_element_by_id('customerphone')

    def get_customer_querry_button(self):
        return self.driver.find_element_by_css_selector('.col-lg-6 > .btn-primary')

    def get_credit_ratio(self):
        self.driver.find_element_by_id('creditratio').clear()
        return self.driver.find_element_by_id('creditratio')

    def get_submit_button(self):
        return self.driver.find_element_by_id('submit')

    def do_buy_goods(self,barcode,discount_ratio):
        self.get_barcode().send_keys(barcode)
        self.get_barcode_button().click()
        element = self.get_discount_ratio()
        js = 'document.querySelector(".discountratio > input").value="";'
        self.driver.execute_script(js)
        element.send_keys(discount_ratio)
        self.get_buy_count_plus().click()

    def do_sell(self,phone,credit_radio):
        self.get_customer_phone().send_keys(phone)
        self.get_customer_querry_button().click()
        self.get_credit_ratio().send_keys(credit_radio)
        self.get_submit_button().click()
        time.sleep(2)
        self.driver.switch_to_alert().accept()
        time.sleep(2)

