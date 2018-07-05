# coding=utf-8
"""
Created on 2018年5月29日
@author: Xiaoxin
Project:......
"""
from selenium import webdriver
import unittest
from pages.order_manage import arrive_order as ar
from test_data import td_arrive_order as td
from pages.element_location import loc_base as loc_b, loc_arrive_order as loc
from pages import base as Base
import time


class CaseDraft(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def test_draft(self):
        page = ar.ArOrder(self.driver)
        page.login()
        page.open_the_menu(u'运单', u'到货分理')  # 从菜单打开到货分理列表页
        # # 激活到货分理frame
        # page.click(loc_b.tab[u'首页'])
        # page.click(loc_b.tab[u'到货分理'][u'到货分理'])
        # # 切换进到货分理frame
        # page.to_frame(*(loc.ar_order['frame']))
        page.order_search(**td.ar_order_search1)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
