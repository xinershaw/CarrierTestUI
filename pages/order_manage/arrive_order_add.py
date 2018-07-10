# coding=utf-8
"""
Created on 2018年5月29日
@author: Xiaoxin
Project:新增到货分理页的操作方法
"""
from pages.base import BasePage
from pages.menu import Menu
from pages.element_location import loc_arrive_order as loc
from pages.element_location import loc_base as loc_base
from pages import get_data_DB as Db
import datetime
import time
from selenium.webdriver.common.action_chains import ActionChains as Ac
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ArOrderAdd(BasePage):
    def open_page_add(self):
        self.login()  # 登录
        menu = Menu(self.driver)
        menu.open_the_menu(u'运单', u'到货分理')  # 从菜单打开到货分理列表页
        # 切换至到货分理frame
        self.to_frame(u'到货分理')
        time.sleep(3)  # 强制等待页面（到货分理列表页）加载，否则新增到货分理按钮无法点击
        self.click(loc.ar_order[u'新增'])
        time.sleep(3)  # 强制等待页面（新增到货分理页）加载，否则日期控件无法点击

    def input_arrive_date(self):  # 录入到货时间
        self.click(loc.ar_add_order[u'到货时间']['input_date'])
        self.click(loc.ar_add_order[u'到货时间']['today'])

    def input_order_code(self):
        today = datetime.datetime.now()
        pre_code = today.strftime('%y')+today.strftime('%m')+today.strftime('%d')
        db_cy = Db.DB('jshc_carrier_v2')
        sql_cy = "SELECT jot.DeliverCode FROM jshc_o_deliverorder jot WHERE jot.DeliverCode like " + "'" + \
                 pre_code+"%'" + "ORDER BY jot.CreateTime DESC LIMIT 1 "
        old_code = db_cy.query(sql_cy)
        if old_code:
            order_code = int(old_code.__str__()[4:14])+1
        else:
            order_code = pre_code + '0001'
        self.send_keys(order_code, *loc.ar_add_order[u'运单号'])
        return order_code

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

    def input_order_info(self, **test_data):
        self.input_arrive_date()
        order_code = self.input_order_code()
        td = self.sort_input_items(u'原票号', u'车厢号', u'客户编码', u'客户名称', u'运输方式', u'服务方式', u'支付方式',
                                    **test_data)
        self.input_items(td.items(), **loc.ar_add_order)
        return order_code

    def input_who_info(self, **test_data):
        self.input_search(test_data[u'发站'], **loc.ar_add_order['input_search'][u'发站'])
        self.input_search(test_data[u'到站'], **loc.ar_add_order['input_search'][u'到站'])
        td = self.sort_input_items(u'发货人', u'发货人手机号', u'发货人座机号', u'收货人', u'收货人手机号',
                                    u'收货人座机号', **test_data)
        self.input_items(td.items(), **loc.ar_add_order)

    def input_goods_info(self, **test_data):
        td = self.sort_input_items(u'货物名称', u'箱型', u'箱数', u'重量', u'体积', u'货物包装', u'件数',u'车型',
                                    **test_data)
        self.input_items(td.items(), **loc.ar_add_order)

    def input_other_info(self, **test_data):
        td = self.sort_input_items(u'其他费', u'取送车费', u'代收费用', u'备注', **test_data)
        self.input_items(td.items(), **loc.ar_add_order)
        self.input_handing_price(1, test_data[u'装卸费铁'])
        self.input_handing_price(0, test_data[u'装卸费收'])

    def save_submit(self, **test_data):  # 保存并提交，且获取录入的运单号
        self.open_page_add()
        order_code = self.input_order_info(**test_data)
        self.input_who_info(**test_data)
        self.input_goods_info(**test_data)
        self.input_other_info(**test_data)
        self.click(loc.ar_add_order[u'保存并提交'])
        WebDriverWait(self.driver, 25).until(EC.invisibility_of_element_located(loc.ar_add_order[u'保存并提交']))
        return order_code






























