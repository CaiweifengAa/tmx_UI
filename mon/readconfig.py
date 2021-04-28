#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 14:49
# @Author  : weifeng.cai
# @Email   : weifeng.cai@things-matrix.com
import os
import configparser

# ConfigParser 是用来读取配置文件的包。配置文件的格式如下：中括号“[ ]”内包含的为section。section 下面为类似于key-value 的配置内容


cur_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前目录绝对路径
# 获取当前目录的上级目录绝对路径
config_path = os.path.dirname(cur_path) + "\\config\\config.ini"
report_path = os.path.dirname(cur_path) + "\\HtmlReport"
data_path = os.path.dirname(cur_path) + "\\data\\test_data.yml"
drivers_path = os.path.dirname(cur_path) + "\\drivers\\chromedriver.exe"
test_data_path = os.path.dirname(cur_path) + "\\data\\test_data.yml"
# img_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\\HtmlReport\\img"
img_path = os.path.dirname(cur_path) + "\\img"

# print(data_path)

conf = configparser.ConfigParser()
conf.read(config_path, encoding='utf-8')  # 直接读取ini文件内容
# 获取配置文件eamil的值
smtp_server = conf.get("email", "smtp_server")
sender = conf.get("email", "sender")
psw = conf.get("email", "psw")
receiver = conf.get("email", "receiver")
port = conf.get("email", "port")
cc = conf.get("email", "cc")
body = conf.get("email", "body")
title = conf.get("email", "title")
# 获取测试地址
test_url = conf.get("测试环境地址", "url")
