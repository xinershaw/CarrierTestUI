# coding=utf-8
"""
Created on 2018年5月29日
@author: Xiaoxin
Project:新增到货分理页的操作方法
"""
from pages.base import BasePage
from pages import page_e_location as loc
from pages import get_data_DB as DB
import datetime
import time
from selenium.webdriver.support.select import Select


class ArOrderAdd(BasePage):

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

    def input_arrive_date(self):  # 录入到货时间
        self.click(loc.ar_add_order[u'到货时间']['input_date'])
        self.click(loc.ar_add_order[u'到货时间']['today'])

    def write_order_code(self):
        today = datetime.datetime.now()
        pre_code = today.strftime('%y')+today.strftime('%m')+today.strftime('%d')
        db_cy = DB.DB('jshc_carrier')
        sql_cy = "SELECT jot.DeliverCode FROM jshc_o_deliverorder jot WHERE jot.DeliverCode like " + "'" + \
                 pre_code+"%'" + "ORDER BY jot.CreateTime DESC LIMIT 1 "
        old_code = db_cy.query(sql_cy)
        if old_code:
            order_code = int(old_code.__str__()[4:14])+1
        else:
            order_code = pre_code + '0001'
        self.find_element(*(loc.ar_add_order[u'运单号'])).send_keys(order_code)

    def select_value(self, item, *loc_select):  # select下拉列表选择某一项
        s = self.find_element(*loc_select)
        Select(s).select_by_visible_text(item)

    def input_group(self, station_name, **loc_input_item):  # 发、到站下拉列表选择
        self.find_element(*loc_input_item['input']).send_keys(station_name)
        self.click(loc_input_item['item'])

    def input_s_station(self, station_name):  # 录入发站
        key_word = {'input': loc.ar_add_order[u'发站'], 'item': loc.ar_add_order[u'发站列表1']}
        self.input_group(station_name, **key_word)

    def input_e_station(self, station_name):  # 录入到站
        key_word = {'input': loc.ar_add_order[u'到站'], 'item': loc.ar_add_order[u'到站列表1']}
        self.input_group(station_name, **key_word)

    def input_g_name(self, goods_name):  # 录入货物名称
        key_word = {'input': loc.ar_add_order[u'货物名称'], 'item': loc.ar_add_order[u'货物列表1']}
        self.input_group(goods_name, **key_word)

    def input_all(self, **all_items):
        self.select_value(all_items[u'运输方式'], *(loc.ar_add_order[u'运输方式']))
        self.select_value(all_items[u'服务方式'], *(loc.ar_add_order[u'服务方式']))
        self.select_value(all_items[u'支付方式'], *(loc.ar_add_order[u'支付方式']))
        self.input_s_station(all_items[u'发站'])
        self.input_e_station(all_items[u'到站'])
        self.find_element(*(loc.ar_add_order[u'发货人'])).send_keys(all_items[u'发货人'])
        self.find_element(*(loc.ar_add_order[u'收货人'])).send_keys(all_items[u'收货人'])
        self.find_element(*(loc.ar_add_order[u'发货人手机号'])).send_keys(all_items[u'发货人手机号'])
        self.find_element(*(loc.ar_add_order[u'收货人手机号'])).send_keys(all_items[u'收货人手机号'])
        self.input_g_name(all_items[u'货物名称'])
        self.find_element(*(loc.ar_add_order[u'件数'])).send_keys(all_items[u'件数'])
        self.find_element(*(loc.ar_add_order[u'其他费'])).send_keys(all_items[u'其他费'])
        self.find_element(*(loc.ar_add_order[u'重量'])).send_keys(all_items[u'重量'])
        self.find_element(*(loc.ar_add_order[u'体积'])).send_keys(all_items[u'体积'])
        self.find_element(*(loc.ar_add_order[u'装卸费铁'])).send_keys(all_items[u'装卸费铁'])
        self.find_element(*(loc.ar_add_order[u'装卸费收'])).send_keys(all_items[u'装卸费收'])

    def just_do_it(self, **all_items):
        self.open_page_add()
        self.input_arrive_date()
        self.write_order_code()
        self.input_all(**all_items)
        self.click(loc.ar_add_order[u'保存并提交'])
























