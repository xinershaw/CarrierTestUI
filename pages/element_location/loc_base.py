# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from selenium.webdriver.common.by import By

login = {
    u'用户名': (By.ID, 'Account'),
    u'密码': (By.ID, 'Password'),
    u'提交': (By.ID, 'btnLogin')
}

menu = {
    u'订单': {
        u'父菜单': (By.LINK_TEXT, u'订单'),
        u'订单管理': (By.LINK_TEXT, u'订单管理'),
        u'收货派车': (By.LINK_TEXT, u'收货派车')
    },
    u'派单': (By.LINK_TEXT,  u'派单'),
    u'运单':{
        u'父菜单': (By.LINK_TEXT, u'运单'),
        u'到货分理': (By.LINK_TEXT, u'到货分理'),
        u'运单管理': (By.LINK_TEXT, u'运单管理'),
        u'入库': (By.LINK_TEXT, u'入库'),
        u'装车': (By.LINK_TEXT, u'装车'),
        u'到货': (By.LINK_TEXT, u'到货'),
        u'送货': (By.LINK_TEXT, u'送货'),
        u'签收': (By.LINK_TEXT, u'签收'),
        u'回单': (By.LINK_TEXT, u'回单')
    },
    u'财务管理': {
        u'父菜单': (By.LINK_TEXT, u'财务管理'),
        u'冲红': (By.LINK_TEXT, u'冲红'),
        u'到账确认查询': (By.LINK_TEXT, u'到账确认查询'),
        u'支付审核列表': (By.LINK_TEXT, u'支付审核列表  '),
        u'支付确认列表': (By.LINK_TEXT, u'支付确认列表'),
        u'收款': (By.LINK_TEXT, u'收款'),
        u'预付款管理': (By.LINK_TEXT, u'预付款管理'),
    },
    u'异常及理赔': {
        u'父菜单': (By.LINK_TEXT, u'异常及理赔'),
        u'理赔处理': (By.LINK_TEXT, u'理赔处理'),
        u'服务异常': (By.LINK_TEXT, u'服务异常'),
    },
    u'客户管理': (By.XPATH, "//a[@title='客户管理']/span"),
    u'运力管理': (By.LINK_TEXT, u'运力管理'),
    u'基础信息管理': (By.LINK_TEXT, u'基础信息管理'),
}

tab = {
    u'首页': (By.ID, 'firstPage'),  # 首页选项卡
    u'订单管理':{
        u'订单管理': (By.XPATH, "//a[contains(@data-id,'/TransitOrder/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/TransitOrder/Index')]/i")
    },
    u'收货派车':{
        u'收货派车': (By.XPATH, "//a[contains(@data-id,'/SendCar/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/SendCar/Index')]/i")
    },
    u'派单':{
        u'派单': (By.XPATH, "//a[contains(@data-id,'/TransitSendOrder/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/TransitSendOrder/Index')]/i")
    },
    u'到货分理': {
        u'到货分理': (By.XPATH, "//a[contains(@data-id,'/ArriveOrder/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/ArriveOrder/Index')]/i")
    },
    u'运单管理': {
        u'运单管理': (By.XPATH, "//a[contains(@data-id,'/DeliverOrder/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/DeliverOrder/Index')]/i")
    },
    u'入库': {
        u'入库': (By.XPATH, "//a[contains(@data-id,'/DeliverOrder/InStorage')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/DeliverOrder/InStorage')]/i")
    },
    u'装车': {
        u'装车': (By.XPATH, "//a[contains(@data-id,'/DeliverOrder/Load')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/DeliverOrder/Load')]/i")
    },
    u'到货': {
        u'到货': (By.XPATH, "//a[contains(@data-id,'/Arrival/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Arrival/Index')]/i")
    },
    u'送货': {
        u'送货': (By.XPATH, "//a[contains(@data-id,'/Delivery/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Delivery/Index')]/i")
    },
    u'签收': {
        u'签收': (By.XPATH, "//a[contains(@data-id,'/Sign/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Sign/Index')]/i")
    },
    u'回单': {
        u'回单': (By.XPATH, "//a[contains(@data-id,'/Receipt/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Receipt/Index')]/i")
    },
    u'客户管理': {
        u'客户管理': (By.XPATH, "//a[contains(@data-id,'/CustomerAdd/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/CustomerAdd/Index')]/i")
    },
    u'冲红': {
        u'冲红': (By.XPATH, "//a[contains(@data-id,'/Dash/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Dash/Index')]/i")
    },
    u'到账确认查询': {
        u'到账确认查询': (By.XPATH, "//a[contains(@data-id,'/Finance/ReceivablesConfirmList')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Finance/ReceivablesConfirmList')]/i")
    },
    u'支付审核列表': {
        u'支付审核列表': (By.XPATH, "//a[contains(@data-id,'/Finance/AuditList')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Finance/AuditList')]/i")
    },
    u'支付确认列表': {
        u'支付确认列表': (By.XPATH, "//a[contains(@data-id,'/Finance/PayList')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Finance/PayList')]/i")
    },
    u'收款': {
        u'收款': (By.XPATH, "//a[contains(@data-id,'/Finance/ReceivablesPage')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Finance/ReceivablesPage')]/i")
    },
    u'预付款管理': {
        u'预付款管理': (By.XPATH, "//a[contains(@data-id,'AdvancePayment/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'AdvancePayment/Index')]/i")
    },
    u'理赔处理': {
        u'理赔处理': (By.XPATH, "//a[contains(@data-id,'/Compensate/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Compensate/Index')]/i")
    },
    u'服务异常': {
        u'服务异常': (By.XPATH, "//a[contains(@data-id,'/ExceptionInfo/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/ExceptionInfo/Index')]/i")
    },
}