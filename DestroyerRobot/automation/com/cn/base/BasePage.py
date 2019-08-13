#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/7/15
# @Author  : vivid-XIEMENG
# @FileName: BasePage.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
from selenium import webdriver
from DestroyerRobot.automation.com.cn.util.LoggerUtil import Log
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class BasePage:
    def __init__(self,driver):
        """
        基础数据驱动封装
        :param driver:
        """
        self.driver =driver

    #日志对象
    logger = Log().logger()
##############################################################################
    """
        driver 数据基础操作
    """
    def title(self):
        """
        获取title
        :return:
        """
        self.logger.info("获取title【%s】", self.driver.title )
        self.implicitly_wait()
        time.sleep(2)
        return self.driver.title

    def implicitly_wait(self):
        time.sleep(1)
        self.driver.implicitly_wait(10)

    def getattribut(self,driver_ele, value):
        """
        获取元素中属性
        #ele = self.driver.find_element(page_keyword, ui_keyword)
        #ele = self.driver.find_elements(page_keyword, ui_keyword)
        #ele[0].get_attribute(value)
        :return:
        """
        self.implicitly_wait()
        self.logger.info("获取元素中属性【%s】", driver_ele.get_attribute(value))
        return self.driver_ele.get_attribute(value)

    def get_text(self,driver_ele):
        """
        获取文本内容
        :param driver_ele:  driver_ele = self.driver.find_elements(page_keyword, ui_keyword)
        :return:
        """
        self.logger.info("获取文本内容【%s】", self.driver_ele.text)
        self.implicitly_wait()
        return self.driver_ele.text

    def get_current_url(self):
        """
        获取当前url
        :return:
        """
        self.logger.info("获取当前url【%s】", self.driver.current_url)
        self.implicitly_wait()
        return self.driver.current_url

    def get_url(self, url):
        """
        打开url
        :param url:
        :return:
        """
        self.logger.info("获取当前url【%s】",url)
        self.implicitly_wait()
        return self.driver.get(url)

    def get_driver(self):
        """
        返回当前驱动
        :return:
        """
        self.logger.info("返回当前驱动")
        self.implicitly_wait()
        return self.driver

    def quit(self):
        """
        关闭浏览器以及驱动
        :return:
        """
        self.implicitly_wait()
        self.driver.quit()

    def clear(self,driver_ele):
        """
        清除文本框中的信息
        :param driver_ele:  driver_ele = self.driver.find_elements(page_keyword, ui_keyword)
        :return:
        """
        self.logger.info("清除文本框中的信息")
        self.implicitly_wait()
        return driver_ele.clear()


    def getElementByElement(self, page_keyword, ui_keyword):
        """
        返回定位的单个元素
        :param page_keyword:
        :param ui_keyword:
        获取驱动
            ID = "id"
            XPATH = "xpath"
            LINK_TEXT = "link text"
            PARTIAL_LINK_TEXT = "partial link text"
            NAME = "name"
            TAG_NAME = "tag name"
            CLASS_NAME = "class name"
            CSS_SELECTOR = "css selector"
        :return:
        """
        self.logger.info("点击【%s】的【%s】元素", page_keyword, ui_keyword)
        self.implicitly_wait()
        return self.driver.find_element(page_keyword,ui_keyword)

    def getElementByElements(self, page_keyword, ui_keyword):
        """
        返回定位的单个元素
        :param page_keyword:
        :param ui_keyword:
        获取驱动
            ID = "id"
            XPATH = "xpath"
            LINK_TEXT = "link text"
            PARTIAL_LINK_TEXT = "partial link text"
            NAME = "name"
            TAG_NAME = "tag name"
            CLASS_NAME = "class name"
            CSS_SELECTOR = "css selector"
        :return:
        """
        self.logger.info("点击【%s】的【%s】元素", page_keyword, ui_keyword)
        self.implicitly_wait()
        return self.driver.find_elements(page_keyword,ui_keyword)

    def click(self, driver_ele):
        """
        点击方法
        :param page_keyword:
        :param ui_keyword:
        :return:
        """
        self.logger.info("点击【%s】元素",driver_ele)
        self.driver.implicitly_wait(5)
        driver_ele.click()

    def sendkeys(self,elements,ele_value):
        self.logger.info("通过【%s】的元素，录入信息为：【%s】", elements, ele_value)
        self.implicitly_wait()
        elements.send_keys(ele_value)


    def get_js(self,js_value):
        self.logger.info("js文本内容:【%s】" %js_value)
        self.implicitly_wait()
        self.driver.execute_script(js_value)

    def save_img(self,img_path,time_stamp):
        """
        截图
        :img_path :图片路径
        :time_stamp: 获取时间格式
        :return:
        """
        self.implicitly_wait()
        self.driver.get_screenshot_as_file("%s/error%s.png" %(img_path,time_stamp))

    def maximize_window(self):
        self.implicitly_wait()
        self.driver.maximize_window()

    def alert_accept(self):
        """
        操作alert弹窗
        :return:
        """
        alert = self.driver.switch_to_alert()
        alert.accept()

    def get_alert_text_and_accept(self):
        alert = self.driver.switch_to_alert()
        text = alert.text

        # alert.accept()
        return text


    def get_switch_to_frame(self,driver_ele):
        """
        :Usage:
            driver.switch_to.frame('frame_name')
            driver.switch_to.frame(1)
            driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
            driver.switch_to.parent_frame()
            driver.switch_to.window('main')
        :param driver_ele: driver_ele = self.driver.find_elements(page_keyword, ui_keyword)
        :return:
        """
        self.logger.info("通过【%s】的元素，录入信息为：【%s】", driver_ele)
        self.driver.switch_to_frame(driver_ele)

    def get_switch_to_default_content(self):
        """
        退出iframe
        :return:
        """
        self.driver.switch_to.default_content()

##############################################################



    def ActionChains(self,driver_ele):
        ActionChains(self.driver).move_to_element(driver_ele).perform()



if __name__ == '__main__':
    # driver = Driver().driver()
    # bp =BasePage(driver)
    # bp.get_url("https://www.baidu.com")
    # bp.get_current_url()
    # print(bp.driver)
    # bpdriver =bp.get_driver()
    # print("bpdriver==",bpdriver)
    pass