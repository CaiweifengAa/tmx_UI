#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 16:16
# @Author  : weifeng.cai
# @Email   : weifeng.cai@things-matrix.com
# 发送outlook邮件
from importlib import reload
# 先Windows安装pypiwin32
import win32com.client as win32
from mon import readconfig
import warnings
import sys
import pythoncom
import datetime
import os

addressee = readconfig.receiver  # 收件人邮箱列表
# cc = '1380965931@139.com' + ';' + readconfig.cs  # 抄送人邮件列表
cc = readconfig.cc
mail_path = readconfig.report_path  # 获取测试报告路径
body = readconfig.body  # 获取邮件内容
title = readconfig.title


class send_email():

    def outlook(self):

        olook = win32.Dispatch("outlook.Application")  # 固定写法
        # mail = olook.CreateItem(win32.constants.olMailItem)  # 固定写法
        mail = olook.CreateItem(0)
        mail.To = addressee  # 收件人
        mail.CC = cc  # 抄送人
        mail.Subject = str(datetime.datetime.now())[0:19] + title  # 邮件主题
        mail.Attachments.Add(mail_path)  # 添加附件
        mail.Body = body  # 邮件内容

        # read = open(mail_path, encoding='utf-8')  # 打开需要发送的测试报告附件文件
        # content = read.read()  # 读取测试报告文件中的内容
        # read.close()
        # mail.Body = content  # 将从报告中读取的内容，作为邮件正文中的内容
        mail.Send()  # 发送

        # return olook, mail, mail.TO, mail.CC, mail.Subject, mail.Attachments.Add(mail_path), mail.Body

if __name__ == '__main__':
    send_email().outlook()
