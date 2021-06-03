#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author Xu Junkai
# coding=utf-8
# @Time    : 2020/8/20 15:22
# @Site    :
# @File    : response.py
# @Software: PyCharm
"""
from flask import request

from utils.response_body.response_code_msg.response_code_msg import ResponseMessage


class ResponseMsg(object):
    """
    封装响应文本
    """

    def __init__(
            self, result="", returncode=200, message=ResponseMessage.Success, rq=request
    ):
        # 获取请求中语言选择,默认为中文
        self._result = result
        self._message = message
        self._returncode = returncode

    def update(self, returncode: object = None, result: object = None, message: object = None):
        """
        更新默认响应文本
        :param returncode:响应编码
        :param result: 响应数据
        :param message: 响应消息
        :return:
        """
        self._returncode = "" if not returncode else returncode
        self._message = "" if not message else message
        self._result = "" if not result else result

    def add_field(self, name=None, value=None):
        """
        在响应文本中加入新的字段，方便使用
        :param name: 变量名
        :param value: 变量值
        :return:
        """
        if name is not None and value is not None:
            self.__dict__[name] = value

    @property
    def data(self):
        """
        输出响应文本内容
        :return:
        """
        body = self.__dict__
        body["result"] = body.pop("_result")
        body["message"] = body.pop("_message")
        body["statusCode"] = body.pop("_returncode")
        return body
