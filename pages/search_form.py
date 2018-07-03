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

    def single_query(self, item_input, item_name, item_type, **loc):  # 单一查询 loc是指定位器中的字典变量
        self.send_keys(item_input, *loc[u'查询条件'][item_type][item_name])
        self.click(loc[u'搜索'])

    def get_line1(self, **loc):  # 到货分理列表，获取列表第一行数据的运单号 loc是指定位器中的字典变量
        line1 = dict()
        for head, data in self.find_elements(*loc[u'列表'][u'表头']), self.find_elements(*loc[u'列表'][u'第一行']):
            line1.update({head.text: data.text})
        return line1



