#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 16:06
# @Author  : weifeng.cai
# @Email   : weifeng.cai@things-matrix.com



import logging
import time
import os


# log_path 是存放日志的路径
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), 'Logs')
# 如果不存在这个 logs 文件夹，就自动创建一个
if not os.path.exists(log_path): os.mkdir(log_path)


class Log():

    def __init__(self):
        # 文件的命名
        self.logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')

    def __console(self, level, message, url=None, data=None):

        # 创建一个 FileHandler，用于写到本地
        # fh = logging.FileHandler(self.logname, 'a')  # 追加模式 这个是 python2 的
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 这个是 python3 的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        # 创建一个 StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == 'INFO1':
            self.logger.info("执行测试用例：{}".format(message))
            self.logger.info("url：{}".format(url))
            self.info("请求参数：{}".format(data))
        elif level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):

        self.__console('debug', message)

    def info(self, message):

        self.__console('info', message)

    def case_info(self, message, url, data):

        self.__console('INFO1', message, url, data)

    def warning(self, message):

        self.__console('warning', message)

    def error(self, message):

        self.__console('error', message)


if __name__ == "__main__":
    log = Log()
    log.debug("test_case")
    # log.info("123")
    # log.info("---测试开始----")
    # log.info("操作步骤 1,2,3")
    # log.warning("----测试结束----")
