#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/7/15
# @Author  : vivid-XIEMENG
# @FileName: TestBaidu.py
# @Software: PyCharm
# @email    ：331597811@QQ.com

from selenium import webdriver
from BeautifulReport import BeautifulReport
from DestroyerRobot.automation.com.cn.markerting_points.servers.MPLoing.test_mplogin import mplogin_test
from DestroyerRobot.automation.com.cn.markerting_points.servers.MPTree.test_mptree import test_mptree
import unittest
class test_login(unittest.TestCase):
    """
    实现unittest操作，到 run目录运行对应脚本操作
    BeautifulReport记录操作失败截图报告
    """
    def setUp(self):
        self.driver = webdriver.Chrome()


    def tearDown(self):
        self.driver.quit()

    @BeautifulReport.add_test_img('test_01_mplogin')#失败后会有报告截图
    def test_01_mplogin(self):
        mplogin = mplogin_test(self.driver)
        login_drivers = mplogin.test_login()
        mptree = test_mptree(login_drivers)
        mptree.get_link_points_shopping()

    # def test_02_mp(self):
    #     pass

if __name__=='__main__':
    unittest.main()
