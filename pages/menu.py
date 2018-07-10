# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from pages.base import BasePage
from selenium.webdriver.common.by import By
from pages.element_location import loc_base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver


class Menu(BasePage):
    def pre_son_click(self, loc):  # 只针对二级菜单
        if not self.is_clickable(loc):
            self.driver.execute_script(
                "var labels = document.getElementsByClassName('r label label-info pull-right');"
                "var i=0, len=labels.length;"
                "for (;i<len;i++)"
                "{document.getElementsByClassName('r label label-info pull-right')[i].style.display = 'none';}")
        if not self.is_visible(loc):
            son_obj = self.find_elements(*(By.XPATH, "//li[@class='active']/ul/li/a"))
            self.driver.execute_script("arguments[0].scrollIntoView();", son_obj[-1])

    def pre_parent_click(self, loc):   # 只针对父菜单
        if not self.is_clickable(loc):  # 菜单a被数字遮挡无法点击，如新增订单后，新增异常后
            self.driver.execute_script(  # 将数字所在span隐藏
                "var label=document.getElementsByClassName('r label label-info');"
                "var i=0, len=label.length;"
                "for (;i<len;i++)"
                "{document.getElementsByClassName('r label label-info')[i].style.display = 'none';}")
        # if not self.is_visible(loc):  # 需要拖动滚动条才能点击菜单，直接拖动滚动条到菜单所在div底部
        #     parent_obj = self.find_elements(*(By.XPATH, "//*[@id='side-menu']/li"))
        #     self.driver.execute_script("arguments[0].scrollIntoView();", parent_obj[-1])

    def open_the_menu(self, parent, son=''):  # 点击页面左侧菜单
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.ID, 'side-menu')))
        # time.sleep(5)
        # print self.find_element(*loc_base.menu[parent][u'父菜单']).is_displayed()
        # print self.find_element(*(By.CLASS_NAME, 'sidebar-collapse')).location
        try:
            if not son:  # 没有子菜单
                self.pre_parent_click(loc_base.menu[parent])
                self.click(loc_base.menu[parent])
                return self.find_element(*loc_base.tab[parent][parent]).text  # 返回tab名称
            else:  # 存在子菜单
                self.pre_parent_click(loc_base.menu[parent][u'父菜单'])
                self.click(loc_base.menu[parent][u'父菜单'])  # 展开父菜单
                self.pre_son_click(loc_base.menu[parent][son])
                self.click(loc_base.menu[parent][son])  # 打开子菜单
                self.pre_parent_click(loc_base.menu[parent][u'父菜单'])
                self.click(loc_base.menu[parent][u'父菜单'])  # 收起子菜单（这一步不可少）
                return self.find_element(*loc_base.tab[son][son]).text  # 返回tab名称
        # raise Exception
        except BaseException as e:
            print u'打开菜单失败！', parent, son, e


