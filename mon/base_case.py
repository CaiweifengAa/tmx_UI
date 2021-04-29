#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/29 10:42
# @Author  : weifeng.cai
# @Email   : weifeng.cai@things-matrix.com
'''
Project: 基础类BasePage，封装所有页面都公用的方法，
定义open函数，重定义find_element，switch_frame，send_keys等函数。
在初始化方法中定义驱动driver，基本url，title
WebDriverWait提供了显式等待方式。
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumbase import BaseCase
from mon import logger
from mon import readconfig
import os

logs = logger.Log()


class BaseTestCase(BaseCase):
    """
    BasePage封装所有页面都公用的方法，例如driver, url ,FindElement等
    """

    # 初始化driver、url、pagetitle等
    # 实例化BasePage类时，最先执行的就是__init__方法，该方法的入参，其实就是BasePage类的入参。
    # __init__方法不能有返回值，只能返回None
    # self只实例本身，相较于类Page而言。
    def __init__(self, selenium_driver, base_url, title):
        self.driver = selenium_driver
        self.base_url = base_url
        self.title = title

    # 通过title断言进入的页面是否正确。
    # 使用title获取当前窗口title，检查输入的title是否在当前title中，返回比较结果（True 或 False）
    def on_page(self, title):
        try:
            return title in self.driver.title
        except:
            logs.error("当前当前窗口页面的title错误")

    # 打开页面，并校验页面链接是否加载正确
    # 以单下划线_开头的方法，在使用import *时，该方法不会被导入，保证该方法为类私有的。
    def _open(self, url):
        # 使用get打开访问链接地址
        self.driver.get(url)
        self.driver.maximize_window()
        # 使用assert进行校验，打开的窗口title是否与配置的title一致。调用on_page()方法
        # assert self.on_page(title), u"打开开页面失败 %s" % url

    # 定义open方法，调用_open()进行打开链接
    def open(self, base_url):
        self._open(self.base_url)

    # 重写元素定位方法
    def find_element(self, *loc):
        #        return self.driver.find_element(*loc)
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            #            WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            logs.error(u"%s 页面中未能找到 %s 元素" % (self, loc))
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    # 重写switch_frame方法
    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)

    # 定义script方法，用于执行js脚本，范围执行结果
    def script(self, src):
        self.driver.execute_script(src)

    # 重写定义send_keys方法
    def send_keys(self, loc, vaule, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            logs.error(u"%s 页面中未能找到 %s 元素" % (self, loc))
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    def save_img(self, img_name):
        try:
            self.driver.get_screenshot_as_file('{}/{}.png'.format(readconfig.img_path, img_name))
            logs.info(img_name + '：已截取屏幕截图')
        except AttributeError:
            logs.error(img_name + ':截取屏幕截图失败')
