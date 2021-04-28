#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 16:05
# @Author  : weifeng.cai
# @Email   : weifeng.cai@things-matrix.com
import yaml
import os
import sys
import readconfig

this_directory = os.path.abspath(os.path.dirname(__file__))


# os.path.dirname(os.path.realname(__file__))：指的是，获得你刚才所引用的模块 所在的绝对路径，__file__为内置属性
def get_yaml_data(file_name):
    with open(readconfig.data_path, "r", encoding="utf-8") as f:
        content = yaml.safe_load(f)
    return content


def get_data(key):
    # yaml_file = os.path.join(this_directory, "../../config.yml")
    yaml_data = get_yaml_data(readconfig.data_path)
    return yaml_data[key]


if __name__ == '__main__':
    print(get_data("env"))
