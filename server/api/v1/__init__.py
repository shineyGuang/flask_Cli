# -*- coding: utf-8 -*-
# @Time    : 2021/5/21 16:30
# @Author  : 20019236
# @File    : __init__.py.py
# @Software: flaskReview
from flask import Blueprint


def create_blueprint_v1():
    bp_v1 = Blueprint("v1", __name__)
    return bp_v1
