# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 19:21
# @Author  : 20019236
# @File    : users_model.py
# @Software: cmsDemo
import time

from sqlalchemy import Column, Integer, String, Date, SmallInteger, Text
from sqlalchemy_utils import ChoiceType
from werkzeug.security import generate_password_hash, check_password_hash

from models.base.base import Base, BaseDataModel
from models.choice_types import GENDER_STATUS, EDUCATIONAL_STATUS, POLITICALSTATUS_STATUS, MARRIAGE_STATUS
from utils.response_body.base_response_status.base_response_status import AuthFailed
from utils.response_body.response_code_msg.response_code_msg import ResponseMessage


class UsersAuthModel(Base):
    """
    USER 用户表
    """
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user_id = Column(String(8), nullable=False, comment="工号")
    is_admin = Column(SmallInteger, default=0)
    username = Column(String(50), nullable=False, comment="用户名")
    _password = Column("password", Text)
    # role_id = Column(Integer, comment="用户角色id", nullable=True)
    email = Column(String(50), comment="邮箱")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

    @staticmethod
    def verify(auth_data):
        user_id = auth_data["user_id"]
        password = auth_data["password"]
        auth_user_obj = UsersAuthModel.query.filter_by(user_id=user_id).first()
        if not auth_user_obj:
            raise AuthFailed(message=ResponseMessage.NotFondUserErr)
        if not auth_user_obj.check_password(password):
            raise AuthFailed(message=ResponseMessage.PasswordErr)
        user_sign = {
            "time_stamp": int(time.time()),
            "username": auth_user_obj.username,
            # "role_id": auth_user_obj.role_id,
            "user_id": auth_user_obj.user_id
        }
        return user_sign

    @property
    def keys(self):
        return [
            "id", "is_admin", "username", "password", "email", "create_time", "update_time"
        ]

    def __str__(self):
        return "<UsersAuthModel {}>".format(self.id)

