# coding=utf-8
"""
Created on 2018年5月29日
@author: Xiaoxin
Project:新增到货分理页的操作方法
"""
from pages.base import BasePage
from pages.element_location import loc_arrive_order as loc
from pages.element_location import loc_base as loc_base
from pages import get_data_DB as Db
import datetime
import time
from selenium.webdriver.common.action_chains import ActionChains as Ac


class ArOrderAdd(BasePage):
    def open_page_add(self):
        self.login()  # 登录
        self.open_the_menu(u'运单', u'到货分理')  # 从菜单打开到货分理列表页
        # 激活到货分理frame
        self.click(loc_base.tab[u'首页'])
        self.click(loc_base.tab[u'到货分理'])
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
        db_cy = Db.DB('jshc_carrier')
        sql_cy = "SELECT jot.DeliverCode FROM jshc_o_deliverorder jot WHERE jot.DeliverCode like " + "'" + \
                 pre_code+"%'" + "ORDER BY jot.CreateTime DESC LIMIT 1 "
        old_code = db_cy.query(sql_cy)
        if old_code:
            order_code = int(old_code.__str__()[4:14])+1
        else:
            order_code = pre_code + '0001'
        self.find_element(*(loc.ar_add_order[u'运单号'])).send_keys(order_code)
        return order_code

    def order_from_db(self, order_code):  # 根据录入运单号到DB查询相应运单并返回运单号
        db_cy = Db.DB('jshc_carrier')
        sql_cy = "SELECT jot.DeliverCode FROM jshc_o_deliverorder jot WHERE jot.DeliverCode = '" + str(order_code) + "'"
        code_db = db_cy.query(sql_cy)
        if code_db:
            return True
        else:
            return False
    #
    # def input_s_station(self, station_name):  # 录入发站
    #     # input_list = {'input': loc.ar_add_order[u'发站']['input'], 'item': loc.ar_add_order[u'发站列表1']}
    #     self.input_group(station_name, **loc.ar_add_order[u'发站'])
    #
    # def input_e_station(self, station_name):  # 录入到站
    #     input_list = {'input': loc.ar_add_order[u'到站'], 'item': loc.ar_add_order[u'到站列表1']}
    #     self.input_group(station_name, **input_list)
    #
    # def input_g_name(self, goods_name):  # 录入货物名称
    #     input_list = {'input': loc.ar_add_order[u'货物名称'], 'item': loc.ar_add_order[u'货物列表1']}
    #     self.input_group(goods_name, **input_list)

    # 两个到站装卸费，由于页面JS有特殊处理，所以脚本需要单独处理，否则只能录入为0
    def input_handing_price(self, is_r, test_data):
        action = Ac(self.driver)
        if is_r:  # 为真，表示铁路清算，反之，则为收货人自付
            time.sleep(1)
            action.move_to_element(self.find_element(*(loc.ar_add_order[u'装卸费铁']))).click().perform()
            js = "document.getElementById('EndReceiverHandingPrice').value =" + str(test_data)
            self.driver.execute_script(js)
        else:
            time.sleep(1)
            action.move_to_element(self.find_element(*(loc.ar_add_order[u'装卸费收']))).click().perform()
            js = "document.getElementById('HandingPrice').value = " + str(test_data)
            self.driver.execute_script(js)

    def input_all(self, **all_items):  # 录入所有必填项
        self.select_value(all_items[u'运输方式'], *(loc.ar_add_order[u'运输方式']))
        self.select_value(all_items[u'服务方式'], *(loc.ar_add_order[u'服务方式']))
        self.select_value(all_items[u'支付方式'], *(loc.ar_add_order[u'支付方式']))
        self.input_search(all_items[u'发站'], **loc.ar_add_order[u'发站'])
        self.input_search(all_items[u'到站'], **loc.ar_add_order[u'到站'])
        self.send_keys(all_items[u'发货人'], *(loc.ar_add_order[u'发货人']))
        self.send_keys(all_items[u'收货人'], *(loc.ar_add_order[u'收货人']))
        self.send_keys(all_items[u'发货人手机号'], *(loc.ar_add_order[u'发货人手机号']))
        self.send_keys(all_items[u'收货人手机号'], *(loc.ar_add_order[u'收货人手机号']))
        self.input_search(all_items[u'货物名称'], **loc.ar_add_order[u'货物名称'])
        self.find_element(*(loc.ar_add_order[u'货物包装'])).send_keys(all_items[u'货物包装'])
        self.find_element(*(loc.ar_add_order[u'件数'])).send_keys(all_items[u'件数'])
        self.send_keys(all_items[u'重量'], *(loc.ar_add_order[u'重量']))
        self.send_keys(all_items[u'体积'], *(loc.ar_add_order[u'体积']))
        self.find_element(*(loc.ar_add_order[u'其他费'])).send_keys(all_items[u'其他费'])
        self.input_handing_price(1, all_items[u'装卸费铁'])
        self.input_handing_price(0, all_items[u'装卸费收'])

    def save_submit(self, **all_items):  # 保存并提交，且获取录入的运单号
        self.open_page_add()
        self.input_arrive_date()
        order_code = self.write_order_code()
        self.input_all(**all_items)
        self.click(loc.ar_add_order[u'保存并提交'])
        return order_code

    def get_table_ordercode(self):  # 到货分理列表，获取列表第一行数据的运单号
        self.is_visible(loc.ar_order[u'列表'][u'整体'])
        return self.find_element(*(loc.ar_order[u'列表'][u'运单号1行'])).text  # get_attribute("value")






























