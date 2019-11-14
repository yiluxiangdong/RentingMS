#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 15:21
# @Author  : Mat
# @File    : run.py.py
# @Software: PyCharm
#模块尽量使用小写命名，首字母保持小写，尽量不要用下划线(除非多个单词，且数量不多的情况)
#类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头
#函数名一律小写，如有多个单词，用下划线隔开
#私有函数在函数前加一个下划线_
#变量名尽量小写, 如有多个单词，用下划线隔开
#常量采用全大写，如有多个单词，使用下划线隔开
#pyinstaller -F -w -i img.ico run.py
import os
os.system('start pythonw setup.py')