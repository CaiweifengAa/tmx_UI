#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 18:06
# @Author  : weifeng.cai
# @Email   : weifeng.cai@things-matrix.com
import time
import unittest
from pages import LoginPage
import sys
from BeautifulReport import BeautifulReport
from selenium import webdriver
from mon import readconfig
import pytest
from parameterized import parameterized
from mon import logger

logs = logger.Log()


class Login_page(unittest.TestCase):
    def save_img(self, img_name):  # ###################失败截图方法（必须要定义在class中）
        login_page.save_img(img_name)

        # try:
        #     self.driver.get_screenshot_as_file('{}/{}.png'.format(readconfig.img_path, img_name))
        #     logs.info(img_name + '：已截取屏幕截图')
        # except AttributeError:
        #     logs.error(img_name + ':截取屏幕截图失败')

    def setUp(self, masterqa_mode=False):
        """前置方法，打开登录页面，每个测试用例执行前自动调用"""
        self.url = readconfig.test_url
        global login_page
        super(Login_page, self)
        self.driver = webdriver.Chrome(readconfig.drivers_path)
        self.driver.implicitly_wait(30)
        # test_Data
        self.username = "admin@things-matrix.com"
        self.passward = "TMXtest2019"
        self.login_success_asset = "ZR"
        self.Sign_in = "Sign In"
        self.page_title = "Home"
        login_page = LoginPage.loginPage(self.driver, self.url, u"登录")
        login_page.open(self)

    def tearDown(self):
        self.driver.quit()

    @pytest.mark.somke
    # #########################################################截图需用到的装饰器，在用例里面调用前面定义的save_img方法
    @BeautifulReport.add_test_img('test_01_login_success')  # 失败后会有报错截图
    def test_01_login_success(self):
        """输入正常的用户名和密码登录成功"""
        # 声明LoginPage类对象,# 初始化driver、url、title等
        login_page.input_username(self.username)
        login_page.input_password(self.passward)
        login_page.click_login()
        login_page.on_page(self.page_title)
        try:
            login_page.login_success_asset(self.login_success_asset)
            logs.info("用例:" + sys._getframe().f_code.co_name + "测试通过")
        except:
            logs.error("用例:" + sys._getframe().f_code.co_name + "执行失败")
            login_page.login_success_asset(self.login_success_asset)

    @parameterized.expand([("weifeng.cai@things-matrix.com", "invalid_password"),
                           ("invalid_username", "TMXtest2019"),
                           ("", "TMXtest2019")
                           ])
    @pytest.mark.fail
    @BeautifulReport.add_test_img('test_02_login_fail')
    # @BeautifulReport.stop  # 不执行该用例
    def test_02_login_fail(self, username, pwd):
        """输入错误的用户名和密码登录失败"""
        login_page.input_username(username)
        login_page.input_password(pwd)
        login_page.click_login()
        try:
            login_page.login_F_asset(self.Sign_in)
            logs.info("用例:" + sys._getframe().f_code.co_name + "测试通过")
        except:
            logs.error("用例:" + sys._getframe().f_code.co_name + "执行失败")
            login_page.login_success_asset(self.Sign_in)


if __name__ == "__main__":
    unittest.main()
