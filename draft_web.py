# coding=utf-8
"""
Created on 2018年5月29日
@author: Xiaoxin
Project:......
"""
from selenium import webdriver
import unittest
from pages.order_manage import arrive_order_add as ar_add
from test_data import td_arrive_order as td
from pages.element_location import loc_base as loc
from pages import base as Base
import time


class CaseDraft(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def test_draft(self):
        page = Base.BasePage(self.driver)
        page.login()
        menus = loc.menu
        for parent in menus:
            # 如果是dict，说明有子菜单,反之则没有子菜单
            if isinstance(menus[parent], dict):
                for menu in menus[parent]:
                    print parent, menu
                    if menu != u'父菜单':
                        page.open_the_menu(parent, menu)
                        time.sleep(1)
                        tab_name = page.is_visible(loc.tab[menu][menu])
                        print tab_name
                        page.close_tab(menu)
                        # try:
                        #     self.assertEqual(menu, tab_name)
                        # except AssertionError as e:
                        #     print e
            # else:
            #     print parent
            #     page.open_the_menu(parent)
            #     time.sleep(1)
            #     tab_name = page.get_tab_name(parent)
            #     page.close_tab(parent)
            #     try:
            #         self.assertEqual(parent, tab_name)
            #     except AssertionError as e:
            #         print e

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
