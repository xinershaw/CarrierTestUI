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
            },
        'select': {},
        'input_search': {},"""
        locator = loc.ar_order[u'查询条件']
        query_form = {'input': {}, 'select': {}, 'input_search': {}}
        for td in test_data:
            if td in locator['input']:
                query_form['input'].update({td: [test_data[td], locator['input'][td]]})
            elif td in locator['select']:
                query_form['select'].update({td: [test_data[td], locator['select'][td]]})
            else:
                query_form['input_search'].update({td: [test_data[td], locator['input_search'][td]]})
        print query_form
