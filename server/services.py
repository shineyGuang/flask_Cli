#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author Xu Junkai
# coding=utf-8
# @Time    : 2021/2/19 17:33
# @Site    :
# @File    : services.py
# @Software: PyCharm
"""
import uuid
import datetime
from decimal import Decimal
from sqlalchemy_utils import Choice
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from utils.response_body.base_response_status.base_response_status import ServerError


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, "keys") and hasattr(o, "__getitem__"):
            # print(dict(o))
            return dict(o)
        if isinstance(o, datetime.datetime):
            # 格式化时间
            return o.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(o, datetime.date):
            return o.strftime("%Y-%m-%d")
        if isinstance(o, Decimal):
            return "%.2f" % o
        if isinstance(o, Choice):
            return o.value
        if isinstance(o, uuid.UUID):
            # 格式化uuid
            return str(o)
        if isinstance(o, bytes):
            # 格式化字节数据
            return o.decode("utf-8")
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder
