# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 19:49
# @Author  : 20019236
# @File    : register.py
# @Software: cmsDemo
from models.base.base import db
from models.users.users_model import UsersAuthModel
from server.api.v1.base.base import Service
from server.validators.user_form_manage.register_form.registerForm import CreateUserForm
from utils.base_response.response import ResponseMsg
from utils.response_body.response_code_msg.response_code_msg import ResponseCode, ResponseMessage


class UserRegisterView(Service):
    __model__ = UsersAuthModel
    __response__ = ResponseMsg()

    def post(self):
        try:
            form = CreateUserForm().validate_for_api()
        except Exception as e:
            message = list(e.message.values())[0][0]
            self.__response__.update(returncode=ResponseCode.AuthFailed, message=message)
            return self.__response__.data
        user_auth = self.__model__()
        user_auth.username = form.username.data
        # user_auth.role_id = form.role_id.data
        user_auth.password = form.password.data
        user_auth.is_admin = form.is_admin.data
        user_auth.email = form.email.data
        user_auth.user_id = form.user_id.data
        db.session.add(user_auth)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            self.__response__.update(message=ResponseMessage.CreateUserFail, returncode=ResponseCode.Fail)
            return self.__response__.data
        self.__response__.update(message=ResponseMessage.Success, returncode=ResponseCode.Success)
        return self.__response__.data
