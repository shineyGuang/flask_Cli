# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 8:20 上午
# @Author  : ShineyZhao
# @File    : router.py
# @Email   : shiney_zhao@163.com
from server.api.v1.robot_manage.robot_register.robot_register import RobotRegisterView


def robot_register_router(bp):
    bp.add_url_rule(
        rule="/addRobot",
        methods=["POST", ],
        endpoint="addRobot",
        view_func=RobotRegisterView.as_view("addRobot")
    )