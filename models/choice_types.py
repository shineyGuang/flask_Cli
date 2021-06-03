#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author Xu Junkai
# coding=utf-8
# @Time    : 2021/2/19 20:37
# @Site    :
# @File    : choice_types.py
# @Software: PyCharm
"""
GENDER_STATUS = (
    ("1", "男"),
    ("2", "女"),
    ("3", "保密"),
)

MARRIAGE_STATUS = (
    ("1", "已婚"),
    ("2", "未婚")
)

EDUCATIONAL_STATUS = (
    ("1", "高中及以下"),
    ("2", "中专/技校"),
    ("3", "专科"),
    ("4", "本科"),
    ("5", "硕士研究生"),
    ("6", "博士研究生"),
)

POLITICALSTATUS_STATUS = (
    ("1", "中共党员"),
    ("2", "中共预备党员"),
    ("3", "共青团员"),
    ("4", "民革党员"),
    ("5", "民盟盟员"),
    ("6", "民建会员"),
    ("7", "民进会员"),
    ("8", "农工党党员"),
    ("9", "致公党党员"),
    ("10", "九三学社社员"),
    ("11", "台盟盟员"),
    ("12", "无党派人士"),
    ("13", "群众"),
)

REQUEST_METHODS_STATUS = {
    ("1", "GET"),
    ("2", "POST"),
    ("3", "DELETE"),
    ("4", "PUT"),
}

CROSS_STATUS = {
    ("1", "本地调用"),
    ("2", "第三方调用"),
}


FILE_STATUS = {
    ("folder", "文件夹"),
    ("tab", "标签"),
    ("view", "视图"),
}

CONTROL_LEVEL = {
    ("1", "菜单"),
    ("2", "按钮"),
}
