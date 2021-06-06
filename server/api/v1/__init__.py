# -*- coding: utf-8 -*-
# @Time    : 2021/5/21 16:30
# @Author  : 20019236
# @File    : __init__.py.py
# @Software: flaskReview
from flask import Blueprint

from server.api.v1.user_manage.login_auth.router import user_login_router
from server.api.v1.user_manage.register.router import user_register_routesRegister


def create_blueprint_v1():
    bp_v1 = Blueprint("v1", __name__)
    user_register_routesRegister(bp_v1)
    user_login_router(bp_v1)
    return bp_v1
