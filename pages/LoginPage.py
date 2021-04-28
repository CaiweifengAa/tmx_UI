#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 17:54
# @Author  : weifeng.cai
# @Email   : weifeng.cai@things-matrix.com
'''
Project_page:页面基本操作方法：如open，input_username，input_password，click_submit
'''
from selenium.webdriver.common.by import By
from mon.base_case import BaseTestCase
# 继承BasePage类
class loginPage(BaseTestCase):
    # 定位器，通过元素属性定位元素对象
    username_loc = (By.ID, 'username')
    password_loc = (By.ID, 'textPassword')
    submit_loc = (By.XPATH, '//*[@id="form-user"]/button')
    span_loc = (By.CSS_SELECTOR, "div.error-tt>p")
    dynpw_loc = (By.ID, "lbDynPw")
    userid_loc = (By.ID, "spnUid")
    login_message_loc = (By.CSS_SELECTOR, ".avatar-img.dropdown-box-title")

    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self, base_url):
        # 调用page中的_open打开连接
        self._open(self.base_url)

    # 输入用户名：调用send_keys对象，输入用户名
    def input_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    # 输入密码：调用send_keys对象，输入密码
    def input_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    # 点击登录：调用send_keys对象，点击登录
    def click_login(self):
        self.find_element(*self.submit_loc).click()

    # 用户名或密码不合理是Tip框内容展示
    def show_span(self):
        return self.find_element(*self.span_loc).text

    # 切换登录模式为动态密码登录（IE下有效）
    def swich_DynPw(self):
        self.find_element(*self.dynpw_loc).click()

    # 登录成功页面中的用户ID查找
    def show_userid(self):
        return self.find_element(*self.userid_loc).text

    # 断言登录成功
    def login_success_asset(self, message):
        assert message in self.find_element(*self.login_message_loc).text

    # 断言登录成功
    def login_F_asset(self, message):
        assert message in self.find_element(*self.submit_loc).text






