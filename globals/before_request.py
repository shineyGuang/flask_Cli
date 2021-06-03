#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author Xu Junkai
# coding=utf-8
# @Time    : 2021/2/19 18:32
# @Site    :
# @File    : before_request.py
# @Software: PyCharm
"""
import re
import json
from globals.bp_v1_manage import bp_v1
from flask import request, current_app, g

from server.libs.redis_tools import UserAuthRds
from utils.jwt.jwt import Jwt
from utils.response_body.base_response_status.base_response_status import Forbidden
from utils.response_body.response_code_msg.response_code_msg import ResponseMessage


@bp_v1.before_app_request
def middleware():
    path = request.path
    method = request.method
    if method == "OPTIONS":
        return
    # # 白名单
    if path in ["/api/v1/LoginAuth/", '/api/v1/obtainPermission/']:
        return
    token = request.headers.get("Authorization")
    if not token:
        raise Forbidden(message=ResponseMessage.IllegalLoginErr)
    try:
        payload = Jwt.decode(token.encode("utf-8"), current_app.config["SIGN"])
    except Exception as e:
        raise Forbidden(message=ResponseMessage.TokeninvalidErr)
    id = payload['id']
    auth_user = UserAuthRds.hgetall(id)
    # token唯一验证
    if token != auth_user['token']:
        raise Forbidden(message=ResponseMessage.UserRepeatLoginErr)
    # 接口验证
    permission_apis = json.loads(auth_user["apis"])
    for api in permission_apis:
        if re.search(api["api"], path) and method == api['method']:
            print('有权限的接口:', api["api"])
            break
    else:
        # raise Forbidden(message = ResponseMessage.NoPermissionApiErr)
        print('当前用户没有api的权限为:', path)
    # # 数据设置：
    g.role_data_id = auth_user["role_data_id"] if auth_user["role_data_id"] else ""
    return


@bp_v1.after_app_request
def after_middleware(response):
    return response
