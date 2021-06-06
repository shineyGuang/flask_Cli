# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 19:49
# @Author  : 20019236
# @File    : login.py
# @Software: cmsDemo
from flask import current_app

from models.users.users_model import UsersAuthModel
from server.api.v1.base.base import Service
from server.validators.user_form_manage.login_form.loginForm import UserLoginForm
from utils.base_response.response import ResponseMsg
from utils.jwt.jwt import Jwt
from utils.response_body.response_code_msg.response_code_msg import ResponseCode, ResponseMessage


class UserLoginView(Service):
    __model__ = UsersAuthModel
    __response__ = ResponseMsg()

    def post(self):
        try:
            form = UserLoginForm().validate_for_api()
        except Exception as e:
            message = list(e.message.values())[0][0]
            self.__response__.update(returncode=ResponseCode.AuthFailed, message=message)
            return self.__response__.data
        try:
            user_sign = self.__model__.verify(form.data)
        except Exception as e:
            self.__response__.update(returncode=ResponseCode.AuthFailed, message=e.__dict__.get("message"))
            return self.__response__.data
        token = Jwt.encode(user_sign, current_app.config["SIGN"], current_app.config["EXP"], current_app.config["DELAY"])
        result = {
            "token": token,
            "user_info": {
                "username": user_sign.get("username"),
                "user_id": user_sign.get("user_id"),
                "_": user_sign.get("time_stamp")
            }
        }
        self.__response__.update(returncode=ResponseCode.Success, result=result, message=ResponseMessage.LoginSuccess)
        return self.__response__.data
