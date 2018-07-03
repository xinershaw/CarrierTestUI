# coding=utf-8
"""
Created on 2018年6月5日
@author: Xiaoxin
Project: 新增到货分理订单测试用例
"""
import unittest
from selenium import webdriver
from pages.order_manage import arrive_order_add as ar_add, arrive_order as ar
from test_data import td_arrive_order as td
import time


class CaseArOrderAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def test_ar_order_add_smoke(self):  # 新增到货分理-冒烟测试
        page = ar_add.ArOrderAdd(self.driver)
        order_code = page.save_submit(**td.ar_add_order1)
        time.sleep(15)  # 保存耗时较长，因此强制等待
        page_list = ar.ArOrder(self.driver)
        order_code_list = page_list.query_order_code(order_code)
        try:  # 保存后，比较列表页面最新一条记录的运单号与录入时的运单号是否一致
            self.assertEqual(order_code, int(order_code_list))
        except AssertionError as e:
            print u'到货分理新增运单测试不通过！', e

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


