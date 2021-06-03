# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 19:50
# @Author  : 20019236
# @File    : registerForm.py
# @Software: cmsDemo
import logging

from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError

from models.users.users_model import UsersAuthModel, UsersInfoModel
from server.validators.user_form_manage.base.baseForm import BaseUserForm
from utils.response_body.response_code_msg.response_code_msg import ResponseMessage

logger = logging.getLogger(__name__)


class CreateUserForm(BaseUserForm):
    """
    创建用户表单
    """
    account_name = StringField(
        label='账户',
        validators=[
            DataRequired(message="没有输入账号"),
            Length(min=5, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
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

    def validate_account_name(self, value):
        if UsersAuthModel.query.filter_by(account_name=value.data).first():
            logger.error(ResponseMessage.UserIsExistsErr)
            raise ValidationError(ResponseMessage.UserIsExistsErr)

    def validate_phone(self, value):
        if UsersInfoModel.query.filter_by(phone=value.data).first():
            logger.error(ResponseMessage.PhoneIsExistsErr)
            raise ValidationError(ResponseMessage.PhoneIsExistsErr)

    def validate_email(self, value):
        if UsersInfoModel.query.filter_by(email=value.data).first():
            logger.error(ResponseMessage.EmailIsExistsErr)
            raise ValidationError(ResponseMessage.EmailIsExistsErr)

    def validate_identity_code(self, value):
        if UsersInfoModel.query.filter_by(identity_code=value.data).first():
            logger.error(ResponseMessage.IdentityCodeIsExistsErr)
            raise ValidationError(ResponseMessage.IdentityCodeIsExistsErr)

    # def validate_role_id(self, value):
    #     if not RoleModel.query.filter_by(id=value.data).first():
    #         logger.error(ResponseMessage.RoleIdIsNotExistsErr)
    #         raise ValidationError(ResponseMessage.RoleIdIsNotExistsErr)
