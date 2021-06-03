# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 19:21
# @Author  : 20019236
# @File    : users_model.py
# @Software: cmsDemo
import time

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy_utils import ChoiceType
from werkzeug.security import generate_password_hash, check_password_hash

from models.base.base import Base, BaseDataModel
from models.choice_types import GENDER_STATUS, EDUCATIONAL_STATUS, POLITICALSTATUS_STATUS, MARRIAGE_STATUS
from utils.response_body.base_response_status.base_response_status import AuthFailed
from utils.response_body.response_code_msg.response_code_msg import ResponseMessage


class UsersAuthModel(Base):
    """
    用户表
    """
    __tablename__ = "user_auth"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(8), nullable=False, comment="工号")
    account_name = Column(String(10), nullable=False, comment="姓名")
    _password = Column("password", String(100))
    role_id = Column(Integer, comment="用户角色id", nullable=True)

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
        account_name = auth_data["account_name"]
        password = auth_data["password"]
        auth_user_obj = UsersAuthModel.query.filter_by(account_name=account_name).first()
        if not auth_user_obj:
            raise AuthFailed(message=ResponseMessage.NotFondUserErr)
        if not auth_user_obj.check_password(password):
            raise AuthFailed(message=ResponseMessage.PasswordErr)
        user_sign = {
            "time_stamp": int(time.time()),
            "account_name": auth_user_obj.account_name,
            "role_id": auth_user_obj.role_id,
            "id": auth_user_obj.id
        }
        return user_sign

    def keys(self):
        return [
            "id", "account_name", "role_id", "create_time", "update_time"
        ]

    def __str__(self):
        return "<UsersAuthModel {}>".format(self.id)


class UsersInfoModel(BaseDataModel):
    """
    用户信息表
    """
    __tablename__ = "user_info"
    id = Column(Integer, primary_key=True)
    phone = Column(String(12), nullable=True, comment="手机号")
    identity_code = Column(String(18), comment="身份证号", nullable=True)
    gender = Column(
        "gender", ChoiceType(GENDER_STATUS, String(1)), default="3", nullable=True
    )
    real_name = Column(String(24), nullable=True, comment="真实姓名")
    birthday = Column(Date, nullable=True, comment="出生日期")
    email = Column(String(64), nullable=True, comment="邮箱")
    education_level = Column(
        "educational_type",
        ChoiceType(EDUCATIONAL_STATUS, String(1)),
        default="1",
        nullable=True,
        comment="教育程度"
    )
    politic_countenance = Column(
        "politic_countenance",
        ChoiceType(POLITICALSTATUS_STATUS, String(2)),
        default="13",
        nullable=True,
        comment="政治面貌"
    )
    is_marriage = Column(
        "is_marriage",
        ChoiceType(MARRIAGE_STATUS, String(1)),
        # default="1",
        nullable=True,
        comment="婚否"
    )
    account_id = Column(Integer, comment="用户id")

    def keys(self):
        return [
            "id", "phone", "identity_code", "gender", "real_name", "birthday", "email", "education_level",
            "politic_countenance", "is_marriage", "account_id", "create_time", "update_time", 'status'
        ]

    def __str__(self):
        return "<UsersInfoModel {}>".format(self.id)
