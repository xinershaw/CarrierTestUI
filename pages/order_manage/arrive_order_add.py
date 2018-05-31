# coding=utf-8
"""
Created on 2018年5月29日
@author: Xiaoxin
Project:新增到货分理页的操作方法
"""
from selenium.webdriver.common.by import By
from pages.base import BasePage
from selenium.webdriver.common.action_chains import ActionChains as Ac
from selenium.webdriver.support.wait import WebDriverWait
from pages import page_e_location as loc
from pages import get_data_DB as db
import datetime
from selenium.webdriver.support import expected_conditions as EC


class ArOrderAdd(BasePage):
    url = u'http://cy.tuluo56.com/Manager/ArriveOrder/AddArriveOrder'

    def open_page_add(self):
        self.login()  # 登录
        self.find_element(*(loc.navbar_left[u'运单'][u'父菜单'])).click()  # 展开运单管理菜单
        self.find_element(*(loc.navbar_left[u'运单'][u'到货分理'])).click()  # 打开到货分理列表页面
        # 切换到到货分理frame
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(self.find_element(*(By.NAME, 'iframe4'))))
        self.find_element(*(loc.ar_order[u'新增'])).click()  # 点击新增到货分理按钮

    def input_arrive_date(self):
        action = Ac(self.driver)
        in_date = self.find_element(*(loc.ar_add_order[u'到货时间']['input_date']))
        action.move_to_element(in_date).click(in_date).perform()  # 打开日历控件
        box = loc.ar_add_order[u'到货时间']['box']
        # print box, type(box)
        WebDriverWait(self.driver, 10).until(lambda is_display: self.find_element(*box).is_displayed())
        today = self.find_element(*(loc.ar_add_order[u'到货时间']['today']))
        action.move_to_element(today).click(today).perform()  # 录入为今天

    def input_order_code(self):
        today = datetime.datetime.now()
        pre_code = today.strftime('%y')+today.strftime('%m')+today.strftime('%d')
        db_cy = db.DB('jshc_carrier')
        sql_cy = "SELECT jot.OrderCode FROM jshc_o_transitorder jot WHERE jot.OrderCode like " + "'" + pre_code+"%'" + \
                 "ORDER BY jot.CreateTime DESC LIMIT 1 "
        old_code = db_cy.query(sql_cy)
        if old_code:
            return old_code + 1
        else:
            return pre_code + '0001'




