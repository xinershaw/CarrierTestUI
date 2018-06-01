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
import time
from selenium.webdriver.support import expected_conditions as EC


class ArOrderAdd(BasePage):
    url = u'http://cy.tuluo56.com/Manager/ArriveOrder/AddArriveOrder'

    def open_page_add(self):
        self.login()  # 登录
        self.find_element(*(loc.navbar[u'运单'][u'父菜单'])).click()  # 展开运单管理菜单
        self.find_element(*(loc.navbar[u'运单'][u'到货分理'])).click()  # 打开到货分理列表页面
        # 激活到货分理frame
        self.click(loc.ar_order[u'首页'])
        self.click(loc.ar_order[u'到货分理'])
        # 切换进到货分理frame
        self.to_frame(*(loc.ar_order['frame']))

        time.sleep(3)  # 强制等待页面（到货分理列表页）加载，否则新增到货分理按钮无法点击
        self.click(loc.ar_order[u'新增'])
        time.sleep(3)  # 强制等待页面（新增到货分理页）加载，否则日期控件无法点击

    def input_arrive_date(self):
        self.click(loc.ar_add_order[u'到货时间']['input_date'])
        self.click(loc.ar_add_order[u'到货时间']['today'])

    def write_ordercode(self):
        today = datetime.datetime.now()
        pre_code = today.strftime('%y')+today.strftime('%m')+today.strftime('%d')
        db_cy = db.DB('jshc_carrier')
        sql_cy = "SELECT jot.DeliverCode FROM jshc_o_deliverorder jot WHERE jot.DeliverCode like " + "'" + \
                 pre_code+"%'" + "ORDER BY jot.CreateTime DESC LIMIT 1 "
        old_code = db_cy.query(sql_cy)
        if old_code:
            return int(old_code.__str__()[4:14])+1
        else:
            return pre_code + '0001'




