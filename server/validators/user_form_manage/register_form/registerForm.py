# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 19:50
# @Author  : 20019236
# @File    : registerForm.py
# @Software: cmsDemo
import logging

from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError, Email

from models.users.users_model import UsersAuthModel
from server.validators.base.baseform import BaseForm as Form
from utils.response_body.response_code_msg.response_code_msg import ResponseMessage

logger = logging.getLogger(__name__)


class CreateUserForm(Form):
    """
    创建用户表单
    """
    user_id = StringField(
        label="工号",
        validators=[
            DataRequired(message="没有输入工号"),
            Length(min=8, max=8, message="工号长度为8位")
        ]
    )
    is_admin = IntegerField(
        label="是否为管理员"
    )
    username = StringField(
        label='账户',
        validators=[
            DataRequired(message="没有输入账号"),
            Length(min=1, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
        ]
    )
    password = PasswordField(
        label='密码',
        validators=[
            DataRequired(message="没有输入密码"),
            #     Length(min=8, message='用户名长度必须大于%(min)d'),
            # Regexp(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}",
            #        message='密码至少8个字符，至少一个大写字母，1个小写字母，1个数字和一个特殊符号')
        ]
    )
    email = StringField(
        label='邮箱',
        validators=[
            DataRequired(message="没有输入邮箱"),
            Email(message="邮箱不合法")
        ]
    )

    def validate_username(self, value):
        if UsersAuthModel.query.filter_by(username=value.data).first():
            logger.error(ResponseMessage.UserIsExistsErr)
            raise ValidationError(ResponseMessage.UserIsExistsErr)

    def validate_user_id(self, value):
        if UsersAuthModel.query.filter_by(user_id=value.data).first():
            logger.error(ResponseMessage.UserIdExistsErr)
            raise ValidationError(ResponseMessage.UserIdExistsErr)

    def validate_email(self, value):
        if UsersAuthModel.query.filter_by(email=value.data).first():
            logger.error(ResponseMessage.EmailIsExistsErr)
            raise ValidationError(ResponseMessage.EmailIsExistsErr)
