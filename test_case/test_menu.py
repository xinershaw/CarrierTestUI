# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
import unittest
from selenium import webdriver
from pages import base
from pages.element_location import loc_base as loc
import time


class CaseMenu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def test_open_menus(self):  # 新增到货分理-冒烟测试
        page = base.BasePage(self.driver)
        page.login()
        menus = loc.menu
        for parent in menus:
            # 如果是dict，说明有子菜单,反之则没有子菜单
            if isinstance(menus[parent], dict):
                for menu in menus[parent]:
                    if menu != u'父菜单':
                        page.open_the_menu(parent, menu)
                        time.sleep(1)
                        tab_name = page.get_tab_name(menu)
                        page.close_tab(menu)
                        try:
                            self.assertEqual(menu, tab_name)
                        except AssertionError as e:
                            print menu, u'打开此菜单测试不通过！', e
            else:
                page.open_the_menu(parent)
                time.sleep(1)
                tab_name = page.get_tab_name(parent)
                page.close_tab(parent)
                try:
                    self.assertEqual(parent, tab_name)
                except AssertionError as e:
                    print parent, u'打开此菜单测试不通过！', e

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
