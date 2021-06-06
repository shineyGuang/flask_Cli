# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 8:57 上午
# @Author  : ShineyZhao
# @File    : router.py
# @Email   : shiney_zhao@163.com
from server.api.v1.user_manage.login_auth.login import UserLoginView


def user_login_router(bp):
    bp.add_url_rule(
        rule="/userLogin",
        methods=["POST", ],
        view_func=UserLoginView.as_view("userLogin"),
        endpoint="userLogin"
    )