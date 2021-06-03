# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 19:49
# @Author  : 20019236
# @File    : register.py
# @Software: cmsDemo
from models.users.users_model import UsersInfoModel
from server.api.v1.base.base import Service


class UserRegisterView(Service):
    __model__ = UsersInfoModel




