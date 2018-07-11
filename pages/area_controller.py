# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AreaController(BasePage):
    def click_area(self, area_type, area_name):
        if self.find_element(*area_type).get_attribute('class') == 'active':  # 如果需要的tab没被选中，则点击选中
            self.click(area_type)
        area_name_loc = (By.LINK_TEXT, area_name)  # 地区在页面中的定位
        self.click(area_name_loc)

    def input_area(self, pro, city, dis, county, *input_loc):
        # document.evaluate("//span[@class='placeholder']", document).iterateNext();  # js通过
        # "//*[@id='shipperForm']/div[4]/div/span/span[1]"
        # "//*[@id='receiveForm']/div[4]/span/span[1]"
        #     self.driver.execute_script(  # 将数字所在span隐藏
        #     "var span=document.getElementsByClassName('city - picker - span');"
        #     "var i=0, len=span.length;"
        #     "for (;i<len;i++)"
        #     "{document.getElementsByClassName('city - picker - span')[i].style.display = 'none';}")
        self.driver.execute_script("document.getElementById('shipperCity').focus()")
        # self.click(input_loc)  # 点击area控件的input
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, 'city-select-wrap')))
        tab_pro = (By.XPATH, "//a[@data-count='province']")
        tab_city = (By.XPATH, "//a[@data-count='city']")
        tab_dis = (By.XPATH, "//a[@data-count='district']")
        tab_county = (By.XPATH, "//a[@data-count='county']")
        self.click_area(tab_pro, pro)
        self.click_area(tab_city, city)
        self.click_area(tab_dis, dis)
        self.click_area(tab_county, county)
