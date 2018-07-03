# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from pages.base import BasePage
from pages.search_form import SearchForm
from pages.element_location import loc_arrive_order as loc_a_o
from test_data.td_arrive_order import ar_order_search1 as td
from pages.element_location import loc_base as loc_base
from pages import get_data_DB as Db
import datetime
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains as Ac


class ArOrder(BasePage):
    def open_page(self):
        self.login()  # 登录
        self.open_the_menu(u'运单', u'到货分理')  # 从菜单打开到货分理列表页
        # 激活到货分理frame
        self.click(loc_base.tab[u'首页'])
        self.click(loc_base.tab[u'到货分理'][u'到货分理'])
        # 切换进到货分理frame
        self.to_frame(*(loc_a_o.ar_order['frame']))
        time.sleep(3)  # 强制等待页面（到货分理列表页）加载，否则新增到货分理按钮无法点击

    def query_order_code(self, code):
        search_form = SearchForm(self.driver)
        item = u'运单号'
        search_form.single_query(code, item, u'input', **loc_a_o.ar_order)
        time.sleep(2)
        line1 = search_form.get_line1(**loc_a_o.ar_order)
        return line1[item]

