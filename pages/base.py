# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException as NoSuchE
from pages.element_location import loc_base as locator
from test_data import td_login as td_l
from selenium.webdriver.support.select import Select


class BasePage(object):
    def __init__(self, driver, base_url='http://cy.tuluo56.com/Home/Login'):
        self.driver = driver
        self.base_url = base_url
        self.log_dir = "F:\\pythonPJ\\platfrom_test\\report\\"

    def _open(self, url):  # 打开页面并最大化窗口
        self.driver.get(url)
        try:
            self.driver.maximize_window()
        except BaseException as e:
            print '窗口未能最大化', e

    def open(self):
        self._open(self.base_url)

    def login(self):
        username = td_l.login[u'用户名']
        password = td_l.login[u'密码']
        username_loc = locator.login[u'用户名']
        password_loc = locator.login[u'密码']
        submit_loc = locator.login[u'提交']
        self.open()
        try:
            self.find_element(*username_loc).send_keys(username)
            self.find_element(*password_loc).send_keys(password)
            self.find_element(*submit_loc).click()
        except Exception as e:
            print "登录失败！", e

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except NoSuchE as e:
            print u"页面中未找到这个元素 ", e

    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except NoSuchE as e:
            print u"页面中未找到这些元素", e

    def to_frame(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(self.find_element(*loc)))
        except NoSuchE as e:
            print u"切换到此frame失败！", e

    def send_keys(self, value, *loc):
        # clear_first = True, click_first = True
        try:
            # loc = getattr(self, "_%s" % loc)
            self.find_element(*loc).click()
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except NoSuchE as e:
            print u"%s 页面中未找到元素", e

    def click(self, loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc)).click()
        except NoSuchE as e:
            print u'点击该元素失败', e

    def is_visible(self, loc):  # 页面是否可见，若是，返回元素对象；反之，返回False
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            print u'尚未定位到该元素！', e

    def open_the_menu(self, parent, node=''):  # 点击页面左侧菜单
        try:
            if not node:
                self.find_element(*(locator.menu[parent])).click()
            else:
                self.find_element(*(locator.menu[parent][u'父菜单'])).click()  # 展开父菜单
                self.find_element(*(locator.menu[parent][node])).click()  # 打开子菜单
        except Exception as e:
            print u'打开菜单失败！', e

    def get_tab_name(self, tab):  # 打开页面后，获取相应的选项卡名称
        return self.find_element(*locator.tab[tab][tab]).text

    def close_tab(self, tab):  # 关闭选项卡
        try:
            self.click(locator.tab[tab]['exit'])
        except Exception as e:
            print u'关闭此tab页失败！', e

    def input_search(self, key_word, **loc_input_item):  # 发、到站、货物等下拉列表选择
        self.find_element(*loc_input_item['input']).send_keys(key_word)  # 先录入关键字
        self.click(loc_input_item['item'])  # 展开的下拉项中点击选择第一项

    def select_value(self, value, *loc_select):  # select下拉列表选择某一项
        s = self.find_element(*loc_select)  # loc_select 是指下拉项input的元素定位
        Select(s).select_by_visible_text(value)  # value是指下拉列表中的文本

    def sort_input_items(self, *items, **test_data):  # 挑选要录入的文本框(items),test_data指test_data路径下的测试数据
        td = dict()
        for i in items:
            try:
                td.update({i: test_data[i]})
            except KeyError:
                continue
        return td

    def input_items(self, *test_data, **locators):
        """ locators={
                input:{
                item1:[value, loc],
                item2:[value, loc],
                ......},
                select:{
                item1:[value, loc],
                item2:[value, loc],
                ......},
                input_search:{
                item1:[value, **loc],
                item2:[value, **loc],
                ......}},
            test_data={item1:data1,
                       item2:data2,
                       .........}
        """
        for t in test_data[0]:
            if t[0] in locators['input']:
                self.send_keys(t[1], *locators['input'][t[0]])
            elif t[0] in locators['select']:
                self.select_value(t[1], *locators['select'][t[0]])
            elif t[0] in locators['input_search']:
                self.input_search(t[1], **locators['input_search'][t[0]])
            else:
                continue


