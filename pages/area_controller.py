# coding=utf-8
"""
Created on 2018年7月12日
@author: Xiaoxin
Project: 地区控件
"""
from pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AreaController(BasePage):
    def click_area(self, area_tab_loc, area_name):
        if self.find_element(*area_tab_loc).get_attribute('class') == 'active':  # 如果需要的tab没被选中，则点击选中
            self.click(area_tab_loc)
        area_name_loc = (By.LINK_TEXT, area_name)  # 地名在控件中的定位
        self.click(area_name_loc)

    def open_controller(self, *input_loc):
        # 弹出地区控件的触发事件是input的focus，但被下面的span干扰，无法通过点击实现，只能通过js聚焦实现
        if 'id' in input_loc[0]:  # 如果地区控件是通过id定位,
            js = "document.getElementById('" + input_loc[1] + "').focus()"
            # js = "document.getElementById('shipperCity').focus()"
        else:  # 如果地区控件是通过name定位
            js = "document.getElementsByName('" + input_loc[1] + "')[0].focus()"
        self.driver.execute_script(js)  # 弹出地区控件
        try:
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, 'city-select-wrap')))
        except BaseException as e:
            print '打开地区控件失败！', e

    def input_area(self, pro, city, dis, county, *input_loc):
        self.open_controller(*input_loc)
        self.click_area((By.XPATH, "//a[@data-count='province']"), pro)
        self.click_area((By.XPATH, "//a[@data-count='city']"), city)
        self.click_area((By.XPATH, "//a[@data-count='district']"), dis)
        self.click_area((By.XPATH, "//a[@data-count='county']"), county)

    def input_clear(self, *input_loc):  # 地区控件中的清空按钮
        self.open_controller(*input_loc)
        self.click((By.XPATH, "//div[@class='city-picker-dropdown' and contains(@style,'block')]/div/div/input"))


