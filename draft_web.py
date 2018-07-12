# coding=utf-8
"""
Created on 2018年5月29日
@author: Xiaoxin
Project:......
"""
from selenium import webdriver
import unittest
from pages.order_manage import arrive_order_add as ar_add
from pages.area_controller import AreaController as area_c
from test_data import td_arrive_order as td
from pages.element_location import loc_base as loc_b, loc_arrive_order as loc_a
from pages import base as Base
import time


class CaseDraft(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def test_draft(self):
        page = ar_add.ArOrderAdd(self.driver)
        page.open_page_add()  # 从菜单打开到货分理列表页
        area_ctroller = area_c(self.driver)
        area_ctroller.input_area(u'四川', u'成都', u'郫县', u'犀浦', *loc_a.ar_add_order[u'发货地址'])
        area_ctroller.input_clear(*loc_a.ar_add_order[u'发货地址'])

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
