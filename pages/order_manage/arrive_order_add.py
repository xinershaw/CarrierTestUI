# coding=utf-8
"""
Created on 2018年5月29日
@author: Xiaoxin
Project:新增到货分理页的操作方法
"""
from selenium.webdriver.common.by import By
from pages.base import BasePage
from selenium.webdriver.common.action_chains import ActionChains as Ac
from selenium.webdriver.support.wait import WebDriverWait
from pages import page_e_location as locator


class ArOrderAdd(BasePage):
    url = u'http://cy.tuluo56.com/Manager/ArriveOrder/AddArriveOrder'

    def open_page_add(self):
        self.find_element(*(locator.navbar_left[u'运单'][u'父菜单'])).click()
        self.find_element(*(locator.navbar_left[u'运单'][u'到货分理'])).click()
        f = self.find_element(*(By.XPATH, "//a[contains(@data-id,'/Manager/ArriveOrder/Index')]"))
        print f.text
        f.click()
        # self.switch_frame(self.driver.find_element(By.XPATH, "//iframe[contains(@src,'/Manager/ArriveOrder/Index')]"))
        self.switch_frame(1)
        self.find_element(*(locator.ar_order[u'新增'])).click()
        print 'wait'

    def input_date(self, *loc):
        self.find_element(*loc).click()
        box = locator.ar_add_order[u'到货时间']['box']
        print box, type(box)
        WebDriverWait(self.driver, 10).until(lambda is_display: self.find_element(box).is_displayed())
        self.find_element(locator.ar_add_order[u'到货时间']['today']).click()

