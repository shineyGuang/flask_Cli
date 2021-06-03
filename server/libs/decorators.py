#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author Xu Junkai
# coding=utf-8
# @Time    : 2021/2/20 17:08
# @Site    :
# @File    : decorator.py
# @Software: PyCharm
"""
import logging
from flask import request, current_app, g

from utils.jwt.jwt import Jwt
from utils.response_body.base_response_status.base_response_status import AuthFailed
from utils.response_body.response_code_msg.response_code_msg import ResponseMessage

logger = logging.getLogger(__name__)


def auth_deco_required(func):
    """
    用户认证
    :param func:
    :return:
    """

    def inner(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            logger.error(ResponseMessage.TokeninvalidErr)
            raise AuthFailed(message=ResponseMessage.TokeninvalidErr)
        payload = Jwt.decode(token.encode("utf-8"), current_app.config["SIGN"])

        g.user_id = payload["id"]
        g.role_id = payload["role_id"]
        g.account_name = payload["account_name"]
        return func(*args, **kwargs)

    inner.__name__ = func.__name__
    return inner
