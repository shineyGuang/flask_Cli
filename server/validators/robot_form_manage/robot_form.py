# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 8:26 上午
# @Author  : ShineyZhao
# @File    : robot_form.py
# @Email   : shiney_zhao@163.com
import logging

from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired, Length, ValidationError

from models.robot.robot_model import RobotModel
from server.validators.base.baseform import BaseForm as Form
from utils.response_body.response_code_msg.response_code_msg import ResponseMessage

logger = logging.getLogger(__name__)


class CreateRobotForm(Form):
    id = IntegerField(label="机器人id")
    name = StringField(
        label="机器人名称",
        validators=[
            DataRequired(message="机器人名称不能为空"),
            Length(max=20, message="长度不能超过%(max)d")
        ]
    )
    pub_id = IntegerField(
        label="发布人工号",
        validators=[
            DataRequired(message="发布人工号不能为空"),
            Length(min=8, max=8, message="工号长度不能超过8位")
        ]
    )
    image = StringField(
        label="图片oss地址",
        validators=[
            # 先不加校验
        ]
    ),
    oss_url = StringField(
        label="Oss下载地址",
        validators=[
            # 先不加校验
        ]
    )
    category_id = IntegerField(
        label="类别"
    )

    def validate_name(self, value):
        if RobotModel.query.filter_by(name=value.data).first():
            logger.error(ResponseMessage.RobotNameIsExistsErr)
            raise ValidationError(ResponseMessage.RobotNameIsExistsErr)
