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
    def clear_info_count(self, class_name):
        # 待处理记录条数会遮挡菜单，导致无法点击，因此点击前需要先将记录条数的display修改为none
        list_str = [
            "var labels = document.getElementsByClassName('",
            class_name,
            "');var i=0, len=labels.length;for (;i<len;i++)",
            "{document.getElementsByClassName('",
            class_name,
            "')[i].style.display = 'none';}"
        ]
        self.driver.execute_script(''.join(list_str))
        # return ''.join(list_str)

    def is_parent(self, menu_name):
        try:
            return u'父菜单' in loc_base.menu[menu_name]
        except KeyError:
            return False

    def is_dink(self, parent):  # 是否有子菜单
        try:
            if isinstance(loc_base.menu[parent], dict):
                return False
            else:
                return True
        except BaseException as e:
            print u'is_dink报错：', parent, e

    def is_parent_visible(self, parent):  # 父菜单是否可见
        if self.is_dink(parent):
            return self.is_visible(loc_base.menu[parent])
        else:
            return self.is_visible(loc_base.menu[parent][u'父菜单'])

    def click_parent(self, parent):
        x_str = "//a[@title='" + parent + "']/.."
        if self.find_element(*(By.XPATH, x_str)).get_attribute('class') != 'active':
            info_count_loc = (By.XPATH, "//span[@class='r label label-info']")
            if parent in [u'订单', u'异常及理赔'] and self.is_visible(info_count_loc):
                # self.driver.execute_script(self.clear_label_info_js('r label label-info'))
                self.clear_info_count('r label label-info')
            if not self.is_parent_visible(parent):
                link_obj = self.find_elements(*(By.XPATH, "//*[@id='side-menu']/li"))
                self.scroll_into_loc(link_obj[-1])
            try:
                if not self.is_dink(parent):
                    self.click(loc_base.menu[parent][u'父菜单'])
                else:
                    self.click(loc_base.menu[parent])
            except BaseException as e:
                print u'打开父菜单失败！', parent, e

    def click_son(self, parent, son):
        info_count_loc = (By.XPATH, "//span[@class='r label label-info pull-right']")  # 待处理记录条数的xpath
        if parent in [u'订单', u'异常及理赔'] and self.is_visible(info_count_loc):
            # self.driver.execute_script(self.clear_label_info_js('r label label-info pull-right'))
            self.clear_info_count('r label label-info pull-right')
        if not self.is_visible(loc_base.menu[parent][son]):
            link_obj = self.find_elements(*(By.XPATH, "//li[@class='active']/ul/li/a"))
            self.scroll_into_loc(link_obj[-1])
        try:
            self.click(loc_base.menu[parent][son])  # 打开子菜单
        except BaseException as e:
            print u'打开子菜单失败', son, e

    def open_the_menu(self, parent, son=''):  # 点击页面左侧菜单
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.ID, 'side-menu')))
        try:
            if not son:  # 没有子菜单
                self.click_parent(parent)
                return self.find_element(*loc_base.tab[parent][parent]).text  # 返回tab名称
            else:  # 存在子菜单
                self.click_parent(parent)
                self.click_son(parent, son)
                return self.find_element(*loc_base.tab[son][son]).text  # 返回tab名称
        except BaseException as e:
            print u'打开菜单失败！', parent, son, e


