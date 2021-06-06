# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 19:50
# @Author  : 20019236
# @File    : loginForm.py
# @Software: cmsDemo
from wtforms import StringField
from wtforms.validators import DataRequired, Regexp

from server.validators.base.baseform import BaseForm as Form


class UserLoginForm(Form):
    user_id = StringField(
       label="工号",
       validators=[
          DataRequired(message="工号不能为空"),
          Regexp(
             regex=r"\d{8}",
             message="长度为8位"
          )
       ]
    )
    password = StringField(
       label="密码"
    )
