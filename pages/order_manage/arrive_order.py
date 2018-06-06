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
    def order_search(self, **test_data):
        """
        u'查询条件':{
        'input': {
            u'订单号': (By.ID, 'TransitOrderCode')>>u'订单号': [value,(By.ID, 'TransitOrderCode')]
            u'原票号': (By.ID, 'OldBillNum'),
            },
        'select': {

        },
        'input_search': {

        },"""
        s = loc.ar_order[u'查询条件']
        for loc_g in s:
            for i in test_data:
                if i in s[loc_g]:
                    s[loc_g][i] = [s[loc_g][i], test_data[i]]
                    print s[loc_g][i]
                    continue
            # test_data[item] = [test_data[item], loc.ar_order[u'查询条件'][item]]
            #         print '++++++++++'
        print '==========end'
        print s
        # self.input_query_item()
        # self.click(loc.ar_order[u'查询条件'][u'搜索'])

