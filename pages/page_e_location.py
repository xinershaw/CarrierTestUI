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

navbar ={
    u'订单': (By.LINK_TEXT, u'订单'),
    u'派单': (By.LINK_TEXT,  u'派单'),
    u'运单':{
        u'父菜单': (By.LINK_TEXT, u'运单'),
        u'到货分理': (By.LINK_TEXT, u'到货分理'),
        u'运单管理': (By.LINK_TEXT, u'运单管理'),
        u'入库': (By.LINK_TEXT, u'入库'),
        u'装车': (By.LINK_TEXT, u'装车'),
        u'到货': (By.LINK_TEXT, u'到货'),
        u'送货': (By.LINK_TEXT, u'送货'),
        u'签收': (By.LINK_TEXT, '签收'),
        u'回单': (By.LINK_TEXT, '回单')
    },
    u'财务管理': (By.LINK_TEXT, u'财务管理'),
    u'异常及理赔': (By.LINK_TEXT, u'异常及理赔'),
    u'客户管理': (By.LINK_TEXT, u'客户管理'),
    u'运力管理': (By.LINK_TEXT, u'运力管理'),
    u'基础信息管理': (By.LINK_TEXT, u'基础信息管理'),
}

# 到货分理
ar_order = {
    u'首页': (By.ID, 'firstPage'),  # 首页选项卡
    u'到货分理': (By.XPATH, "//a[contains(@data-id,'/ArriveOrder/Index')]"),  # 到货分理选项卡
    'frame': (By.NAME, 'iframe4'),
    # u'新增': (By.XPATH, "//*[@id='searchForm']/div[12]/a"),
    u'新增': (By.LINK_TEXT, u'新增到货分理'),
    u'导出': (By.ID, 'btnExport'),
    u'搜索': (By.ID, 'btnSearch'),
    u'查询条件':{
        u'订单号': (By.ID, 'TransitOrderCode'),
        u'原票号': (By.ID, 'OldBillNum')
    }
}

# 新增到货分理
ar_add_order = {
    u'到货时间': {
        'input_date': (By.ID, 'Estimatedtime'),
        'box': (By.ID, 'laydate_box'),
        'today': (By.ID, 'laydate_today')
              },
    u'运单号': (By.ID, 'OrderCode'),
    u'原票号': (By.ID, 'OldBillNum'),
    u'车厢号': (By.ID, 'CarriageNo'),
    u'客户编码': (By.ID, 'UserNumber'),
    u'客户名称': (By.ID, 'UserName'),
    u'运输方式': (By.ID, 'DeliverType'),
    u'服务方式': (By.ID, 'ServiceType'),
    u'支付方式': (By.ID, 'PayType'),
    u'发站': (By.ID, ''),
    u'到站': (By.ID, ''),
    u'发货人': (By.ID, 'ShipperName'),
    u'收货人': (By.ID, 'ReceiverName'),
    u'发货人手机号': (By.ID, 'ShipperPhone'),
    u'收货人手机号': (By.ID, 'ReceiverPhone'),
    u'收货人地址': (By.ID, ''),
    u'货物名称': (By.ID, ''),
    u'货物包装': (By.ID, 'GoodsPacking'),
    u'件数': (By.ID, 'TotalCount'),
    u'重量': (By.ID, 'TotalWeight'),
    u'体积': (By.ID, 'TotalVolume'),
    u'装卸费铁': (By.ID, 'ERHandingPrice'),
    u'装卸费收': (By.ID, 'HandingPrice')}
    # u'': (By., ''),
    # u'': (By., ''),

