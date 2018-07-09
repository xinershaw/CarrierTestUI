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
        u'支付审核列表': (By.LINK_TEXT, u'支付审核列表'),
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
    u'运力管理': {
        u'父菜单': (By.LINK_TEXT, u'运力管理'),
        u'站台库':(By.LINK_TEXT, u'站台库'),
        u'司机管理': (By.LINK_TEXT, u'司机管理'),
        u'车辆管理': (By.LINK_TEXT, u'车辆管理'),
        u'承运商管理': (By.LINK_TEXT, u'承运商管理'),
        },
    u'基础信息管理':{
        u'父菜单': (By.LINK_TEXT, u'基础信息管理'),
        u'货物类别': (By.LINK_TEXT, u'货物类别'),
        },
    u'规则设置': {
        u'父菜单': (By.LINK_TEXT, u'规则设置'),
        u'保价规则': (By.LINK_TEXT, u'保价规则'),
        u'代收货款规则': (By.LINK_TEXT, u'代收货款规则'),
        u'重轻货规则': (By.LINK_TEXT, u'重轻货规则'),
        u'铁路站点管理': (By.LINK_TEXT, u'铁路站点管理'),
        u'返单价格': (By.LINK_TEXT, u'返单价格'),
        u'装卸费成本规则': (By.LINK_TEXT, u'装卸费成本规则'),
        u'税费费率规则': (By.LINK_TEXT, u'税费费率规则'),
        u'集装箱接取送达费(遂宁)': (By.LINK_TEXT, u'集装箱接取送达费(遂宁)'),
        u'装卸费(遂宁)': (By.LINK_TEXT, u'装卸费(遂宁)')
    },
    u'权限管理': {
        u'父菜单': (By.LINK_TEXT, u'权限管理'),
        u'人员管理':(By.LINK_TEXT, u'人员管理'),
        u'角色管理': (By.LINK_TEXT, u'角色管理'),
    },
    u'用户管理': {
        u'父菜单': (By.LINK_TEXT, u'用户管理'),
        u'账户管理':(By.LINK_TEXT, u'账户管理')
              },
    u'统计报表': {
        u'父菜单': (By.LINK_TEXT, u'统计报表'),
        u'提货派车成本统计表': (By.LINK_TEXT, u'提货派车成本统计表'),
        u'送货派车成本统计表': (By.LINK_TEXT, u'送货派车成本统计表'),
        u'总表（收入类）': (By.LINK_TEXT, u'总表（收入类）'),
        u'装卸费成本统计表': (By.LINK_TEXT, u'装卸费成本统计表'),
        u'库存报表': (By.LINK_TEXT, u'库存报表'),
        u'到付款查询报表': (By.LINK_TEXT, u'到付款查询报表'),
        u'票据整理报告': (By.LINK_TEXT, u'票据整理报告'),
        u'总表(利润表)': (By.LINK_TEXT, u'总表(利润表)'),
        u'发站收款报表': (By.LINK_TEXT, u'发站收款报表'),
        u'到付款收款报表': (By.LINK_TEXT, u'到付款收款报表'),
        u'干线成本统计表': (By.LINK_TEXT, u'干线成本统计表'),
        u'其他成本统计表': (By.LINK_TEXT, u'其他成本统计表')}
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
    u'站台库': {
        u'站台库': (By.XPATH, "//a[contains(@data-id,'/RailStationWarehouse/index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/RailStationWarehouse/index')]/i")
    },
    u'司机管理': {
        u'司机管理': (By.XPATH, "//a[contains(@data-id,'/Driverex/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Driverex/Index')]/i")
    },
    u'车辆管理': {
        u'车辆管理': (By.XPATH, "//a[contains(@data-id,'/Car/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Car/Index')]/i")
    },
    u'承运商管理': {
        u'承运商管理': (By.XPATH, "//a[contains(@data-id,'/Carrier/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Carrier/Index')]/i")
    },
    u'货物类别': {
        u'货物类别': (By.XPATH, "//a[contains(@data-id,'/Basic/CargoType')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Basic/CargoType')]/i")
    },
    u'保价规则': {
        u'保价规则': (By.XPATH, "//a[contains(@data-id,'/Basic/InsuranceRule')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Basic/InsuranceRule')]/i")
    },
    u'代收货款规则': {
        u'代收货款规则': (By.XPATH, "//a[contains(@data-id,'/Basic/CollectRule')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Basic/CollectRule')]/i")
    },
    u'重轻货规则': {
        u'重轻货规则': (By.XPATH, "//a[contains(@data-id,'/Basic/CargoRule')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Basic/CargoRule')]/i")
    },
    u'铁路站点管理': {
        u'铁路站点管理': (By.XPATH, "//a[contains(@data-id,'/RailStation/index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/RailStation/index')]/i")
    },
    u'返单价格': {
        u'返单价格': (By.XPATH, "//a[contains(@data-id,'/Basic/Recipt')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Basic/Recipt')]/i")
    },
    u'装卸费成本规则': {
        u'装卸费成本规则': (By.XPATH, "//a[contains(@data-id,'/Basic/HandlingCostRule')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Basic/HandlingCostRule')]/i")
    },
    u'税费费率规则': {
        u'税费费率规则': (By.XPATH, "//a[contains(@data-id,'/Basic/TaxFeeRateRule')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Basic/TaxFeeRateRule')]/i")
    },
    u'集装箱接取送达费(遂宁)': {
        u'集装箱接取送达费(遂宁)': (By.XPATH, "//a[contains(@data-id,'/railstation/areapriceindex')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/railstation/areapriceindex')]/i")
    },
    u'装卸费(遂宁)': {
        u'装卸费(遂宁)': (By.XPATH, "//a[contains(@data-id,'/railstation/handingpriceindex')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/railstation/handingpriceindex')]/i")
    },
    u'人员管理': {
        u'人员管理': (By.XPATH, "//a[contains(@data-id,'/Admin/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Admin/Index')]/i")
    },
    u'角色管理': {
        u'角色管理': (By.XPATH, "//a[contains(@data-id,'/Role/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Role/Index')]/i")
    },
    u'账户管理': {
        u'账户管理': (By.XPATH, "//a[contains(@data-id,'/Account/Index')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Account/Index')]/i")
    },
    u'提货派车成本统计表': {
        u'提货派车成本统计表': (By.XPATH, "//a[contains(@data-id,'/Report/SendCarCost')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Report/SendCarCost')]/i")
    },
    u'送货派车成本统计表': {
        u'送货派车成本统计表': (By.XPATH, "//a[contains(@data-id,'/Report/SendGoodsCost')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Report/SendGoodsCost')]/i")
    },
    u'总表（收入类）': {
        u'总表（收入类）': (By.XPATH, "//a[contains(@data-id,'/Report/IncomeReport')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Report/IncomeReport')]/i")
    },
    u'装卸费成本统计表': {
        u'装卸费成本统计表': (By.XPATH, "//a[contains(@data-id,'/Report/HandingCost')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Report/HandingCost')]/i")
    },
    u'库存报表': {
        u'库存报表': (By.XPATH, "//a[contains(@data-id,'/Report/InventoryReport')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Report/InventoryReport')]/i")
    },
    u'到付款查询报表': {
        u'到付款查询报表': (By.XPATH, "//a[contains(@data-id,'/Report/ArriveSearchReport')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Report/ArriveSearchReport')]/i")
    },
    u'票据整理报告': {
        u'票据整理报告': (By.XPATH, "//a[contains(@data-id,'/Report/BillReport')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Report/BillReport')]/i")
    },
    u'总表(利润表)': {
        u'总表(利润表)': (By.XPATH, "//a[contains(@data-id,'/Report/IncomeProfit')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Report/IncomeProfit')]/i")
    },
    u'发站收款报表': {
        u'发站收款报表': (By.XPATH, "//a[contains(@data-id,'/Report/StartStationReport')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Report/StartStationReport')]/i")
    },
    u'到付款收款报表': {
        u'到付款收款报表': (By.XPATH, "//a[contains(@data-id,'/Report/ArriveReceivablesReport')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Report/ArriveReceivablesReport')]/i")
    },
    u'干线成本统计表': {
        u'干线成本统计表': (By.XPATH, "//a[contains(@data-id,'/Report/RailLineCost')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Report/RailLineCost')]/i")
    },
    u'其他成本统计表': {
        u'其他成本统计表': (By.XPATH, "//a[contains(@data-id,'/Report/OtheCost')]"),
        'exit': (By.XPATH, "//a[contains(@data-id,'/Report/OtheCost')]/i")
    },
}

frame = {
    u'首页': (By.XPATH, "//iframe[contains(@data-id,'/Home/Main')]"),
    u'订单管理': (By.XPATH, "//iframe[contains(@data-id,'/TransitOrder/Index')]"),
    u'收货派车': (By.XPATH, "//iframe[contains(@data-id,'/SendCar/Index')]"),
    u'派单': (By.XPATH, "//iframe[contains(@data-id,'/TransitSendOrder/Index')]"),
    u'到货分理': (By.XPATH, "//iframe[contains(@data-id,'/ArriveOrder/Index')]"),
    u'运单管理': (By.XPATH, "//iframe[contains(@data-id,'/DeliverOrder/Index')]"),
    u'入库': (By.XPATH, "//iframe[contains(@data-id,'/DeliverOrder/InStorage')]"),
    u'装车': (By.XPATH, "//iframe[contains(@data-id,'/DeliverOrder/Load')]"),
    u'到货': (By.XPATH, "//iframe[contains(@data-id,'/Arrival/Index')]"),
    u'送货': (By.XPATH, "//iframe[contains(@data-id,'/Delivery/Index')]"),
    u'签收': (By.XPATH, "//iframe[contains(@data-id,'/Sign/Index')]"),
    u'回单': (By.XPATH, "//iframe[contains(@data-id,'/Receipt/Index')]"),
    u'客户管理': (By.XPATH, "//iframe[contains(@data-id,'/CustomerAdd/Index')]"),
    u'冲红': (By.XPATH, "//iframe[contains(@data-id,'/Dash/Index')]"),
    u'到账确认查询': (By.XPATH, "//iframe[contains(@data-id,'/Finance/ReceivablesConfirmList')]"),
    u'支付审核列表': (By.XPATH, "//iframe[contains(@data-id,'/Finance/AuditList')]"),
    u'支付确认列表': (By.XPATH, "//iframe[contains(@data-id,'/Finance/PayList')]"),
    u'收款': (By.XPATH, "//iframe[contains(@data-id,'/Finance/ReceivablesPage')]"),
    u'预付款管理': (By.XPATH, "//iframe[contains(@data-id,'AdvancePayment/Index')]"),
    u'理赔处理': (By.XPATH, "//iframe[contains(@data-id,'/Compensate/Index')]"),
    u'服务异常': (By.XPATH, "//iframe[contains(@data-id,'/ExceptionInfo/Index')]"),
    u'站台库': (By.XPATH, "//iframe[contains(@data-id,'/RailStationWarehouse/index')]"),
    u'司机管理': (By.XPATH, "//iframe[contains(@data-id,'/Driverex/Index')]"),
    u'车辆管理': (By.XPATH, "//iframe[contains(@data-id,'/Car/Index')]"),
    u'承运商管理': (By.XPATH, "//iframe[contains(@data-id,'/Carrier/Index')]"),
    u'货物类别': (By.XPATH, "//iframe[contains(@data-id,'/Basic/CargoType')]"),
    u'保价规则': (By.XPATH, "//iframe[contains(@data-id,'/Basic/InsuranceRule')]"),
    u'代收货款规则': (By.XPATH, "//iframe[contains(@data-id,'/Basic/CollectRule')]"),
    u'重轻货规则': (By.XPATH, "//iframe[contains(@data-id,'/Basic/CargoRule')]"),
    u'铁路站点管理': (By.XPATH, "//iframe[contains(@data-id,'/RailStation/index')]"),
    u'返单价格': (By.XPATH, "//iframe[contains(@data-id,'/Basic/Recipt')]"),
    u'装卸费成本规则': (By.XPATH, "//iframe[contains(@data-id,'/Basic/HandlingCostRule')]"),
    u'税费费率规则': (By.XPATH, "//iframe[contains(@data-id,'/Basic/TaxFeeRateRule')]"),
    u'集装箱接取送达费(遂宁)': (By.XPATH, "//iframe[contains(@data-id,'/railstation/areapriceindex')]"),
    u'装卸费(遂宁)': (By.XPATH, "//iframe[contains(@data-id,'/railstation/handingpriceindex')]"),
    u'人员管理': (By.XPATH, "//iframe[contains(@data-id,'/Admin/Index')]"),
    u'角色管理': (By.XPATH, "//iframe[contains(@data-id,'/Role/Index')]"),
    u'账户管理': (By.XPATH, "//iframe[contains(@data-id,'/Account/Index')]"),
    u'提货派车成本统计表': (By.XPATH, "//iframe[contains(@data-id,'/Report/SendCarCost')]"),
    u'送货派车成本统计表': (By.XPATH, "//iframe[contains(@data-id,'/Report/SendGoodsCost')]"),
    u'总表（收入类）': (By.XPATH, "//iframe[contains(@data-id,'/Report/IncomeReport')]"),
    u'装卸费成本统计表': (By.XPATH, "//iframe[contains(@data-id,'/Report/HandingCost')]"),
    u'库存报表': (By.XPATH, "//iframe[contains(@data-id,'/Report/InventoryReport')]"),
    u'到付款查询报表': (By.XPATH, "//iframe[contains(@data-id,'/Report/ArriveSearchReport')]"),
    u'票据整理报告': (By.XPATH, "//iframe[contains(@data-id,'/Report/BillReport')]"),
    u'总表(利润表)': (By.XPATH, "//iframe[contains(@data-id,'/Report/IncomeProfit')]"),
    u'发站收款报表': (By.XPATH, "//iframe[contains(@data-id,'/Report/StartStationReport')]"),
    u'到付款收款报表': (By.XPATH, "//iframe[contains(@data-id,'/Report/ArriveReceivablesReport')]"),
    u'干线成本统计表': (By.XPATH, "//iframe[contains(@data-id,'/Report/RailLineCost')]"),
    u'其他成本统计表': (By.XPATH, "//iframe[contains(@data-id,'/Report/OtheCost')]"),
}