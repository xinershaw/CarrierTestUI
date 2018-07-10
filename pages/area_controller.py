# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


class AreaController(BasePage):
    def click_area(self, item, item_text):
        if self.find_element(*item).get_attribute('class') == 'active':
            self.click(item)
        item_text_loc = (By.LINK_TEXT, item_text)
        self.click(item_text_loc)

    def input_area(self, pro, city, dis, county, *input_loc):
        self.click(*input_loc)

        tab_pro = (By.XPATH, "//a[@data-count='province']")
        tab_city = (By.XPATH, "//a[@data-count='city']")
        tab_dis = (By.XPATH, "//a[@data-count='district']")
        tab_county = (By.XPATH, "//a[@data-count='county']")
        self.click_area(tab_pro, pro)
        self.click_area(tab_city, city)
        self.click_area(tab_dis, dis)
        self.click_area(tab_county, county)
