# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from selenium.webdriver.common.by import By

# 到货分理列表
ar_order = {
    u'首页': (By.ID, 'firstPage'),  # 首页选项卡
    u'到货分理': (By.XPATH, "//a[contains(@data-id,'/ArriveOrder/Index')]"),  # 到货分理选项卡
    'frame': (By.NAME, 'iframe4'),
    # u'新增': (By.XPATH, "//*[@id='searchForm']/div[12]/a"),
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
        u'搜索': (),
        },
    u'列表': {
        u'整体': (By.ID, 'tablelist'),
        u'运单号表头': (By.XPATH, "//*[@id='tablelist']/div[2]/div[1]/table/thead/tr/th[3]"),
        u'运单号1行': (By.XPATH, "//*[@id='tablelist']/div[2]/div[1]/table/tbody/tr[1]/td[3]/span")
    },
    # u'': (),
    # u'': (),
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
    u'发站': {  # 固定格式
        'input': (By.ID, 'StartPlaceName'),
        'item': (By.XPATH, "//*[@id='shipperForm']/div[1]/div/div/ul/table/tbody/tr[1]")
        },
    u'到站': {  # 固定格式
        'input': (By.ID, 'EndPlaceName'),
        'item': (By.XPATH, "//*[@id='receiveForm']/div[1]/div/div/ul/table/tbody/tr[1]")
        },
    u'发货人': (By.ID, 'ShipperName'),
    u'收货人': (By.ID, 'ReceiverName'),
    u'发货人手机号': (By.ID, 'ShipperPhone'),
    u'收货人手机号': (By.ID, 'ReceiverPhone'),
    u'收货人地址': (By.ID, ''),
    u'货物名称': {  # 固定格式
        'input': (By.ID, 'CargoTypeId'),
        'item': (By.XPATH, "//*[@id='sel']/table/tbody/tr[1]")
        },
    u'车型': (By.ID, 'GoodsPacking'),
    u'货物包装': (By.ID, 'GoodsPacking'),
    u'件数': (By.ID, 'TotalCount'),
    u'重量': (By.ID, 'TotalWeight'),
    u'体积': (By.ID, 'TotalVolume'),
    u'装卸费铁': (By.ID, 'EndReceiverHandingPrice'),
    u'装卸费收': (By.ID, 'HandingPrice'),
    u'保存并提交': (By.ID, 'a-save'),
    u'其他费': (By.ID, 'OtherPrice'),
}

