#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author Xu Junkai
# coding=utf-8
# @Time    : 2021/2/28 15:26
# @Site    :
# @File    : redis_tools.py
# @Software: PyCharm
"""
from flask import current_app


class BaseRedis(object):
    @classmethod
    def locker(cls):
        return current_app.redis_lock(keys=["write_lock"], args=["islock", 3, 3])

    @classmethod
    def release(self):
        current_app.redis_release(keys=["write_lock"], args=["islock"])


class UserAuthRds(BaseRedis):
    key = 'Zcg_back_auth:{}'

    @classmethod
    def hmset(cls, id, kv: dict):
        name = cls.key.format(id)
        current_app.redis.hmset(name, kv)
        set_time = current_app.redis.expire(name, current_app.config["EXP"])
        print('set_time', set_time)

    @classmethod
    def hgetall(cls, id):
        name = cls.key.format(id)
        return current_app.redis.hgetall(name)


