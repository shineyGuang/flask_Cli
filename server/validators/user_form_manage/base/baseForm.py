# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 10:33 下午
# @Author  : ShineyZhao
# @File    : baseForm.py
# @Email   : shiney_zhao@163.com
from wtforms import StringField, DateField, IntegerField
from wtforms.validators import DataRequired, Email, Regexp, Length

from models.choice_types import EDUCATIONAL_STATUS, GENDER_STATUS, MARRIAGE_STATUS, POLITICALSTATUS_STATUS
from server.validators.base.baseform import BaseForm as Form
from server.validators.utils.select_tool import PreDealtSelectField


class BaseUserForm(Form):
    real_name = StringField(label="真实姓名")
    birthday = DateField(label='出生日期', )
    email = StringField(label='邮箱', validators=[DataRequired(message='邮箱不能为空'), Email(message="邮箱不合法")])
    phone = StringField('手机', validators=[
        DataRequired(message="手机号不合法"), Length(11, 11, "手机号要求11位"), Regexp(r'^1[35789]\d{9}$', 0, '手机号码不合法')],
                        )
    identity_code = StringField('身份证号', validators=[
        DataRequired(), Length(18, 18, '身份证号要求18位'), Regexp(
            r'^[1-9]\d{5}(18|19|20|(3\d))\d{2}((0[1-9])|(1[0-2]))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$', 0,
            '身份证号不合法')],
                                )
    role_id = IntegerField(label="角色id", validators=[
        DataRequired(message="角色id不能为空")
    ])

    education_level = PreDealtSelectField(
        label='教育程度', choices=EDUCATIONAL_STATUS, coerce=str
    )
    gender = PreDealtSelectField(
        label='性别', choices=GENDER_STATUS, coerce=str
    )
    is_marriage = PreDealtSelectField(
        label='婚否', choices=MARRIAGE_STATUS, coerce=str
    )
    politic_countenance = PreDealtSelectField(
        label='政治面貌', choices=POLITICALSTATUS_STATUS, coerce=str
    )
