# coding=utf-8
"""
Created on 2018年5月29日
@author: Xiaoxin
Project:......
"""
from selenium import webdriver
import unittest
from pages.order_manage import arrive_order_add as ar_add
from pages.base import BasePage as b
from pages import page_e_location as loc
from testcase import test_data as td


class CaseDraft(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def test_draft(self):
        # 运费计算
        page = ar_add.ArOrderAdd(self.driver)
        page.just_do_it(**td.ar_add_order1)
        # s = td.ar_add_order1[u'重量']
        # print type(s), eval(s)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
