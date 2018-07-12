# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project: 每个字典变量指每个页面的所有元素定位
"""
from selenium.webdriver.common.by import By

# 到货分理列表页
ar_order = {
    u'新增': (By.LINK_TEXT, u'新增到货分理'),
    u'导出': (By.ID, 'btnExport'),
    u'查询条件':{
        'input': {
            u'订单号': (By.ID, 'TransitOrderCode'),
            u'原票号': (By.ID, 'OldBillNum'),
            u'运单号': (By.ID, 'DeliverCode')
            },
        'select': {
            u'运输方式': (By.ID, 'DeliverType')
        },
        'input_search': {
            u'发站': {  # 固定格式
                'input': (By.ID, 'StartPlaceName'),
                'item': (By.XPATH, "//*[@id='searchForm']/div[6]/div/div/ul/table/tbody/tr[1]")
            },
            u'到站': {  # 固定格式
                'input': (By.ID, 'EndPlaceName'),
                'item': (By.XPATH, "//*[@id='searchForm']/div[7]/div/div/ul/table/tbody/tr[1]")
            }
        },
    },
    u'搜索': (By.ID, 'btnSearch'),
    u'重置':(By.ID, 'btnReset'),
    u'列表': {
        u'整体': (By.ID, 'tablelist'),
        u'表头': (By.XPATH, "//*[@id='tablelist']/div[2]/div[1]/table/thead/tr/th"),
        u'第一行': (By.XPATH, "//*[@id='tablelist']/div[2]/div[1]/table/tbody/tr[1]"),
        u'第一行所有数据': (By.XPATH, "//*[@id='tablelist']/div[2]/div[1]/table/tbody/tr[1]/td/span")
    },
}

# 新增到货分理
ar_add_order = {
    'input': {
            u'原票号': (By.ID, 'OldBillNum'),
            u'车厢号': (By.ID, 'CarriageNo'),
            u'发货人': (By.ID, 'ShipperName'),
            u'收货人': (By.ID, 'ReceiverName'),
            u'发货人手机号': (By.ID, 'ShipperPhone'),
            u'收货人手机号': (By.ID, 'ReceiverPhone'),
            u'货物包装': (By.ID, 'GoodsPacking'),
            u'件数': (By.ID, 'TotalCount'),
            u'重量': (By.ID, 'TotalWeight'),
            u'体积': (By.ID, 'TotalVolume'),
            u'其他费': (By.ID, 'OtherPrice'),
    },
    'select': {
            u'运输方式': (By.ID, 'DeliverType'),
            u'服务方式': (By.ID, 'ServiceType'),
            u'支付方式': (By.ID, 'PayType'),
            u'车型': (By.ID, 'GoodsPacking'),
    },
    'input_search': {
            u'客户编码': (By.ID, 'UserNumber'),
            u'客户名称': (By.ID, 'UserName'),
            u'发站': {  # 固定格式
                'input': (By.ID, 'StartPlaceName'),
                'item': (By.XPATH, "//*[@id='shipperForm1']/div[1]/div/div/ul/table/tbody/tr[1]")
                },
            u'到站': {  # 固定格式
                'input': (By.ID, 'EndPlaceName'),
                'item': (By.XPATH, "//*[@id='shipperForm1']/div[2]/div/div/ul/table/tbody/tr[1]")
                },
            u'收货详细地址': (By.ID, ''),
            u'货物名称': {  # 固定格式
                'input': (By.ID, 'CargoTypeId'),
                'item': (By.XPATH, "//*[@id='sel']/table/tbody/tr[1]")
                },
    },
    u'发货地址': (By.ID, "shipperCity"),  # 地区控件只能用id或者name定位
    u'收货地址': (By.ID, "receiverCity"),  # 地区控件只能用id或者name定位
    u'运单号': (By.ID, 'OrderCode'),
    u'到货时间': {
        'input_date': (By.ID, 'Estimatedtime'),
        'box': (By.ID, 'laydate_box'),
        'today': (By.ID, 'laydate_today')
    },
    u'装卸费铁': (By.ID, 'EndReceiverHandingPrice'),
    u'装卸费收': (By.ID, 'HandingPrice'),
    u'保存并提交': (By.ID, 'a-save'),
}

