# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from pages.base import BasePage
from pages.element_location import loc_base as loc_base
from pages import get_data_DB as Db
import datetime
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains as Ac


class SearchForm(BasePage):
    def combined_query(self, *test_data, **loc):  # 组合查询 loc是指定位器中的字典变量
        self.input_items(*test_data, **loc)
        self.click(loc[u'搜索'])

    def single_query(self, item, test_data, **loc):  # 单一查询 loc是指定位器中的字典变量
        self.send_keys(test_data, loc[u'查询条件'][item])
        self.click(loc[u'搜索'])

    def get_line1(self, **loc):  # 到货分理列表，获取列表第一行数据的运单号 loc是指定位器中的字典变量
        line1 = dict()
        heads = self.find_elements(loc[u'列表'][u'表头']).text
        line1_data = self.find_elements(loc[u'列表'][u'第一行']).text
        for n in range(1, len(heads)):
            line1.update({heads[n], line1_data[n]})
        return line1



