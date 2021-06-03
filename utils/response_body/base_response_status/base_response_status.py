#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author Xu Junkai
# coding=utf-8
# @Time    : 2021/2/19 17:47
# @Site    :
# @File    : base_response_status.py
# @Software: PyCharm
"""
from utils.response_body.base_response.base_response import APIException


class Success(APIException):
    """
    成功
    """
    code = 200
    returncode = 200
    message = "成功"
    result = ""


class CreateSuccess(APIException):
    """
    创建成功
    """
    code = 201
    returncode = 201
    message = "创建成功"
    result = ""


class DeleteSuccess(APIException):
    """
    删除成功
    """
    code = 204
    returncode = 204
    message = "删除成功"


class ServerError(APIException):
    """
    服务器错误
    """
    code = 500
    returncode = 500
    message = "服务器未响应"
    result = ""

class ClientTypeEnumError(APIException):
    """
    请求content-type格式错误
    """
    code = 422
    returncode = 422
    message = "请求参数，语义错误"
    result = ""


class ClientTypeError(APIException):
    """
    错误的请求
    """
    code = 400
    returncode = 400
    message = "非法请求"
    result = ""


class NotFound(APIException):
    """
    资源不存在
    """
    code = 404
    returncode = 404
    message = "找不到资源"
    result = ""


class AuthFailed(APIException):
    """
    身份验证失败，需要登录
    """
    code = 401
    returncode = 401
    message = "授权失败"
    result = ""


class Forbidden(APIException):
    """
    禁止访问，权限禁止
    """
    code = 403
    returncode = 403
    message = "禁止访问"
    result = ""
