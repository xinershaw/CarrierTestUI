# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from pages.base import BasePage
from pages.element_location import loc_arrive_order as loc
from pages.element_location import loc_base as loc_base
from pages import get_data_DB as Db
import datetime
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains as Ac


class ArOrder(BasePage):
    def search(self, **keyword):
        """
        keyword={
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
        ......}
        """
        for i in keyword:
            if i == 'input':
                for j in keyword[i]:
                    self.send_keys(keyword[i][j][0], keyword[i][j][1])
            if i == 'select':
                for j in keyword[i]:
                    self.select_value(keyword[i][j][0], keyword[i][j][1])
            else:
                for j in keyword[i]:
                    self.input_search(keyword[i][j][0], **keyword[i][j][1])
        self.click(loc.ar_order[u'查询条件'][u'搜索'])

