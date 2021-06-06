# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 8:19 上午
# @Author  : ShineyZhao
# @File    : robot_register.py
# @Email   : shiney_zhao@163.com
from models.robot.robot_model import RobotModel
from server.api.v1.base.base import Service
from utils.base_response.response import ResponseMsg


class RobotRegisterView(Service):
    __model__ = RobotModel
    __response__ = ResponseMsg()
