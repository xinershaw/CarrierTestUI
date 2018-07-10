# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from pages.base import BasePage
from pages.menu import Menu
from pages.search_form import SearchForm
from pages.element_location import loc_arrive_order as loc_a_o
from pages.element_location import loc_base as loc_base
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ArOrder(BasePage):
    def open_page(self):
        self.login()  # 登录
        menu = Menu(self.driver)
        menu.open_the_menu(u'运单', u'到货分理')  # 从菜单打开到货分理列表页
        # 切换进到货分理frame
        self.to_frame(u'到货分理')
        time.sleep(3)  # 强制等待页面（到货分理列表页）加载，否则新增到货分理按钮无法点击

    def query_order_code(self, code):
        search_form = SearchForm(self.driver)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc_a_o.ar_order[u'列表'][u'整体']))
        search_form.single_query(code, u'运单号', **loc_a_o.ar_order)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc_a_o.ar_order[u'列表'][u'第一行']))
        line1 = search_form.get_line1(**loc_a_o.ar_order)
        return line1[u'运单号']

