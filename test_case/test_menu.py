# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
import unittest
from selenium import webdriver
from pages import base
from pages.element_location import loc_base
import time


class CaseMenu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def test_open_menus(self):  # 新增到货分理-冒烟测试
        page = base.BasePage(self.driver)
        page.login()
        menus = loc_base.menu
        for parents_menu in menus:
            # 如果是dict，说明有子菜单,反之则没有子菜单
            if isinstance(menus[parents_menu], dict):
                for son_menu in menus[parents_menu]:
                    if son_menu != u'父菜单':
                        tab_name = page.open_the_menu(parents_menu, son_menu)  # 打开菜单
                        time.sleep(1)
                        page.to_frame(son_menu)
                        try:
                            self.assertNotIn(u'服务器错误', page.driver.page_source)
                        except AssertionError as e:
                            print son_menu, u'打开此页面报错！', e
                        self.driver.switch_to.default_content()  # 从frame中出来，否则定位不到tab
                        page.close_tab(son_menu)
                        try:
                            self.assertEqual(son_menu, tab_name)
                        except AssertionError as e:
                            print son_menu, u'打开此菜单的tab页测试不通过！', e
            else:  # 没有二级菜单的情况
                # print parents_menu
                tab_name = page.open_the_menu(parents_menu)
                time.sleep(1)
                page.to_frame(parents_menu)
                try:
                    self.assertNotIn(u'服务器错误', page.driver.page_source)
                except AssertionError as e:
                    print parents_menu, u'打开此页面报错！', e
                self.driver.switch_to.default_content()
                page.close_tab(parents_menu)
                try:
                    self.assertEqual(parents_menu, tab_name)
                except AssertionError as e:
                    print parents_menu, u'打开此菜单的tab页测试不通过！', e

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
