#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 11:28
# @Author  : Mat
# @File    : __init__.py.py
# @Software: PyCharm
#模块尽量使用小写命名，首字母保持小写，尽量不要用下划线(除非多个单词，且数量不多的情况)
#类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头
#函数名一律小写，如有多个单词，用下划线隔开
#私有函数在函数前加一个下划线_
#变量名尽量小写, 如有多个单词，用下划线隔开
#常量采用全大写，如有多个单词，使用下划线隔开

class Farm():
    MAX_CLIENT = 100
    MAX_CONNECTION = 1000
    CONNECTION_TIMEOUT = 600

    def run():
        count = 0
        school_name = ''
        pass

    def run_with_env():
        pass

    def _private_func():
        pass


class AnimalFarm(Farm):
    pass


class _PrivateFarm(Farm):
    pass
    