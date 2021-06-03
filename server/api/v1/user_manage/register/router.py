# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 19:51
# @Author  : 20019236
# @File    : router.py
# @Software: cmsDemo
from server.api.v1.user_manage.register.register import UserRegisterView


def user_register_routesRegister(bp):
    bp.add_url_rule(
        rule="/register",
        methods=["POST", ],
        endpoint="register",
        view_func=UserRegisterView.as_view("register")
    )