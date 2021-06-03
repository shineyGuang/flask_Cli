# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 19:49
# @Author  : 20019236
# @File    : register.py
# @Software: cmsDemo
from models.base.base import db
from models.users.users_model import UsersInfoModel, UsersAuthModel
from server.api.v1.base.base import Service
from server.validators.user_form_manage.register_form.registerForm import CreateUserForm
from utils.base_response.response import ResponseMsg
from utils.response_body.response_code_msg.response_code_msg import ResponseCode, ResponseMessage


class UserRegisterView(Service):
    __model__ = UsersInfoModel
    __response__ = ResponseMsg()

    def post(self):
        try:
            form = CreateUserForm().validate_for_api()
        except Exception as e:
            message = list(e.message.values())[0][0]
            self.__response__.update(returncode=ResponseCode.AuthFailed, message=message)
            return self.__response__.data
        user_auth = UsersAuthModel()
        user_auth.account_name = form.account_name.data
        user_auth.role_id = form.role_id.data
        user_auth.password = form.password.data
        db.session.add(user_auth)
        db.session.flush()
        account_id = user_auth.id
        try:
            db.session.commit()
        except Exception as e:
            account_id = None
            db.session.rollback()
        if account_id:
            with db.auto_commit():
                user_info = self.__model__()
                user_info.id = account_id
                user_info.birthday = form.birthday.data
                user_info.education_level = form.education_level.data
                user_info.gender = form.gender.data
                user_info.email = form.email.data
                user_info.phone = form.phone.data
                user_info.is_marriage = form.is_marriage.data
                user_info.politic_countenance = form.politic_countenance.data
                user_info.real_name = form.real_name.data
                user_info.identity_code = form.identity_code.data
                user_info.account_id = account_id
                user_info.role_rowdata_id = form.role_id.data
                db.session.add(user_info)
        else:
            self.__response__.update(
                message=ResponseMessage.CreateUserFail,
                returncode=ResponseCode.Fail
            )
        return self.__response__.data



