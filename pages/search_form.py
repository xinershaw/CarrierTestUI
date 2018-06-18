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
    def input_search_form(self, **query_conditions):
        """ query_conditions={'loc':{
                input:{
                item1:[value, loc],
                item2:[value, loc],
                ......},
                select:{
                item1:[value, loc],
                item2:[value, loc],
                ......},
                input_search:{
                item1:[value, **loc],
                item2:[value, **loc],
                ......}},
                'test_data':{item1:data1,
                           item2:data2]
                           .........}
                        }
        """
        loc = query_conditions['loc']
        td = query_conditions['test_data'].items()
        for t in td:
            if t[0] in loc['input']:
                self.send_keys(t[1], loc['input'][t[0]])
            elif t[0] in loc['select']:
                self.select_value(t[1], loc['select'][t[0]])
            elif t[0] in loc['input_search']:
                self.input_search(t[1], **loc['input_search'][t[0]])

    def combined_query(self, **loc, **test_data):  # 组合查询 loc是指定位器中的字典变量
        query_condition = {'loc': loc[u'查询条件'],
                           'test_data': test_data}
        self.input_search_form(**query_condition)
        self.click(loc[u'搜索'])

    def single_query(self, test_data, item,  **loc):  # 单一查询 loc是指定位器中的字典变量
        self.send_keys(test_data, loc[u'查询条件'][item])
        self.click(loc[u'搜索'])

    def get_line1(self, **loc):  # 到货分理列表，获取列表第一行数据的运单号 loc是指定位器中的字典变量
        line1 = dict()
        heads = self.find_elements(loc[u'列表'][u'表头']).text
        line1_data = self.find_elements(loc[u'列表'][u'第一行']).text
        for n in range(1, len(heads)):
            line1.update({heads[n], line1_data[n]})
        return line1



