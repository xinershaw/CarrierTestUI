# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException as NoSuchE
from selenium.webdriver.common.by import By
from pages import page_e_location as loc
from testcase import test_data as td


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
        username = td.login[u'用户名']
        password = td.login[u'密码']
        username_loc = loc.login[u'用户名']
        password_loc = loc.login[u'密码']
        submit_loc = loc.login[u'提交']
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
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except NoSuchE as e:
            print u"页面中未找到这些元素", e

    def switch_frame(self, keyword):
        return self.driver.switch_to.frame(keyword)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except NoSuchE as e:
            print u"%s 页面中未找到元素", e

