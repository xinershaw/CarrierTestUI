# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from pages.base import BasePage
from pages.search_form import SearchForm as sf
from pages.element_location import loc_arrive_order as loc_a_o
from test_data.td_arrive_order import ar_order_search1 as td
from pages.element_location import loc_base as loc_base
from pages import get_data_DB as Db
import datetime
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains as Ac


class ArOrder(BasePage):
    def query_order_code(self, code):
        item = u'运单号'
        sf.single_query(item, code, loc_a_o.ar_order)
        line1 = sf.get_line1(loc_a_o.ar_order)
        sf.combined_query(td.items(), loc_a_o.ar_order)
        return line1[item]

