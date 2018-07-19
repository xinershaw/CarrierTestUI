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


class Menu(BasePage):
    def clear_label_info_js(self, class_name):
        list_str = [
            "var labels = document.getElementsByClassName('",
            class_name,
            "');var i=0, len=labels.length;for (;i<len;i++)",
            "{document.getElementsByClassName('",
            class_name,
            "')[i].style.display = 'none';}"
        ]
        return ''.join(list_str)

    def is_parent(self, menu_name):
        try:
            return u'父菜单' in loc_base.menu[menu_name]
        except KeyError:
            return False

    def click_parent(self, parent):
        x_str = "//a[@title='" + parent + "']/.."
        if self.find_element(*(By.XPATH, x_str)).get_attribute('class') != 'active':
            if not self.is_visible(loc_base.menu[parent][u'父菜单']):
                self.scroll_into_loc((By.XPATH, "//*[@id='side-menu']/li[last()]"))
            if parent in [u'订单', u'异常及理赔'] and self.is_visible((By.CLASS_NAME, 'r label label-info')):
                self.driver.execute_script(self.clear_label_info_js('r label label-info'))
            self.click(loc_base.menu[parent][u'父菜单'])

    def click_son(self, parent, son):
        if not self.is_visible(loc_base.menu[parent][son]):
            self.scroll_into_loc((By.XPATH, "//li[@class='active']/ul/li[last()]/a"))
        if parent in [u'订单', u'异常及理赔'] and self.is_visible((By.CLASS_NAME, 'r label label-info pull-right')):
            self.driver.execute_script(self.clear_label_info_js('r label label-info pull-right'))
        self.click(loc_base.menu[parent][son])  # 打开子菜单

    def open_the_menu(self, parent, son=''):  # 点击页面左侧菜单
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.ID, 'side-menu')))
        try:
            if not son:  # 没有子菜单
                self.click_parent(parent)
                return self.find_element(*loc_base.tab[parent][parent]).text  # 返回tab名称
            else:  # 存在子菜单
                self.click_parent(parent)
                self.click_son(parent, son)
                # self.click_parent(parent)
            return self.find_element(*loc_base.tab[son][son]).text  # 返回tab名称
        except BaseException as e:
            print u'打开菜单失败！', parent, son, e


