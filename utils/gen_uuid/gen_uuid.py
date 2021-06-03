#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author Xu Junkai
# coding=utf-8
# @Time    : 2020/11/9 23:10
# @Site    :
# @File    : gen_uuid.py
# @Software: PyCharm
"""
import uuid


def gen_id():
    return str(uuid.uuid4().hex).upper()
