#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 14:35
# @Author  : weifeng.cai
# @Email   : weifeng.cai@things-matrix.com
import unittest
from BeautifulReport import BeautifulReport
# from SendEmail import send_email
import test_cases.test_login
from test_cases import *
from mon import logger
# import readconfig
import pytest


# 测试用例模板
def test_case_all():
    log = logger.Log()

    log.info("------------开始执行所有测试用例---------------")
    # 方法1：
    test_suite = unittest.defaultTestLoader.discover('test_cases', pattern='test*.py')
    BeautifulReport(test_suite).report(filename='TMX_ui_Test_result', description='TMX系统ui自动化测试',
                                       log_path='./HtmlReport')
    # 方法2：
    # suite = unittest.TestSuite()
    # # # #makeSuite()方法，一次性加载一个类文件下所有测试用例到suite中去
    # suite.addTest(unittest.makeSuite(test_cases.test_login.Login_page))
    # BeautifulReport(suite).report(filename='TMX_UI_Test_result', description='TMX自动化测试',
    #                               log_path="./HtmlReport")  # log_path='.'把report放到当前目录下
    log.info("------------测试完成生成测试报告---------------")
    #  发送邮件
    #     send_email().outlook()
    #     log.info("邮件发送完成！")


if __name__ == '__main__':
    # pytest.main(["-v", './test_case/test_api.py::test_Telemetry_API.py::test_use_api.py'])
    test_case_all()
